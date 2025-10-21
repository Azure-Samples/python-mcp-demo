# Python MCP Demos

This repository implements a **minimal MCP expense tracker**.

The Model Context Protocol (MCP) is an open standard that enables LLMs to connect to external data sources and tools.

## Table of Contents

- [Getting Started](#getting-started)
  - [Environment Setup](#environment-setup)
  - [Run the MCP Server in VS Code](#run-the-mcp-server-in-vs-code)
  - [GitHub Copilot Chat Integration](#github-copilot-chat-integration)
  - [MCP Inspector](#mcp-inspector)
- [Debugging](#debugging)
  - [Debugging with VS Code and debugpy](#debugging-with-vs-code-and-debugpy)
  - [Testing with MCP Inspector](#testing-with-mcp-inspector)
- [Contributing](#contributing)

## Getting Started

### Environment Setup

#### 1. GitHub Codespaces 

1. Click the **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for the environment to build (dependencies install automatically)

#### 2. Local VS Code Dev Container

**Requirements:** Docker + VS Code + Dev Containers extension

1. Open the repo in VS Code
2. When prompted, select **Reopen in Container** (or run `Dev Containers: Reopen in Container` from the Command Palette)
3. Wait for the container to build

#### 3. Local Machine Without a Dev Container

If you prefer a plain local environment, use **uv** for dependency management:

```bash
uv sync
```

### Use MCP Server with  GitHub Copilot Chat

### Run the MCP Server in VS Code

1. Open `.vscode/mcp.json` in the editor
1. Click the **Start** button (▶) above the server name `expenses-mcp`
1. Confirm in the output panel that the server is running
1. Open the GitHub Copilot Chat panel (bottom right, or via Command Palette: `GitHub Copilot: Focus Chat`)
1. Click the **Tools** icon (wrench) at the bottom of the chat panel
1. Ensure `expenses-mcp` is selected in the list of available tools
1. Ask Copilot to invoke the tool:
   - "Use add_expense to record a $12 lunch today paid with visa"
   - "Read the expenses resource"

### MCP Inspector

The MCP Inspector is a browser-based visual testing and debugging tool for MCP servers.

#### Launch the MCP Inspector in GitHub Codespaces

1. Run the following command in the terminal:
   ```bash
   .devcontainer/launch-inspector-codespace.sh
   ```

2. Note the **Inspector Proxy Address** and **Session Token** from the terminal output

3. In the **Ports** view, set port **6277** to **PUBLIC** visibility

4. Access the Inspector UI and configure:
   - **Transport Type**: `SSE`
   - **Inspector Proxy Address**: (from terminal output)
   - **Proxy Session Token**: (from terminal output)
   - **Command**: `uv`
   - **Arguments**: `run main.py`

#### Launch the MCP Inspector inside of a Dev Container

1. Run the following command in the terminal:
   ```bash
   HOST=0.0.0.0 DANGEROUSLY_OMIT_AUTH=true npx -y @modelcontextprotocol/inspector
   ```
2. Open `http://localhost:6274` in your browser
3. The Inspector should now connect to your MCP server

> **Note:** `HOST=0.0.0.0` is required in devcontainer environments to bind the Inspector to all network interfaces, allowing proper communication between the UI and proxy server. `DANGEROUSLY_OMIT_AUTH=true` disables authentication - only use in trusted development environments.

#### Launch the inspector locally without Dev Container:**

1. Run the following command in the terminal:
   ```bash
   npx @modelcontextprotocol/inspector uv run main.py
   ```
2. The Inspector will automatically open in your browser at `http://localhost:6274`


---

## Debugging

You can attach the VS Code debugger to the running MCP server to set breakpoints and inspect code execution.

### Debugging stdio server with GitHub Copilot

To debug the stdio server (`main.py`) while using it with GitHub Copilot:

1. Open `.vscode/mcp.json` in the editor

2. Start the **expenses-mcp-debug** server (instead of expenses-mcp)

3. In VS Code, open the Run and Debug panel (Ctrl+Shift+D / Cmd+Shift+D)

4. Select **"Attach to MCP Server"** from the dropdown and click the play button (or press F5)

5. In GitHub Copilot Chat, make sure **expenses-mcp-debug** is selected in the tools menu

6. Set breakpoints in `main.py` and use the server from GitHub Copilot Chat. Breakpoints will be hit when tools are invoked.

### Debugging HTTP server with MCP Inspector

To debug the HTTP server (`main_http.py`) while testing with the MCP Inspector:

1. Start the HTTP server with debugpy enabled:
   ```bash
   uv run -- python -m debugpy --listen 0.0.0.0:5678 main_http.py
   ```

2. In VS Code, open the Run and Debug panel (Ctrl+Shift+D / Cmd+Shift+D)

3. Select **"Attach to MCP Server"** from the dropdown and click the play button (or press F5)

4. Open the MCP Inspector UI and configure:
   - **Transport Type**: `HTTP`
   - **URL**: `http://localhost:8000`
   - Click **Connect**

5. Set breakpoints in `main_http.py` and test your tools from the Inspector UI. Breakpoints will be hit when you invoke tools.

---


## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.
