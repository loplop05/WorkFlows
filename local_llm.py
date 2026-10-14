
import json
from urllib.request import Request, urlopen

def ask_llm(prompt):
    payload = json.dumps({
        "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")

    request = Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    with urlopen(request, timeout=180) as response:
        result = json.load(response)

    return result["response"].strip()
