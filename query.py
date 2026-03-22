import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np
import os

def load_index():
    if not os.path.exists("data/vector_store/index.faiss"):
        return None, None

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_index():
    index = faiss.read_index("data/vector_store/index.faiss")
    with open("data/vector_store/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def get_relevant_chunks(query, top_k=3):
    index, chunks = load_index()

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)

    results = [chunks[i] for i in I[0]]
    return results
