from tutoring.retrieval import retrieve_relevant_chunks
from tutoring.explanation import explain_with_llm
from tutoring.question_gen import generate_question


def student_chat_response(user_question, selected_topic, vectorstore, student_progress):
    user_question_lower = user_question.lower()

    # ---- INTENT: ASK FOR PRACTICE QUESTIONS ----
    if any(phrase in user_question_lower for phrase in [
        "another question",
        "more questions",
        "practice question",
        "new question",
        "quiz",
        "test me"
    ]):
        return generate_question(
            topic=selected_topic,
            difficulty="beginner"
        )

    # ---- INTENT: WHY / HOW / EXPLANATION ----
    retrieved = retrieve_relevant_chunks(
        vectorstore,
        f"{user_question} about {selected_topic}",
        k=1
    )

    return explain_with_llm(retrieved, style="simple")
