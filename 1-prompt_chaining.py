
def extract_information(review):
    return {
        "original": review,
        "mentions_delivery": "delivery" in review.lower()
    }


def classify_sentiment(data):
    review = data["original"].lower()

    if "late" in review or "bad" in review:
        data["sentiment"] = "negative"
    else:
        data["sentiment"] = "positive"

    return data


def generate_response(data):
    if data["sentiment"] == "negative":
        return "We're sorry about your experience."

    return "Thank you for your positive feedback!"


def run_workflow(review):
    data = extract_information(review)
    data = classify_sentiment(data)
    response = generate_response(data)

    return response


review = "The delivery is so good."
print(run_workflow(review))
