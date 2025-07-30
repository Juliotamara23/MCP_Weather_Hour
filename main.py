from praisonaiagents import Agent, MCP
import gradio as gr

def search_weather(query):
    agent = Agent(
        instructions="Ayuda a saber cual es la hora y el clima.",
        llm="ollama/gemma3:12b",
        tools=MCP("npx -y tsx E:/DEV/Proyects/0.1-start/main.ts")
    )
    result = agent.start(query)
    return f"## Resultados de la consulta: \n\n{result}"

demo = gr.Interface(
    fn=search_weather,
    inputs=gr.Textbox(placeholder="Cual es el clima y hora de Colombia?...."),
    outputs=gr.Markdown(),
    title="MCP - LOCAL OLLAMA - Asistente de clima y hora",
    description="Introduce tu pregunta."
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)