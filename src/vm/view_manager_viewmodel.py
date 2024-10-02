from PropertyChangedNotifier import PropertyChangedNotifier
from model.view_manager import ViewManager
from model.abstract_view import AbstractView

class ViewManagerViewModel(PropertyChangedNotifier):
    def __init__(self):
        super().__init__()
        self._view_manager = ViewManager()

    def add_view(self, view_instance: AbstractView):
        self._view_manager.add_view(view_instance)
        self.notify_property_changed("active_views")

    def remove_view(self, view_type):
        self._view_manager.remove_view(view_type)
        self.notify_property_changed("active_views")

    def get_active_views(self):
        return self._view_manager.get_active_views()

    def has_view(self, view_type):
        return self._view_manager.has_view(view_type)


if __name__ == "__main__":

    class MockView(AbstractView):
        def __init__(self, view_type):
            super().__init__()
            self._type = view_type
            
        def get_type(self):
            return self._type

        def display(self):
            print(f"{self._type} view is now being displayed.")

        def close(self):
            print(f"{self._type} view has been closed.")

    view_manager_vm = ViewManagerViewModel()

    # Create and add mock views
    screen_view = MockView("screen")
    keyboard_view = MockView("keyboard")

    view_manager_vm.add_view(screen_view)
    view_manager_vm.add_view(keyboard_view)

    # Output active views
    print("Active Views:")
    for view in view_manager_vm.get_active_views():
        print(view.get_type())

    # Remove a view
    view_manager_vm.remove_view("keyboard")
    print("\nAfter removing Keyboard View:")
    for view in view_manager_vm.get_active_views():
        print(view.get_type())

