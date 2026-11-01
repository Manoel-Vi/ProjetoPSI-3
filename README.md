# Nome do Projeto:
Nexus GX

# Tema escolhido:
Biblioteca de Jogos

# Integrantes:
- Gabriel de Medeiros Lima
- Lucival dos Santos Lves
- Manoel Victor Lopes de Medeiros
- Alisson Bezerra Cândido da Silva

# Responsabilidade de cada integrante:
Lucival:
- Responsável pelos modelos relacionais no banco de dados - Model.

Gabriel:
- Responsável pela criação de templates, aquivos html - View.

Manoel: 
- Responsável pela criação de rotas - Controller.

Alisson:
- Responsável pela estilização das páginas, arquivo css - View.

OBS: Cada integrante tem sua responsabilidade principal porém todos mexem no projeto como um todo, ou seja cada um pode alterar os arquivos de outra camada do projeto para que ele possa funcionar, eles não estão presos somente a aquela responsabilidade principal imposta acima.

# Descrição do sistema:
NexusGX tem como objetivo permitir que os usuários organizem e gerenciem sua própria biblioteca de jogos, podendo adicionar jogos aos seus pedidos, visualizar os títulos disponíveis e acompanhar suas seleções. Cada usuário terá seus próprios jogos, pedidos e carrinhos, separados por meio de seu ID. Os pedidos poderão conter informações como nome dos jogos, e comentários ou descrições opcionais. Como o projeto tem foco no universo dos games, o sistema contará com diversos títulos de diferentes gêneros e categorias, proporcionando uma experiência simples e organizada para os usuarios.

# Entidades do sistema:

# Usuario
- id (Integer, PK)
- nome (String)
- email (String, Unique)
- senha (String)
  
# Jogo
- id (Integer, PK)
- nome (String)
- descricao (String)
- imagem (String)
- 
# Categoria
# Pedido

# Explicação do relacionamento 1:N ;

# Explicação do relacionamento N:N ;

# Instruções para rodar o projeto
- 1: Criar o ambiente vitual. py -m venv env

- 2: Ativar o ambiente. .\env\scripts\activate

- 3: Instalar os requerimentos. pip install -r requirements

- 4: flask run --debug

- 5: Ser feliz

# Declaração de autoria:
Declaro que desenvolvemos este projeto e compreendenmos o código entregue e que sou capaz de explicar e modificar suas partes principais.

# Uso de IA:
Usamos.

# Descrição do uso, se houver: (houve)
- na criação da rota para fazer o botão de adicionar o jogo aos pedidos.
- na div "esconder fundo" no css.

# Justificativa e menções sobre o uso da IA generativa
Prazo apertado e um pouco de falta de conhecimento técnico em algumas partes especificas. Romerito, você, é o cara.
