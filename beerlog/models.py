from logging import raiseExceptions
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint, Column, String
from sqlmodel import select
from pydantic import validator
from datetime import datetime


class Inadiplente(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    rg: str
    cpf: str = Field(sa_column=Column("cpf", String, unique=True))
    endereco: str
    objeto: str
    date: datetime = Field(default_factory=datetime.now)

    @validator("cpf")
    def validate_cpf(cls, v, field):
        if (len(v) != 11 or not v.isdigit()):
            raise RuntimeError(
                f"{field.name} Quantidade de Números no CPF incorreto ou entrada incorreta. Verifique os dados inseridos"
            )
        return v

    @validator("rg")
    def validate_rg(cls, v, field):
        rg = [int(char) for char in v if char.isdigit()]
        if len(rg) != 10:
            raise RuntimeError(
                f"{field.name} Quantidade de Números no RG incorreto"
            )
        return v


