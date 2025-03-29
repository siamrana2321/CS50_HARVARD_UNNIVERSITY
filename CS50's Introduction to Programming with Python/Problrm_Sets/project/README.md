# Task Manager

**Video Demo :**https://youtu.be/U1LkmTtOeZE?si=YN77Pvusykxh5ddp

**Description :**

Task Manager is a command-line utility that allows users to easily organize and manage their routine tasks.   This project was produced as part of the CS50p final project and demonstrates a range of Python programming skills, such as file processing, user interaction, and automated testing with Pytest.

The program enables users to Add, View, Update, Delete and Save tasks, resulting in an ordered workflow for personal and professional task management.   To ensure that tasks survive across sessions, they are maintained in a JSON file.   The project's aim is to develop a simple but effective task management application that requires minimal user effort.



**Features :**

1. Add Tasks: Users can add tasks which includes (description, category, due date, and priority level).

2. View Tasks: Displays tasks along with their completion status and tasks are organized by ID.

3. Mark Task as Completed: Users can mark tasks as completed by entering the task ID.

4. Delete Tasks: Allows users to remove tasks from the list.

5. Save and Load Tasks: The program saves tasks in a JSON file (tasks.json), ensuring durability between sessions.

**File Breakdown :**
- project.py - Core script containing functions for task management, including adding, viewing, completing, deleting, saving, and loading tasks.
- test_project.py - Contains unit tests for task management functions to ensure reliability.
- tasks.json - Stores all user-created tasks to maintain data persistence.


This Task Manager gives a simple yet effective approach to keep track of assignments and deadlines.
