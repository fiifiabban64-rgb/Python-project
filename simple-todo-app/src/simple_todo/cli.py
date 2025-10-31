# Contents of /simple-todo-app/simple-todo-app/src/simple_todo/cli.py

import click
from .storage import load_tasks, save_tasks
from .models import TodoItem

tasks = load_tasks()

@click.group()
def cli():
    """Simple To-Do Application CLI."""
    pass

@cli.command()
@click.argument('title')
def add(title):
    """Add a new task."""
    task_id = len(tasks) + 1
    task = TodoItem(id=task_id, title=title, completed=False)
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f'Task "{title}" added with ID {task_id}.')

@cli.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Remove a task by ID."""
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    save_tasks(tasks)
    click.echo(f'Task with ID {task_id} removed.')

@cli.command()
def list():
    """List all tasks."""
    if not tasks:
        click.echo("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task.completed else "✗"
        click.echo(f'[{status}] {task.id}: {task.title}')

if __name__ == '__main__':
    cli()