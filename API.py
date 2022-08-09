import sqlite3
from os import remove
# This is connection
conn = sqlite3.connect("Tasks_DateBase.db")

cursor = conn.cursor()

def init() : 

    "Create table"

    # create table 
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
        TaskCategory TEXT ,
        description TEXT , 
        status TEXT 
        ) 
        """)

    # Save
    conn.commit()


def insert(task_category , task_msg , task_status) :
    "insert a task to date base"

    cursor.execute(f'''INSERT INTO tasks VALUES (:task_category , :task_msg , :task_status) ''' , 
    {'task_category' : task_category , 'task_msg' : task_msg , 'task_status' : task_status})
    conn.commit()


def display(task_category = None): 
    "Show the tasks"

    if task_category == None : 

        # Show all tasks 

        cursor.execute("""SELECT * FROM tasks""")
        result = cursor.fetchall()

    else : 
        
        cursor.execute('''SELECT * FROM tasks WHERE TaskCategory = :TaskCategory''' , 
        {'TaskCategory' : task_category})

        result = cursor.fetchall()

    return result 


def delete(category = None) : 
    "Delete category"

    if category == None : 
        input("Enter any thing for delete date base file ...")
        conn.close()

        remove("Tasks_DateBase.db")

        print("Date base delete :(")

    elif category != None : 
        input("Enter any thing for delete the task...")
        
        cursor.execute("""DELETE FROM tasks WHERE TaskCategory = :TaskCategory """ , 
        {'TaskCategory' : category})

        conn.commit()

        print("Task Removed :(")
