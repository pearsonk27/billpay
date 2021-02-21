import psycopg2
from web.views import my_info

def insert_task(task_name):
    """Initiates connection, inserts task, returns task id"""
    task_id = insert_record("INSERT INTO task(name) VALUES (%s) RETURNING id;", (task_name,))
    return task_id

def insert_record(sql, params):
    """Gets connection, executes given SQL with given params, returns generated id"""
    conn = None
    id = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return id

def exec_sql_return_scalar(sql, params):
    """Gets connection, executes given SQL with given params, returns produced scalar"""
    conn = None
    res = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        res = cur.fetchone()[0]
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return res

def start_task(task_id):
    """Insert execution log record for the chosen task and return execution log id"""
    execution_log_id = insert_record("INSERT INTO execution_log (task_id, start_date_time) SELECT %s, NOW() RETURNING id;", (task_id,))
    return execution_log_id

def get_connection():
    return psycopg2.connect(
            host=my_info.database_host(),
            database=my_info.database_name(),
            user=my_info.database_user(),
            password=my_info.database_password())

def end_task(execution_log_id):
    """"""
    update_one_row("UPDATE execution_log SET end_date_time = NOW() WHERE id = %s;", (execution_log_id,))

def update_one_row(sql, params):
    """"""
    conn = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql, params)
        updated_rows = cur.rowcount
        if updated_rows != 1:
            raise Exception("Unexpected number of rows updated ({updated_rows})")
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_task_id(task_name):
    """"""
    conn = None
    id = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM task WHERE name = %s;", (task_name,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        raise LookupError(f"'{task_name}' search did not produce a result", error)

    finally:
        if conn is not None:
            conn.close()

    return id

def get_step_id(step_name, task_id):
    """"""
    conn = None
    id = None

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM execution_step WHERE name = %s AND task_id = %s;", (step_name,task_id,))
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO execution_step (name, task_id) VALUES (%s, %s) RETURNING id;", (step_name,task_id,))
            row = cur.fetchone()
        id = row[0]
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
    
    return id

def start_execution_step(execution_log_id, step_name):
    """"""
    task_id = get_task_id_with_execution_log_id(execution_log_id)
    step_id = get_step_id(step_name, task_id)
    execution_step_log_id = exec_sql_return_scalar("INSERT INTO execution_step_log (execution_log_id, execution_step_id, start_date_time) VALUES (%s, %s, NOW()) RETURNING id;", (execution_log_id, step_id,))
    return execution_step_log_id

def end_execution_step(execution_step_log_id):
    """"""
    update_one_row("UPDATE execution_step_log SET end_date_time = NOW() WHERE id = %s;", (execution_step_log_id,))

def get_task_id_with_execution_log_id(execution_log_id):
    """"""
    return exec_sql_return_scalar("SELECT task_id FROM execution_log WHERE id = %s", (execution_log_id,))
