import streamlit as st
from PIL import Image

st.title("Grade 2 Mathematics Quiz")

def display_question(question, options, correct_option):
    st.write(question)
    option = st.radio("Select your answer:", options, label_visibility="collapsed")
    return option == correct_option


questions = [
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_option": "4"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["30", "25", "35", "40"],
            "correct_option": "30"
        },
        {
            "question": "What is 12 / 4?",
            "options": ["1", "2", "3", "4"],
            "correct_option": "3"
        },
        {
            "question": "What is 2 + (2 * 4)?",
            "options": ["17", "10", "8", "6"],
            "correct_option": "10"
        },
        {
            "question": "What is 25 / 5?",
            "options": ["9", "4", "5", "7"],
            "correct_option": "5"
        },
    ]


score = 0

for question in questions:
        if display_question(question["question"], question["options"], question["correct_option"]):
            score += 1

if st.button("Submit"):
        st.write(f"Your score is {score} out of {len(questions)}")


        