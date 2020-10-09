# type: ignore[attr-defined]

from typing import Optional

import random
from enum import Enum

import typer
from latam import __version__
from latam.example import hello
from latam.paises import *
from rich.console import Console


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="latam",
    help="Un paquete para trabajar facilmente con metadatos de paises en latinoamerica.",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(f"[yellow]latam[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for name. If not specified then choice will be random.",
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the latam package.",
    ),
):
    """Prints a greeting for a giving name."""
    if color is None:
        # If no color specified use random value from `Color` class
        color = random.choice(list(Color.__members__.values()))

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")
