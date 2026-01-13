# 🎓 Adaptive AI Learning Tutor  
**E-Learning Content Assistant with Adaptive Learning Paths (GenAI Project)**

---

## 📌 Overview

The **Adaptive AI Learning Tutor** is an end-to-end **Generative AI–powered personalized education platform** designed to simulate how a real teacher explains concepts, evaluates understanding, tracks progress, and adapts learning paths for each learner.

The system combines **LLMs, Retrieval-Augmented Generation (RAG), semantic search, and adaptive logic** to deliver personalized learning experiences for students and actionable insights for instructors.

---

## ❓ Problem Statement

Traditional e-learning platforms are mostly static:

- Same content for all learners  
- No personalization or pacing  
- Limited remediation and feedback  
- Minimal insight into learner weaknesses  

Learners vary in:
- Background knowledge
- Learning speed
- Conceptual understanding  

This project addresses these gaps by building an **AI-driven adaptive tutoring system** that dynamically adjusts learning paths based on learner performance.

---

## 🧠 Solution Architecture

### High-Level Flow

Curriculum Content
↓
Concept-Level Chunking
↓
FAISS Vector Index (Semantic Search)
↓
Student / Instructor Query
↓
Relevant Content Retrieval
↓
LLM Reasoning (Groq + LangChain)
↓
Explanation / Question / Feedback
↓
Progress Tracking & Adaptive Learning Path

yaml
Copy code

### Design Principles
- Curriculum-grounded responses (hallucination control)
- Explainable adaptive logic
- Human-in-the-loop learning
- Modular and extensible system design

---

## ✨ Key Features

### 👨‍🎓 Student Features
- Multi-style concept explanations (simple, detailed, intuitive)
- AI-generated practice questions
- Automated answer evaluation with feedback
- Adaptive learning path recommendations
- Visual mastery tracking using progress bars
- Chat-based AI tutor for:
  - “Why” and “How” questions
  - Alternative explanations
  - Additional practice questions

### 🧑‍🏫 Instructor Features
- Topic-wise learner progress analytics
- Mastery and accuracy visualization
- Weak-topic and risk detection
- Instructor insights (high risk, needs attention, doing well)
- Chat-based instructor assistant for teaching guidance

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| LLM | Groq (LLaMA 3.1) |
| Prompt Orchestration | LangChain |
| Vector Store | FAISS |
| Backend | Python |
| Frontend | Streamlit |
| Data Models | Pydantic |
| State Management | Streamlit Session State |

---

## 🗂 Project Structure

├── app.py
├── ingestion/
│ ├── ingest_content.py
│ ├── chunking.py
├── tutoring/
│ ├── retrieval.py
│ ├── explanation.py
│ ├── question_gen.py
│ ├── feedback.py
│ ├── student_chat.py
├── adaptive/
│ ├── student_progress.py
│ ├── learning_path.py
│ ├── verdict_parser.py
│ ├── instructor_insights.py
│ ├── instructor_chat.py
├── vectorstore/
│ ├── faiss_index.py
├── requirements.txt
├── README.md

yaml
Copy code

---

## 🔄 System Workflow

1. Curriculum is ingested and structured into Course → Module → Topic  
2. Content is chunked at concept level  
3. FAISS indexes semantic embeddings  
4. Student interacts via UI or chat  
5. Relevant content is retrieved using semantic search  
6. LLM generates explanation, questions, or feedback  
7. Student responses are evaluated  
8. Progress and mastery are updated  
9. Learning path adapts dynamically  
10. Instructor analytics update in real time  

---

## 🧪 Evaluation Scenarios

### Scenario 1: Beginner Learner
- Starts from scratch  
- Receives simple explanations  
- Practices until mastery  
- Progress tracked accurately  

### Scenario 2: Learner Struggling with a Topic
- Multiple incorrect attempts  
- Topic flagged as high risk  
- Instructor receives insight  

### Scenario 3: Fast Learner
- High accuracy early  
- Topic marked as mastered  
- Learning path skips ahead  

---

## 📊 Adaptive Learning Logic

- Learning states:
  - Not Started
  - In Progress
  - Mastered
- Mastery criteria:
  - At least 2 attempts
  - Accuracy ≥ 80%
- Learning path adapts based on:
  - Performance
  - Prerequisite gaps
  - Learning speed  

This ensures robustness against guessing and promotes true understanding.

---

## ⚠️ Ethics & Limitations

- Responses are grounded in curriculum (hallucination control)
- No personal or sensitive data stored
- Instructor oversight encouraged
- AI assists learning but does not replace teachers
- Educational support system, not an authoritative source

---

## ▶️ How to Run the Project

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Set API Key
Create a .env file:

env
Copy code
GROQ_API_KEY=your_api_key_here
4. Run the Application
bash
Copy code
streamlit run app.py
🚀 Future Improvements
Multi-student support

File-based curriculum ingestion (Markdown / PDF)

Advanced learning analytics dashboards

Cloud deployment

LMS integration

🎯 Educational & Social Impact
This project demonstrates how Generative AI can improve education quality, accessibility, and personalization, making it applicable for:

EdTech companies

Universities and schools

Corporate training platforms

NGOs and educational initiatives

🏁 Conclusion
The Adaptive AI Learning Tutor is a complete, production-style GenAI system that combines:

Retrieval-Augmented Generation (RAG)

Adaptive learning theory

Student and instructor experiences

Explainable AI-driven decision-making

It is portfolio-ready, interview-ready, and industry-relevant.

yaml
Copy code

---

✅ This is the **final, complete README.md**  
Nothing more is required.

If you want next:
- Resume bullet points
- Interview Q&A from this project
- Deployment guide
- Architecture diagram explanation

Just tell me 👍