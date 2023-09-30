from flask import Flask, request, jsonify
from flask_cors import CORS 
from retrieval import retrieve_documents_with_embeddings
from retrieval import get_question_embedding
from elasticsearch import Elasticsearch
from gen_ai import generate_direct_answer  # Import the generative AI function

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
    http_auth=('elastic', 'RzV=KhxPU*PV925d3jat'),
    verify_certs=False
)  # Elasticsearch server address
index_name = 'qa_index'

@app.route('/api/question', methods=['POST'])
def get_answer():
    data = request.get_json()
    user_question = data['question']
    query_embedding = get_question_embedding(user_question)
    passages, relevance_scores, metadata = retrieve_documents_with_embeddings(es, index_name, query_embedding)
    # Generate direct answer using the generative AI module
    direct_answer = generate_direct_answer(user_question, passages)
    
    response = {
        "question": user_question,
        "answers": [{
            "passage": passages[i],
            "relevance_score": relevance_scores[i],
            "metadata": metadata[i]
        } for i in range(len(passages))],
        "direct_answer": direct_answer  # Include the direct answer in the response
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
