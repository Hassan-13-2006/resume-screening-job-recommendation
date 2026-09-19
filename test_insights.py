from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from final_matcher import analyze_jobs
from resume_insights import generate_resume_insights


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


insights = generate_resume_insights(
    resume_skills,
    results
)


print("----- RESUME INSIGHTS -----")


print("\n💪 STRENGTHS")

for strength in insights["strengths"]:

    print("✓", strength)


print("\n📚 SKILLS TO IMPROVE")

for skill in insights["missing_skills"]:

    print("→", skill)


print("\n💡 SUGGESTIONS")

for suggestion in insights["suggestions"]:

    print("•", suggestion)