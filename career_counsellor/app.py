import streamlit as st
from chatbot import update_profile
from career_engine import recommend_careers

st.set_page_config(page_title="AI Career Counsellor", layout="centered")

st.title("🤖 AI Virtual Career Counsellor")

if "profile" not in st.session_state:
    st.session_state.profile = {
        "interest": None,
        "skills": []
    }

user_input = st.text_input("Tell me about your interests, skills, or goals:")

if user_input:
    st.session_state.profile = update_profile(
        st.session_state.profile,
        user_input
    )

    st.write("### 🔍 Understanding You")
    st.json(st.session_state.profile)

    recommendations = recommend_careers(st.session_state.profile)

    st.write("## 🎯 Career Recommendations")
    for career, score in recommendations:
        st.success(
            f"**{career['name']}**\n\n"
            f"• Market Demand: {career['demand']}/10\n"
            f"• Avg Salary: ₹{career['salary']} LPA\n"
            f"• Why: Matches your skills & interests"
        )
