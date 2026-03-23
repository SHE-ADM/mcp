from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
import asyncio

app = Server("MeuPrimeiroServidor")

@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="get_clima",
            description="Retorna o clima de uma cidade",
            inputSchema={
                "type": "object",
                "properties": {
                    "cidade": {
                        "type": "string",
                        "description": "Nome da cidade"
                    }
                },
                "required": ["cidade"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_clima":
        cidade = arguments.get("cidade", "São Paulo")
        # Aqui você pode integrar uma API real de clima
        return [types.TextContent(
            type="text",
            text=f"O clima em {cidade} está ensolarado, 25°C."
        )]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())