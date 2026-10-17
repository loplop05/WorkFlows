import gradio as gr
from local_llm import ask_llm 
gr.Interface(fn=    ask_llm,
    inputs=gr.Textbox(lines=10, placeholder="Enter your prompt here..."),
    outputs=gr.Textbox(lines=10, placeholder="LLM response will appear here..."),
    title="Local LLM Interface",
    description="This interface allows you to interact with a local LLM model. Enter your prompt and receive a response from the model.",
    theme="default",
    allow_flagging="never",
    allow_screenshot=False,
    allow_download=False,
    
).launch()
    