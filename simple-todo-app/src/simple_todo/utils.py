def validate_input(input_str):
    if not input_str or input_str.isspace():
        raise ValueError("Input cannot be empty or whitespace.")
    return input_str.strip()

def format_todo_item(todo_item):
    return f"[{'X' if todo_item.completed else ' '}] {todo_item.title}"