import typer

from .decompile_multi import app as multi_app

# from .decompile_single import app as single_app

app = typer.Typer(
    help="Decompile .gin files.",
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)

# app.add_typer(single_app)
app.add_typer(multi_app)
