import time
import redis
import psycopg2
import os
from flask import Flask

app = Flask(__name__)

# Configurações via Variáveis de Ambiente (Boas Práticas!)
# Note que os 'hostnames' são os nomes dos serviços no docker-compose
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'appdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'senha123')
    )
    return conn

# Cria tabela se não existir (apenas para teste)
def init_db():
    retries = 5
    while retries > 0:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS acessos (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')
            conn.commit()
            cur.close()
            conn.close()
            return
        except Exception as e:
            print(f"Banco ainda não pronto... tentando de novo. Erro: {e}")
            time.sleep(2)
            retries -= 1

@app.route('/')
def hello():
    # 1. Incrementa contador no Redis
    count = cache.incr('hits')
    
    # 2. Registra acesso no Postgres
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO acessos DEFAULT VALUES;')
        conn.commit()
        cur.close()
        conn.close()
        db_status = "Gravado no Postgres com sucesso!"
    except Exception as e:
        db_status = f"Erro no Postgres: {e}"

    return f'Ola! Eu fui visto {count} vezes. Status DB: {db_status}.\n'

if __name__ == "__main__":
    init_db() # Tenta criar a tabela ao iniciar
    app.run(host="0.0.0.0", port=5000)