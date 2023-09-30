from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  # Import cosine_similarity function

# Initialize Elasticsearch and SentenceTransformer model
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
    http_auth=('elastic', 'RzV=KhxPU*PV925d3jat'),
    verify_certs=False
) # Elasticsearch server address
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # You can choose a different model if needed

# def get_question_embedding(question):
#     return model.encode(question).reshape(1, -1)
def get_question_embedding(question):
    return np.array(model.encode(question)).reshape(1, -1)


# def retrieve_documents_with_embeddings(es, index_name, query_embedding):
#     # Get all embeddings from Elasticsearch
#     embedding_results = es.search(index=index_name, body={"size": 1000, "query": {"match_all": {}}})['hits']['hits']
    
#     # Extract embeddings and metadata
#     embeddings = [np.array(hit['_source']['embedding']).reshape(1, -1) for hit in embedding_results]
#     metadata = [hit['_source']['metadata'] for hit in embedding_results]
    
#     # Calculate cosine similarity between query embedding and all passage embeddings
#     similarity_scores = [cosine_similarity(query_embedding, emb)[0][0] for emb in embeddings]
    
#     # Sort passages by similarity scores and get top 3
#     sorted_indices = np.argsort(similarity_scores)[::-1][:3]
#     passages = [embedding_results[i]['_source']['passage'] for i in sorted_indices]
#     relevance_scores = [similarity_scores[i] for i in sorted_indices]
#     metadata = [metadata[i] for i in sorted_indices]
    
#     return passages, relevance_scores, metadata

def retrieve_documents_with_embeddings(es, index_name, query_embedding):
    # Get all embeddings from Elasticsearch
    embedding_results = es.search(index=index_name, body={"size": 1000, "query": {"match_all": {}}})['hits']['hits']
    
    # Extract embeddings and metadata
    embeddings = [np.array(hit['_source']['embedding']).reshape(1, -1) for hit in embedding_results]
    metadata = [hit['_source']['metadata'] for hit in embedding_results]
    
    # Calculate cosine similarity between query embedding and all passage embeddings
    similarity_scores = [cosine_similarity(query_embedding.reshape(1, -1), emb)[0][0] for emb in embeddings]
    
    # Sort passages by similarity scores and get top 3
    sorted_indices = np.argsort(similarity_scores)[::-1][:3]
    passages = [embedding_results[i]['_source']['passage'] for i in sorted_indices]
    relevance_scores = [similarity_scores[i] for i in sorted_indices]
    metadata = [metadata[i] for i in sorted_indices]
    
    return passages, relevance_scores, metadata

# Example usage
user_question = "what is a valid offer"
query_embedding = get_question_embedding(user_question)
index_name = "qa_index"
passages, relevance_scores, metadata = retrieve_documents_with_embeddings(es, index_name, query_embedding)

# Create DataFrame and save to CSV
data = {
    "Question": [user_question],
    "Passage 1": [passages[0]],
    "Relevance Score 1": [relevance_scores[0]],
    "Passage 1 Metadata": [metadata[0]],
    "Passage 2": [passages[1]],
    "Relevance Score 2": [relevance_scores[1]],
    "Passage 2 Metadata": [metadata[1]],
    "Passage 3": [passages[2]],
    "Relevance Score 3": [relevance_scores[2]],
    "Passage 3 Metadata": [metadata[2]]
}

df = pd.DataFrame(data)
df.to_csv('questions_answers.csv', index=False)
