# ☁️🕒 MCP - Local Ollama - Asistente de Clima y Hora

Este proyecto es una prueba de concepto que demuestra cómo integrar un **Model Context Protocol (MCP)** basado en TypeScript con un agente de IA de **PraisonAI**, utilizando un modelo de lenguaje local (`gemma3:12b`) ejecutado con **Ollama** y una interfaz de usuario creada con **Gradio**.

El asistente permite a los usuarios consultar la hora y el clima de ubicaciones específicas, extendiendo las capacidades del LLM mediante herramientas personalizadas.

---

## 🛠️ Tecnologías Utilizadas

* **PraisonAI Agents**: Framework para construir agentes de IA con capacidades de herramientas.
* **Model Context Protocol (MCP)**: Estándar para que los modelos de lenguaje accedan a herramientas externas y contexto.
* **Ollama**: Plataforma para ejecutar modelos de lenguaje grandes (LLMs) localmente.
* **Gradio**: Librería de Python para crear interfaces de usuario web rápidas para modelos de ML.
* **TypeScript**: Lenguaje de programación para el desarrollo del servidor MCP.
* **Node.js / npm**: Entorno de ejecución y gestor de paquetes para el servidor MCP.
* **worldtimeapi.org**: API pública utilizada para obtener la hora global.
* **Open-Meteo**: API pública utilizada para obtener datos meteorológicos.

---

## 🚀 De qué trata la prueba

Esta prueba valida la capacidad de un agente de IA para:
1.  **Interactuar con herramientas externas**: Utilizando un servidor MCP personalizado para acceder a datos de tiempo y clima en tiempo real.
2.  **Ejecutar modelos de lenguaje localmente**: Demostrando la integración con Ollama para mantener el procesamiento de IA en una maquina local.
3.  **Proporcionar una interfaz de usuario interactiva**: A través de Gradio, permitiendo a los usuarios hacer consultas de forma sencilla.

El objetivo es mostrar un flujo completo donde un usuario pregunta sobre el clima o la hora, el agente utiliza las herramientas del MCP para obtener la información necesaria y luego responde al usuario.

---

## ⚙️ Paso a paso para instalar y ejecutar

Asegúrate de tener **Node.js**, **npm**, **Python 3.9+** y **Ollama** instalados en tu sistema.

### 1. Clonar el repositorio

```bash
git clone https://github.com/Juliotamara23/MCP_Weather_Hour.git>
cd <MCP_Weather_Hour>
```

### 2. Configurar el servidor MCP (TypeScript)

**En proceso**

### 3. Instalar Ollama y descargar el modelo

Asegúrate de tener Ollama instalado y ejecutándose. Luego, descarga el modelo gemma3:12b:

```bash
ollama pull gemma3:12b
```

### 4. Configurar el entorno de Python

Crea un entorno virtual (opcional pero recomendado) e instala las dependencias de Python:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows
source .venv/Scripts/activate  # En Linux/Mac

pip install -r requirements.txt
```

### 5. Ejecutar la aplicación Gradio

```bash
python main.py
```