from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.embeddings import Embeddings
import numpy as np


class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)
    
    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()
    
    def embed_query(self, text):
        return self.model.encode([text]).tolist()[0]


def create_faiss_index(chunks):
    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    embeddings = SentenceTransformerEmbeddings('all-MiniLM-L6-v2')
    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    return vectorstore
