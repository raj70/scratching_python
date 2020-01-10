import app_constant as constant
from todo import Todo
from todo_service import Todo_Service


class Todo_Abstract:
    def __init__(self, todo: Todo, todo_service: Todo_Service):
        self.todo = todo
        self.whatyoudoing: ''

    def menu(self):
        print("\n")
        header = '---------------App: {} Todo-----------------------------'
        print(header.format(self.whatyoudoing))
        print("Type text for prompt")
        print("To Save: " + constant.to_save)
        print("To Go Back: " + constant.to_exit)

    def process(self):
        self.menu()
        self.to_exist = 'start'

        while self.to_exist != 'e':
            title = input("Enter title for Todo: " + self.todo.title + ": ")
            description = input(
                "Enter description for Todo: " + self.todo.description + ": ")

            self.save(title, description)

    def save(self, title, description):
        pass
