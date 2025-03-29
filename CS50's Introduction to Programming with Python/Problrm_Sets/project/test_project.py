import pytest
from project import add_task, mark_task_completed, delete_task

def test_add_task():
    tasks = []
    add_task(tasks, "Finish CS50p project", "School", "2025-04-10", "High")
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Finish CS50p project"

def test_mark_task_completed():
    tasks = [{"id": 1, "task": "Test Task", "category": "Work", "due_date": "2025-03-30", "priority": "Medium", "completed": False}]
    mark_task_completed(tasks, 1)
    assert tasks[0]["completed"] is True

def test_delete_task():
    tasks = [{"id": 1, "task": "Test Task", "category": "Work", "due_date": "2025-03-30", "priority": "Medium", "completed": False}]
    delete_task(tasks, 1)
    assert len(tasks) == 0
