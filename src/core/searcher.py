import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class Searcher:
    def __init__(self, config, index, df):
        self.config = config
        self.model = SentenceTransformer(config['model']['name'])
        self.index = index
        self.df = df

    def search(self, query, k=None):
        if k is None:
            k = self.config['search']['top_k']
        query_vector = self.model.encode([query])
        faiss.normalize_L2(query_vector)
        distances, indices = self.index.search(query_vector, k)
        results = self.df.loc[indices[0]]
        results['similarity'] = distances[0]
        return results.sort_values('similarity', ascending=False)