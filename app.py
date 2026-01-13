import streamlit as st

from ingestion.ingest_content import ingest_sample_course
from ingestion.chunking import chunk_course
from vectorstore.faiss_index import create_faiss_index

from tutoring.retrieval import retrieve_relevant_chunks
from tutoring.explanation import explain_with_llm
from tutoring.question_gen import generate_question
from tutoring.feedback import evaluate_answer
from tutoring.student_chat import student_chat_response

from adaptive.student_progress import update_progress, get_student_progress
from adaptive.learning_path import recommend_next_topics
from adaptive.verdict_parser import extract_verdict
from adaptive.instructor_insights import analyze_student_progress
from adaptive.instructor_chat import instructor_chat_response


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Learning Tutor",
    page_icon="🎓",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.markdown(
    "<h1 style='font-size:42px;font-weight:800;'>🎓 AI Adaptive Learning Tutor</h1>",
    unsafe_allow_html=True
)

st.write(
    "A personalized AI tutor that explains concepts, evaluates answers, "
    "tracks progress, and adapts learning paths — just like a real teacher."
)

student_id = "student_1"

mode = st.sidebar.radio(
    "Select Mode",
    ["Student", "Instructor"]
)

# =========================
# LOAD SYSTEM (CACHED)
# =========================
@st.cache_resource
def load_system():
    course = ingest_sample_course()
    chunks = chunk_course(course)
    vectorstore = create_faiss_index(chunks)
    return course, vectorstore

course, vectorstore = load_system()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📚 Learning Control")

topics = []
for module in course.modules:
    for topic in module.topics:
        topics.append(topic.name)

selected_topic = st.sidebar.selectbox("Select Topic", topics)

st.sidebar.markdown("---")
st.sidebar.write("👤 **Student ID**")
st.sidebar.code(student_id)

# =========================
# STUDENT MODE
# =========================
if mode == "Student":
    col1, col2 = st.columns([2, 1])

    # -------- LEFT COLUMN --------
    with col1:
        st.subheader("📖 Concept Explanation")

        if st.button("Explain Topic", use_container_width=True):
            retrieved = retrieve_relevant_chunks(
                vectorstore,
                f"Explain {selected_topic}",
                k=1
            )
            explanation = explain_with_llm(retrieved, style="simple")
            st.write(explanation)
            st.session_state["retrieved"] = retrieved

        st.markdown("---")

        st.subheader("❓ Practice Question")

        if st.button("Generate Question", use_container_width=True):
            st.session_state["question"] = generate_question(
                selected_topic, difficulty="beginner"
            )

        if "question" in st.session_state:
            st.write("**Question:**")
            st.write(st.session_state["question"])

        student_answer = st.text_area("✍️ Your Answer", height=120)

        if st.button("Submit Answer", use_container_width=True):
            if "retrieved" not in st.session_state:
                st.warning("Please read the explanation first.")
            else:
                evaluation = evaluate_answer(
                    question=f"What is {selected_topic}?",
                    student_answer=student_answer,
                    reference_chunks=st.session_state["retrieved"]
                )

                st.subheader("🧠 Tutor Feedback")
                st.write(evaluation)

                verdict = extract_verdict(evaluation)

                update_progress(
                    student_id=student_id,
                    topic=selected_topic,
                    verdict=verdict
                )

        st.markdown("---")

        # -------- STUDENT CHAT TUTOR --------
        st.subheader("💬 Ask the Tutor")

        student_chat_input = st.text_input(
            "Ask why, how, or request more practice questions"
        )

        if st.button("Ask Tutor"):
            if not student_chat_input:
                st.warning("Please ask a question.")
            else:
                response = student_chat_response(
                    user_question=student_chat_input,
                    selected_topic=selected_topic,
                    vectorstore=vectorstore,
                    student_progress=get_student_progress(student_id)
                )

                st.markdown("### 🤖 Tutor Response")
                st.write(response)

    # -------- RIGHT COLUMN --------
    with col2:
        st.subheader("🧭 Learning Path")

        recommendations = recommend_next_topics(student_id, course)
        if recommendations:
            for rec in recommendations:
                st.write("•", rec)
        else:
            st.success("🎉 All topics mastered!")

        st.markdown("---")

        st.subheader("📊 Progress Overview")

        progress = get_student_progress(student_id)

        if not progress:
            st.info("No progress yet. Start learning!")
        else:
            for topic, data in progress.items():
                attempts = data["attempts"]
                correct = data["correct"]
                status = data["status"]

                accuracy = correct / attempts if attempts > 0 else 0

                st.markdown(f"### 📘 {topic}")
                st.progress(accuracy)

                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Attempts", attempts)
                col_b.metric("Correct", correct)

                if status == "Mastered":
                    col_c.success("✅ Mastered")
                else:
                    col_c.warning("⏳ In Progress")

# =========================
# INSTRUCTOR MODE
# =========================
if mode == "Instructor":
    st.subheader("🧑‍🏫 Instructor Dashboard")

    all_progress = get_student_progress(student_id)
    insights = analyze_student_progress(all_progress)

    st.subheader("📌 Instructor Insights")

    if insights["high_risk"]:
        st.error("🔴 High Risk Topics")
        for t in insights["high_risk"]:
            st.write("•", t)

    if insights["needs_attention"]:
        st.warning("🟡 Needs Attention")
        for t in insights["needs_attention"]:
            st.write("•", t)

    if insights["doing_well"]:
        st.success("🟢 Doing Well")
        for t in insights["doing_well"]:
            st.write("•", t)

    st.markdown("---")

    if not all_progress:
        st.info("No student activity yet.")
    else:
        for topic, data in all_progress.items():
            attempts = data["attempts"]
            correct = data["correct"]
            status = data["status"]

            accuracy = correct / attempts if attempts > 0 else 0

            st.markdown(f"### 📘 {topic}")
            st.progress(accuracy)

            col1, col2, col3 = st.columns(3)
            col1.metric("Attempts", attempts)
            col2.metric("Correct", correct)
            col3.metric("Status", status)

    st.markdown("---")
    st.subheader("💬 Instructor Assistant")

    instructor_question = st.text_area(
        "Ask about student progress, weaknesses, or teaching strategy",
        height=100
    )

    if st.button("Ask Assistant"):
        if not all_progress:
            st.warning("No student data available yet.")
        else:
            response = instructor_chat_response(
                instructor_question,
                all_progress
            )
            st.write(response)
