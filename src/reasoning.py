def generate_reasoning(candidate):

    reasons = []

    years = candidate["profile"].get(
        "years_of_experience",
        0
    )

    if 5 <= years <= 9:
        reasons.append(
            f"{years} years relevant experience"
        )

    skills = {
        skill["name"]
        for skill in candidate.get(
            "skills",
            []
        )
    }

    important = [
        "Embeddings",
        "Information Retrieval",
        "Sentence Transformers",
        "FAISS",
        "Pinecone",
        "Milvus",
        "Machine Learning",
        "MLOps",
        "Hugging Face Transformers"
    ]

    matched = [
        s for s in important
        if s in skills
    ]

    if matched:
        reasons.append(
            "Strong skills in " +
            ", ".join(
                matched[:3]
            )
        )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    if signals.get(
        "recruiter_response_rate",
        0
    ) > 0.8:

        reasons.append(
            "High recruiter response rate"
        )

    if signals.get(
        "open_to_work_flag",
        False
    ):

        reasons.append(
            "Open to work"
        )

    return "; ".join(reasons)
