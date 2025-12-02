# Desafio 2: Persistência de Dados com Volumes Docker

Este projeto demonstra como garantir a durabilidade dos dados em ambientes de containers, utilizando Docker Volumes para desacoplar o ciclo de vida dos dados do ciclo de vida do container.

## 🏗️ Arquitetura

Utilizou-se o banco de dados **PostgreSQL** devido à sua robustez e padrão de armazenamento em diretórios específicos (`/var/lib/postgresql/data`).

### Componentes:
1.  **Docker Volume (`volume-dados-pg`)**:
    * Um volume gerenciado ("Named Volume") que armazena os arquivos físicos do banco de dados no host.
    * **Decisão Técnica**: Optou-se por um *Named Volume* em vez de *Bind Mount* por ser a prática recomendada para bancos de dados, garantindo melhor performance e gestão de permissões pelo Docker.

2.  **Container PostgreSQL (`postgres:alpine`)**:
    * Executa o serviço de banco de dados.
    * Mapeia o volume criado para o diretório interno de dados.

## 🚀 Instruções de Execução e Teste de Persistência

O teste consiste em gravar dados num container, destruí-lo, e recuperar os dados em um container novo.

### 1. Configuração do Volume
Criar o volume isolado:
```bash
docker volume create volume-dados-pg
```

### 2. Ciclo de Vida 1: Gravação
Iniciamos o primeiro container (pg-antigo) e inserimos um registro.
```bash
# Iniciar
docker run -d --name pg-antigo -e POSTGRES_PASSWORD=senha123 -v volume-dados-pg:/var/lib/postgresql/data postgres:alpine

# Gravar Dados
docker exec -it pg-antigo psql -U postgres -c "CREATE TABLE desafio (mensagem TEXT); INSERT INTO desafio VALUES ('Os dados sobreviveram!');"
```

### 3. Simulação de Perda
Removemos o container de forma forçada para simular uma falha ou atualização.
```bash
docker rm -f pg-antigo
```

### 4. Ciclo de Vida 2: Recuperação
Iniciamos um novo container (pg-novo), ligando-o ao mesmo volume.
```bash
docker run -d --name pg-novo -e POSTGRES_PASSWORD=senha123 -v volume-dados-pg:/var/lib/postgresql/data postgres:alpine
```

### 5. Validação
Consultamos a tabela no novo container para confirmar a persistência.
```bash
docker exec -it pg-novo psql -U postgres -c "SELECT * FROM desafio;"
```
Resultado Esperado: O comando acima deve retornar a string: Os dados sobreviveram!

### 6. Limpeza (Recomendada)
Para remover os containers e o volume (cuidado, isso apaga os dados permanentemente):
```bash
docker rm -f pg-novo
docker volume rm volume-dados-pg
```