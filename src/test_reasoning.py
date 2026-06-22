from load_data import load_candidates
from reasoning import generate_reasoning

candidates = load_candidates(
    "data/candidates.jsonl"
)

print(
    generate_reasoning(
        candidates[30]
    )
)