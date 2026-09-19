from skill_weights import SKILL_WEIGHTS


def get_skill_weight(skill):

    for skill_name, weight in SKILL_WEIGHTS.items():

        if skill_name.lower() == skill.lower():
            return weight

    return 1.0


def get_resume_strengths(resume_skills):

    strengths = []

    if len(resume_skills) >= 5:
        strengths.append(
            "Good variety of technical and professional skills."
        )

    if "Python" in resume_skills:
        strengths.append(
            "Python knowledge is useful for software development, "
            "data analysis and AI/ML roles."
        )

    if "Java" in resume_skills:
        strengths.append(
            "Java knowledge can support software development opportunities."
        )

    if "JavaScript" in resume_skills:
        strengths.append(
            "JavaScript knowledge is useful for web development roles."
        )

    if "HTML" in resume_skills and "CSS" in resume_skills:
        strengths.append(
            "HTML and CSS provide a foundation for frontend development."
        )

    if "Git" in resume_skills and "GitHub" in resume_skills:
        strengths.append(
            "Git and GitHub experience is useful for collaborative software development."
        )

    if "Communication" in resume_skills:
        strengths.append(
            "Communication is a useful professional skill."
        )

    if "Problem Solving" in resume_skills:
        strengths.append(
            "Problem-solving is valuable across technical roles."
        )

    return strengths


def get_missing_skills(results, top_n=3):

    missing_skills = {}

    for job in results[:top_n]:

        for skill in job["missing_skills"]:

            if skill not in missing_skills:
                missing_skills[skill] = 0

            missing_skills[skill] += get_skill_weight(skill)

    sorted_skills = sorted(
        missing_skills.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        skill
        for skill, weight in sorted_skills
    ]


def get_improvement_suggestions(
    resume_skills,
    results
):

    suggestions = []

    if not resume_skills:

        suggestions.append(
            "Add technical skills to your resume."
        )

        return suggestions

    if len(resume_skills) < 5:

        suggestions.append(
            "Consider adding more relevant technical skills "
            "that you have actually learned or used."
        )

    if results:

        top_job = results[0]

        if top_job["missing_skills"]:

            suggestions.append(
                f"Learn or strengthen these skills for "
                f"{top_job['title']}: "
                + ", ".join(top_job["missing_skills"][:5])
                + "."
            )

    if "Git" not in resume_skills:

        suggestions.append(
            "Consider learning Git for version control."
        )

    if "GitHub" not in resume_skills:

        suggestions.append(
            "Add GitHub projects to demonstrate your practical work."
        )

    suggestions.append(
        "Add measurable project achievements and clear project descriptions."
    )

    suggestions.append(
        "Keep the resume focused on skills and projects relevant to the jobs you want."
    )

    return suggestions


def generate_resume_insights(
    resume_skills,
    results
):

    strengths = get_resume_strengths(
        resume_skills
    )

    missing_skills = get_missing_skills(
        results
    )

    suggestions = get_improvement_suggestions(
        resume_skills,
        results
    )

    return {
        "strengths": strengths,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }