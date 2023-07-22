import click

from src.commands.algo_to_script import convert_ipynb_to_py

@click.group()
def cli():
    pass

cli.add_command(convert_ipynb_to_py)
