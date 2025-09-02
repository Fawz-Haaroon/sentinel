import click
from rich.console import Console

from app.core.services import detect_url, analyze_url

console = Console()

@click.group()
def main():
    pass

@main.command("serve")
@click.argument("args", nargs=-1)
def serve(args):
    from app import server
    import uvicorn
  
    uvicorn.run(server.app)

@main.command("detect")
@click.argument("URL", nargs=1)
@click.argument("args", nargs=-1)
def check(url, args):
    console.print(detect_url(url))

@main.command("analze")
@click.argument("URL", nargs=1)
@click.argument("args", nargs=-1)
def analyze(url, args):
    console.print(analyze_url(url))
