from pydantic import BaseModel
from typing import List

class LearningResource(BaseModel):
    """one way of explaining a topic"""
    explanation: str
    examples: List[str]
    difficulty: str  # e.g., "beginner", "intermediate", "advanced"

class Topic(BaseModel):
    """One concept the student learns"""
    name: str
    learning_objectives: List[str]
    prerequisites: List[str]
    resources: List[LearningResource]

class Module(BaseModel):
    """A group of related topics"""
    name: str
    topics: List[Topic]

class Course(BaseModel):
    """Complete learning program"""
    name: str
    description: str
    modules: List[Module]