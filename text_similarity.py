from sentence_transformers import SentenceTransformer, util
import time

model = SentenceTransformer("all-MiniLM-L6-v2")

# Two lists of sentences
sentences1 = [
    "I want to know about financial advice about car loan.",
]

sentences2 = [
    "How to get car loan financial advice",
]

t1 = time.time()
# Compute embedding 
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)
pt_cosine = util.pytorch_cos_sim(embeddings1, embeddings2)
t2 = time.time()

print(f"contextual similarity: {cosine_scores}, with time {t2 - t1} seconds")

# reference
# https://enjoymachinelearning.com/blog/finding-semantic-similarity-between-sentences-in-python/
