import time

from load_data import load_candidates
from candidate_text import candidate_to_text
from jd_parser import load_jd
from scoring import final_score
from reasoning import generate_reasoning

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

start_time = time.time()

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
jd_embedding = model.encode([jd])[0]

print("Preparing 1000 candidates...")
candidates = candidates[:1000]

candidate_texts = [
    candidate_to_text(candidate)
    for candidate in candidates
]

print("Creating embeddings...")
embedding_start = time.time()

candidate_embeddings = model.encode(
    candidate_texts,
    batch_size=64,
    show_progress_bar=True
)

embedding_end = time.time()

results = []

print("Scoring...")

for candidate, candidate_embedding in zip(
    candidates,
    candidate_embeddings
):

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    score = final_score(
        candidate,
        similarity
    )

    reasoning = generate_reasoning(
        candidate
    )

    results.append(
        (
            candidate["candidate_id"],
            score,
            reasoning
        )
    )

results.sort(
    key=lambda x: (-x[1], x[0])
)

end_time = time.time()

print("\n========== RESULTS ==========")
print(
    f"Total Time: "
    f"{end_time - start_time:.2f} seconds"
)

print(
    f"Embedding Time: "
    f"{embedding_end - embedding_start:.2f} seconds"
)

print(
    f"Estimated 100k Runtime: "
    f"{((end_time-start_time)*100):.2f} seconds"
)

print(
    f"Estimated 100k Runtime: "
    f"{((end_time-start_time)*100)/60:.2f} minutes"
)

print("============================")