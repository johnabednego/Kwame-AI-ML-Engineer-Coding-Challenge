from sentence_transformers import SentenceTransformer
import pandas as pd

def generate_embeddings(input_csv, output_csv):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    data = pd.read_csv(input_csv)
    passages = data['Passage'].tolist()
    embeddings = model.encode(passages)
    
    data['Embedding'] = [emb.tolist() for emb in embeddings]
    data.to_csv(output_csv, index=False)

# Example usage
input_csv = 'passage_metadata.csv'
output_csv = 'passage_metadata_emb.csv'
generate_embeddings(input_csv, output_csv)
