from db import connect_db

def register():
    username = input("Enter username :")
    email = input("Enter email: ")
    password = input("Enter password: ")

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO
    users(username,email,password_hash)
    VALUES(%s,%s,%s)
    """


    cursor.execute(query,(username,email,password))

    conn.commit()

    print("Registration Successfull")

    cursor.close()
    conn.close()