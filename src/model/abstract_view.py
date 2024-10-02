# abstract_view.py in the model folder

from abc import ABC, abstractmethod

class AbstractView(ABC):
    @abstractmethod
    def display(self):
        """
        Display the view to the user. 
        Each view should define its own way to display itself.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close or deactivate the view.
        Each view should define its own way to close itself.
        """
        pass

    @abstractmethod
    def get_type(self):
        """
        Return the type of the view (e.g., 'screen', 'keyboard').
        This is used by the ViewManager to manage views.
        """
        pass
