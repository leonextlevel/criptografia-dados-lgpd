# 1ª ENTREGA (18/03)

## Resumo

Grande parte do avanço foi em estruturar o projeto, definir as melhores ferramentas e criar algo simples em cima delas,
como resultado temos:

* Modelo de um banco de dados genérico que será utilizado para desenvolvimento;
* Hospedagem de um banco Postgresql no elephantSQL;
* Algoritmo Python com a ORM Peewee gerando uma conexão com o banco e estrutura do banco de acordo com o modelo;


## Ferramentas
* brModelo 3.0
* Postgresql
* ElephantSQL
* Peewee
* Pipenv

O [brModelo](http://www.sis4.com/brModelo/brModelo.pdf) foi usado para criarmos um Banco hipotético já que necessitamos de um Banco genérico para trabalhar as dificuldades da implementação da LGPD.

Já o gerenciador de Banco de Dados esta sendo utilizado o [Postgresql](https://www.postgresql.org/) já que possuímos um conhecimento mais elevado sobre esse gerenciador facilitando o processo de implementação do banco. O banco de teste esta sendo hospedado através do [ElephantSQL](https://www.elephantsql.com/plans.html/).

Como o algoritmo utilizado será em Python, utlizamos o Pipenv uma ferramenta completa  para o gerenciamento de dependências em projetos em Python, sendo elas:

* [Peewee](http://docs.peewee-orm.com/en/latest/) - para trabalharmos com o banco, assim facilitando o manuseio do próprio. Peewee é um ORM que destinada a criar e gerenciar tabelas do banco relacional através do de objetos Python que basicamente transforma classes no Python em tabelas no banco;

* [Psycopg2](https://www.psycopg.org/) – Um driver adaptador de Postgresql para a linguagem Python.
