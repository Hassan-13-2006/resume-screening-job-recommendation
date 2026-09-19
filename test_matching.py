from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from job_matcher import match_jobs


file_path = "resumes/resume.pdf"

resume_text = extract_resume_text(file_path)

resume_skills = extract_skills(resume_text)

results = match_jobs(resume_skills)


print("----- JOB RECOMMENDATIONS -----")

for job in results:

    print(f"\n{job['title']} - {job['score']}%")

    print(f"Company: {job['company']}")

    print(
        "Matched Skills:",
        ", ".join(job["matched_skills"])
    )

    print(
        "Missing Skills:",
        ", ".join(job["missing_skills"])
    )