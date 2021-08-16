# Desafio programação - para vaga desenvolvedor

Como proposto no desafio, esta aplicação permite o upload de um arquivo CNAE e o interpreta, fazendo com que as informações contidas no arquivo seja transformada em uma tabela. No arquivo exemplo, ainda crio uma segunda tabela trazendo as informações de saldo de cada cliente apresentado.

# Tecnologias aplicadas

Para realizar esse desafio, utilizei a linguagem `Python`. Para a aplicação web, fiz o uso do `Django`, seu framework web e do seu próprio banco, o `sqlite`. Optei pelo sqlite pela integração mais rápida ao projeto, assim dependendo menos de ferramentas externas para implementar o banco de dados. Utilizei o seu ORM para deixar o código mais limpo e claro de se entender, sem strings de SQL, utilizando o máximo da ferramenta disponível nativamente do django. 
Para manipular algumas informações principalmente na tabela onde trago os saldos dos clientes, utilizei a biblioteca `Pandas`, na qual tenho uma grande familiaridade. Tentei criar um código simples, escalável e performatico que fosse de fácil entendimento e que não tivesse complexidades que poderia dificultar futuras melhorias e/ou complementos da ferramenta. 
Também fiz uso do `Django-admin` onde é criada uma página de administração que permite o acesso as tabelas criadas pela aplicação.

# Configurando o ambiente

Para rodar o programa é preciso fazer o clone do repositório em sua máquina local com o comando a seguir `git clone https://github.com/Giovannisb/desafio-dev.git`. Após realizar a clonagem do repositório, iremos acessar a pasta do projeto com `cd desafio`. Tendo a premissa que em sua máquina já tenha instalado o python nas versões 3.6 ou superiores, iremos instalar as dependências do projeto. `pip install -r requirements.txt`. Após instalar todas as dependências, podemos iniciar o projeto em `python manage.py runserver`, esse comando irá iniciar o servidor, assim podemos acessar a aplicação pelo navegador em `http://127.0.0.1:8000/`. Pronto, agora podemos realizar o upload do arquivo CNAE e ver a mágica acontecer.

### Extra

Para complementar, também foi gerada uma página admin, onde é possível acessar as tabelas do banco, basta acessar `http://127.0.0.1:8000/admin`, o login é bem genérico com usuário e senha admin. Dessa forma podemos visualizar, manipular, criar e deletar as informações contidas no banco de dados.
