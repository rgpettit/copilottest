def grade(score, late):
    """Return "invalid", "pass", or "fail" for a score from 0 to 100."""
    if score < 0:
        return "invalid"
    if late:
        score -= 10
    if score > 60:
        return "pass"
    return "fail"