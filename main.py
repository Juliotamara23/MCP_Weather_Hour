from praisonaiagents import Agent, MCP
import gradio as gr

def search_weather(query):
    # Instancia MCP para que PraisonAIAgents gestione el proceso del servidor MCP.
    # El primer argumento es la ruta al script de tu servidor MCP.
    # PraisonAIAgents se encargará de ejecutar 'npx -y tsx' por ti.
    mcp_tool = MCP("E:/DEV/Proyects/0.1-start/main.ts") # Asegúrate de que esta ruta sea correcta.

    agent = Agent (
        instructions="""Ayuda a saber cual es la hora y el clima.""",
        llm="ollama/gemma3:4b",
        tools=[mcp_tool] # Las herramientas deben ser una lista, incluso si es solo una.
    )
    result = agent.start(query)
    return f"## Resultados de la consulta: \n\n{result}"

demo = gr.Interface(
    fn=search_weather,
    inputs=gr.Textbox(placeholder="Cual es el clima y hora de Colombia?...."),
    outputs=gr.Markdown(),
    title="MCP - LOCAL OLLAMA - Asistente de clima y hora",
    description="Introduce tu pregunta.:"
)

if __name__ == "__main__":
    demo.launch()