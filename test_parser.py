from resume_parser import extract_resume_text
from skill_extractor import extract_skills


file_path = "resumes/resume.pdf"

# Extract resume text
text = extract_resume_text(file_path)

print("----- RESUME TEXT -----")
print(text)

# Extract skills
skills = extract_skills(text)

print("\n----- EXTRACTED SKILLS -----")

for skill in skills:
    print("✓", skill)