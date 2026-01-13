from langchain_groq import ChatGroq


def generate_question(topic, difficulty="beginner"):
    """
    Generate a question for a given topic using Groq
    """

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.4
    )

    prompt = f"""
    You are a teacher.

    Create ONE {difficulty}-level question on the topic: {topic}.

    Also provide:
    1. The correct answer
    2. A short explanation

    Format exactly like this:
    Question:
    Answer:
    Explanation:
    """

    response = llm.invoke(prompt)
    return response.content
