def extract_verdict(feedback_text: str) -> str:
    """
    Extract verdict from LLM feedback text safely.
    Expected format:
    Verdict: Correct
    Feedback: ...
    """
    for line in feedback_text.splitlines():
        line_lower = line.lower().strip()

        if line_lower.startswith("verdict:"):
            return line.split(":", 1)[1].strip()

    return "Unknown"
