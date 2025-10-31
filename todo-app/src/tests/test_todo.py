import unittest
from todo_app.models import TodoItem
from todo_app.storage import Storage

class TestTodoItem(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()
        self.item = TodoItem(title="Test Task", description="This is a test task.")

    def test_todo_item_creation(self):
        self.assertEqual(self.item.title, "Test Task")
        self.assertEqual(self.item.description, "This is a test task.")
        self.assertFalse(self.item.completed)

    def test_storage_add_item(self):
        self.storage.add_item(self.item)
        self.assertIn(self.item, self.storage.get_all_items())

    def test_storage_remove_item(self):
        self.storage.add_item(self.item)
        self.storage.remove_item(self.item.id)
        self.assertNotIn(self.item, self.storage.get_all_items())

    def test_storage_get_all_items(self):
        self.storage.add_item(self.item)
        items = self.storage.get_all_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], self.item)

if __name__ == '__main__':
    unittest.main()