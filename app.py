import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="NERCHUKO | Online Learning",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}



section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1e293b 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.brand {
    font-size: 31px;
    font-weight: 800;
    color: white;
    letter-spacing: 1px;
}

.brand-sub {
    color: #94a3b8 !important;
    font-size: 13px;
    margin-top: 5px;
    margin-bottom: 25px;
}



.welcome {
    font-size: 35px;
    font-weight: 800;
    color: #111827;
}

.welcome-sub {
    font-size: 16px;
    color: #64748b;
    margin-top: 5px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #111827;
    margin-top: 30px;
    margin-bottom: 18px;
}


.course-hero {
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    border-radius: 18px;
    padding: 30px;
    color: white;
    box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
    margin-bottom: 20px;
}

.course-hero h2 {
    color: white;
    font-size: 27px;
    margin: 0 0 10px 0;
}

.course-hero p {
    color: #e0e7ff;
    font-size: 15px;
    margin: 0;
}


.skill {
    display: inline-block;
    background-color: #eff6ff;
    color: #2563eb;
    padding: 8px 14px;
    border-radius: 20px;
    margin: 4px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #dbeafe;
}



.achievement {
    background-color: white;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
    min-height: 150px;
}

.achievement-icon {
    font-size: 34px;
    margin-bottom: 10px;
}

.achievement-title {
    font-size: 17px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 7px;
}

.achievement-sub {
    font-size: 13px;
    color: #64748b;
}


.profile-card {
    background-color: white;
    border-radius: 18px;
    padding: 30px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
}

.profile-avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 15px;
}

.profile-name {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
}

.profile-role {
    color: #64748b;
    font-size: 14px;
}


.footer {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.markdown(
        """
        <div class="brand">🎓 NERCHUKO</div>
        <div class="brand-sub">Learn. Build. Grow.</div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### MENU")

    page = st.radio(
        "",
        [
            "🏠 Dashboard",
            "👤 My Profile",
            "📚 My Courses",
            "📊 Analytics",
            "🏆 Achievements"
        ]
    )

    st.divider()

    st.markdown("### ⚡ Learning Streak")

    st.metric(
        "Current Streak",
        "12 Days",
        "+2"
    )

    st.caption("Keep learning every day! 🔥")



if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="welcome">
            Welcome back, Bharadhwaj! 👋
        </div>

        <div class="welcome-sub">
            Continue your learning journey and achieve your goals.
        </div>
        """,
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Courses",
            "4",
            "+1"
        )

    with col2:
        st.metric(
            "📈 Overall Progress",
            "58%",
            "+8%"
        )

    with col3:
        st.metric(
            "⏱ Learning Hours",
            "46.5",
            "+6.2"
        )

    with col4:
        st.metric(
            "🏆 Certificates",
            "2",
            "+1"
        )


    st.markdown(
        '<div class="section-title">Continue Learning</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="course-hero">
            <h2>🐍 Python Programming</h2>
            <p>
                Master Python from fundamentals to advanced programming,
                data analysis and real-world projects.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        st.write("Course Progress")

        st.progress(0.72)

        st.write("**72% completed**")

    with col2:

        st.metric(
            "Lessons",
            "18 / 25"
        )

    with col3:

        st.metric(
            "Time Left",
            "6.5 hrs"
        )

    if st.button(
        "▶ Continue Learning",
        use_container_width=True
    ):
        st.success(
            "Opening Python Programming course..."
        )

  

    st.markdown(
        '<div class="section-title">Learning Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.5, 1])


    with col1:

        progress_data = pd.DataFrame({
            "Course": [
                "Python",
                "Data Analysis",
                "SQL",
                "Machine Learning"
            ],
            "Completion": [
                72,
                45,
                30,
                10
            ]
        })

        fig = px.bar(
            progress_data,
            x="Course",
            y="Completion",
            text="Completion",
            title="Course Completion"
        )

        fig.update_traces(
            texttemplate="%{text}%",
            textposition="outside"
        )

        fig.update_layout(
            yaxis=dict(
                range=[0, 100],
                title="Completion (%)"
            ),
            xaxis_title="",
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- SKILLS ----------------

    with col2:

        st.markdown(
            """
            <div class="section-title">
                🧠 Skills Learnt
            </div>
            """,
            unsafe_allow_html=True
        )

        skills = [
            "Python",
            "Pandas",
            "Functions",
            "SQL",
            "Data Analysis",
            "Problem Solving",
            "Git",
            "Statistics"
        ]

        for skill in skills:

            st.markdown(
                f'<span class="skill">{skill}</span>',
                unsafe_allow_html=True
            )


    st.markdown(
        '<div class="section-title">Recent Achievements</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="achievement">
                <div class="achievement-icon">🔥</div>

                <div class="achievement-title">
                    10 Day Streak
                </div>

                <div class="achievement-sub">
                    Learned for 10 consecutive days
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="achievement">
                <div class="achievement-icon">🐍</div>

                <div class="achievement-title">
                    Python Beginner
                </div>

                <div class="achievement-sub">
                    Completed Python fundamentals
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="achievement">
                <div class="achievement-icon">🏆</div>

                <div class="achievement-title">
                    First Certificate
                </div>

                <div class="achievement-sub">
                    Earned your first certificate
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )



elif page == "👤 My Profile":

    st.title("👤 My Profile")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown(
            """
            <div class="profile-card">

                <div class="profile-avatar">
                    B
                </div>

                <div class="profile-name">
                    Bharadhwaj
                </div>

                <div class="profile-role">
                    NERCHUKO Student
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.subheader("Personal Information")

        st.text_input(
            "Full Name",
            value="Bharadhwaj"
        )

        st.text_input(
            "Email",
            value="student@example.com"
        )

        st.text_input(
            "Contact",
            value="+91 9876543210"
        )

        st.text_input(
            "Ongoing Course",
            value="Python Programming"
        )

        if st.button(
            "💾 Save Changes",
            use_container_width=True
        ):

            st.success(
                "Profile updated successfully!"
            )


elif page == "📚 My Courses":

    st.title("📚 My Courses")

    courses = [
        ("🐍", "Python Programming", 72, "18 / 25 lessons"),
        ("📊", "Data Analysis", 45, "9 / 20 lessons"),
        ("🗄️", "SQL Database", 30, "6 / 20 lessons"),
        ("🤖", "Machine Learning", 10, "2 / 20 lessons")
    ]

    for icon, name, progress, lessons in courses:

        st.markdown(
            """
            <div style="
                background:white;
                padding:22px;
                border-radius:16px;
                margin-bottom:15px;
                border:1px solid #e5e7eb;
                box-shadow:0 5px 15px rgba(15,23,42,0.05);
            ">
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:

            st.markdown(
                f"### {icon} {name}"
            )

            st.caption(
                "Continue learning and improve your skills."
            )

        with col2:

            st.progress(
                progress / 100
            )

            st.caption(
                f"{progress}% completed • {lessons}"
            )

        with col3:

            st.metric(
                "Progress",
                f"{progress}%"
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


elif page == "📊 Analytics":

    st.title("📊 Learning Analytics")


    weekly_data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Hours": [
            1.5,
            2.0,
            1.2,
            2.5,
            3.0,
            4.2,
            2.8
        ]
    })

    fig = px.line(
        weekly_data,
        x="Day",
        y="Hours",
        markers=True,
        title="Weekly Learning Hours"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis_title="Hours",
        xaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    course_data = pd.DataFrame({
        "Course": [
            "Python",
            "Data Analysis",
            "SQL",
            "Machine Learning"
        ],
        "Hours": [
            20,
            12,
            8,
            6
        ]
    })

    fig2 = px.pie(
        course_data,
        names="Course",
        values="Hours",
        title="Learning Time Distribution",
        hole=0.45
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


elif page == "🏆 Achievements":

    st.title("🏆 Achievements")

    c1, c2, c3 = st.columns(3)

    achievements = [
        (
            "🔥",
            "10 Day Streak",
            "Learned for 10 consecutive days"
        ),
        (
            "🐍",
            "Python Beginner",
            "Completed Python fundamentals"
        ),
        (
            "📊",
            "Data Explorer",
            "Completed Data Analysis basics"
        ),
        (
            "🏆",
            "First Certificate",
            "Earned your first certificate"
        ),
        (
            "⚡",
            "Fast Learner",
            "Completed 5 lessons in one day"
        ),
        (
            "🎯",
            "Goal Setter",
            "Completed your weekly goal"
        )
    ]

    for index, achievement in enumerate(achievements):

        col = [c1, c2, c3][index % 3]

        with col:

            st.markdown(
                f"""
                <div class="achievement">

                    <div class="achievement-icon">
                        {achievement[0]}
                    </div>

                    <div class="achievement-title">
                        {achievement[1]}
                    </div>

                    <div class="achievement-sub">
                        {achievement[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

st.markdown(
    """
    <div class="footer">
        🎓 <strong>NERCHUKO</strong> — Learn. Build. Grow.<br>
        Your personalized online learning platform.
    </div>
    """,
    unsafe_allow_html=True
)
