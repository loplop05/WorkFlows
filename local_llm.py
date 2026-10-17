
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
    
import gradio as gr 
gr.Interface(fn=ask_llm,
    inputs=gr.Textbox(lines=10, placeholder="Enter your prompt here..."),
    outputs=gr.Textbox(lines=10, placeholder="LLM response will appear here..."),
    title="Local LLM Interface",
    description="This interface allows you to interact with a local LLM model. Enter your prompt and receive a response from the model.",
    theme="default",
 
).launch()
