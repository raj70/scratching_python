import app_constant as constant

from todo_service import Todo_Service
from todo_update import Todo_Update
import todo


class Todo_App_Update:

    def __init__(self, todo_service: Todo_Service):
        self.todo_service = todo_service

    def menu(self):
        print("\n")
        print('---------------App: Update Todo--------------------------')
        print("To Update type: " + constant.to_update + " and follow the prompt")
        print("To get another list type: " + constant.to_next_list)
        print("To get previous list type: " + constant.to_previous_list)
        print("To Go Back To Main Menu: " + constant.to_exit)
        # print("\n")

        self.todo_service.get_todo_list()

    def process(self):
        self.menu()

        input_text = ""
        while input_text != constant.to_exit:
            input_text = input("What would you like to do? ")
            if input_text == constant.to_update:
                self.update_process()
            elif input_text == constant.to_next_list:
                self.todo_service.balance_history(self.todo_service.last_id)
            elif input_text == constant.to_previous_list:
                self.todo_service.last_last_id()
            elif input_text == constant.to_exit:
                pass
            else:
                print("Not a valid entry")

            if input_text != constant.to_exit:
                self.menu()

    def update_process(self):
        print('---------------App: Updating Todo--------------------------')
        input_text = "start"
        while input_text != 'e':
            print(
                "Please enter a number from above list, next to a todo.\nTo Go Back To Menu: ")
            input_text = input(": ")

            if input_text == 'e':
                break

            try:
                selected_id = int(input_text)
                if type(selected_id) is int:
                    if str(selected_id) in self.todo_service.selected_id:
                        todo = self.todo_service.get_todo(selected_id)
                        update = Todo_Update(todo, self.todo_service)
                        update.set_todo(todo)
                        update.process()
                    else:
                        print('please select a number from above list\n')
            except Exception as e:
                print("Error: " + str(e))
