import os
import streamlit as st
from groq import Groq

# Set up Groq API key
os.environ['GROQ_API_KEY'] = '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'
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# UI Layout
st.title("Writing Assistant for Exam Preparation")
st.sidebar.header("Select a Plan")
plan = st.sidebar.selectbox("Choose your study plan:", ["30 Days", "45 Days", "60 Days"])

# Sample topics for each plan
topics = {
    "30 Days": ["Day 1: Discuss the impact of technology on communication", "Day 2: Benefits of global travel", "..."],
    "45 Days": ["Day 1: Importance of public transportation", "Day 2: Effects of advertising on children", "..."],
    "60 Days": ["Day 1: Role of education in career success", "Day 2: Should homework be banned?", "..."],
}

# Current day dropdown for topics
current_day = st.selectbox("Select your current day:", range(1, len(topics[plan]) + 1))
st.write("Today's Topic:", topics[plan][current_day - 1])
st.write("Upcoming Topics:", topics[plan][current_day:])

# Essay Input Section
essay = st.text_area("Write your essay here:", height=300)
submit_button = st.button("Submit for Feedback")

# Submit essay to Groq for feedback
if submit_button and essay:
    # Groq API call
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": essay}
        ],
        model="llama3-8b-8192",
    )

    feedback = chat_completion.choices[0].message.content
    st.subheader("Feedback")
    st.write(feedback)

# Additional sections for gamification, progress tracking, etc., can be added below.
