from load_data import load_candidates
from candidate_text import candidate_to_text
from jd_parser import load_jd
from scoring import final_score

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Loading candidates...")

candidates = load_candidates(
    "data/candidates.jsonl"
)

print("Loading JD...")

jd = load_jd(
    "data/job_description.docx"
)

print("Creating JD embedding...")

jd_embedding = model.encode([jd])

results = []

print("Scoring candidates...")

# Keep 100 for now
for candidate in candidates[:100]:

    text = candidate_to_text(
        candidate
    )

    candidate_embedding = model.encode(
        [text]
    )

    similarity = cosine_similarity(
        jd_embedding,
        candidate_embedding
    )[0][0]

    score = final_score(
        candidate,
        similarity
    )

    results.append(
        (
            candidate["candidate_id"],
            score,
            similarity
        )
    )

results.sort(
    key=lambda x: (-x[1], x[0])
)

print("\n" + "=" * 60)
print("TOP 10 CANDIDATES")
print("=" * 60)

for rank, (
    candidate_id,
    score,
    similarity
) in enumerate(
    results[:10],
    start=1
):

    print(
        f"{rank}. "
        f"{candidate_id} | "
        f"Final Score: {score:.4f} | "
        f"Similarity: {similarity:.4f}"
    )

print("=" * 60)