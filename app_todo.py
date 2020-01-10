import app_constant as constant

from todo_service import Todo_Service
from todo_add import Todo_Add
from todo_app_update import Todo_App_Update
from todo_list import Todo_List
from todo_delete import Todo_Delete


class App_Todo:

    def __init__(self):
        # self.todo_service = Todo_Service() # we need to reset on each task

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
                self.app_delete_todo()
            elif input_text.upper() == 'U':
                self.app_update_todo()
            elif input_text.upper() == 'L':
                self.app_list_todo()

            self.app_menu()

    def app_new_todo(self):
        appNew = Todo_Add(Todo_Service())
        appNew.process()

    def app_update_todo(self):
        appUpdate = Todo_App_Update(Todo_Service())
        appUpdate.process()

    def app_list_todo(self):
        list = Todo_List(Todo_Service())
        list.process()

    def app_delete_todo(self):
        appDelete = Todo_Delete(Todo_Service())
        appDelete.process()
