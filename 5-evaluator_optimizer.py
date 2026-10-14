
def generator(topic, feedback=""):
    if feedback:
        return (
            f"{topic} is good because "
        )

    return f"{topic} is useful."


def evaluator(text):
    if len(text.split()) >= 10:
        return {
            "passed": True,
            "feedback": "Good length"
        }

    return {
        "passed": False,
        "feedback": "Make the explanation longer"
    }


def run_workflow(topic, max_attempts=3):
    feedback = ""
    last_text = ""

    for attempt in range(max_attempts):
        text = generator(topic, feedback)
        last_text = text
        evaluation = evaluator(text)

        print(f"Attempt {attempt + 1}: {text}")

        if evaluation["passed"]:
            return {
                "status": "passed",
                "result": text
            }

        feedback = evaluation["feedback"]

    return {
        "status": "failed",
        "result": last_text
    }


print(run_workflow("Agentic AI"))
