import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils import load_pdf, chunk_text
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')

def ingest_pdf(pdf_path):
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    os.makedirs("data/vector_store", exist_ok=True)

    faiss.write_index(index, "data/vector_store/index.faiss")

    with open("data/vector_store/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("✅ PDF Ingested Successfully")
