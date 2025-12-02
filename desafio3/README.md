# Desafio 3: Orquestração de Serviços com Docker Compose

Este projeto implementa uma aplicação web completa composta por três serviços interdependentes, orquestrados via Docker Compose.

## 🏗️ Arquitetura

A solução utiliza uma arquitetura de microsserviços simples onde a aplicação web atua como orquestradora de lógica, conectando-se a dois serviços de dados distintos.

### Serviços:
1.  **Web (`flask`)**:
    * Aplicação Python que serve o endpoint principal.
    * Conecta-se ao Redis para contador de visitas (Cache).
    * Conecta-se ao PostgreSQL para log de acessos (Persistência).
2.  **Cache (`redis`)**:
    * Armazena o contador de visualizações em memória RAM para acesso rápido.
3.  **Banco de Dados (`db`)**:
    * PostgreSQL para armazenamento persistente dos logs de acesso.

### ⚙️ Decisões Técnicas no docker-compose.yml

* **`depends_on`**: Foi configurado no serviço `web` para garantir que o Docker inicie os containers de banco e cache antes da aplicação.
* **`environment`**: As credenciais e hosts (DNS) não estão "chumbados" no código Python. Eles são injetados como variáveis de ambiente, permitindo fácil alteração sem recompilar a imagem.
* **Redes**: Foi criada uma rede interna `minha-rede-interna`. Isso isola os serviços do mundo externo (o Redis e o Postgres não expõem portas para fora, apenas para a aplicação Web na porta 5000).

## 🚀 Instruções de Execução

### 1. Build e Execução
Na raiz do projeto, execute o comando para construir a imagem local e subir a infraestrutura:

```bash
docker-compose up -d --build
```

### 2. Validação
Acesse a aplicação via navegador ou terminal:

```bash
curl http://localhost:5000
```
Resultado Esperado: Ola! Eu fui visto 1 vezes. Status DB: Gravado no Postgres com sucesso!.

A cada nova requisição, o contador (Redis) deve incrementar e o status do DB deve confirmar a gravação.

### 3. Parar o Projeto
Para derrubar a infraestrutura:

```bash
docker-compose down
```
