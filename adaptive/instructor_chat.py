from tutoring.explanation import explain_with_llm


def instructor_chat_response(question, student_progress):
    """
    Generate instructor-focused response using student analytics
    """

    progress_summary = []

    for topic, data in student_progress.items():
        attempts = data["attempts"]
        correct = data["correct"]
        status = data["status"]
        accuracy = correct / attempts if attempts > 0 else 0

        progress_summary.append(
            f"- Topic: {topic}, Attempts: {attempts}, "
            f"Accuracy: {accuracy:.2f}, Status: {status}"
        )

    context = "\n".join(progress_summary)

    prompt = f"""
    You are an AI teaching assistant helping an instructor.

    Student progress summary:
    {context}

    Instructor question:
    {question}

    Give clear, actionable teaching advice.
    Be concise and practical.
    """

    response = explain_with_llm(
        [{"text": prompt}],
        style="detailed"
    )

    return response
