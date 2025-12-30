# Phase 1 Task Breakdown

## Task 1: Data Model Definition
- Create `src/models.py`.
- Define `Todo` dataclass with standard attributes.

## Task 2: Logic Layer Implementation
- Create `src/todo.py`.
- Implement `TodoManager` class.
- Add `add_todo` method with auto-ID logic.
- Add retrieval methods (`get_all`, `find_by_id`).
- Add mutation methods (`update`, `delete`, `toggle`).

## Task 3: CLI Interface Implementation
- Create `src/main.py`.
- Implement main loop and menu display.
- Map menu options to `TodoManager` methods.
- Implement specialized input handlers for Add/Update/Delete.

## Task 4: Final Assembly and Local Testing
- Ensure imports are correct between files.
- Verify basic CRUD flow.
- Verify that data is lost on restart (confirming in-memory constraint).
