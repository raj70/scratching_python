import app_constant as constant
from todo import Todo
from todo_abstract import Todo_Abstract
from todo_service import Todo_Service


class Todo_Add(Todo_Abstract):
    def __init__(self, todo_service: Todo_Service):
        super().__init__(Todo(0, '', '', False), todo_service)
        self.whatyoudoing = 'Adding'

    def menu(self):
        super().menu()
        print("To Continue adding New Todo hit Enter")

    def save(self, title, description):
        todo = Todo(0, title, description, False)

        if title != '' or description != '':
            saveOr = input(
                "\nPress \'s\' To Save \nHit Enter to skip the save: ")

            if saveOr.upper() == 'S':
                service = Todo_Service()
                service.add_todo(todo)
        else:
            print("Cannot save empty todo")

        self.menu()
        self.to_exist = input("What would you like to do?: ")
