from langchain_groq import ChatGroq


def evaluate_answer(question, student_answer, reference_chunks):
    """
    Evaluate student answer and provide feedback
    """

    reference_text = "\n".join([chunk["text"] for chunk in reference_chunks])

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2
    )

    prompt = f"""
    You are a strict but helpful teacher.

    Question:
    {question}

    Student Answer:
    {student_answer}

    Correct Reference Content:
    {reference_text}

    Tasks:
    1. Decide if the student's answer is Correct, Partially Correct, or Incorrect
    2. Explain why
    3. If incorrect, explain the correct concept simply

    Format EXACTLY like this:
    Verdict:
    Feedback:
    """

    response = llm.invoke(prompt)
    return response.content
