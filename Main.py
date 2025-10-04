#todo
"""
Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress

Store to JSON
"""
from Task import *

tasks = [
    Task("MAS", "Dve predavacky", "so 4.10.2025", "15:00"),
    Task("SI", "Interview", "po 6.10.2025", "13:00", Progress.IN_PROGRESS)
]

for task in tasks:
    print("________________________")
    task.print_task()
    print("________________________")

print("****************************")
print("What would you like to do?: ")
print("1. Add task")
print("2. Update task")
print("3. Delete task")
print("****************************")

while True:
    x = str(input("Make a choice: "))
    print("Your choice was " + x + ".")

