# Segurança da Informação

### Integrantes do Grupo

* Leandro Lopes (Master)
* Murilo Leme
* Matheus Henrique
* Guilherme Rodrigo
* Mônica Torres

### Proposta

Tendo como referência a disponibilidade das informações para um usuário, dentro da nova [LGPD](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm), a ideia é mapear bancos de dados (Postgresql) disponibilizando a opção de geração de relatórios contendo todas as informações e métricas que o sistema possui relacionadas ao usuário.

### Observações

Requisito da LGPD: O usuário deve ter acesso aos seus dados a qualquer momento.

Proposta: Mapear em busco de todas as informações de um usuário respectivo.

Problema: Os dados podem estar criptografados, qual o impacto nas querys?

### Entregas

1. (18/03) Estrutura genérica do banco de dados com o requisitos necessários,
dentro das normas da LGPD, contendo um algoritmo de conexão.

2. (01/04)...

3.

4.

5.

6.

7. (Final) Algoritmo de mapeamento funcionando, capaz de descriptografar dados
sensíveis, desde que seja passado a chave de criptografia do usuário e as credenciais
do banco. Como resultado, ele emitirá um relatório de tudo encontrado.


