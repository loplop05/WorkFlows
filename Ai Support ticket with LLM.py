

from local_llm import ask_llm

VALID_CATEGORIES = {"billing", "technical", "general"}


def route_ticket_with_llm(ticket):
    prompt = f"""
Classify the following customer support ticket.

Return exactly one word:
billing
technical
general

Ticket:
{ticket["original"]}

Category:
"""

    result = ask_llm(prompt).strip().lower()

    if result not in VALID_CATEGORIES:
        return "general"

    return result
