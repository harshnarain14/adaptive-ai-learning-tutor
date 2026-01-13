from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv() 
def explain_with_llm(retrieved_chunks,style="simple"):
    """Use Groq LLM to explain retrieved content
    in a specified style.
    """
    #Combine retrieved text into one context
    context="\n".join([chunk["text"] for chunk in retrieved_chunks])
    llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.3)
    prompt=f""" You are a helpful tutor.
    Explain the following content in a {style} way.
    Use clear language and simple examples
    Content:
    {context}
    """
    response=llm.invoke(prompt)
    return response.content