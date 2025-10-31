# To-Do Application

This is a simple To-Do application built in Python. It allows users to manage their tasks efficiently through a command-line interface.

## Features

- Add, update, and delete tasks
- View all tasks
- Mark tasks as complete
- Persistent storage of tasks

## Project Structure

```
todo-app
├── src
│   ├── todo_app
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── cli.py
│   │   ├── models.py
│   │   ├── storage.py
│   │   ├── services.py
│   │   └── api.py
│   └── tests
│       ├── __init__.py
│       └── test_todo.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd todo-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:
```
python -m todo_app
```

## Running Tests

To run the tests, navigate to the `src/tests` directory and execute:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.