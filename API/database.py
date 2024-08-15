import mysql.connector
import config

def connect_to_database():
    try:
        connection = mysql.connector.connect(host=config.db_hostname, user=config.db_username,
                                             password=config.db_password)
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to database:", error)
        return error


def execute_sql_query(sql_query, query_parameters=None):
    connection = connect_to_database()
    result = ''
    try:
        cursor = connection.cursor()
        if query_parameters:
            cursor.execute(sql_query, query_parameters)
        else:
            cursor.execute(sql_query)

        if sql_query.upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = True

    except mysql.connector.Error as exception:
        print("Error executing SQL query:", exception)
        result = exception

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

        return result


def execute_sql_query_with_params(sql_query, query_parameters):
    connection = connect_to_database()
    result = ''
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, query_parameters)

        if sql_query.upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = True

    except mysql.connector.Error as exception:
        print("Error executing SQL query:", exception)
        result = exception

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

        return result