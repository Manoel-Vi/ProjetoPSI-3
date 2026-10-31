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

def popular_jogos():
    db = SessionLocal()

    if not db.execute(select(Jogo)).scalar():
        jogos = [Jogo(nome='Call of Duty: Modern Warfare 4', descricao='Jogo de tiro em primeira pessoa com combates intensos, operações militares e modos multiplayer competitivos.', imagem='static/imagensUsadas/codmw4.png'),
                Jogo(nome='Dark Souls 2', descricao='RPG de ação desafiador em um mundo sombrio, com exploração, combates estratégicos e chefes poderosos.', imagem='static/imagensUsadas/ds2.png'),
                Jogo(nome='Elden Ring', descricao='RPG de ação em mundo aberto que combina exploração, fantasia sombria, combates desafiadores e liberdade de progressão.', imagem='static/imagensUsadas/eldenring.png'),
                Jogo(nome='Far Cry 6', descricao='Jogo de tiro em mundo aberto ambientado em uma ilha caribenha fictícia, onde você luta contra um regime ditatorial.', imagem='static/imagensUsadas/farcry6.png'),
                Jogo(nome='Terraria', descricao='Aventura 2D que mistura exploração, construção, mineração e batalhas contra criaturas e chefes.', imagem='static/imagensUsadas/terraria.png'),
                Jogo(nome='EA Sports FC 26 (FIFA 26)', descricao='Simulador de futebol com equipes, jogadores e competições, oferecendo modos individuais e multiplayer.', imagem='static/imagensUsadas/fifa26.png'),
                Jogo(nome='Hollow Knight: Silksong', descricao='Aventura de ação em 2D na qual Hornet explora um reino misterioso, enfrentando inimigos e chefes desafiadores.', imagem='static/imagensUsadas/silksong.png'),
                Jogo(nome='Monster Hunter Wilds', descricao='RPG de ação em que você caça monstros gigantes, coleta recursos e cria equipamentos cada vez mais poderosos.', imagem='static/imagensUsadas/mhw.png'),
                Jogo(nome='Monster Hunter Rise', descricao='RPG de ação focado na caça de monstros, com combates dinâmicos, exploração e diversas armas.', imagem='static/imagensUsadas/mhr.png'),
                Jogo(nome='The Binding of Isaac', descricao='Roguelike de ação com exploração de masmorras, itens aleatórios e desafios cada vez mais difíceis.', imagem='static/imagensUsadas/tboi.png'),]

        db.add_all(jogos)
        db.commit()
        db.close()