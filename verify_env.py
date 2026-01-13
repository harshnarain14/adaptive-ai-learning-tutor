import sys
print("Python executable:")
print(sys.executable)
print("\nChecking core imports.....")
import langchain
import openai
import faiss
import streamlit
import pydantic
import numpy
import pandas
import tiktoken
print("All core imports successful!")