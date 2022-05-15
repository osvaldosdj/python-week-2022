import typer
from typing import Optional
from beerlog.core import add_inadip_to_database, list_inad_from_database
from rich.table import Table 
from rich.console import Console 

main = typer.Typer(help="Gestão de Indiplentes")

console = Console()

@main.command("add")
def add(name: str, rg: str, cpf: str, endereco: str, objeto: str):
    """Adiciona Inadiplentes na base de dados"""
    if add_inadip_to_database (name,rg,cpf,endereco,objeto):
        print("Inserido com sucesso")
    else:
        print("Erro ao inserir no banco de dados. Use beerlog --help para uma ajuda do comando")

@main.command("list")
def list_inad(cpf: Optional[str] = None):
    """Lista Inadiplentes da base de dados"""
    caloteiros = list_inad_from_database()
    table = Table(title="Caloteiros")
    headers = ["id", "name", "rg", "cpf", "endereco", "objeto", "date"]
    for header in headers:
        table.add_column(header,style="magenta")
    for inadiplente in caloteiros:
        inadiplente.date = inadiplente.date.strftime("%Y-%m-%d")
        values = [str(getattr(inadiplente,header)) for header in headers]
        table.add_row(*values)
    console.print(table)
    #print(caloteiros)



