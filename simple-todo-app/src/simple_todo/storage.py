def load_todos(file_path):
    try:
        with open(file_path, 'r') as file:
            todos = [line.strip() for line in file.readlines()]
        return todos
    except FileNotFoundError:
        return []

def save_todos(todos, file_path):
    with open(file_path, 'w') as file:
        for todo in todos:
            file.write(f"{todo}\n")