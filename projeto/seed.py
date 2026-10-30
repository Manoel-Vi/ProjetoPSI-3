from database import SessionLocal
from sqlalchemy import select
from models import Usuario, Jogo, Categoria
from werkzeug.security import generate_password_hash

def adicionar_admin():
    db = SessionLocal()

    stmt = select(Usuario).where(Usuario.email == "admin@nexusgx.com")
    admin = db.execute(stmt).scalar()

    if not admin:
        admin = Usuario(
            nome="Admin Nexus",
            email="admin@nexusgx.com",
            senha=generate_password_hash("nexus")
        )

        db.add(admin)
        
        db.commit()
        db.close()

def adicionar_categorias():

    db = SessionLocal()

    if not db.execute(select(Categoria)).scalar():
        categoria_acao = Categoria(nome="Ação")
        categoria_rpg = Categoria(nome="RPG")
        categoria_aventura = Categoria(nome="Aventura")
        categoria_ficcao_cientifica = Categoria(nome="Ficção Científica")
        categoria_souls = Categoria(nome="Souls-like")
        categoria_estrategia = Categoria(nome="Estratégia")
        categoria_tiro = Categoria(nome="Tiro")
        categoria_simulacao = Categoria(nome="Simulação")
        categoria_esportes = Categoria(nome="Esportes")
        categoria_terror = Categoria(nome="Terror")

        db.add_all([categoria_acao, categoria_rpg, categoria_aventura, categoria_ficcao_cientifica, categoria_souls, categoria_estrategia, categoria_terror, categoria_tiro, categoria_simulacao, categoria_esportes])

        db.commit()
        db.close()