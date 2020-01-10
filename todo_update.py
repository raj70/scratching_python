import app_constant as constant

from todo_abstract import Todo_Abstract
from todo_service import Todo_Service
from todo import Todo


class Todo_Update(Todo_Abstract):
    def __init__(self, todo: Todo, todo_service: Todo_Service):
        super().__init__(todo, todo_service)
        self.todo_service = todo_service
        self.todo: todo  # why object has not attribue, error
        self.whatyoudoing = "Updating"

    def menu(self):
        super().menu()

    def set_todo(self, todo: Todo):
        self.todo = todo

    def save(self, title, description):
        # if hasattr(self, "todo"):
        #     print("YES")
        # else:
        #     print("NO")

        # if hasattr(self, "todo_service"):
        #     print("YES")
        # else:
        #     print("NO")

        is_completed = input("Is todo completed (0: false; 1: true): ")
        if is_completed != '':
            if is_completed == str(0):
                self.todo.is_completed = False
            elif is_completed == str(1):
                self.todo.is_completed = True
            else:
                pass

        if title != '':
            self.todo.title = title

        if description != '':
            self.todo.description = description

        if self.todo.title == title and self.todo.description == description:
            return
        else:
            pass

        saveOr = input("\nPress \'s\' To Save \nHit Enter to skip the save: ")

        if saveOr.upper() == 'S':
            self.todo_service.update_todo(self.todo)
        else:
            print("Cannot save empty todo")

        self.to_exist = 'e'
