from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List
import click
import httpx
import base64
import sys

class JokeData(BaseModel):
    """Joke information structure."""
    categories: List[str]
    created_at: str
    icon_url: str
    id: str
    updated_at: str
    url: str
    value: str

@click.command()
@click.option("--port", default=8085, help="Port to listen", type=int)
def main(port: int):
    mcp = FastMCP(
        "mcp-tools",
        debug=True,
        log_level="INFO",
        port=port,
        host="0.0.0.0",
    )

    @mcp.tool()
    def get_joke() -> str:
        """
        Get me a Chuck Norris Joke
        """
        try:
            response = httpx.get("https://api.chucknorris.io/jokes/random?category=movie", timeout=10.0)
            response.raise_for_status()
            joke = JokeData.model_validate(response.json())
            return joke
        except httpx.HTTPError as exc:
            return {"error": "Failed to fetch Chuck Norris joke", "detail": str(exc)}

    mcp.run(transport='sse')
    return 0

if __name__ == "__main__":
    sys.exit(main())
