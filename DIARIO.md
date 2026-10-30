Data: 22/10/2026

O que foi feito: app.py adicionado

Dificuldade encontrada:

Como resolvi:

Próximo passo: adicionar as rotas e templates



Data: 26/10/2026

O que foi feito: atualização na rota de cadastro, agora os dados inseridos nela são adicionados no banco de dados

Dificuldade encontrada: Os links do html e dos controladores estavam divergentes

Como resolvi: Foi observado cada arquivo e alterado o url_for para que ele tenha o prefixo do blueprint, que o cado era auth.

Próximo passo: adicionar as verificações na rota de login e em diante



Data: 28/10/2026

O que foi feito: Atualização na rota de cadastro e login, para que elas possam ser usadas com as funções do flask_login, login_user(), e a criação da rota logout, também utilizando as funções do flask_login, logout_user(), a session foi retirada, e a sessionLocal foi alterada, antes a gente usava a classe Session para criar a sessão do usuário, agora estamos utilizando a função sessiomaker para criar uma SessionLocal, pois ela gera uma sessão a cada usuário e também a fecha quando não existe um usuário logado, a classe Session ia gerar uma sessão global o que não é bom para o site

Dificuldade encontrada: Foi dificil mudar da classe Session para a função sessionmaker, e depois nas rotas, porque a gente não podia chamar a SessionLocal.execute direto

Como resolvi: Nós tivemos que criar uma variavel db que recebe a SessionLocal, para ai a gente chamar o execute, db = SessionLocal(), e depois db.execute(...), nessa parte a gente não entendeu muito bem como funcionava essa mecânica do sessionmaker então utilizamos IA para compreendermos melhor e deixar as rotas funcionando corretamente

Próximo passo: Adicionar as rotas de comprar de jogos, de visualizar jogos, de ver jogos por categoria, implementar no seed alguns jogos padrões para já estarem na loja



Data: 29/10/2026

O que foi feito: atualização no css, nova rota para alterar o nome do usuario, foi criado novos templates e novas rotas para as páginas relacionadas aos jogos(bases foram criadas)

Dificuldade encontrada: Hoje não teve nenhuma

Como resolvi: 

Próximo passo: Melhorar as rotas relacionadas aos jogos atualizar o css, e adicionar jogos padrões no banco de dados



Data: 30/10/2026

O que foi feito: Css atualizado, criação da classe pedidos e atualizações nas classes jogos e usuarios, para que os dados do usuario fiquem salvos quando ele for adicionar um jogo, função de adicionar categorias e admin no seed.py, troca de lógica no app.py, antes usava db = SessionLocal() o que não fecha a coexão, e agora usa o with que fecha a sessão sem problemas

Dificuldade encontrada: Css tava mal organizado, com algumas classes sem utilizar o que confundiu bastante, quando a função de adicionar admin funcionava a gente entrava no projeto já logado na conta por causa do db = SessionLocal()

Como resolvi: As classes e ids foram retiradas ou alteradas para melhorar o funcionamento do css e deixa-lo mais claro, a lógica foi trocada de db = SessionLocal() para usarmos o with que resolveu o erro de já entrar logado no site

Próximo passo: Atualizar mais o css, e desenvolver as rotas relacionadas aos jogos, adicionar jogos padrões e imagens para os jogos