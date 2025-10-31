class Storage:
    def __init__(self, storage_file='todos.json'):
        self.storage_file = storage_file
        self.todos = self.load_todos()

    def load_todos(self):
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_todos(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.todos, file)

    def add_todo(self, todo):
        self.todos.append(todo)
        self.save_todos()

    def remove_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        self.save_todos()

    def get_all_todos(self):
        return self.todos

    def find_todo(self, todo_id):
        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None