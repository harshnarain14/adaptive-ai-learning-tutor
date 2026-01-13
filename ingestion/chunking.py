def chunk_course(course):
    chunks = []
    for module in course.modules:
        for topic in module.topics:
            for resource in topic.resources:
                chunk = {
                    "text": resource.explanation,
                    "metadata": {
                        "course": course.name,
                        "module": module.name,
                        "topic": topic.name,
                        "difficulty": resource.difficulty,
                        "prerequisites": topic.prerequisites
                    }
                }
                chunks.append(chunk)
    return chunks