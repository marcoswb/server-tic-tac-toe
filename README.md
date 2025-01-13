# Servidor Jogo da Velha

Esse projeto visa a criação de dois servidores(API e servidor socket) para o controle de um jogo da velha via Rede.

### API
A API foi feita utilizando o framework Flask e é responsável por controlar o login/registro dos jogadores, além de fornecer informações que serão tratadas e demonstradas no frontend.

Para persistência de dados foi utilizado o [DynamoDB](https://aws.amazon.com/pt/dynamodb/) da AWS. A escolha desse banco de dados foi motivada por ser tratar de um banco de dados não relacional, que serviu como fonte prática de estudos a fim de conhecer melhor o funcionamento desse modelo de banco que é amplamente utilizado e testar na prática os seus diferenciais.

Como padrões de segurança as senhas dos jogadores foram todas armazenadas utilizando técnicas de hashing irreversíveis(eficaz contra ameaças em caso de exposição dos dados) e o serviço de API conta com criptografia de todas as requisições por meio do protocolo https, que foi implementando utilizando certificados SSL no servidor e cliente.

A API conta com os seguintes endpoints:
- '/login': Responsável por realizar o controle de login dos usuários e fornecer um código de acesso que será usado posteriormente para realizar a conexão com o servidor socket.
- '/register': Responsável por realizar o cadastro dos jogadores.
- '/users/free': Retorna os usuários livres no momento para uma partida, informação importante para ser demonstrada aos jogadores e assim os mesmos poderem convidar outros jogadores para uma partida.
- '/users/status': Retorna o status de todos os jogadores.
- '/history': Retorna o histórico de partidas de um jogador.
- '/logout': Responsável pelo controle de logout dos jogadores, atualizando seu status para os demais jogadores online.

### Servidor socket
Esse servidor é o responsável por gerenciar os jogadores presentes na mesma rede e atribuir partidas aleatórias conforme necessidade ou iniciar partida entre dois jogadores específicos.

Para o modo de partida aleatória o servidor age criando uma fila de jogadores, onde sempre que dois usuários se conectarem ao servidor socket uma partida será iniciada entre esses dois usuários. Além disso, o servidor suporta indefinidas partidas simultâneas pois trabalha de forma paralela usando o recursos de Threads da linguagem Python, sendo assim podem ser iniciadas várias partidas diferentes entre clientes na mesma rede, e todas serão conduzidas de forma isolada pelo servidor, sem uma interferir na outra.

Já no modo de partida entre dois jogadores específicos, o servidor recebe o pedido de partida com um usuário específico e checa em sua memória, caso o oponente já tenha realizando conexão com o servidor, a partida é iniciada de forma isolada utilizando Threads conforme no modo aleatório, e caso o oponente ainda não tenha se conectado, o primeiro jogador irá ficar aguardando até que ambos estejam conectados e a partida possa ser iniciada.

Como forma de segurança a fim de evitar conexões indevidas ao servidor, foi implementado um sistema de "login", onde para se conectar ao servidor socket o cliente necessita encaminhar um código que é fornecido pela API no momento do login no app, assim o servidor socket recebe esse código e checa diretamente com o código que está salvo no banco de dados para permitir ou não a conexão do cliente.

### Execução do projeto

Para a inicialização dos servidores basta seguir os passos abaixo:
1. Realizar o clone do repositório com o comando `git clone https://github.com/marcoswb/server-tic-tac-toe.git`;
2. Realizar a instalação das dependências com o comando `pip install -r requirements.txt`;
3. Criar um arquivo .env para a inicialização das variáveis de ambiente conforme exemplo abaixo:
  - host=localhost;
  - port=8000;
  - size_buffer_packets=1024
4. Realizar a criação da chaves SSL e colocar os arquivos 'cert.pem' e 'key.pem' no mesmo diretório do projeto.
5. Inicializar ambos os servidores com os seguintes comandos:
  - `python apy.py`: Inicializar API;
  - `python server.py`: Inicializar servidor socket;
6. Não é necessário realizar nenhum passo a mais para a criação da estrutura do banco de dados, isso porque ela é criada automaticamente caso não exista no momento que for utilizada.
