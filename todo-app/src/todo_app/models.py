class TodoItem:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f'TodoItem(title={self.title}, description={self.description}, completed={self.completed})'

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False