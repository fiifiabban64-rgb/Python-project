# Simple To-Do Application

This is a simple to-do application built in Python. It allows users to manage their tasks through a command-line interface.

## Features

- Add tasks
- Remove tasks
- List all tasks
- Mark tasks as completed

## Project Structure

```
simple-todo-app
├── src
│   ├── simple_todo
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── cli.py
│   │   ├── models.py
│   │   ├── storage.py
│   │   └── utils.py
├── tests
│   └── test_todo.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd simple-todo-app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python -m simple_todo.main
```

You can use the command-line interface to manage your tasks. For help with commands, use:
```
python -m simple_todo.cli --help
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.