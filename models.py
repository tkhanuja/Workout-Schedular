import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
        
    except Error as e:
        print(e)
    return conn
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    
    sql_create_workouts_table =  """CREATE TABLE IF NOT EXISTS workouts (
                                        id integer PRIMARY KEY,
                                        category text NOT NULL,
                                        name text NOT NULL,
                                        per_set integer,
                                        weight integer,
                                        sets integer,
                                        duration integer
                                    );"""
    # id, month of , num completed, total 
    # sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
    #                                 id integer PRIMARY KEY,
    #                                 name text NOT NULL,
    #                                 priority integer,
    #                                 status_id integer NOT NULL,
    #                                 project_id integer NOT NULL,
    #                                 begin_date text NOT NULL,
    #                                 end_date text NOT NULL,
    #                                 FOREIGN KEY (project_id) REFERENCES projects (id)
    #                             );"""
    conn = create_connection('workouts.db')
    
    create_table(conn, sql_create_workouts_table)
    