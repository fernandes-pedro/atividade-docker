# Desafio 4: Microsserviços Independentes

Este projeto simula um ambiente distribuído com dois microsserviços Python (Flask) comunicando-se via protocolo HTTP dentro de uma rede Docker.

## 🏗️ Arquitetura

O sistema não possui banco de dados. A dependência é direta entre serviços (Síncrona).

### Fluxo de Comunicação:
1.  **Cliente (Externo)** → faz requisição `GET /profile` para o **Service B**.
2.  **Service B** → faz requisição interna `GET http://service-a:5000/users` para o **Service A**.
3.  **Service A** → retorna JSON com dados básicos do usuário.
4.  **Service B** → enriquece os dados e retorna a resposta final ao cliente.

### Componentes:
* **Service A (`/service-a`)**:
    * Imagem customizada baseada em `python:3.9-slim`.
    * Endpoint: `/users`.
    * Porta: 5000 (Apenas interna).
* **Service B (`/service-b`)**:
    * Imagem customizada baseada em `python:3.9-slim`.
    * Endpoint: `/profile`.
    * Porta: 5000 (Exposta no host como 8080).
* **Rede (`rede-microservicos`)**:
    * Permite a resolução de nomes (DNS) onde `service-a` é resolvido para o IP do container correspondente.

## 🚀 Instruções de Execução

Este desafio foca na construção manual das imagens para demonstrar a independência dos serviços.

### 1. Criar Rede
```bash
docker network create rede-microservicos
```

### 2. Service A (Provedor)
```bash
cd service-a
docker build -t imagem-service-a .
docker run -d --name service-a --network rede-microservicos imagem-service-a
cd ..
```

### 3. Service B (Consumidor)
```bash
cd service-b
docker build -t imagem-service-b .
docker run -d --name service-b --network rede-microservicos -p 8080:5000 imagem-service-b
cd ..
```

### 4. Validação
Acesse o endpoint do consumidor:
```bash
curl http://localhost:8080/profile
```

### 5. Limpeza (Recomendado)
```bash
docker rm -f service-a service-b
docker network rm rede-microservicos
```