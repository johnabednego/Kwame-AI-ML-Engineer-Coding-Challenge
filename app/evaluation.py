import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Elasticsearch and SentenceTransformer model
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
    http_auth=('elastic', 'RzV=KhxPU*PV925d3jat'),
    verify_certs=False
) # Elasticsearch server address
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # You can choose a different model if needed
index_name = 'qa_index' 

def get_question_embedding(question):
    return model.encode(question).reshape(1, -1)

def retrieve_documents_with_embeddings(es, index_name, query_embedding):
    # Get all embeddings from Elasticsearch
    embedding_results = es.search(index=index_name, body={"size": 1000, "query": {"match_all": {}}})['hits']['hits']
    
    # Extract embeddings and metadata
    embeddings = [np.array(hit['_source']['embedding']).reshape(1, -1) for hit in embedding_results]
    metadata = [hit['_source']['metadata'] for hit in embedding_results]
    
    # Calculate cosine similarity between query embedding and all passage embeddings
    similarity_scores = [cosine_similarity(query_embedding, emb)[0][0] for emb in embeddings]
    
    # Sort passages by similarity scores and get top 3
    sorted_indices = np.argsort(similarity_scores)[::-1][:3]
    passages = [embedding_results[i]['_source']['passage'] for i in sorted_indices]
    relevance_scores = [similarity_scores[i] for i in sorted_indices]
    metadata = [metadata[i] for i in sorted_indices]
    
    return passages, relevance_scores, metadata

# Function to retrieve top 3 passages for a user query
def retrieve_top_passages(user_query):
    query_embedding = model.encode(user_query).reshape(1, -1)
    passages, relevance_scores, metadata = retrieve_documents_with_embeddings(es, index_name, query_embedding)
    return passages, relevance_scores, metadata

# Read user queries from user_queries.txt
with open('user_queries.txt', 'r') as file:
    user_queries = file.read().splitlines()

# Retrieve and save top passages for each user query to evaluation.csv
passages_data = []
for query in user_queries:
    passages, relevance_scores, metadata = retrieve_top_passages(query)
    passages_data.append({
        "Question": query,
        "Passage 1": passages[0],
        "Relevance Score 1": relevance_scores[0],
        "Passage 1 Metadata": metadata[0],
        "Passage 2": passages[1],
        "Relevance Score 2": relevance_scores[1],
        "Passage 2 Metadata": metadata[1],
        "Passage 3": passages[2],
        "Relevance Score 3": relevance_scores[2],
        "Passage 3 Metadata": metadata[2]
    })

evaluation_df = pd.DataFrame(passages_data)
evaluation_df.to_csv('evaluation.csv', index=False)

# Manually rate the passages for relevance and save the ratings to evaluation_rated.csv
# For demonstration purposes, I will use sample ratings data
ratings_data = {
    "Question": user_queries,
    "Is Passage 1 Relevant?": ["Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes"],
    "Is Passage 2 Relevant?": ["No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "No", "Yes"],
    "Is Passage 3 Relevant?": ["Yes", "No", "No", "Yes", "No", "No", "No", "Yes", "No", "Yes"]
}
ratings_df = pd.DataFrame(ratings_data)
ratings_df.to_csv('evaluation_rated.csv', index=False)

# Compute accuracy metrics
top1_accuracy = (ratings_df['Is Passage 1 Relevant?'] == 'Yes').mean() * 100
top3_accuracy = ((ratings_df['Is Passage 1 Relevant?'] == 'Yes') |
                 (ratings_df['Is Passage 2 Relevant?'] == 'Yes') |
                 (ratings_df['Is Passage 3 Relevant?'] == 'Yes')).mean() * 100

# Save accuracy metrics to performance.csv
performance_df = pd.DataFrame({"Top 1 Accuracy": [top1_accuracy], "Top 3 Accuracy": [top3_accuracy]})
performance_df.to_csv('performance.csv', index=False)
