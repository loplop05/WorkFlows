
def classify_request(message):
    text = message.lower()

    if any(word in text for word in
           ["payment", "refund", "invoice"]):
        return "billing"

    if any(word in text for word in
           ["error", "bug", "crash"]):
        return "technical"
    if any(word in text for word in ["upgrade", "purchase", "buy"]):
        return "sales"
    if any(word in text for word in ["security", "hacked", "website"]):
        return "security"
    return "general"


def billing_handler(message):
    return "Forwarded to billing support."


def technical_handler(message):
    return "Forwarded to technical support."


def general_handler(message):
    return "Forwarded to general support."

def sales_handler(message):
    return "Forwarded to sales support."

def security_handler(message):
    return "Forwarded to security support."


HANDLERS = {
    "billing": billing_handler,
    "technical": technical_handler,
    "general": general_handler,
    "sales": sales_handler,
    "security": security_handler
}


def run_workflow(message):
    category = classify_request(message)

    handler = HANDLERS[category]
    return handler(message)


requests = [
    "I want to upgrade my subscription",
    "Someone accessed my account",
    "I need my invoice",
    "The website crashes",
    "Hello!"
]

for request in requests:
    response = run_workflow(request)
    print(f"Request: {request} ->  Response: {response}\n")