from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[String] = mapped_column(String(100))
    email: Mapped[String] = mapped_column(String(120), unique=True)
    senha: Mapped[String] = mapped_column(String(80))

    jogos: Mapped[List['Jogo']] = relationship(back_populates='usuario')

class Jogo(Base):
    __tablename__ = 'jogos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[String] = mapped_column(String(100))
    descricao: Mapped[String] = mapped_column(String(200))
    id_usuario:Mapped[int] = mapped_column(ForeignKey('usuarios.id'))

    usuario:Mapped['Usuario'] = relationship(back_populates='jogos')