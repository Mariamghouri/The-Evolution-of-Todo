from dataclasses import dataclass

@dataclass
class Todo:
    """
    Core data model for a Todo item.
    Attributes:
        id (int): Unique identifier.
        title (str): Title of the task.
        description (str): Detailed description.
        is_completed (bool): Status of the task (default: False).
    """
    id: int
    title: str
    description: str
    is_completed: bool = False
