# Phase 1 Implementation Plan

## File Responsibilities
- **src/models.py**: Contains the `Todo` data structure (dataclass) to ensure clear data typing.
- **src/todo.py**: Contains the `TodoManager` class responsible for in-memory storage (a list of objects) and CRUD logic.
- **src/main.py**: Contains the `TodoApp` class for CLI interaction, inputs, and output formatting.

## Data Structures
- **Todo Object**: Attributes: `id` (int), `title` (str), `description` (str), `is_completed` (bool).
- **Storage**: A Python `list` inside the manager class.
- **ID Counter**: A simple integer starting at 1, incremented on each addition.

## Control Flow
1. Initializing the `TodoManager` and `TodoApp`.
2. Entering the `TodoApp` main loop.
3. Displaying the menu.
4. Capturing user selection.
5. Delegating logic to `TodoManager`.
6. Displaying results or errors.
7. Continuing or exiting.

## CLI Interaction Logic
- Use `input()` for capturing user commands and task details.
- Use `print()` for menus and formatted task tables.
- Handle `ValueError` for invalid ID inputs to prevent crashes.
