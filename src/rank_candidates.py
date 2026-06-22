from load_data import load_candidates
from candidate_text import candidate_to_text

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

candidates = load_candidates("data/candidates.jsonl")

jd = """
Senior AI Engineer

Required Skills:
LLMs
Embeddings
Retrieval
Ranking Systems
Fine-tuning
Product Mindset
"""

jd_embedding = model.encode([jd])

results = []

for candidate in candidates[:100]:

    candidate_text = candidate_to_text(candidate)

    candidate_embedding = model.encode([candidate_text])

    similarity = cosine_similarity(
        jd_embedding,
        candidate_embedding
    )[0][0]

    results.append(
        (
            candidate["candidate_id"],
            similarity
        )
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

top_candidate = results[0][0]

for candidate in candidates:

    if candidate["candidate_id"] == top_candidate:

        print(candidate)

        break