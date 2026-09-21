import streamlit as st
import os

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from final_matcher import analyze_jobs
from resume_insights import generate_resume_insights


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .job-card {
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 12px;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("📌 About")

    st.write(
        """
        **AI Resume Screening & Job Recommendation System**

        This system:

        • Extracts resume text  
        • Detects candidate skills  
        • Compares skills with jobs  
        • Uses TF-IDF text similarity  
        • Calculates final match scores  
        • Recommends suitable jobs  
        • Provides resume improvement insights
        """
    )

    st.divider()

    st.write("### 🛠️ Technologies")

    st.write(
        """
        Python  
        Streamlit  
        Scikit-learn  
        Pandas  
        pypdf  
        python-docx
        """
    )


# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📄 AI Resume Screening & Job Recommendation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload your resume and discover suitable job opportunities using AI-based matching.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

st.subheader("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if uploaded_file is not None:

    st.info(
        f"Selected file: **{uploaded_file.name}**"
    )

    analyze_button = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )

    if analyze_button:

        file_path = os.path.join(
            os.getcwd(),
            uploaded_file.name
        )

        # --------------------------------------------------
        # SAVE UPLOADED FILE
        # --------------------------------------------------

        with open(file_path, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )

        try:

            # --------------------------------------------------
            # EXTRACT RESUME TEXT
            # --------------------------------------------------

            with st.spinner(
                "📖 Extracting resume text..."
            ):

                resume_text = extract_resume_text(
                    file_path
                )


            # --------------------------------------------------
            # EXTRACT SKILLS
            # --------------------------------------------------

            with st.spinner(
                "🔎 Detecting skills..."
            ):

                resume_skills = extract_skills(
                    resume_text
                )


            # --------------------------------------------------
            # ANALYZE JOBS
            # --------------------------------------------------

            with st.spinner(
                "🤖 Calculating AI job matches..."
            ):

                results = analyze_jobs(
                    resume_text,
                    resume_skills
                )


            # --------------------------------------------------
            # GENERATE RESUME INSIGHTS
            # --------------------------------------------------

            with st.spinner(
                "💡 Generating resume insights..."
            ):

                insights = generate_resume_insights(
                    resume_skills,
                    results
                )


            # --------------------------------------------------
            # EXTRACTED SKILLS
            # --------------------------------------------------

            st.markdown(
                '<div class="section-title">🧠 Extracted Skills</div>',
                unsafe_allow_html=True
            )

            if resume_skills:

                columns = st.columns(4)

                for index, skill in enumerate(
                    resume_skills
                ):

                    columns[
                        index % 4
                    ].success(
                        f"✓ {skill}"
                    )

            else:

                st.warning(
                    "No skills detected from the resume."
                )


            # --------------------------------------------------
            # TOP RECOMMENDATION
            # --------------------------------------------------

            if results:

                top_job = results[0]

                st.markdown(
                    '<div class="section-title">🏆 Top Job Recommendation</div>',
                    unsafe_allow_html=True
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Recommended Job",
                        top_job["title"]
                    )

                with col2:

                    st.metric(
                        "Final AI Match",
                        f'{top_job["score"]}%'
                    )

                with col3:

                    st.metric(
                        "Location",
                        top_job["location"]
                    )


            # --------------------------------------------------
            # ALL JOB RECOMMENDATIONS
            # --------------------------------------------------

            st.markdown(
                '<div class="section-title">💼 Job Recommendations</div>',
                unsafe_allow_html=True
            )


            for index, job in enumerate(results):

            


                # Job title

                st.subheader(
                    f"{index + 1}. {job['title']}"
                )


                # Company

                st.write(
                    f"🏢 **Company:** {job['company']}"
                )


                # Location

                st.write(
                    f"📍 **Location:** {job['location']}"
                )


                # --------------------------------------------------
                # SCORES
                # --------------------------------------------------

                score_col1, score_col2, score_col3 = st.columns(3)


                with score_col1:

                    st.metric(
                        "🤖 Final AI Match",
                        f'{job["score"]}%'
                    )


                with score_col2:

                    st.metric(
                        "🛠️ Skill Score",
                        f'{job["skill_score"]}%'
                    )


                with score_col3:

                    st.metric(
                        "📝 Text Similarity",
                        f'{job["text_similarity"]}%'
                    )


                # --------------------------------------------------
                # FINAL SCORE PROGRESS BAR
                # --------------------------------------------------

                st.progress(
                    min(
                        int(job["score"]),
                        100
                    )
                )


                # --------------------------------------------------
                # MATCHED SKILLS
                # --------------------------------------------------

                st.write(
                    "🟢 **Matched Skills**"
                )

                if job["matched_skills"]:

                    st.write(
                        ", ".join(
                            job["matched_skills"]
                        )
                    )

                else:

                    st.write(
                        "No matching skills found."
                    )


                # --------------------------------------------------
                # MISSING SKILLS
                # --------------------------------------------------

                st.write(
                    "🔴 **Missing Skills**"
                )

                if job["missing_skills"]:

                    st.write(
                        ", ".join(
                            job["missing_skills"]
                        )
                    )

                else:

                    st.write(
                        "No major missing skills."
                    )


                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            # --------------------------------------------------
            # RESUME INSIGHTS
            # --------------------------------------------------

            st.markdown(
                '<div class="section-title">💡 Resume Insights</div>',
                unsafe_allow_html=True
            )


            # --------------------------------------------------
            # STRENGTHS AND SKILLS TO IMPROVE
            # --------------------------------------------------

            col1, col2 = st.columns(2)


            with col1:

                st.subheader(
                    "💪 Resume Strengths"
                )

                if insights["strengths"]:

                    for strength in insights["strengths"]:

                        st.success(
                            f"✓ {strength}"
                        )

                else:

                    st.info(
                        "No specific strengths detected."
                    )


            with col2:

                st.subheader(
                    "📚 Skills to Improve"
                )

                if insights["missing_skills"]:

                    for skill in insights["missing_skills"]:

                        st.warning(
                            f"→ {skill}"
                        )

                else:

                    st.success(
                        "No major skill gaps detected."
                    )


            # --------------------------------------------------
            # IMPROVEMENT SUGGESTIONS
            # --------------------------------------------------

            st.subheader(
                "💡 Improvement Suggestions"
            )


            for suggestion in insights["suggestions"]:

                st.info(
                    f"• {suggestion}"
                )


            # --------------------------------------------------
            # JOB SCORE CHART
            # --------------------------------------------------

            st.markdown(
                '<div class="section-title">📊 Job Match Comparison</div>',
                unsafe_allow_html=True
            )


            chart_data = {
                job["title"]: job["score"]
                for job in results
            }


            st.bar_chart(
                chart_data
            )


            # --------------------------------------------------
            # SUCCESS MESSAGE
            # --------------------------------------------------

            st.success(
                "✅ Resume analysis completed successfully!"
            )


        except Exception as error:

            st.error(
                f"❌ Error while analyzing resume: {error}"
            )


        finally:

            # --------------------------------------------------
            # REMOVE UPLOADED FILE
            # --------------------------------------------------

            if os.path.exists(file_path):

                os.remove(file_path)