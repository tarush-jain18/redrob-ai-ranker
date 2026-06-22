import json

def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":
    candidates = load_candidates("data/candidates.jsonl")

    print(f"Total Candidates: {len(candidates)}")
    print()

    first = candidates[0]

    print("Candidate ID:", first["candidate_id"])
    print("Headline:", first["profile"]["headline"])
    print("Experience:", first["profile"]["years_of_experience"])