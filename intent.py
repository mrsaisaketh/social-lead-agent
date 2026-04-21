def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in text for word in ["price", "plan", "cost"]):
        return "pricing"

    elif any(word in text for word in [
        "buy", "purchase", "purch", "try",
        "start", "subscribe", "want", "interested"
    ]):
        return "high_intent"

    return "unknown"