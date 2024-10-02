import unittest
from view_manager import ViewManager
from abstract_view import AbstractView

# Define some mock views for testing purposes
class MockScreenView(AbstractView):
    def display(self):
        pass

    def close(self):
        pass

    def get_type(self):
        return "screen"

class MockKeyboardView(AbstractView):
    def display(self):
        pass

    def close(self):
        pass

    def get_type(self):
        return "keyboard"

class TestViewManager(unittest.TestCase):
    
    def setUp(self):
        # Initialize ViewManager for each test
        self.view_manager = ViewManager()
        self.screen_view = MockScreenView()
        self.keyboard_view = MockKeyboardView()

    def test_add_view(self):
        # Add a view and check if it's active
        self.view_manager.add_view(self.screen_view)
        self.assertTrue(self.view_manager.has_view("screen"))
        self.assertEqual(len(self.view_manager.get_active_views()), 1)

    def test_remove_view(self):
        # Add then remove a view and check if it's no longer active
        self.view_manager.add_view(self.keyboard_view)
        self.assertTrue(self.view_manager.has_view("keyboard"))
        
        self.view_manager.remove_view("keyboard")
        self.assertFalse(self.view_manager.has_view("keyboard"))
        self.assertEqual(len(self.view_manager.get_active_views()), 0)

    def test_add_multiple_views(self):
        # Add both views and check if they are active
        self.view_manager.add_view(self.screen_view)
        self.view_manager.add_view(self.keyboard_view)

        self.assertTrue(self.view_manager.has_view("screen"))
        self.assertTrue(self.view_manager.has_view("keyboard"))
        self.assertEqual(len(self.view_manager.get_active_views()), 2)

    def test_remove_one_of_multiple_views(self):
        # Add both views, remove one, and check if the correct one remains active
        self.view_manager.add_view(self.screen_view)
        self.view_manager.add_view(self.keyboard_view)
        
        self.view_manager.remove_view("screen")
        self.assertFalse(self.view_manager.has_view("screen"))
        self.assertTrue(self.view_manager.has_view("keyboard"))
        self.assertEqual(len(self.view_manager.get_active_views()), 1)

    def test_remove_non_existent_view(self):
        # Removing a view that was never added should not raise an error
        self.view_manager.remove_view("non_existent_view")
        self.assertEqual(len(self.view_manager.get_active_views()), 0)

if __name__ == '__main__':
    unittest.main()
