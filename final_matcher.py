from jobs import get_all_jobs
from skill_weights import SKILL_WEIGHTS
from tfidf_matcher import calculate_text_similarity


def get_skill_weight(skill):

    for skill_name, weight in SKILL_WEIGHTS.items():

        if skill_name.lower() == skill.lower():
            return weight

    return 1.0


def calculate_weighted_skill_score(
    resume_skills,
    job_skills
):

    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    matched_weight = 0
    total_weight = 0

    for job_skill in job_skills:

        weight = get_skill_weight(job_skill)

        total_weight += weight

        if job_skill.lower() in resume_skills_lower:

            matched_skills.append(job_skill)

            matched_weight += weight

        else:

            missing_skills.append(job_skill)

    if total_weight == 0:

        return 0, matched_skills, missing_skills

    score = (
        matched_weight / total_weight
    ) * 100

    return (
        round(score, 2),
        matched_skills,
        missing_skills
    )


def calculate_final_score(
    skill_score,
    text_similarity
):

    final_score = (
        skill_score * 0.70
        +
        text_similarity * 0.30
    )

    return round(final_score, 2)


def analyze_jobs(
    resume_text,
    resume_skills
):

    jobs = get_all_jobs()

    results = []

    for job in jobs:

        skill_score, matched_skills, missing_skills = (
            calculate_weighted_skill_score(
                resume_skills,
                job["skills"]
            )
        )

        text_similarity = calculate_text_similarity(
            resume_text,
            job["description"]
        )

        final_score = calculate_final_score(
            skill_score,
            text_similarity
        )

        results.append({

            "title": job["title"],

            "company": job["company"],

            "location": job["location"],

            "score": final_score,

            "skill_score": skill_score,

            "text_similarity": text_similarity,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "required_skills": job["skills"]

        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results