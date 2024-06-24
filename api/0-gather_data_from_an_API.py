#!/usr/bin/python3
"""Get to-do progress of an employee"""

import requests
import sys


"""Module"""

if __name__ == '__main__':
    employee_id = sys.argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    employee_info = requests.get(employee_url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info["name"]
    tasks_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todo_info))
    number_of_done_tasks = len(tasks_completed)
    total_number_of_tasks = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, number_of_done_tasks, total_number_of_tasks))

    [print("\t " + task["title"]) for task in tasks_completed]
