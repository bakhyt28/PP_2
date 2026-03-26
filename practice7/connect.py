import psycopg2
from config import config

def connect():
    try:
        conn = psycopg2.connect(
            host=config["host"],
            database=config["database"],
            user=config["user"],
            password=config["password"]
        )
        print("Connected!")
        return conn
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    connect()