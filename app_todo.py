import app_constant as constant

from todo_service import Todo_Service
from todo_add import Todo_Add
from todo_app_update import Todo_App_Update
from todo_list import Todo_List


class App_Todo:

    def __init__(self):
        self.todo_service = Todo_Service()

    def app_menu(self):
        print('---------------App: TodoList-----------------------------')
        print("1) To Add New Todo: " + constant.to_add)
        print("2) To Delete: " + constant.to_delete)
        print("3) To Update: " + constant.to_update)
        print("4) To Show List: " + constant.to_list)
        print("5) To Exist: " + constant.to_exit)
        print('--------------------------------------------------------')

    def app_process(self):
        input_text = ''
        while input_text != constant.to_exit:
            input_text = input(":")
            if input_text.upper() == 'A':
                self.app_new_todo()
            elif input_text.upper() == 'D':
                print("Not implemented")
            elif input_text.upper() == 'U':
                self.app_update_todo()
            elif input_text.upper() == 'L':
                self.app_list_todo()

            self.app_menu()

    def app_new_todo(self):
        appNew = Todo_Add(self.todo_service)
        appNew.process()

    def app_update_todo(self):
        appUpdate = Todo_App_Update(self.todo_service)
        appUpdate.process()

    def app_list_todo(self):
        list = Todo_List(self.todo_service)
        list.process()
