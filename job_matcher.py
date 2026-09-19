from jobs import get_all_jobs
from skill_weights import SKILL_WEIGHTS


def get_skill_weight(skill):
    """
    Returns the importance/weight of a skill.
    Unknown skills receive a default weight of 1.0.
    """

    for skill_name, weight in SKILL_WEIGHTS.items():

        if skill_name.lower() == skill.lower():
            return weight

    return 1.0


def calculate_weighted_match(resume_skills, job_skills):

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

        score = 0

    else:

        score = (
            matched_weight / total_weight
        ) * 100


    return (
        round(score, 2),
        matched_skills,
        missing_skills
    )


def match_jobs(resume_skills):

    jobs = get_all_jobs()

    results = []

    for job in jobs:

        (
            score,
            matched_skills,
            missing_skills
        ) = calculate_weighted_match(
            resume_skills,
            job["skills"]
        )

        results.append({

            "title": job["title"],

            "company": job["company"],

            "location": job["location"],

            "score": score,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "required_skills": job["skills"]

        })


    # Highest score first

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results