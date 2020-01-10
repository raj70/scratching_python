import app_constant as constant

from todo_service import Todo_Service
import todo


class Todo_List:

    def __init__(self, todo_service: Todo_Service):
        self.todo_service = todo_service

    def menu(self):
        print("\n")
        print('---------------App: List of Todos--------------------------')
        print("To get another list type: " + constant.to_next_list)
        print("To get previous list type: " + constant.to_previous_list)
        print("To Go Back To Main Menu: " + constant.to_exit)

        self.todo_service.get_todo_list()

    def process(self):
        self.menu()

        input_text = ""
        while input_text != constant.to_exit:
            input_text = input("What would you like to do? ")
            if input_text == constant.to_next_list:
                self.todo_service.balance_history(self.todo_service.last_id)
            elif input_text == constant.to_previous_list:
                self.todo_service.last_last_id()
            elif input_text == constant.to_exit:
                pass
            else:
                print("Not a valid entry")

            if input_text != constant.to_exit:
                self.menu()
