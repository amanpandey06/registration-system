import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user ="root",
        password ="@man2006ABC",
        database = "registration_system"
    )

    return connection
