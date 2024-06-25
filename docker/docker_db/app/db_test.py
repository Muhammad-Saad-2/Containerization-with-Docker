import os
import psycopg2

DATABASE_URL = os.getenv('DATABASE_URL')

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connected to the database!")
except Exception as e:
    print(f"Failed to connect: {e}")
