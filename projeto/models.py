from typing import List
from sqlalchemy import ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, engine, session
from flask_login import UserMixin

jogo_categoria = Table(
    "jogos_categorias",
    Base.metadata,
    Column("jogo_id", ForeignKey("jogos.id"), primary_key=True),
    Column("categoria_id", ForeignKey("categorias.id"), primary_key=True),
)

class Usuario(Base, UserMixin):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    senha: Mapped[str] = mapped_column(String(80))

    jogos: Mapped[List['Jogo']] = relationship(back_populates='usuario')

class Jogo(Base):
    __tablename__ = 'jogos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(String(200))
    id_usuario:Mapped[int] = mapped_column(ForeignKey('usuarios.id'))

    usuario:Mapped['Usuario'] = relationship(back_populates='jogos')

    categorias:Mapped[List['Categoria']] = relationship(secondary= jogo_categoria ,back_populates= 'jogos')


class Categoria(Base):
    __tablename__ = 'categorias'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))

    jogos:Mapped[List['Jogo']] = relationship(secondary = jogo_categoria ,back_populates= 'categorias')

Base.metadata.create_all(bind=engine)