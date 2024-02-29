from sentence_transformers import SentenceTransformer
import numpy as np

def predict_similarity(txt1, txt2):
    sentences = [txt1, txt2]
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)

    # Calcul de la similarité cosinus
    cosine_similarity = np.dot(embeddings[0], embeddings[1])/(np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
    
    return cosine_similarity
