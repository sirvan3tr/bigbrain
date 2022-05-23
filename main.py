import meilisearch
import json
import click

from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import uuid


client = meilisearch.Client('http://127.0.0.1:7700')
console = Console()

@click.group()
def cli():
  pass

@cli.command()
@click.option('--index', default='movies', help='Index to search in.')
@click.option('--query', prompt='Your search query')
def search(index, query):
    """
    """
    ret = client.index(index).search(query)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Description", style="dim", width=24)
    table.add_column("Code")

    for item in ret['hits']:
        syntax = Syntax(
            item['code'],
            "python",
            theme="monokai")
        table.add_row(
            str(item['desc']),
            syntax,
        )

    console.print(table)


@cli.command()
@click.option('--index', prompt='Index...')
@click.option('--desc', prompt='Enter description...')
@click.option('--code', prompt='Enter code snippet...')
def add(index, desc, code):
    doc_id = uuid.uuid4().hex

    doc = {
        "id": doc_id,
        "desc": desc,
        "code": code
    }

    print(doc)
    client.index(index).add_documents([doc])


if __name__ == '__main__':
    cli()
