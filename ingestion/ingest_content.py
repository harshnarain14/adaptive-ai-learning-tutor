# ingestion/ingest_content.py

from models.content_models import Course, Module, Topic, LearningResource


def ingest_sample_course() -> Course:
    """
    Create and return the course content.
    NO execution, NO AI, NO side effects.
    """

    # -------------------------
    # Topic: Variables
    # -------------------------
    variables_resource = LearningResource(
        explanation="A variable is a name that stores a value in memory.",
        examples=[
            "x = 10",
            "name = 'Rahul'"
        ],
        difficulty="beginner"
    )

    variables_topic = Topic(
        name="Variables",
        learning_objectives=[
            "Understand what variables are",
            "Learn how to store values"
        ],
        prerequisites=[],
        resources=[variables_resource]
    )

    # -------------------------
    # Topic: Functions
    # -------------------------
    functions_resource = LearningResource(
        explanation="A function is a reusable block of code that performs a task.",
        examples=[
            "def add(a, b): return a + b"
        ],
        difficulty="beginner"
    )

    functions_topic = Topic(
        name="Functions",
        learning_objectives=[
            "Understand functions",
            "Learn code reuse"
        ],
        prerequisites=["Variables"],
        resources=[functions_resource]
    )

    # -------------------------
    # Module
    # -------------------------
    foundation_module = Module(
        name="Foundations",
        topics=[variables_topic, functions_topic]
    )

    # -------------------------
    # Course
    # -------------------------
    course = Course(
        name="Python Basics",
        description="Introductory Python course for beginners",
        modules=[foundation_module]
    )

    return course


# -------------------------
# Optional local test ONLY
# -------------------------
if __name__ == "__main__":
    course = ingest_sample_course()
    print("Course loaded successfully:")
    print(course)
