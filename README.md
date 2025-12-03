# 🐳 Portfólio de Desafios Docker

Este repositório contém as soluções para a atividade prática de Docker, abordando desde conceitos fundamentais de redes e volumes até a orquestração de microsserviços complexos com API Gateway.

**Aluno:** Pedro Fernandes  
**Disciplina:** DevOps / Arquitetura de Software

---

## 📂 Estrutura do Repositório

O projeto está dividido em 5 desafios incrementais. Cada diretório possui seu próprio `README.md` com instruções detalhadas de execução e explicação da arquitetura.

| Diretório | Tópico Abordado | Tecnologias Principais |
| :--- | :--- | :--- |
| [**📂 desafio1**](./desafio1) | **Containers em Rede**<br>Comunicação entre containers via rede *bridge* customizada. | Python (http.server), Curl, Docker Network |
| [**📂 desafio2**](./desafio2) | **Persistência de Dados**<br>Uso de Docker Volumes para garantir a durabilidade de dados de banco. | PostgreSQL, Docker Volumes |
| [**📂 desafio3**](./desafio3) | **Orquestração (Compose)**<br>Aplicação completa com Web, Cache e Banco orquestrada via Docker Compose. | Python (Flask), Redis, PostgreSQL, Docker Compose |
| [**📂 desafio4**](./desafio4) | **Microsserviços**<br>Comunicação HTTP síncrona entre dois serviços independentes. | Python (Flask), Requests, Dockerfiles Multi-stage |
| [**📂 desafio5**](./desafio5) | **API Gateway**<br>Implementação do padrão Gateway com Nginx para roteamento centralizado. | Nginx (Reverse Proxy), Python (Flask), Docker Compose |

---

## 🛠️ Tecnologias Utilizadas

* **Docker & Docker Compose:** Containerização e orquestração.
* **Python (Flask):** Desenvolvimento das APIs e microsserviços.
* **PostgreSQL:** Banco de dados relacional para persistência.
* **Redis:** Banco de dados em memória para cache.
* **Nginx:** Servidor web utilizado como Reverse Proxy/API Gateway.
* **Alpine Linux:** Imagens base para otimização de tamanho.

---

## 🚀 Como Executar

Pré-requisitos: Tenha o **Docker** e o **Git** instalados.

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/desafios-docker.git](https://github.com/SEU_USUARIO/desafios-docker.git)
    cd desafios-docker
    ```

2.  **Escolha um desafio:**
    Navegue até a pasta do desafio desejado. Exemplo:
    ```bash
    cd desafio3
    ```

3.  **Siga as instruções locais:**
    Leia o arquivo `README.md` dentro da pasta escolhida para ver os comandos específicos de `build` e `run`.

---

## ✅ Checklist de Avaliação

- [x] **Desafio 1:** Rede customizada configurada e comunicação funcional.
- [x] **Desafio 2:** Persistência de dados comprovada após remoção do container.
- [x] **Desafio 3:** `docker-compose.yml` estruturado com `depends_on` e variáveis de ambiente.
- [x] **Desafio 4:** Microsserviços independentes com Dockerfiles isolados.
- [x] **Desafio 5:** API Gateway (Nginx) roteando corretamente para os serviços de backend.

---
*Desenvolvido para fins acadêmicos.*