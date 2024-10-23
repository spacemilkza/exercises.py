import sqlite3

tasks = []

def todo_create(tasks):
  try:
    new_task = input() 
    tasks.append({task:new_task, completed:False})
  except Exception as err:
    print(err) 
  finally:
    return tasks 
    
todo_create(tasks)
