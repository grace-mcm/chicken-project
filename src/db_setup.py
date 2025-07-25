import psycopg2
import csv
from dotenv import load_dotenv
import os

#create connection to database
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

connection = psycopg2.connect(f"""
    host={host_name}
    dbname={database_name}
    user={user_name}
    password={user_password}
    """)

cursor = connection.cursor()

# Create the chickens table
def create_chickens_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chickens (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            breed VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            birthday DATE NOT NULL
        );
    """)
    connection.commit()
    cursor.close()

def extract_csv():
    with open('data/british_chickens.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute("""
            INSERT INTO chickens (name, breed, age, birthday)
            VALUES (%s, %s, %s, %s);
        """, row)
    connection.commit()