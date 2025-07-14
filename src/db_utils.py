import psycopg2
import os
from dotenv import load_dotenv

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

#fetches all current entries in the chickens table
def chicken_list():
    chicken = "SELECT * FROM chickens"
    cursor.execute(chicken)
    result = cursor.fetchall()
    for row in result:
        print(row)

def add_new_chicken(name, breed, age, birthday):
    add_chicken = """
                    INSERT INTO chickens(name, breed, age, birthday)
                    VALUES(%s, %s, %s, %s)
                    RETURNING chicken_id, name, breed, age, birthday
                    """
    new_chicken_values = (name, breed, age, birthday)
    cursor.execute(add_chicken, new_chicken_values)
    connection.commit()

def update_chicken(chicken_id, name, breed, age, birthday):
    update_chicken_query = """
                            UPDATE chickens
                            SET name = %s, breed = %s, age = %s, birthday = %s
                            WHERE chicken_id = %s
                            RETURNING chicken_id, name, breed, age, birthday
                            """
    update_values = (name, breed, age, birthday, chicken_id)
    cursor.execute(update_chicken_query, update_values)
    connection.commit()

def remove_chicken(chicken_id):
    remove_chicken_query = """
                            DELETE FROM chickens
                            WHERE chicken_id = %s
                            RETURNING chicken_id
                            """
    cursor.execute(remove_chicken_query, (chicken_id,))
    connection.commit()