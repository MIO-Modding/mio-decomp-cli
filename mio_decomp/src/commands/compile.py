from pathlib import Path
from typing import Annotated

import typer
from rich import print

from mio_decomp.src.libraries.decompiler.decompiler import GinDecompiler

app = typer.Typer()


@app.command()
def compile(
    header_file: Annotated[
        Path,
        typer.Argument(
            help="The path to the header JSON file to build into a .gin file.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    mappings_file: Annotated[
        Path,
        typer.Option(
            "-m",
            "--mapping",
            help="The path to the mapping file.",
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    output_file: Annotated[
        Path | None,
        typer.Option(
            "-o",
            "--output",
            help="The file to output the compiled .gin file to.",
            file_okay=True,
            dir_okay=False,
            writable=True,
            readable=True,
            resolve_path=True,
        ),
    ] = None,
    debug: Annotated[
        bool, typer.Option(help="Enables print statements used in debugging.")
    ] = False,
):
    """Compiles files into a .gin file."""
    if not header_file.exists():
        print(
            f'"{str(header_file)}" not found! Please double check that the input .gin file exists.'
        )
        typer.Abort()

    if not mappings_file.exists():
        print(
            f'"{str(mappings_file)}" not found! Please double check that the input .gin file exists.'
        )
        typer.Abort()

    if output_file is None:
        output_file: Path = Path(".") / header_file.with_suffix("").name
        output_file: Path = output_file.resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    if output_file.exists():
        output_file.unlink()
    output_file.touch()

    compiler: GinDecompiler = GinDecompiler(silent=not debug)
    compiler.compile_single(
        header_file=header_file,
        mappings_file=mappings_file,
        output_file=output_file,
    )
