# Desafio 5: Arquitetura de Microsserviços com API Gateway

Este projeto implementa o padrão de design **API Gateway** utilizando Nginx para centralizar e rotear o tráfego para múltiplos microsserviços backend.

## 🏗️ Arquitetura

O cliente não comunica diretamente com os microsserviços. Todo o tráfego passa por um ponto único de entrada (Gateway), que atua como um *Reverse Proxy*.

### Benefícios desta abordagem:
* **Segurança**: Os serviços de backend (Users/Orders) não expõem portas para a rede externa, vivendo numa rede privada do Docker.
* **Simplicidade**: O cliente precisa conhecer apenas uma URL base (`localhost`), sem gerir múltiplas portas.

### Componentes:
1.  **API Gateway (`nginx`)**:
    * Porta Exposta: 80.
    * Rota `/users` → Encaminha para `user-service:5000`.
    * Rota `/orders` → Encaminha para `order-service:5000`.
2.  **User Service**:
    * Microsserviço Python/Flask retornando lista de usuários.
    * Acessível apenas internamente.
3.  **Order Service**:
    * Microsserviço Python/Flask retornando lista de pedidos.
    * Acessível apenas internamente.

## 🚀 Instruções de Execução

Utilizamos Docker Compose para construir e orquestrar os três containers simultaneamente.

### 1. Execução
```bash
docker-compose up -d --build
```

### 2. Validação
O Gateway está escutando na porta padrão HTTP (80).

Teste Users:

```bash
curl http://localhost/users
```
Teste Orders:
```bash
curl http://localhost/orders
```

### 3. Parar a Aplicação
```bash
docker-compose down
```