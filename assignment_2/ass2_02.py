

import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

emp_id = int(input("Enter emp_id: "))
name = input("Enter name :")
salary = int(input("Enter salary :"))
dept = (input("Enter dept :"))
email = input("Enter email")
date_of_joining = input("Enter date")

query = f"insert into employee values({emp_id},'{name}',{salary},'{dept}','{email}','{date_of_joining}');"

cursor= connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

def delete_employee(emp_id):
    query = f"delete from persons where emp_id = %s;"
    val = (emp_id, )

    cursor= connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

    connection.close()


delete_employee(8101)

# def update_employee(salary):



