# Python MCP Demo

Una demo para mostrar implementaciones del Model Context Protocol (MCP) usando FastMCP, con ejemplos de transporte stdio y HTTP, y integración con LangChain y Agent Framework.

## Tabla de contenidos

- [Requisitos](#requisitos)
- [Setup](#setup)
- [Scripts en Python](#scripts-en-python)
- [Configuración del servidor MCP](#configuracion-del-servidor-mcp)
- [Debugging](#debugging)
- [License](#license)

## Requisitos

- Python 3.13 
- [uv](https://docs.astral.sh/uv/)
- Acceso a una API de uno de los siguientes proveedores:
  - GitHub Models (token de GitHub)
  - Azure OpenAI (credenciales de Azure)
  - Ollama (instalación local)
  - OpenAI API (API key)

## Setup

1. Instala dependencias usando `uv`:

```bash
uv sync
```

2. Copia `.env-sample` a `.env` y configura tus variables de entorno:

```bash
cp .env-sample .env
```

3. Edita `.env` con tus credenciales. Selecciona el proveedor definiendo `API_HOST`:
   - `github` - GitHub Models (requiere `GITHUB_TOKEN`)
   - `azure` - Azure OpenAI (requiere credenciales de Azure)
   - `ollama` - Instancia local de Ollama
   - `openai` - OpenAI API (requiere `OPENAI_API_KEY`)

## Scripts en Python

Ejecuta cualquier script con: `uv run <script_name>`

- **basic_mcp_http.py** - MCP server con transporte HTTP en el puerto 8000
- **basic_mcp_stdio.py** - MCP server con transporte stdio (útil para integración con VS Code / Copilot)
- **langchainv1_mcp_http.py** - Agente LangChain que usa MCP tools
- **agentframework_mcp_learn.py** - Integración con Microsoft Agent Framework y MCP

## Configuración del servidor MCP

### Usando MCP Inspector

El [MCP Inspector](https://github.com/modelcontextprotocol/inspector) es una herramienta para interactuar con y depurar MCP servers.

> Nota: Aunque técnicamente los servidores HTTP pueden funcionar con port forwarding en Codespaces o Dev Containers, armar el Inspector + adjuntar el debugger puede ser complicado. Para una experiencia más simple y completa con debugging, lo mejor es correr el proyecto localmente.

**Para servidores stdio:**

```bash
npx @modelcontextprotocol/inspector uv run basic_mcp_stdio.py
```

**Para servidores HTTP:**

1. Corre el servidor HTTP:
```bash
uv run basic_mcp_http.py
```

2. En otra terminal, corre el inspector:
```bash
npx @modelcontextprotocol/inspector http://localhost:8000/mcp
```

El Inspector te da una interfaz web para:
- Ver las herramientas (tools), recursos y prompts disponibles
- Probar llamadas a tools con parámetros personalizados
- Inspeccionar respuestas y errores del servidor
- Debuggear la comunicación con el servidor

### Usando con GitHub Copilot

El archivo `.vscode/mcp.json` configura servidores MCP para la integración con GitHub Copilot:

**Servidores disponibles:**

- **expenses-mcp**: transporte stdio para uso normal
- **expenses-mcp-debug**: stdio con debugpy en el puerto 5678
- **expenses-mcp-http**: server HTTP en `http://localhost:8000/mcp`
- **expenses-mcp-http-debug**: stdio con debugpy en el puerto 5679

**Cambiar servidores:**

En la UI del Chat de GitHub Copilot, seleccioná el servidor desde el ícono de herramientas.

## Debugging

### Configuraciones de debug

El archivo `.vscode/launch.json` tiene cuatro configuraciones:

#### Launch (arrancar servidor con debugger)

1. **Launch MCP HTTP Server (Debug)**
   - Arranca `basic_mcp_http.py` con el debugger conectado
   - Ideal para pruebas locales y scripts LangChain

2. **Launch MCP stdio Server (Debug)**
   - Arranca `basic_mcp_stdio.py` con el debugger conectado
   - Útil para probar comunicación stdio

#### Attach (adjuntar a servidor ya corriendo)

3. **Attach to MCP Server (stdio)** - Puerto 5678
   - Se adjunta al servidor iniciado desde `expenses-mcp-debug` en `mcp.json`

4. **Attach to MCP Server (HTTP)** - Puerto 5679
   - Se adjunta al servidor iniciado desde `expenses-mcp-http-debug` en `mcp.json`

### Flujo de debugging

#### Opción 1: Launch y Debug (Standalone)

Este método funciona bien con MCP Inspector y scripts LangChain:

1. Pon breakpoints en `basic_mcp_http.py` o `basic_mcp_stdio.py`
2. Abrí Run and Debug (`Cmd+Shift+D`)
3. Elegí "Launch MCP HTTP Server (Debug)" o "Launch MCP stdio Server (Debug)"
4. Presioná `F5` o el botón de play
5. Conectá MCP Inspector o corré tu script LangChain para disparar los breakpoints
   - Para HTTP: `npx @modelcontextprotocol/inspector http://localhost:8000/mcp`
   - Para stdio: `npx @modelcontextprotocol/inspector uv run basic_mcp_stdio.py` (si vas a debuggear con stdio, normalmente tenés que arrancar sin debugger y luego adjuntar)

#### Opción 2: Adjuntar a servidor en ejecución (integración con Copilot)

1. Pon breakpoints en tu archivo del servidor MCP
2. Arrancá el servidor de debug definido en `mcp.json`:
   - Elegí `expenses-mcp-debug` o `expenses-mcp-http-debug`
3. Abrí Run and Debug (`Cmd+Shift+D`)
4. Elegí la configuración "Attach to MCP Server" correspondiente
5. Presioná `F5` para adjuntar
6. En el chat de GitHub Copilot, seleccioná el server correcto en las herramientas
7. Usá Copilot Chat para llamar a las tools y el debugger debería detenerse en los breakpoints

## License

MIT
