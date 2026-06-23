
import csv

from load_data import load_candidates
from candidate_text import candidate_to_text
from jd_parser import load_jd
from scoring import final_score
from reasoning import generate_reasoning

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

print(f"Total candidates: {len(candidates)}")

print("Loading JD...")
jd = load_jd(
    "data/job_description.docx"
)

print("Creating JD embedding...")
jd_embedding = model.encode([jd])[0]

results = []

print("Creating candidate texts...")

candidate_texts = [
    candidate_to_text(candidate)
    for candidate in candidates
]

print("Creating candidate embeddings...")

candidate_embeddings = model.encode(
    candidate_texts,
    batch_size=64,
    show_progress_bar=True
)

print("Scoring candidates...")

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

print("Sorting results...")

results.sort(
    key=lambda x: (-x[1], x[0])
)

print("Saving submission...")

with open(
    "output/submission.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    for rank, (
        candidate_id,
        score,
        reasoning
    ) in enumerate(
        results[:100],
        start=1
    ):

        writer.writerow(
            [
                candidate_id,
                rank,
                round(score, 6),
                reasoning
            ]
        )

print("Submission saved to output/submission.csv")
print("Top 100 candidates selected from FULL dataset.")

