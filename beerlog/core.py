from typing import Optional, List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Inadiplente



def add_inadip_to_database(
    name: str,
    rg: str,
    cpf: str,
    endereco: str,
    objeto: str
) -> bool:
    with get_session() as session:
        inadiplente = Inadiplente(
                name=name,
                rg=rg,
                cpf=cpf,
                endereco=endereco,
                objeto=objeto
        )
        session.add(inadiplente)
        session.commit()
    return True

def list_inad_from_database() -> List[Inadiplente]:
    with get_session() as session:
            sql = select(Inadiplente)
            return list(session.exec(sql))