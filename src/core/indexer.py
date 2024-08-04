import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pickle
import os


class Indexer:
    def __init__(self, config):
        self.config = config
        self.model = SentenceTransformer(config['model']['name'])
        self.dense_vectors_file = config['model']['dense_vectors_file']
        self.faiss_index_file = config['model']['faiss_index_file']

    def encode_data(self, df):
        return np.vstack(df.apply(self.encode_row, axis=1).values)

    def encode_row(self, row):
        text = row['snippet'] if pd.notna(row['snippet']) else row['page_title']
        return self.model.encode(text)

    def create_or_load_index(self, df):
        if os.path.exists(self.dense_vectors_file) and os.path.exists(self.faiss_index_file):
            with open(self.dense_vectors_file, 'rb') as file:
                vectors = pickle.load(file)
            index = faiss.read_index(self.faiss_index_file)
        else:
            vectors = self.encode_data(df)
            faiss.normalize_L2(vectors)
            with open(self.dense_vectors_file, 'wb') as file:
                pickle.dump(vectors, file)

            index = faiss.IndexIDMap(faiss.IndexFlatIP(vectors.shape[1]))
            index.add_with_ids(vectors, np.array(df.index.values).astype('int64'))
            faiss.write_index(index, self.faiss_index_file)

        return index, vectors