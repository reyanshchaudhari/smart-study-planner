import streamlit as st

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Study Planner")
st.write("Create a personalized plan for every subject!")

subjects = st.multiselect(
    "Choose your subjects",
    [
        "Maths",
        "Science",
        "English",
        "Social Science",
        "Computer",
        "Hindi",
        "Marathi"
    ]
)

details = {}

# Ask for details for every selected subject
for subject in subjects:
    st.subheader(f"📖 {subject}")

    col1, col2, col3 = st.columns(3)

    with col1:
        hours = st.number_input(
            f"Study hours for {subject}",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.5,
            key=f"hours_{subject}"
        )

    with col2:
        difficulty = st.selectbox(
            f"Difficulty of {subject}",
            ["Easy", "Medium", "Hard"],
            key=f"difficulty_{subject}"
        )

    with col3:
        topic = st.text_input(
            f"Topic for {subject}",
            placeholder="e.g. Fractions",
            key=f"topic_{subject}"
        )

    details[subject] = {
        "hours": hours,
        "difficulty": difficulty,
        "topic": topic
    }

st.divider()

if st.button("✨ Create My Study Plan"):

    if not subjects:
        st.warning("Please select at least one subject!")

    else:
        st.success("Your personalized study plan is ready! 🎉")

        for subject in subjects:

            data = details[subject]

            hours = data["hours"]
            difficulty = data["difficulty"]
            topic = data["topic"]

            # Different study/revision split
            if difficulty == "Easy":
                study_percent = 0.60
            elif difficulty == "Medium":
                study_percent = 0.70
            else:
                study_percent = 0.80

            study_time = hours * study_percent
            revision_time = hours - study_time

            st.markdown(f"## 📚 {subject}")

            if topic:
                st.write(f"🎯 **Topic:** {topic}")

            st.write(f"⭐ **Difficulty:** {difficulty}")
            st.write(f"⏱️ **Total Time:** {hours:.1f} hours")

            col1, col2 = st.columns(2)

            with col1:
                st.info(
                    f"🧠 Learn / Practice\n\n"
                    f"**{study_time:.1f} hours**"
                )

            with col2:
                st.success(
                    f"🔄 Revision\n\n"
                    f"**{revision_time:.1f} hours**"
                )

            st.divider()

        st.info(
            "💡 Tip: Take a 5–10 minute break after about "
            "40–50 minutes of focused study."
        )
