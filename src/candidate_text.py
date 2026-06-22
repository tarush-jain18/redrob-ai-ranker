from load_data import load_candidates


def candidate_to_text(candidate):

    profile = candidate["profile"]

    # Skills
    skills = candidate.get("skills", [])
    skill_text = ", ".join(
        [skill.get("name", "") for skill in skills]
    )

    # Career History
    career_history = candidate.get("career_history", [])

    career_text = ""

    for job in career_history:
        career_text += (
            f"{job.get('title', '')} at "
            f"{job.get('company', '')}. "
        )

    text = f"""
Headline:
{profile.get('headline', '')}

Summary:
{profile.get('summary', '')}

Years of Experience:
{profile.get('years_of_experience', '')}

Current Title:
{profile.get('current_title', '')}

Current Company:
{profile.get('current_company', '')}

Skills:
{skill_text}

Career History:
{career_text}
"""

    return text


if __name__ == "__main__":

    candidates = load_candidates("data/candidates.jsonl")

    print(candidate_to_text(candidates[0]))