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

print("Loading JD...")
jd = load_jd(
    "data/job_description.docx"
)

jd_embedding = model.encode([jd])

results = []

print("Ranking candidates...")

# For now test on 1000 candidates
for candidate in candidates[:1000]:

    text = candidate_to_text(candidate)

    candidate_embedding = model.encode([text])

    similarity = cosine_similarity(
        jd_embedding,
        candidate_embedding
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
    key=lambda x: x[1],
    reverse=True
)

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
                round(score, 4),
                reasoning
            ]
        )

print(
    "Submission saved to output/submission.csv"
)