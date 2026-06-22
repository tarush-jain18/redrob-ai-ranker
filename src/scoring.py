def experience_score(candidate):

    years = candidate["profile"].get(
        "years_of_experience",
        0
    )

    if 5 <= years <= 9:
        return 1.0

    elif 4 <= years < 5:
        return 0.8

    elif 9 < years <= 11:
        return 0.8

    elif 2 <= years < 4:
        return 0.5

    return 0.2


def skill_score(candidate):

    important_skills = {
        "Embeddings",
        "Information Retrieval",
        "Sentence Transformers",
        "FAISS",
        "Pinecone",
        "Milvus",
        "Qdrant",
        "Hugging Face Transformers",
        "Machine Learning",
        "MLOps",
        "Python",
        "Ranking",
        "Retrieval",
        "NLP"
    }

    skills = candidate.get("skills", [])

    candidate_skills = {
        skill["name"]
        for skill in skills
    }

    matches = len(
        important_skills &
        candidate_skills
    )

    return matches / len(
        important_skills
    )


def recruiter_signal_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    response_rate = signals.get(
        "recruiter_response_rate",
        0
    )

    saved = signals.get(
        "saved_by_recruiters_30d",
        0
    )

    views = signals.get(
        "profile_views_received_30d",
        0
    )

    score = (
        response_rate +
        min(saved / 20, 1) +
        min(views / 500, 1)
    ) / 3

    return score


def readiness_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    score = 0

    if signals.get(
        "open_to_work_flag",
        False
    ):
        score += 0.4

    if signals.get(
        "notice_period_days",
        999
    ) <= 60:
        score += 0.3

    score += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 0.3
    )

    return score


def final_score(
    candidate,
    semantic_similarity
):

    return (
        0.40 * semantic_similarity +
        0.20 * experience_score(candidate) +
        0.15 * skill_score(candidate) +
        0.15 * recruiter_signal_score(candidate) +
        0.10 * readiness_score(candidate)
    )