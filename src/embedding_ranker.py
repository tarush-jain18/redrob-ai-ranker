from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

jd = """
Senior AI Engineer
LLMs
Embeddings
Retrieval
Ranking Systems
Fine-tuning
"""

candidate = """
Backend Engineer
NLP
Fine-tuning LLMs
Milvus
LoRA
AWS
"""

jd_emb = model.encode([jd])
cand_emb = model.encode([candidate])

score = cosine_similarity(jd_emb, cand_emb)[0][0]

print("Similarity:", score)