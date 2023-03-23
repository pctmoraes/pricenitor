# PRICENITOR: o seu monitor de preços

Projeto tem como objetivo permitir ao usuário pesquisar o melhor preço de um determinado produto, para tal, foi desenvolvida uma API que se comunica com o banco de dados PostegreSQL para o consumo dos dados de Preços de produtos e retorna, caso seja encontrada a opção do produto passada pelo usuário, as informações do nome do produto, loja com o menor preço e o preço.

### Tecnologias utilizadas
- Python 3.9
- FastAPI
- Uvicorn
- Docker
- PostgreSQL
- PgAdmin
- Postman

## Instruções para execução do projeto
## Pre-requisitos:
- repositório clonado <br>
- docker desktop instalado e rodando
- python e pip instalados
<br>

1. Acesse a pasta -> `cd pricenitor`
2. Execute o comando para instalação das dependências -> `pip install -r requirements.txt`
3. Execute o comando para composição do container docker -> `docker-compose up -d`
    - Serão criados dois containers, um com o banco de dados PostgreSQL e um com pgAdmin para a gestão do db
4. Acesse o pgAdmin pelo seu navegador através da URL -> `localhost:5050`
    - Insira o login `admin@gmail.com` e senha `admin`
    - Com o botão direito no menu `Server` clique em `Register > Server`
    - Na aba General insira:
        - Name = `db`
    - Na aba Connection insira:
        - Host name/address = `postgresql`
        - Port = 5432
        - Username = admin
        - Password = admin
    - Clique em `Save`
    - Com queries de inserção popule a tabela com dados fictícios para utilizá-los com o scraper python.
5. Execute o comando para rodar o servidor -> `uvicorn main:app`
    - Por padrão o servidor irá utilizar a porta 8000, mas é possível alterar passando uma outra porta através da flag --port, por exemplo -> `uvicorn main:app`
    - A documentação da API, gerada automaticamente pelo FastAPI, poderá ser consultada acessando o endpoint `localhost:8000/docs`, nela é possível verificar todos os endpoints disponíveis
6. Rode o scraper com o comando -> `python scraper.py`
7. O programara irá pedir por uma descrição de produto, digite e clique em enter, caso encontre a opção, o programá retornará o produto, a loja com o menor preço e o preço, caso contrário, irá retornar uma mensagem informando o usuário.