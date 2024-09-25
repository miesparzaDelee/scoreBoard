class PropertyChangedNotifier:
    def __init__(self):
        self._property_changed_callbacks = {}  # Property-specific callbacks
        self._general_property_changed_callbacks = []  # General listeners

    def add_property_changed_listener(self, property_name, callback):
        """
        Add a listener for a specific property change.
        
        :param property_name: The name of the property to listen for.
        :param callback: The function to call when the property changes.
        """
        if property_name not in self._property_changed_callbacks:
            self._property_changed_callbacks[property_name] = []
        self._property_changed_callbacks[property_name].append(callback)

    def subscribe_property_changed(self, callback):
        """
        Subscribe a listener that will be notified when any property changes.

        :param callback: The function to call when any property changes.
        """
        self._general_property_changed_callbacks.append(callback)

    def notify_property_changed(self, property_name):
        """
        Notify all listeners that a specific property has changed.
        
        :param property_name: The name of the property that changed.
        """
        # Notify specific property listeners
        if property_name in self._property_changed_callbacks:
            for callback in self._property_changed_callbacks[property_name]:
                callback()  # Call the subscribed callback

        # Notify general listeners
        for callback in self._general_property_changed_callbacks:
            callback(property_name)


if __name__ == "__main__":
    # Define a simple ViewModel class to simulate a changing property
    from PropertyChangedNotifier import PropertyChangedNotifier
    from Command import Command

    class CounterViewModel(PropertyChangedNotifier):
        def __init__(self):
            super().__init__()
            self._counter = 0
            self.increment_command = Command(self.increment_counter, self.can_increment)

        @property
        def counter(self):
            return self._counter

        def increment_counter(self):
            self._counter += 1
            self.notify_property_changed("counter")

        def can_increment(self):
            # You can add logic here to enable/disable the command (e.g., based on maximum counter value)
            return True

    # Create an instance of the view model
    counter_vm = CounterViewModel()

    # Define a simple listener that updates when the counter changes
    def on_counter_changed():
        print(f"Counter changed: {counter_vm.counter}")

    # Add the listener to listen for changes to the "counter" property
    counter_vm.add_property_changed_listener("counter", on_counter_changed)

    # Simulate updating the counter
    for _ in range(5):
        counter_vm.increment_counter()
