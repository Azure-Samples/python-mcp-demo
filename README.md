# Python MCP Demos

This repository implements a **minimal MCP expense tracker**.

The Model Context Protocol (MCP) is an open standard that enables LLMs to connect to external data sources and tools.

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

### Run the MCP Server in VS Code

1. Open `.vscode/mcp.json` in the editor
2. Click the **Start** button (▶) above the server name `expenses-mcp`
3. Confirm in the output panel that the server is running

### GitHub Copilot Chat Integration

Make sure the MCP server is running, then:

1. Open the GitHub Copilot Chat panel (bottom right, or via Command Palette: `GitHub Copilot: Focus Chat`)
2. Click the **Tools** icon (wrench) at the bottom of the chat panel
3. Ensure `expenses-mcp` is selected in the list of available tools
4. Ask Copilot to invoke the tool:
   - "Use add_expense to record a $12 lunch today paid with visa"
   - "Read the expenses resource"

### MCP Inspector

The MCP Inspector is a browser-based visual testing and debugging tool for MCP servers.

**Launch the inspector in GitHub Codespaces:**

1. Run the following command in the terminal:
   ```bash
   .devcontainer/launch-inspector.sh
   ```

2. Note the **Inspector Proxy Address** and **Session Token** from the terminal output

3. In the **Ports** view, set port **6277** to **PUBLIC** visibility

4. Access the Inspector UI and configure:
   - **Transport Type**: `SSE`
   - **Inspector Proxy Address**: (from terminal output)
   - **Proxy Session Token**: (from terminal output)
   - **Command**: `uv`
   - **Arguments**: `run main.py`

**Launch the inspector inside of a Dev Container:**

1. Run the following command in the terminal:
   ```bash
   HOST=0.0.0.0 DANGEROUSLY_OMIT_AUTH=true npx @modelcontextprotocol/inspector uv run main.py
   ```
2. Open `http://localhost:6274` in your browser
3. The Inspector should now connect to your MCP server

> **Note:** `HOST=0.0.0.0` is required in devcontainer environments to bind the Inspector to all network interfaces, allowing proper communication between the UI and proxy server. `DANGEROUSLY_OMIT_AUTH=true` disables authentication - only use in trusted development environments.

**Launch the inspector locally without Dev Container:**

1. Run the following command in the terminal:
   ```bash
   npx @modelcontextprotocol/inspector uv run main.py
   ```
2. The Inspector will automatically open in your browser at `http://localhost:6274`



---


## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.