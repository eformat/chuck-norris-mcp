# chuck norris joke mcp

[FastMCP](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md)

To test using `mcp dev server.py` move mcp out of main:

```python
port=8000
mcp = FastMCP(
    "mcp-tools",
    debug=True,
    log_level="INFO",
    port=port,
)
```

```bash
podman build --no-cache -t quay.io/eformat/chuck-mcp:latest -f Containerfile
```
