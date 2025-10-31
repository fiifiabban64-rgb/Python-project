class TodoItem:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __repr__(self):
        return f'TodoItem(id={self.id}, title="{self.title}", completed={self.completed})'