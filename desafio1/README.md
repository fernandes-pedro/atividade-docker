# Desafio 1: Comunicação entre Contentores em Rede

Este projeto foi desenvolvido como parte da atividade prática de Docker. O objetivo é demonstrar a capacidade de criar uma comunicação isolada e nomeada entre dois contentores distintos utilizando uma rede Docker personalizada.

## 🏗️ Arquitetura e Fluxo

O sistema é composto por dois microsserviços simples que partilham a mesma rede virtual (`bridge network`). A comunicação não é feita por endereços IP fixos, mas sim através da resolução de nomes (DNS) interna do Docker.

### Componentes:

1.  **Rede Docker (`rede-desafio-1`)**:
    * Uma rede do tipo `bridge` criada explicitamente para permitir que os contentores se "vejam" e resolvam os nomes de host um do outro.
    * **Decisão Técnica**: O uso de uma rede personalizada é preferível à rede padrão (`default bridge`), pois esta última não suporta a resolução automática de nomes de contentores (Service Discovery).

2.  **Servidor Web (`servidor-python`)**:
    * **Imagem**: `python:alpine`.
    * **Porta**: 8080 (Interna).
    * **Função**: Executa um servidor HTTP simples nativo do Python (`http.server`).
    * **Decisão Técnica**: Escolheu-se a imagem `alpine` pelo seu tamanho reduzido e o Python pela facilidade de levantar um servidor web sem necessidade de código adicional ou configurações complexas como no Nginx.

3.  **Cliente (`cliente-curl`)**:
    * **Imagem**: `curlimages/curl`.
    * **Função**: Realiza pedidos HTTP `GET` periódicos (a cada 5 segundos) ao servidor.
    * **Decisão Técnica**: Utilização de uma imagem minimalista focada apenas no utilitário `curl` para simular tráfego de rede e validar a conectividade.

---

## 🚀 Instruções de Execução

Siga os passos abaixo no terminal (PowerShell, Bash ou CMD) para colocar o projeto em funcionamento.

### 1. Criar a Rede
Primeiramente, criamos a camada de rede que isolará os nossos contentores.

```bash
docker network create rede-desafio-1
```
### 2. Iniciar o Servidor 

Iniciamos o contentor que servirá o conteúdo na porta 8080.

```bash
docker run -d --name servidor-python --network rede-desafio-1 python:alpine python -m http.server 8080
```
### 3. Iniciar o Cliente
Iniciamos o contentor que fará os pedidos. Note que utilizamos http://servidor-python na URL. O Docker resolve automaticamente este nome para o IP correto do contentor do servidor.

```bash
docker run -d --name cliente-curl --network rede-desafio-1 curlimages/curl /bin/sh -c "while true; do curl -v http://servidor-python:8080; sleep 5; done"
```
### 4. Validação e testes

Verificar se o servidor está a receber pedidos: Deve ver registos com o código 200 vindos do IP do cliente.

```bash
docker logs servidor-python
```
Verificar se o cliente está a receber respostas: Deve ver o código HTML da página padrão do Python e o cabeçalho HTTP 200.

```bash
docker logs cliente-curl
```
### 5. Limpeza (Recomendada)

Para parar a execução e remover os recursos criados:

```bash
# Remover os contentores (forçando a paragem)
docker rm -f servidor-python cliente-curl

# Remover a rede criada
docker network rm rede-desafio-1
```

