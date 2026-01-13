# adaptive/student_progress.py

import streamlit as st


def initialize_student(student_id):
    """
    Ensure student progress exists in Streamlit session state
    """
    if "student_progress" not in st.session_state:
        st.session_state.student_progress = {}

    if student_id not in st.session_state.student_progress:
        st.session_state.student_progress[student_id] = {}


def update_progress(student_id, topic, verdict):
    """
    Update attempts, correct count, and mastery status
    """
    initialize_student(student_id)

    progress = st.session_state.student_progress

    if topic not in progress[student_id]:
        progress[student_id][topic] = {
            "attempts": 0,
            "correct": 0,
            "status": "Not Started"
        }

    record = progress[student_id][topic]

    # ---- update attempts ----
    record["attempts"] += 1

    # ---- normalize verdict safely ----
    clean_verdict = verdict.lower().strip()

    # IMPORTANT:
    # "incorrect" contains "correct", so order matters
    if "incorrect" not in clean_verdict and "correct" in clean_verdict:
        record["correct"] += 1

    # ---- mastery logic ----
    accuracy = record["correct"] / record["attempts"]

    if accuracy >= 0.8 and record["attempts"] >= 2:
        record["status"] = "Mastered"
    else:
        record["status"] = "In Progress"

    return record


def get_student_progress(student_id):
    """
    Return student progress safely
    """
    if "student_progress" not in st.session_state:
        return {}

    return st.session_state.student_progress.get(student_id, {})
