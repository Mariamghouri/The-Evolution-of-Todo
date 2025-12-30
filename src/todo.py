from typing import List, Optional
from src.models import Todo

class TodoManager:
    """
    In-memory manager for Todo operations.
    Handles storage, unique ID generation, and CRUD logic.
    """
    def __init__(self):
        self._todos: List[Todo] = []
        self._current_id: int = 1

    def add_todo(self, title: str, description: str) -> Todo:
        new_todo = Todo(
            id=self._current_id,
            title=title,
            description=description
        )
        self._todos.append(new_todo)
        self._current_id += 1
        return new_todo

    def get_all_todos(self) -> List[Todo]:
        return self._todos

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        return next((t for t in self._todos if t.id == todo_id), None)

    def update_todo(self, todo_id: int, title: str = None, description: str = None) -> bool:
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return False
        
        if title:
            todo.title = title
        if description:
            todo.description = description
        return True

    def delete_todo(self, todo_id: int) -> bool:
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return False
        self._todos.remove(todo)
        return True

    def toggle_status(self, todo_id: int) -> bool:
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return False
        todo.is_completed = not todo.is_completed
        return True
