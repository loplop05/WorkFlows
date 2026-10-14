
# MODULE 4 MINI PROJECT
# AI Support Ticket Workflow
# Free, standard-library-only version


def extract_ticket(message):
    return {
        "original": message,
        "normalized": message.lower().strip()
    }


def route_ticket(ticket):
    text = ticket["normalized"]

    if any(x in text for x in
           ["refund", "payment", "invoice"]):
        return "billing"

    if any(x in text for x in
           ["error", "crash", "bug"]):
        return "technical"

    return "general"


def generate_response(category, feedback=""):
    templates = {
        "billing": (
            "Our billing team will review your "
            "payment or refund request."
        ),
        "technical": (
            "Our technical team will investigate "
            "the reported issue."
        ),
        "general": (
            "Our support team will review "
            "your question."
        )
    }

    response = templates[category]

    if feedback:
        response += (
            " Please share any additional details "
            "that could help our team."
        )

    return response


def evaluate_response(response):
    passed = len(response.split()) >= 15

    return {
        "passed": passed,
        "feedback": (
            "" if passed else
            "Response must contain at least 15 words."
        )
    }


def improve_response(category, max_attempts=3):
    feedback = ""

    for attempt in range(max_attempts):
        response = generate_response(category, feedback)
        evaluation = evaluate_response(response)

        if evaluation["passed"]:
            return {
                "response": response,
                "passed": True,
                "attempts": attempt + 1
            }

        feedback = evaluation["feedback"]

    return {
        "response": response,
        "passed": False,
        "attempts": max_attempts
    }


def process_ticket(message):
    ticket = extract_ticket(message)
    category = route_ticket(ticket)
    result = improve_response(category)

    return {
        "ticket": message,
        "category": category,
        **result
    }


if __name__ == "__main__":
    tickets = [
        "I want a refund",
        "My application keeps crashing",
        "How can I contact your company?"
    ]

    for ticket in tickets:
        result = process_ticket(ticket)
        print(result)
        print("-" * 40)
