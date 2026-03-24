import asyncio
import logging
import os

from agent_framework import Agent, MCPStreamableHTTPTool
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from rich import print
from rich.logging import RichHandler

# Configure logging
logging.basicConfig(level=logging.WARNING, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
logger = logging.getLogger("agentframework_learn")
logger.setLevel(logging.INFO)

# Load environment variables
load_dotenv(override=True)

# Configure chat client based on API_HOST
API_HOST = os.getenv("API_HOST", "github")
async_credential = None
if API_HOST == "azure":
    async_credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")
    client = OpenAIChatClient(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
        api_key=token_provider,
        model_id=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
    )
elif API_HOST == "github":
    client = OpenAIChatClient(
        base_url="https://models.github.ai/inference",
        api_key=os.environ["GITHUB_TOKEN"],
        model_id=os.getenv("GITHUB_MODEL", "openai/gpt-4.1-mini"),
    )
elif API_HOST == "ollama":
    client = OpenAIChatClient(
        base_url=os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434/v1"),
        api_key="none",
        model_id=os.environ.get("OLLAMA_MODEL", "llama3.1:latest"),
    )
else:
    client = OpenAIChatClient(
        api_key=os.environ.get("OPENAI_API_KEY"), model_id=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    )


async def http_mcp_example() -> None:
    """
    Creates an agent that can answer questions about Microsoft documentation
    using the Microsoft Learn MCP server.
    """

    try:
        async with (
            MCPStreamableHTTPTool(name="Microsoft Learn MCP", url="https://learn.microsoft.com/api/mcp") as mcp_server,
            Agent(
                client=client,
                name="DocsAgent",
                instructions="You help with Microsoft documentation questions.",
                tools=[mcp_server],
            ) as agent,
        ):
            query = "How to create an Azure storage account using az cli?"
            result = await agent.run(query)
            print(result.text)

    finally:
        if async_credential:
            await async_credential.close()


if __name__ == "__main__":
    asyncio.run(http_mcp_example())
