from resume_parser import extract_resume_text
from jobs import get_all_jobs
from tfidf_matcher import calculate_text_similarity


# -----------------------------------------------------------
# LOAD RESUME
# -----------------------------------------------------------

file_path = "resumes/resume.pdf"

resume_text = extract_resume_text(
    file_path
)


# -----------------------------------------------------------
# GET JOBS
# -----------------------------------------------------------

jobs = get_all_jobs()


# -----------------------------------------------------------
# CALCULATE SIMILARITY
# -----------------------------------------------------------

print("----- TF-IDF JOB SIMILARITY -----")


for job in jobs:

    similarity = calculate_text_similarity(
        resume_text,
        job["description"]
    )

    print(
        f"{job['title']} → {similarity}%"
    )