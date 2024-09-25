class Command:
    def __init__(self, execute_function, can_execute_function=None):
        """
        Initialize a command with an execute function and an optional can_execute function.
        
        :param execute_function: The function to be executed when the command is triggered.
        :param can_execute_function: An optional function to determine if the command can execute.
        """
        self.execute_function = execute_function
        self.can_execute_function = can_execute_function

    def execute(self):
        """
        Execute the command's function if it can be executed.
        """
        if self.can_execute():
            self.execute_function()

    def can_execute(self):
        """
        Check if the command can be executed. If no can_execute_function is provided, assume it's always executable.
        """
        if self.can_execute_function:
            return self.can_execute_function()
        return True
