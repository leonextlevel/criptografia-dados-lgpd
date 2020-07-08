# Segurança da Informação

##  Entrega Final 
[Banco com Dados Criptografados](https://github.com/LLBueno/seguranca-informacao/blob/master/Dados_Criptografados.png)

[Mostrando os dados do usuario](https://github.com/LLBueno/seguranca-informacao/blob/master/Mostrando%20dados%20do%20usuario%207.png)

[Pedindo PDF do usuario](https://github.com/LLBueno/seguranca-informacao/blob/master/Geração%20do%20PDF.png)

[PDF do usuario](https://github.com/LLBueno/seguranca-informacao/blob/master/Modelo%20PDF.png)

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

[Entrega 3](https://github.com/LLBueno/seguranca-informacao/blob/master/docs/3entrega.md)

[Entrega 4](https://github.com/LLBueno/seguranca-informacao/blob/master/docs/4entrega.md)

[Entrega 5](https://github.com/LLBueno/seguranca-informacao/blob/master/docs/5entrega.md)

### Integrantes do Grupo

* Leandro Lopes (Master)
* Murilo Leme
* Matheus Henrique
* Guilherme Rodrigo
* Mônica Torres

### Executando o projeto

1. Todo o projeto está "dockerizado", logo só é necessário ter instalada
um versão recente do Docker e Docker Compose.

2. Realize um build para construir o ambiente e instalar as dependencias
   > $ docker-compose build

3. Crie um arquivo `.env` com base no arquivo `env-sample`.

4. Suba o vault para depois configurarmos
   > $ docker-compose up -d vault

   **Configurando o vault...**

   * Entre no container para configurar o vault (esse processo só será necessário 1 vez)
      > $ docker exec -it seg_info_vault /bin/sh
      
   * Inicie o vault, isso gerará as chaves e o Token, é importante salvá-los.
      > vault operator init -key-shares=6 -key-threshold=3

   * Escolha 3 das 6 chaves e execute o comando de "unseal" para cada uma delas.
      Por exemplo:
      > vault operator unseal RntjR...DQv

   * Faça login utilizando o Token. Por exemplo:
      > vault login s.tdlEqsfzGbePVlke5hTpr9Um

   * Por último habilite o sistema de segredos do vault
      > vault secrets enable -version=1 -path=secret kv

5. Pegue o Token gerado e mais 3 chaves e edite o seu `.env`.

6. Agora já possível executar a aplicação
   > $ docker-compose run --service-ports --rm python
