from typing import List
from sqlalchemy import ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
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
    senha: Mapped[str] = mapped_column(String(255))

    pedidos: Mapped[List['Pedido']] = relationship(back_populates='usuario')

class Jogo(Base):
    __tablename__ = 'jogos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(String(200))
    imagem: Mapped[str] = mapped_column(String(100))

    pedidos: Mapped[List['Pedido']] = relationship(back_populates='jogo')

    categorias:Mapped[List['Categoria']] = relationship(secondary= jogo_categoria ,back_populates= 'jogos')


class Categoria(Base):
    __tablename__ = 'categorias'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))

    jogos:Mapped[List['Jogo']] = relationship(secondary = jogo_categoria ,back_populates= 'categorias')

class Pedido(Base):
    __tablename__ = 'pedidos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuarios.id'))
    id_jogo: Mapped[int] = mapped_column(ForeignKey('jogos.id'))

    jogo: Mapped['Jogo'] = relationship(back_populates='pedidos')
    usuario: Mapped['Usuario'] = relationship(back_populates='pedidos')
