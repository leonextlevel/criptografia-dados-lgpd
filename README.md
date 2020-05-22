# Segurança da Informação


### Problema

Com a nova LGPD, é possível que os dados sensíveis precisem ser criptografados no banco,
sendo assim é preciso uma rotina que automatize e torne viável essa pratica.

### Proposta

A ideia é um sistema que dentro da rotina de criar dados, utilize de uma criptografia simétrica
para esconder os dados sensíveis dos usuários, guarde a chave em um ambiente seguro e a utilize,
quando necessário, para recuperar os dados.

Para demonstrar o funcionamento, será gerado um relatório em PDF.

### Observações

Requisito da LGPD: O usuário deve ter acesso aos seus dados a qualquer momento.

Proposta: Mapear em busco de todas as informações de um usuário respectivo.

Problema: Os dados podem estar criptografados, qual o impacto nas querys?

### Entregas

1. **(18/03)** Estrutura genérica do banco de dados com o requisitos necessários,
dentro das normas da LGPD, contendo um algoritmo de conexão;

1. **(13/05)** Integração da Criptografia com o gerador de dados, salvando inicialmente as chaves
em um arquivo `.key`;

3. **(27/05)** Integração com o Vault. As chaves serão salvas e recuperadas de um servidor Vault;

4. **(10/06)** Gerador de relatório em formato pdf implementado, consumindo dados reais do banco;

5. **(24/06)** Aprimoramento do código;

6. **(08/07)** Entrega funcional.


### Relatórios de Entrega

[Entrega 1](https://github.com/LLBueno/seguranca-informacao/blob/master/docs/1entrega.md)

[Entrega 2](https://github.com/LLBueno/seguranca-informacao/blob/master/docs/2entrega.md)

### Integrantes do Grupo

* Leandro Lopes (Master)
* Murilo Leme
* Matheus Henrique
* Guilherme Rodrigo
* Mônica Torres

### Executando o projeto

A partir do diretório raiz:

1. Instale as dependencias utilizando o pipenv
   > pipenv sync -d

2. Entre no ambiente virtual com pipenv
   > pipenv shell

Após isso já é possível trabalhar os dados com o python por meio do
arquivo `src/main.py`