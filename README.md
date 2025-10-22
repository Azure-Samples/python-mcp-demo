# Python MCP Demo

A demonstration project showcasing Model Context Protocol (MCP) implementations using FastMCP, with examples of stdio, HTTP transports, and integration with LangChain and Agent Framework.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Python Scripts](#python-scripts)
- [MCP Server Configuration](#mcp-server-configuration)
- [Debugging](#debugging)
- [License](#license)

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/)
- API access to one of the following:
  - GitHub Models (GitHub token)
  - Azure OpenAI (Azure credentials)
  - Ollama (local installation)
  - OpenAI API (API key)

## Setup

1. Install dependencies using `uv`:

```bash
uv sync
```

2. Copy `.env-sample` to `.env` and configure your environment variables:

```bash
cp .env-sample .env
```

3. Edit `.env` with your API credentials. Choose one of the following providers by setting `API_HOST`:
   - `github` - GitHub Models (requires `GITHUB_TOKEN`)
   - `azure` - Azure OpenAI (requires Azure credentials)
   - `ollama` - Local Ollama instance
   - `openai` - OpenAI API (requires `OPENAI_API_KEY`)

## Python Scripts

Run any script with: `uv run <script_name>`

- **basic_mcp_http.py** - MCP server with HTTP transport on port 8000
- **basic_mcp_stdio.py** - MCP server with stdio transport for VS Code integration
- **langchainv1_mcp_http.py** - LangChain agent with MCP tool integration and temporal context handling
- **agentframework_mcp_learn.py** - Microsoft Agent Framework integration with MCP

## MCP Server Configuration

### Using with MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a developer tool for testing and debugging MCP servers.

> **Note:** While HTTP servers can technically work with port forwarding in Codespaces/Dev Containers, the setup for MCP Inspector and debugger attachment is not straightforward. For the best development experience with full debugging capabilities, we recommend running this project locally.

**For stdio servers:**

```bash
npx @modelcontextprotocol/inspector uv run basic_mcp_stdio.py
```

**For HTTP servers:**

1. Start the HTTP server:
```bash
uv run basic_mcp_http.py
```

2. In another terminal, run the inspector:
```bash
npx @modelcontextprotocol/inspector http://localhost:8000/mcp
```

The inspector provides a web interface to:
- View available tools, resources, and prompts
- Test tool invocations with custom parameters
- Inspect server responses and errors
- Debug server communication

### Using with GitHub Copilot

The `.vscode/mcp.json` file configures MCP servers for GitHub Copilot integration:

**Available Servers:**

- **expenses-mcp**: stdio transport server for production use
- **expenses-mcp-debug**: stdio server with debugpy on port 5678
- **expenses-mcp-http**: HTTP transport server at `http://localhost:8000/mcp`
- **expenses-mcp-http-debug**: stdio server with debugpy on port 5679

**Switching Servers:**

Configure which server GitHub Copilot uses by selecting it in the Chat panel selecting the tools icon.

## Debugging

### Debug Configurations

The `.vscode/launch.json` provides four debug configurations:

#### Launch Configurations (Start server with debugging)

1. **Launch MCP HTTP Server (Debug)**
   - Directly starts `basic_mcp_http.py` with debugger attached
   - Best for: Standalone testing and LangChain script debugging

2. **Launch MCP stdio Server (Debug)**
   - Directly starts `basic_mcp_stdio.py` with debugger attached
   - Best for: Testing stdio communication

#### Attach Configurations (Attach to running server)

3. **Attach to MCP Server (stdio)** - Port 5678
   - Attaches to server started via `expenses-mcp-debug` in `mcp.json`
   - Best for: Debugging during GitHub Copilot Chat usage

4. **Attach to MCP Server (HTTP)** - Port 5679
   - Attaches to server started via `expenses-mcp-http-debug` in `mcp.json`
   - Best for: Debugging HTTP server during Copilot usage

### Debugging Workflow

#### Option 1: Launch and Debug (Standalone)

Use this approach for debugging with MCP Inspector or LangChain scripts:

1. Set breakpoints in `basic_mcp_http.py` or `basic_mcp_stdio.py`
2. Press `Cmd+Shift+D` to open Run and Debug
3. Select "Launch MCP HTTP Server (Debug)" or "Launch MCP stdio Server (Debug)"
4. Press `F5` or click the green play button
5. Connect MCP Inspector or run your LangChain script to trigger breakpoints
   - For HTTP: `npx @modelcontextprotocol/inspector http://localhost:8000/mcp`
   - For stdio: `npx @modelcontextprotocol/inspector uv run basic_mcp_stdio.py` (start without debugger first)

#### Option 2: Attach to Running Server (Copilot Integration)

1. Set breakpoints in your MCP server file
1. Start the debug server via `mcp.json` configuration:
   - Select `expenses-mcp-debug` or `expenses-mcp-http-debug`
1. Press `Cmd+Shift+D` to open Run and Debug
1. Select appropriate "Attach to MCP Server" configuration
1. Press `F5` to attach
1. Select correct expense mcp server in GitHub Copilot Chat tools
1. Use GitHub Copilot Chat to trigger the MCP tools
1. Debugger pauses at breakpoints

## License

MIT
