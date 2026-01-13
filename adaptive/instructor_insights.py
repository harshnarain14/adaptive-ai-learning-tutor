def analyze_student_progress(progress):
    """
    Generate instructor insights from student progress
    """
    insights = {
        "high_risk": [],
        "needs_attention": [],
        "doing_well": []
    }

    for topic, data in progress.items():
        attempts = data["attempts"]
        correct = data["correct"]
        status = data["status"]

        accuracy = correct / attempts if attempts > 0 else 0

        if attempts >= 3 and accuracy < 0.5:
            insights["high_risk"].append(topic)
        elif status == "In Progress" and attempts >= 2:
            insights["needs_attention"].append(topic)
        elif status == "Mastered":
            insights["doing_well"].append(topic)

    return insights
