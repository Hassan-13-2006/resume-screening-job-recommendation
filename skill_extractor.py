# ============================================================
# SKILL DATABASE
# ============================================================

SKILLS = [

    # ---------------- PROGRAMMING LANGUAGES ----------------
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
    "Go", "Golang", "Rust", "Kotlin", "Swift", "Dart", "PHP",
    "Ruby", "R", "Scala", "Perl", "MATLAB", "Bash", "Shell",
    "PowerShell", "Objective-C", "Lua", "Groovy",

    # ---------------- WEB DEVELOPMENT ----------------
    "HTML", "HTML5", "CSS", "CSS3", "Sass", "SCSS", "Bootstrap",
    "Tailwind CSS", "Material UI", "JavaScript", "React", "React.js",
    "Angular", "Vue", "Vue.js", "Next.js", "Nuxt.js",
    "Node.js", "Express.js", "Express", "Django", "Flask",
    "FastAPI", "Spring", "Spring Boot", "ASP.NET", ".NET",
    "Laravel", "Ruby on Rails", "jQuery", "Redux",
    "GraphQL", "REST API", "RESTful API", "WebSockets",

    # ---------------- FRONTEND ----------------
    "Frontend Development", "Front End Development",
    "Responsive Design", "UI Development", "UX Design",
    "User Interface", "User Experience", "DOM", "AJAX",
    "JSON", "XML",

    # ---------------- DATABASES ----------------
    "SQL", "MySQL", "PostgreSQL", "Oracle", "SQLite",
    "Microsoft SQL Server", "SQL Server", "MongoDB",
    "MongoDB Atlas", "Redis", "Firebase", "Firestore",
    "Cassandra", "DynamoDB", "MariaDB", "Neo4j",
    "Database Management", "DBMS", "PL/SQL",

    # ---------------- AI / MACHINE LEARNING ----------------
    "Artificial Intelligence", "AI", "Machine Learning", "ML",
    "Deep Learning", "Natural Language Processing", "NLP",
    "Computer Vision", "Generative AI", "GenAI",
    "Large Language Models", "LLM", "Neural Networks",
    "Artificial Neural Networks", "ANN", "Reinforcement Learning",
    "Supervised Learning", "Unsupervised Learning",
    "Semi-Supervised Learning", "Transfer Learning",
    "Feature Engineering", "Model Training", "Model Evaluation",
    "Predictive Modeling", "Classification", "Regression",
    "Clustering", "Recommendation Systems",
    "Sentiment Analysis", "Text Classification",
    "Object Detection", "Image Classification",
    "Time Series", "Speech Recognition",

    # ---------------- AI / ML LIBRARIES ----------------
    "Scikit-learn", "Scikit Learn", "TensorFlow", "Keras",
    "PyTorch", "OpenCV", "Hugging Face", "Transformers",
    "XGBoost", "LightGBM", "CatBoost",
    "NLTK", "spaCy", "Gensim",
    "LangChain", "LlamaIndex",

    # ---------------- DATA SCIENCE ----------------
    "Data Science", "Data Analysis", "Data Analytics",
    "Data Visualization", "Statistics", "Probability",
    "Pandas", "NumPy", "Matplotlib", "Seaborn",
    "Plotly", "SciPy", "Jupyter Notebook",
    "Jupyter", "Google Colab", "Exploratory Data Analysis",
    "EDA", "Data Cleaning", "Data Preprocessing",
    "Data Mining", "ETL",

    # ---------------- CLOUD ----------------
    "Cloud Computing", "AWS", "Amazon Web Services",
    "Microsoft Azure", "Azure", "Google Cloud",
    "Google Cloud Platform", "GCP",
    "EC2", "S3", "Lambda", "RDS",
    "Azure Functions", "Azure Storage",
    "Cloud Deployment", "Cloud Architecture",

    # ---------------- DEVOPS ----------------
    "DevOps", "Docker", "Kubernetes", "Jenkins",
    "GitHub Actions", "GitLab CI", "CI/CD",
    "Continuous Integration", "Continuous Deployment",
    "Terraform", "Ansible", "Linux", "Unix",
    "Nginx", "Apache",

    # ---------------- VERSION CONTROL ----------------
    "Git", "GitHub", "GitLab", "Bitbucket",
    "Version Control", "Source Control",

    # ---------------- SOFTWARE ENGINEERING ----------------
    "Software Development", "Software Engineering",
    "Object Oriented Programming", "OOP",
    "Data Structures", "Algorithms", "DSA",
    "Design Patterns", "System Design",
    "SDLC", "Agile", "Scrum", "Kanban",
    "Software Testing", "Unit Testing", "Integration Testing",
    "Test Automation", "Debugging",

    # ---------------- TESTING ----------------
    "Selenium", "Cypress", "Playwright", "Postman",
    "JUnit", "PyTest", "pytest", "Jest",
    "Mocha", "Chai", "API Testing",
    "Manual Testing", "Automation Testing",

    # ---------------- MOBILE DEVELOPMENT ----------------
    "Android Development", "Android",
    "Android Studio", "Kotlin", "Java Android",
    "iOS Development", "iOS", "Swift",
    "Flutter", "React Native",
    "Mobile App Development",

    # ---------------- CYBER SECURITY ----------------
    "Cyber Security", "Cybersecurity", "Information Security",
    "Network Security", "Application Security",
    "Ethical Hacking", "Penetration Testing",
    "Vulnerability Assessment", "Cryptography",
    "Digital Forensics", "Incident Response",
    "OWASP", "Burp Suite", "Kali Linux",
    "Firewall", "SIEM",

    # ---------------- NETWORKING ----------------
    "Computer Networks", "Networking", "TCP/IP",
    "HTTP", "HTTPS", "DNS", "DHCP",
    "IP Addressing", "IPv4", "IPv6",
    "Routing", "Switching", "VPN",
    "LAN", "WAN", "OSI Model",
    "Network Administration",

    # ---------------- OPERATING SYSTEMS ----------------
    "Operating Systems", "Windows", "Linux",
    "Ubuntu", "Unix", "MacOS",
    "Process Management", "Memory Management",

    # ---------------- APIs / TOOLS ----------------
    "API", "REST", "Postman", "Swagger",
    "OpenAPI", "OAuth", "JWT",
    "Authentication", "Authorization",

    # ---------------- MICROSOFT / PRODUCTIVITY ----------------
    "Microsoft Office", "Microsoft Word", "Microsoft Excel",
    "Microsoft PowerPoint", "Excel", "Power BI",

    # ---------------- PROJECT MANAGEMENT ----------------
    "Project Management", "Team Management",
    "Leadership", "Communication", "Teamwork",
    "Time Management", "Problem Solving",
    "Critical Thinking", "Decision Making",

    # ---------------- BUSINESS / GENERAL ----------------
    "Business Analysis", "Business Intelligence",
    "Requirements Analysis", "Technical Documentation",
    "Documentation", "Research",

    # ---------------- BIG DATA ----------------
    "Big Data", "Hadoop", "Spark", "Apache Spark",
    "Hive", "Kafka", "Apache Kafka",

    # ---------------- DATA ENGINEERING ----------------
    "Data Engineering", "Data Pipeline",
    "Data Warehouse", "Data Lake",
    "Apache Airflow", "Snowflake", "Databricks",

    # ---------------- BLOCKCHAIN ----------------
    "Blockchain", "Ethereum", "Solidity",
    "Smart Contracts", "Web3",

    # ---------------- ROBOTICS / IOT ----------------
    "Robotics", "Internet of Things", "IoT",
    "Arduino", "Raspberry Pi", "Embedded Systems",

    # ---------------- OTHER COMMON SKILLS ----------------
    "GitHub Copilot", "VS Code", "Visual Studio",
    "IntelliJ IDEA", "Eclipse", "Sublime Text",
    "Linux Command Line", "Command Line",
    "Problem Solving", "Communication",
    "Presentation Skills", "Team Coordination"
]

# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {
    "js": "JavaScript",
    "javascript": "JavaScript",

    "reactjs": "React",
    "react.js": "React",

    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",

    "express": "Express.js",
    "expressjs": "Express.js",
    "express.js": "Express.js",

    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",

    "nlp": "Natural Language Processing",

    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    "mongo": "MongoDB",
    "mongodb": "MongoDB",

    "rest": "REST API",
    "restful api": "REST API",

    "git": "Git",
    "github": "GitHub"
}
# ============================================================
# SKILL EXTRACTION FUNCTION
# ============================================================

import re


def extract_skills(resume_text):

    found_skills = []

    resume_text_lower = resume_text.lower()

    for skill in SKILLS:

        skill_lower = skill.lower()

        if len(skill_lower) <= 3:

            pattern = r"\b" + re.escape(skill_lower) + r"\b"

            if re.search(pattern, resume_text_lower):
                found_skills.append(skill)

        else:

            if skill_lower in resume_text_lower:
                found_skills.append(skill)

    # Remove duplicates
    found_skills = list(dict.fromkeys(found_skills))

    # Add normalized aliases
    for alias, standard_skill in SKILL_ALIASES.items():

        pattern = r"\b" + re.escape(alias) + r"\b"

        if re.search(pattern, resume_text_lower):

            if standard_skill not in found_skills:
                found_skills.append(standard_skill)

    return found_skills