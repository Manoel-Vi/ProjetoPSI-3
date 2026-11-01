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
- pedidos (Lista) -> Pedido
  
# Jogo
- id (Integer, PK)
- nome (String)
- descricao (String)
- imagem (String)

- pedidos (Lista) -> Pedido
- categorias (Lista) -> jogo_categoria(tabela intermediaria)

# Categoria
- id (Integer, PK)
- nome (String)

- jogos (Listaa) -> jogo_categoria(tabela intermediaria)

# Pedido
- id (Integer, PK)
- id_usuario (ForeignKey) -> Usuario
- id_jogo (ForeignKey) -> Jogo

- usuario (Lista) -> Usuario
- jogo (Lista) -> Jogo


# Explicação do relacionamento 1:N ;
Usuario é a entidade capaz de possuir vários pedidos relacionados a si, porém a Entidade Pedido não pode ter vários usuários, tendo em vista que cada pedido pertence a somente um usuário e a um jogo por vez. Um relacionamento 1:N consiste, basicamente, em uma das tabelas poder ter elementos ligados a quantidades indeterminadas de elementos da outra tabela, porém sem que esses outros elementos possam se ligar a mais de um elemento da primeira.

# Explicação do relacionamento N:N ;
O relacionamento N:N define um relacionamento onde cada elemento de uma tabela pode possuir, de forma indireta, mais de um elemento de uma outra tabela, sendo indireto em teoria, por ser mediado através de uma terceira tabela que guarda as informações essenciais (ids) de cada um dos elementos das outras duas tabelas principais, como exemplo: Um usuário pode possuir vários jogos, e vice versa, através do relacionamento mútuo com uma terceira tabela chamada pedidos, que tem um relacionamento de 1:N com Usuário e com Jogo, tendo também como exemplo o relacionamento entre a tabela Categorias e a tabela de Jogos, que têm um relacionamento N:N intermediado pela tabela jogo_categoria, que é uma lista de dicionários com os ids do jogo e da categoria que se relacionam entre si.

# Instruções para rodar o projeto
- 1: Criar o ambiente virtual. comando: py -m venv env

- 2: Ativar o ambiente. .\env\Scripts\activate

- 3: Instalar os requerimentos. pip install -r requirements.txt

- 4: flask run --debug

- 5: Ser feliz

# Declaração de autoria:
Declaro que desenvolvemos este projeto e compreendenmos o código entregue e que sou capaz de explicar e modificar suas partes principais.

# Uso de IA:
Usamos.

# Descrição do uso, se houver: (houve)
- na criação da rota para fazer o botão de adicionar o jogo aos pedidos.
- na div "esconder fundo" no css.
- na rota dos jogos pessoais do usuário, para conseguir usar Pedido como intermediário, através de um select.

# Justificativa e menções sobre o uso da IA generativa
Prazo apertado e um pouco de falta de conhecimento técnico em algumas partes especificas. Romerito, você, é o cara.
Principal uso: auxilio durante a produção do select na página que mostra os jogos do usuário, devido aos joins que o responsável por essa parte(Lucival), nao tinha tanta noção sobre como utilizar, principalmente por caausa do relacionamento N:N, que não conseguimos encontrar na documentação(talvez um erro de atenção nosso).