import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


try:
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_USER"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    print("connected succesfully")
except Exception as e:
    print(f"Failed to connect: {e}")
