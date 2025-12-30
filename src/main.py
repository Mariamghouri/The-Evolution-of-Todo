import sys
import os
from src.todo import TodoManager

# ANSI Color Constants
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TodoApp:
    """
    CLI Interface for the Evolution of Todo app.
    Handles user interaction and display logic with enhanced styling.
    """
    def __init__(self):
        self.manager = TodoManager()

    def _clear_console(self):
        # Clears console for a cleaner look
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        self._clear_console()
        while True:
            self._print_menu()
            choice = input(f"\n{Colors.BOLD}{Colors.CYAN}Select an option (1-6): {Colors.END}").strip()
            
            if choice == "1":
                self._handle_add()
            elif choice == "2":
                self._handle_view()
            elif choice == "3":
                self._handle_update()
            elif choice == "4":
                self._handle_delete()
            elif choice == "5":
                self._handle_toggle()
            elif choice == "6":
                print(f"\n{Colors.YELLOW}Exiting application. Goodbye!{Colors.END}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}Invalid selection. Please try again.{Colors.END}")

    def _print_menu(self):
        print(f"\n{Colors.BLUE}{Colors.BOLD}" + "="*45)
        print("      🚀 THE EVOLUTION OF TODO – PHASE 1")
        print("="*45 + f"{Colors.END}")
        print(f"{Colors.CYAN}  1.{Colors.END} {Colors.BOLD}Add New Todo{Colors.END}")
        print(f"{Colors.CYAN}  2.{Colors.END} {Colors.BOLD}View All Todos{Colors.END}")
        print(f"{Colors.CYAN}  3.{Colors.END} {Colors.BOLD}Update Todo Details{Colors.END}")
        print(f"{Colors.CYAN}  4.{Colors.END} {Colors.BOLD}Delete a Todo{Colors.END}")
        print(f"{Colors.CYAN}  5.{Colors.END} {Colors.BOLD}Mark Complete/Incomplete{Colors.END}")
        print(f"{Colors.CYAN}  6.{Colors.END} {Colors.RED}Exit{Colors.END}")
        print(f"{Colors.BLUE}" + "="*45 + f"{Colors.END}")

    def _handle_add(self):
        print(f"\n{Colors.HEADER}{Colors.BOLD}✨ CREATE NEW TASK{Colors.END}")
        title = input(f"{Colors.BLUE}🏷️  Enter Title:{Colors.END} ").strip()
        description = input(f"{Colors.BLUE}📝 Enter Description:{Colors.END} ").strip()
        
        if not title:
            print(f"{Colors.RED}❌ Error: Title cannot be empty.{Colors.END}")
            return
            
        todo = self.manager.add_todo(title, description)
        print(f"{Colors.GREEN}✅ Success: Task #{todo.id} '{todo.title}' has been successfully created.{Colors.END}")

    def _handle_view(self):
        todos = self.manager.get_all_todos()
        if not todos:
            print(f"\n{Colors.YELLOW}📭 No tasks found. Please add a new task first!{Colors.END}")
            return
        
        print(f"\n{Colors.BLUE}{Colors.BOLD}" + "═"*60)
        print(f"{'ID':<4} | {'Status':<12} | {'Task Title'}")
        print("─"*60 + f"{Colors.END}")
        
        for t in todos:
            if t.is_completed:
                status = f"{Colors.GREEN}[COMPLETED]{Colors.END}"
                title_style = f"{Colors.BLUE}"
            else:
                status = f"{Colors.YELLOW}[PENDING]{Colors.END}"
                title_style = f"{Colors.BOLD}"
            
            print(f"{t.id:<4} | {status:<12} | {title_style}{t.title}{Colors.END}")
            if t.description:
                print(f"     {Colors.CYAN}└─ Description: {t.description}{Colors.END}")
        
        print(f"{Colors.BLUE}" + "═"*60 + f"{Colors.END}")

    def _handle_update(self):
        todos = self.manager.get_all_todos()
        if not todos:
            print(f"\n{Colors.YELLOW}📭 Nothing to update. Add a task first.{Colors.END}")
            return

        print(f"\n{Colors.HEADER}{Colors.BOLD}📝 UPDATE TASK DETAILS{Colors.END}")
        self._handle_view() 
        
        try:
            choice = input(f"\n{Colors.BOLD}Enter the ID of the task to update (or press Enter to cancel): {Colors.END}").strip()
            if not choice: return
            
            todo_id = int(choice)
            todo = self.manager.get_todo_by_id(todo_id)
            if not todo:
                print(f"{Colors.RED}❌ Error: Task ID #{todo_id} not found.{Colors.END}")
                return

            print(f"{Colors.CYAN}Current Title: {todo.title}{Colors.END}")
            new_title = input(f"New Title {Colors.CYAN}(press Enter to keep current):{Colors.END} ").strip()
            
            print(f"{Colors.CYAN}Current Description: {todo.description}{Colors.END}")
            new_desc = input(f"New Description {Colors.CYAN}(press Enter to keep current):{Colors.END} ").strip()
            
            if self.manager.update_todo(todo_id, new_title or None, new_desc or None):
                print(f"{Colors.GREEN}✅ Success: Task #{todo_id} updated successfully.{Colors.END}")
            else:
                print(f"{Colors.RED}❌ Error: Failed to update task.{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid number for the ID.{Colors.END}")

    def _handle_delete(self):
        todos = self.manager.get_all_todos()
        if not todos:
            print(f"\n{Colors.YELLOW}📭 No tasks available for deletion.{Colors.END}")
            return

        print(f"\n{Colors.HEADER}{Colors.BOLD}🗑️  DELETE TASK{Colors.END}")
        self._handle_view()
        
        try:
            choice = input(f"\n{Colors.BOLD}{Colors.RED}Enter the ID to delete (or press Enter to cancel): {Colors.END}").strip()
            if not choice: return
            
            todo_id = int(choice)
            if self.manager.delete_todo(todo_id):
                print(f"{Colors.GREEN}🗑️ Success: Task #{todo_id} has been permanently deleted.{Colors.END}")
            else:
                print(f"{Colors.RED}❌ Error: Task ID #{todo_id} not found.{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}❌ Error: ID must be a valid number.{Colors.END}")

    def _handle_toggle(self):
        todos = self.manager.get_all_todos()
        if not todos:
            print(f"\n{Colors.YELLOW}📭 No tasks found to toggle status!{Colors.END}")
            return
            
        print(f"\n{Colors.HEADER}{Colors.BOLD}🔄 TOGGLE COMPLETION{Colors.END}")
        for t in todos:
            status = "✅" if t.is_completed else "⏳"
            print(f" {status} ID {t.id}: {t.title}")
            
        try:
            choice = input(f"\n{Colors.BOLD}Enter ID to toggle status (or press Enter to cancel): {Colors.END}").strip()
            if not choice:
                return
                
            todo_id = int(choice)
            if self.manager.toggle_status(todo_id):
                todo = self.manager.get_todo_by_id(todo_id)
                new_status = f"{Colors.GREEN}[COMPLETED]{Colors.END}" if todo.is_completed else f"{Colors.YELLOW}[PENDING]{Colors.END}"
                print(f"{Colors.GREEN}✨ Success: Task '{todo.title}' is now {new_status}.{Colors.END}")
            else:
                print(f"{Colors.RED}❌ Error: Task ID #{todo_id} not found.{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid numeric ID.{Colors.END}")

def main():
    app = TodoApp()
    app.run()

if __name__ == "__main__":
    main()
