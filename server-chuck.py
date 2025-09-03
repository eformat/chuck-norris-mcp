from mcp.server.fastmcp import FastMCP
import click
import httpx
import base64
import sys
import httpx

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
    def get_joke():
        """
        Get me a Chuck Norris Joke
        """
        try:
            response = httpx.get("https://api.chucknorris.io/jokes/random", timeout=10.0)
            response.raise_for_status()
            #return response.json()
            return response.json()['value'].replace('\n', '')
        except httpx.HTTPError as exc:
            return {"error": "Failed to fetch Chuck Norris joke", "detail": str(exc)}

    mcp.run(transport='sse')
    return 0

if __name__ == "__main__":
    sys.exit(main())
