from typing import Dict, List
from abstract_view import AbstractView

class ViewManager:
    def __init__(self):
        self._active_views: Dict[str, AbstractView] = {}

    def add_view(self, view_instance: AbstractView) -> None:
        """
        Add a view to the active view dictionary and display it.
        
        :param view_instance: The instance of the view to add.
        """
        view_type = view_instance.get_type()
        self._active_views[view_type] = view_instance
        view_instance.display()

    def remove_view(self, view_type: str) -> None:
        """
        Remove a view from the active view dictionary and close it.
        
        :param view_type: The unique string identifier for the view to remove.
        """
        if view_type in self._active_views:
            self._active_views[view_type].close()
            del self._active_views[view_type]

    def get_active_views(self) -> List[AbstractView]:
        """
        Return the list of currently active views.
        
        :return: List of active view instances.
        """
        return list(self._active_views.values())

    def has_view(self, view_type: str) -> bool:
        """
        Check if a specific view is active.
        
        :param view_type: The unique string identifier for the view.
        :return: Boolean indicating whether the view is active.
        """
        return view_type in self._active_views
