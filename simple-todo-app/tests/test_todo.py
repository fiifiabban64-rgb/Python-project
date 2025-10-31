import unittest
from simple_todo.models import TodoItem
from simple_todo.storage import save_todo_items, load_todo_items

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.todo_item = TodoItem(id=1, title="Test Task", completed=False)

    def test_todo_item_creation(self):
        self.assertEqual(self.todo_item.id, 1)
        self.assertEqual(self.todo_item.title, "Test Task")
        self.assertFalse(self.todo_item.completed)

    def test_todo_item_completion(self):
        self.todo_item.completed = True
        self.assertTrue(self.todo_item.completed)

    def test_save_and_load_todo_items(self):
        todo_list = [self.todo_item]
        save_todo_items(todo_list, 'test_todos.json')
        loaded_todos = load_todo_items('test_todos.json')
        self.assertEqual(len(loaded_todos), 1)
        self.assertEqual(loaded_todos[0].title, "Test Task")

if __name__ == '__main__':
    unittest.main()