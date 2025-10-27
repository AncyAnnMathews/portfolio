import streamlit as st

# === PAGE CONFIG ===
st.set_page_config(
    page_title="Ancy Mathews – Python Developer & AI/ML Enthusiast",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === FORCE LIGHT MODE VIA CSS (overrides OS/browser preference) ===
st.markdown("""
<style>
    /* Hide Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Enforce light theme globally */
    html, body, [class*="css"] {
        background-color: #ffffff !important;
        color: #2d3748 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #3498db, #8e44ad);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        font-size: 1.3rem;
        color: #3498db;
        margin-bottom: 1.5rem;
    }

    .contact-badge {
        display: inline-block;
        background: #f8f9fa;
        color: #2980b9;
        padding: 0.35rem 1rem;
        border-radius: 30px;
        font-weight: 600;
        margin: 0.2rem 0.6rem 0.2rem 0;
        box-shadow: 0 2px 4px rgba(52, 152, 219, 0.1);
    }

    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 2.5rem 0 1.2rem;
        padding-bottom: 0.4rem;
        border-bottom: 3px solid #3498db;
        display: inline-block;
    }

    .project-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.4rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        transition: transform 0.2s ease;
        border-left: 4px solid #3498db;
    }
    .project-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }

    .project-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.3rem;
    }

    .project-tech {
        font-size: 0.95rem;
        color: #7f8c8d;
        font-style: italic;
        margin-bottom: 0.6rem;
    }

    .timeline-item {
        padding-left: 1.2rem;
        border-left: 2px solid #3498db;
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        color: #2d3748;
    }
    .timeline-item:last-child {
        border-left: 2px dashed #bdc3c7;
    }

    a {
        color: #2980b9 !important;
        font-weight: 600;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    .footer-note {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #7f8c8d;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# === HEADER ===
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Use your actual photo if available; fallback to placeholder
    try:
        st.image("  ", width=250)
    except:
        st.image("https://via.placeholder.com/250/3498db/ffffff?text=Ancy", width=250)

with col2:
    st.markdown('<div class="main-title">Ancy Mathews</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">B.Tech in Information Technology • Python Developer • AI/ML Enthusiast</div>', unsafe_allow_html=True)
    st.markdown(
        '''
        <span class="contact-badge">📧 ancymathews2003@gmail.com</span>
        <span class="contact-badge">📱 +91-9072294122</span>
        <span class="contact-badge">🔗 <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a></span>
        <span class="contact-badge">💻 <a href="https://github.com/yourusername" target="_blank">GitHub</a></span>
        ''',
        unsafe_allow_html=True
    )

# === CAREER OBJECTIVE ===
st.markdown('<div class="section-header">🎯 Career Objective</div>', unsafe_allow_html=True)
st.write("""
Motivated and detail-oriented B.Tech student in Information Technology with strong foundational skills in programming, web development, and machine learning. Seeking opportunities to apply technical knowledge in real-world projects, gain professional experience, and contribute to impactful tech initiatives.
""")

# === EDUCATION & SKILLS ===
st.markdown('<div class="section-header">🎓 Education & Skills</div>', unsafe_allow_html=True)
edu_col, skills_col = st.columns(2, gap="large")

with edu_col:
    st.markdown("### Education")
    st.markdown("""
    - **B.Tech in Information Technology** (2022–Present)  
      Government Engineering College, Barton Hill  
      **CGPA: 8.54/10**

    - **Higher Secondary (12th)** – Government Model HSS, Kerala  
      **98.33%** (2022)

    - **Secondary (10th)** – Mar Thoma Central School (CBSE)  
      **88.88%** (2020)
    """)

with skills_col:
    st.markdown("### Technical Skills")
    st.markdown("""
    - **Languages**: Python, C, Java  
    - **Tools & Platforms**: VS Code, SQL  
    - **Core Concepts**: Data Structures, Algorithms, OOP, DBMS, Web Development
    """)

# === PROJECTS ===
st.markdown('<div class="section-header">🚀 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Smart Gym Coach (Ongoing)",
        "tech": "Python, AI/ML",
        "desc": "Web-based real-time AI fitness system that detects and corrects form errors during exercises like squats and planks."
    },
    {
        "title": "Resume Screener",
        "tech": "Python, Streamlit",
        "desc": "Upload multiple resumes + job description; app scores and ranks candidates using weighted skill matching.",
        "link": "https://resume-screener-app-en5ytaf7fstzyridvzkuvt.streamlit.app/"
    },
    {
        "title": "Weather Forecasting using Stacked LSTM",
        "tech": "Python, AI/ML",
        "desc": "Sequence-to-sequence LSTM model to predict hourly weather for the next 7 days using time-series data."
    },
    {
        "title": "Train Ticket Booking System",
        "tech": "MySQL",
        "desc": "Database-backed reservation system with modules for booking, scheduling, and user registration."
    }
]

for i in range(0, len(projects), 2):
    cols = st.columns(2, gap="medium")
    for j, col in enumerate(cols):
        if i + j < len(projects):
            p = projects[i + j]
            with col:
                link_html = f'<br><a href="{p["link"]}" target="_blank">🔗 Live Demo</a>' if "link" in p else ''
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{p['title']}</div>
                    <div class="project-tech">{p['tech']}</div>
                    <div class="project-desc">{p['desc']}</div>
                    {link_html}
                </div>
                """, unsafe_allow_html=True)

# === EXPERIENCE & VOLUNTEERING ===
st.markdown('<div class="section-header">💼 Experience & Leadership</div>', unsafe_allow_html=True)
exp_col, vol_col = st.columns(2, gap="large")

with exp_col:
    st.markdown("### Internships & Roles")
    st.markdown("""
    <div class="timeline-item">
        <strong>Python Development Intern</strong> – CodSoft<br>
        <em>Jun–Jul 2025</em><br>
        Built automation scripts and terminal games; strengthened programming fundamentals and logical problem-solving.
    </div>
    
    <div class="timeline-item">
        <strong>Project Mentor</strong> – CSI Projectaro 5.0<br>
        Guided development of a Flutter QR Code Scanner app; reviewed code and ensured timely delivery.
    </div>

    <div class="timeline-item">
        <strong>Event Organizer</strong> – CSI Scripting Showdown<br>
        Managed campus-wide scripting competition from promotion to execution.
    </div>
    """, unsafe_allow_html=True)

with vol_col:
    st.markdown("### Volunteering & Achievements")
    st.markdown("""
    <div class="timeline-item">
        <strong>Recognized Volunteer</strong><br>
        CSI IGNITE Techfest & ARISE Summer Camp
    </div>
    
    <div class="timeline-item">
        <strong>Project Completion</strong><br>
        CSI Projectaro 3.0 – Built a validated Calculator app with UI
    </div>

    <div class="timeline-item">
        <strong>FOSS Cell & NSS Volunteer</strong><br>
        Promoted open-source awareness and engaged in social/environmental initiatives.
    </div>

    <div class="timeline-item">
        <strong>Active CSI Member (2023–24)</strong><br>
        Participated in coding contests, workshops, and tech talks.
    </div>
    """, unsafe_allow_html=True)

# === FOOTER ===
st.markdown('<div class="footer-note">✨ Portfolio built with Streamlit • Last updated: October 2025</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center;"><a href="Resume.pdf" target="_blank">📄 Download Full Resume</a></div>', unsafe_allow_html=True)
