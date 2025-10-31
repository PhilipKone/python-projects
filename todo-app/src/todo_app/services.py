from typing import List, Optional

class TodoItem:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

class TodoService:
    def __init__(self):
        self.todos: List[TodoItem] = []
        self.next_id: int = 1

    def add_todo(self, title: str) -> TodoItem:
        todo = TodoItem(id=self.next_id, title=title)
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def update_todo(self, id: int, title: Optional[str] = None, completed: Optional[bool] = None) -> Optional[TodoItem]:
        todo = self.get_todo(id)
        if todo:
            if title is not None:
                todo.title = title
            if completed is not None:
                todo.completed = completed
            return todo
        return None

    def delete_todo(self, id: int) -> bool:
        todo = self.get_todo(id)
        if todo:
            self.todos.remove(todo)
            return True
        return False

    def get_todo(self, id: int) -> Optional[TodoItem]:
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None

    def get_all_todos(self) -> List[TodoItem]:
        return self.todos.copy()