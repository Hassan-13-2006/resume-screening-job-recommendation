# ============================================================
# JOB DATABASE
# ============================================================

JOBS = [

    # --------------------------------------------------------
    # 1. PYTHON DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Python Developer",
        "company": "Tech Solutions",
        "location": "Bangalore",

        "description": """
        We are looking for a Python Developer to develop and
        maintain web applications and backend services. The
        candidate should have experience with Python, Django,
        Flask, SQL, REST API, Git and GitHub. Knowledge of
        software development and problem solving is preferred.
        """,

        "skills": [
            "Python",
            "Django",
            "Flask",
            "SQL",
            "REST API",
            "Git",
            "GitHub"
        ]
    },


    # --------------------------------------------------------
    # 2. JAVA DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Java Developer",
        "company": "Software Systems",
        "location": "Bangalore",

        "description": """
        We are looking for a Java Developer to design, develop
        and maintain software applications. The candidate should
        have strong knowledge of Java, Spring Boot, SQL, REST API,
        Git and GitHub. Good understanding of software development,
        object oriented programming and problem solving is preferred.
        """,

        "skills": [
            "Java",
            "Spring Boot",
            "SQL",
            "REST API",
            "Git",
            "GitHub"
        ]
    },


    # --------------------------------------------------------
    # 3. FRONTEND DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Frontend Developer",
        "company": "Web Technologies",
        "location": "Bangalore",

        "description": """
        We are looking for a Frontend Developer to build
        responsive and user-friendly web applications. The
        candidate should have experience with HTML, CSS,
        JavaScript and React. Knowledge of Git and GitHub,
        responsive design and user interface development
        is required.
        """,

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
            "GitHub"
        ]
    },


    # --------------------------------------------------------
    # 4. FULL STACK DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Full Stack Developer",
        "company": "Digital Solutions",
        "location": "Bangalore",

        "description": """
        We are looking for a Full Stack Developer to develop
        complete web applications from frontend to backend.
        The candidate should have experience with HTML, CSS,
        JavaScript, React, Node.js, Express.js, MongoDB, Git
        and GitHub. Knowledge of REST APIs and responsive web
        development is preferred.
        """,

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Express.js",
            "MongoDB",
            "Git",
            "GitHub"
        ]
    },


    # --------------------------------------------------------
    # 5. DATA ANALYST
    # --------------------------------------------------------

    {
        "title": "Data Analyst",
        "company": "Data Insights",
        "location": "Bangalore",

        "description": """
        We are looking for a Data Analyst to collect, clean
        and analyze data and create useful business insights.
        The candidate should have knowledge of Python, SQL,
        Pandas, NumPy, Excel, Power BI and data analysis.
        Data visualization, statistics and problem solving
        skills are also useful.
        """,

        "skills": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Excel",
            "Power BI",
            "Data Analysis"
        ]
    },


    # --------------------------------------------------------
    # 6. MACHINE LEARNING ENGINEER
    # --------------------------------------------------------

    {
        "title": "Machine Learning Engineer",
        "company": "AI Technologies",
        "location": "Bangalore",

        "description": """
        We are looking for a Machine Learning Engineer to
        build, train and evaluate machine learning models.
        The candidate should have experience with Python,
        Machine Learning, Scikit-learn, Pandas and NumPy.
        Knowledge of SQL, data preprocessing, feature
        engineering and model evaluation is preferred.
        """,

        "skills": [
            "Python",
            "Machine Learning",
            "Scikit-learn",
            "Pandas",
            "NumPy",
            "SQL",
            "Git"
        ]
    },


    # --------------------------------------------------------
    # 7. AI ENGINEER
    # --------------------------------------------------------

    {
        "title": "AI Engineer",
        "company": "Artificial Intelligence Labs",
        "location": "Bangalore",

        "description": """
        We are looking for an AI Engineer to develop artificial
        intelligence and machine learning solutions. The candidate
        should have knowledge of Python, Artificial Intelligence,
        Machine Learning, Deep Learning, TensorFlow and PyTorch.
        Experience with neural networks, model training and
        problem solving is preferred.
        """,

        "skills": [
            "Python",
            "Artificial Intelligence",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Git"
        ]
    },


    # --------------------------------------------------------
    # 8. SOFTWARE DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Software Developer",
        "company": "IT Solutions",
        "location": "Bangalore",

        "description": """
        We are looking for a Software Developer to design,
        develop, test and maintain software applications.
        The candidate should have programming experience in
        Python, Java and C, along with knowledge of data
        structures, algorithms, SQL, Git and GitHub.
        Strong problem solving and software development
        skills are important.
        """,

        "skills": [
            "Python",
            "Java",
            "C",
            "Data Structures",
            "Algorithms",
            "SQL",
            "Git",
            "GitHub"
        ]
    },


    # --------------------------------------------------------
    # 9. BACKEND DEVELOPER
    # --------------------------------------------------------

    {
        "title": "Backend Developer",
        "company": "Cloud Systems",
        "location": "Bangalore",

        "description": """
        We are looking for a Backend Developer to build
        reliable server-side applications and APIs. The
        candidate should have experience with Python,
        Node.js, Express.js, SQL, MongoDB and REST API
        development. Knowledge of Git, GitHub and backend
        architecture is preferred.
        """,

        "skills": [
            "Python",
            "Node.js",
            "Express.js",
            "SQL",
            "MongoDB",
            "REST API",
            "Git"
        ]
    },


    # --------------------------------------------------------
    # 10. CYBER SECURITY INTERN
    # --------------------------------------------------------

    {
        "title": "Cyber Security Intern",
        "company": "SecureTech",
        "location": "Bangalore",

        "description": """
        We are looking for a Cyber Security Intern to assist
        with security monitoring, network security and
        vulnerability analysis. The candidate should have
        knowledge of Cybersecurity, Computer Networks,
        Network Security, Linux, Python and Git. Basic
        knowledge of ethical hacking and information security
        is beneficial.
        """,

        "skills": [
            "Cybersecurity",
            "Network Security",
            "Linux",
            "Python",
            "Computer Networks",
            "Git"
        ]
    }

]


# ============================================================
# GET ALL JOBS
# ============================================================

def get_all_jobs():
    return JOBS