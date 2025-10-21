#!/usr/bin/env bash
set -euo pipefail

if [ -n "${CODESPACE_NAME:-}" ]; then
    CODESPACE_URL="https://${CODESPACE_NAME}-6274.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
    PROXY_URL="https://${CODESPACE_NAME}-6277.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
    
    echo "🚀 Launching MCP Inspector..."
    echo ""
    echo "📋 Configuration for Inspector UI:"
    echo "   Inspector Proxy Address: $PROXY_URL"
    echo ""
    
    ALLOWED_ORIGINS="$CODESPACE_URL" npx -y @modelcontextprotocol/inspector uv run main.py
else
    echo "🚀 Launching MCP Inspector..."
    npx -y @modelcontextprotocol/inspector 
fi
