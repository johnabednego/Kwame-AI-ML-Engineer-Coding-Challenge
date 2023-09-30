from elasticsearch import Elasticsearch
import pandas as pd

def create_index(es, index_name):
    es.indices.create(index=index_name, ignore=400)

def index_data(es, index_name, data_csv):
    data = pd.read_csv(data_csv)
    for _, row in data.iterrows():
        doc = {
            "passage": row['Passage'],
            "metadata": row['Metadata'],
            "embedding": [float(val) for val in row['Embedding'].strip('[]').split(',')]
        }
        es.index(index=index_name, body=doc)

# Example usage
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
    http_auth=('elastic', 'RzV=KhxPU*PV925d3jat'),
    verify_certs=False
)  # Elasticsearch server address
index_name = 'qa_index'
data_csv = 'passage_metadata_emb.csv'
create_index(es, index_name)
index_data(es, index_name, data_csv)
