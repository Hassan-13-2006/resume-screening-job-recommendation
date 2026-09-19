from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from final_matcher import analyze_jobs


file_path = "resumes/resume.pdf"


resume_text = extract_resume_text(
    file_path
)


resume_skills = extract_skills(
    resume_text
)


results = analyze_jobs(
    resume_text,
    resume_skills
)


print("----- FINAL AI JOB MATCH -----")


for job in results:

    print(
        f"\n{job['title']} - "
        f"{job['score']}%"
    )

    print(
        f"Skill Score: "
        f"{job['skill_score']}%"
    )

    print(
        f"Text Similarity: "
        f"{job['text_similarity']}%"
    )

    print(
        "Matched Skills:",
        ", ".join(job["matched_skills"])
    )

    print(
        "Missing Skills:",
        ", ".join(job["missing_skills"])
    )