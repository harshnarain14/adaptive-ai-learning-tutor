from adaptive.student_progress import get_student_progress


def recommend_next_topics(student_id, course):
    """
    Recommend next topics based on student progress and prerequisites
    """
    recommendations = []
    progress = get_student_progress(student_id)

    for module in course.modules:
        for topic in module.topics:
            topic_name = topic.name
            topic_status = progress.get(topic_name, {}).get("status", "Not Started")

            # Check prerequisites
            prerequisites_met = True
            for prereq in topic.prerequisites:
                prereq_status = progress.get(prereq, {}).get("status", "Not Started")
                if prereq_status != "Mastered":
                    prerequisites_met = False
                    recommendations.append(
                        f"Revise prerequisite topic: {prereq}"
                    )

            if not prerequisites_met:
                continue

            # Decide recommendation
            if topic_status == "Not Started":
                recommendations.append(f"Start learning topic: {topic_name}")
            elif topic_status == "In Progress":
                recommendations.append(f"Continue practicing topic: {topic_name}")
            elif topic_status == "Mastered":
                continue  # skip mastered topics

    return recommendations
