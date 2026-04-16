import psycopg2
from config import load_config


def connect():
    try:
        conn = psycopg2.connect(**load_config())
        print("Connected successfully")
        conn.close()
    except Exception as e:
        print("Connection error:", e)


if __name__ == "__main__":
    connect()