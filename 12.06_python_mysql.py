import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="cwiczenia"
    )

def create_job(title, min, max):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO jobs (title, min_salary, max_salary) VALUES (%s, %s, %s)" #argumenty w takiej jakie
    variables = (title, min, max)
    cursor.execute(query, variables)
    conn.commit()
    print(f"Dodano stanowisko {title}")
    conn.close()

# create_job("Murarz", 4000, 10000)

#to nie jest najlepszy sposob
def read_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM jobs"
    cursor.execute(query)

    for job in cursor.fetchall():
        print(job)

#lepszy ten
def read_jobs_pandas():
    conn = get_connection()
    query = "SELECT * FROM jobs"
    df = pd.read_sql(query, conn)
    df.to_excel("plik.xlsx")
    conn.close()
    print(df)

# read_jobs_pandas()

def update_job(id, field, value):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"UPDATE jobs SET {field} = %s WHERE id = %s"
    variables = (value, id)
    cursor.execute(query, variables)
    conn.commit()
    print(f"Zaktualizowane kolumnę {field}")
    conn.close()

# update_job(16, 'title', 'Tynkarz')
update_job(1, 'min_salary', 999)

def delete_job(id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM jobs WHERE id = %s"
    cursor.execute(query,(id,))
    conn.commit()
    print("usunięto")
    conn.close()

# delete_job(16)

def read_with_pandas(query):
    conn = get_connection()
    df = pd.read_sql(query,conn)
    df.to_excel("plik.xlsx")
    conn.close()
    print(df)

# read_with_pandas("SELECT * FROM jobs")
# read_with_pandas("SELECT * FROM employees")

read_with_pandas(
    """
        SELECT e.email, j.title 
        FROM employees AS e
        INNER JOIN jobs AS j
        ON e.job_id = j.id
    """
)