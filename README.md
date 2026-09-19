
# 📄 Resume Screening & Job Recommendation System

An AI-based Resume Screening and Job Recommendation System built using Python, Streamlit, and Natural Language Processing (NLP).

The system analyzes a candidate's resume, extracts skills, compares them with available job requirements, calculates a job-match score, recommends suitable jobs, and provides resume improvement suggestions.

## 🚀 Features

- 📄 Upload resumes in PDF or DOCX format
- 📖 Extract text from resumes
- 🧠 Automatically extract candidate skills
- ⚖️ Weighted skill matching
- 📝 TF-IDF text similarity
- 🤖 Calculate final AI job-match score
- 💼 Recommend suitable jobs
- 🟢 Display matched skills
- 🔴 Display missing skills
- 💪 Identify resume strengths
- 📚 Identify skills to improve
- 💡 Generate resume improvement suggestions
- 📊 Visualize job-match scores
- 🌐 Interactive Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- pypdf
- python-docx
- Regular Expressions (Regex)
- TF-IDF
- Cosine Similarity

## 🧠 How It Works

```text
Resume Upload
      ↓
Resume Text Extraction
      ↓
Skill Extraction
      ↓
Weighted Skill Matching
      ↓
TF-IDF Text Similarity
      ↓
Final Match Score
      ↓
Job Recommendation
      ↓
Resume Insights

## 🤖 AI Matching Methodology

The system uses two main techniques.

### 1. Weighted Skill Matching

The candidate's extracted skills are compared with the skills required for each job.

Different skills have different weights based on their importance.

### 2. TF-IDF Text Similarity

TF-IDF (Term Frequency-Inverse Document Frequency) converts the resume and job description into numerical vectors.

Cosine similarity is then used to measure the similarity between the resume and job description.

### 3. Final Match Score

The final score combines both methods:


Final Score =
(70% × Skill Score) +
(30% × TF-IDF Text Similarity)

## 📂 Project Structure


Resume_Job_Description/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── skill_weights.py
├── jobs.py
├── job_matcher.py
├── tfidf_matcher.py
├── final_matcher.py
├── resume_insights.py
│
├── test_parser.py
├── test_jobs.py
├── test_matching.py
├── test_weights.py
├── test_tfidf.py
├── test_final.py
├── test_insights.py
│
├── requirements.txt
├── .gitignore
└── README.md


## 📌 Main Modules

### `app.py`

Main Streamlit application that provides the user interface and connects all modules.

### `resume_parser.py`

Extracts text from PDF and DOCX resumes.

### `skill_extractor.py`

Detects technical and professional skills from the extracted resume text.

### `skill_weights.py`

Contains weights assigned to different skills for job matching.

### `jobs.py`

Contains job descriptions, companies, locations, and required skills.

### `tfidf_matcher.py`

Calculates text similarity between the resume and job descriptions using TF-IDF and cosine similarity.

### `final_matcher.py`

Combines weighted skill matching and TF-IDF similarity to calculate the final job-match score.

### `resume_insights.py`

Generates resume strengths, missing skills, and improvement suggestions.

## 💻 Installation

### 1. Clone the repository

git clone https://github.com/Hassan-13-2006/resume-screening-job-recommendation.git


### 2. Open the project folder

cd resume-screening-job-recommendation


### 3. Create a virtual environment

python -m venv venv


### 4. Activate the virtual environment

#### Windows

venv\Scripts\activate

#### Linux/macOS

source venv/bin/activate

### 5. Install dependencies

pip install -r requirements.txt

## ▶️ Run the Application

Run:

streamlit run app.py

The application will open in your browser.

## 📄 How to Use

1. Open the application.
2. Upload your resume in PDF or DOCX format.
3. Click **Analyze Resume**.
4. The system extracts the resume text.
5. Skills are automatically detected.
6. The resume is compared with available jobs.
7. Match scores are calculated.
8. Recommended jobs are displayed.
9. Matched and missing skills are shown.
10. Resume strengths and improvement suggestions are generated.

## 📊 Example Output

Job: Frontend Developer

Final AI Match: 56.33%
Skill Score: 73.33%
Text Similarity: 16.68%

Matched Skills:
HTML
CSS
JavaScript
Git
GitHub

Missing Skills:
React

The actual results depend on the resume uploaded by the user.

## 🎯 Objectives

- Automate basic resume screening.
- Reduce manual job-search effort.
- Match candidate skills with job requirements.
- Identify missing skills.
- Recommend suitable jobs.
- Provide resume improvement suggestions.

## ✅ Advantages

- Simple and easy to use
- Fast resume analysis
- Supports PDF and DOCX resumes
- Provides explainable matching results
- Shows matched and missing skills
- Provides resume improvement suggestions
- Runs locally
- Does not require an external AI API

## ⚠️ Limitations

- Skill extraction depends on the predefined skill database.
- The system may not recognize completely new or unusual skill names.
- Job data is currently predefined.
- TF-IDF mainly measures textual similarity and does not fully understand semantic meaning.
- The current system does not use a large language model or transformer-based model.

## 🔮 Future Scope

The project can be improved by adding:

- Transformer-based NLP models
- Semantic embeddings
- Larger real-world job databases
- Automatic job-data collection
- Resume section analysis
- Experience-level detection
- Education matching
- Personalized learning recommendations
- More advanced resume scoring
- Deployment as a public web application

## 🎓 Project Information

**Project Type:** Academic AI & NLP Project

**Domain:**
- Artificial Intelligence
- Natural Language Processing
- Machine Learning
- Resume Screening
- Job Recommendation

## 👨‍💻 Author

**Khan Mohd Hassan Mohd Saeed**

GitHub:  
https://github.com/Hassan-13-2006

## 📜 License

This project is developed for educational and academic purposes.
