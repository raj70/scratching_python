import app_constant as constant

from todo_abstract import Todo_Abstract
from todo_service import Todo_Service
from todo import Todo


class Todo_Delete(Todo_Abstract):
    def __init__(self, todo_service: Todo_Service):
        super().__init__(Todo(0, '', '', False), todo_service)
        self.todo_service = todo_service
        self.todo_service.history = [0]
        self.whatyoudoing = "Deleting"
        self.to_exist = constant.to_exit

    def menu(self):
        print("\n")
        header = '---------------App: {} Todo-----------------------------'
        print(header.format(self.whatyoudoing))
        print("To get another list type: " + constant.to_next_list)
        print("To get previous list type: " + constant.to_previous_list)
        print("To Go Back: " + constant.to_exit)

        self.todo_service.get_todo_list()

    def process(self):
        self.menu()

        for i in self.todo_service.history:
            print(str(i))

        input_text = ''
        while self.to_exist != input_text:
            input_text = input(
                "Please enter a number from above list, next to a todo, to delete: ")

            if input_text == constant.to_next_list:
                self.todo_service.balance_history(self.todo_service.last_id)
            elif input_text == constant.to_previous_list:
                self.todo_service.last_last_id()
            elif input_text == self.to_exist:
                self.todo_service.last_id = self.todo_service.selected_id[0]
                return

            try:
                selected_id = int(input_text)
                if isinstance(selected_id, int):
                    if selected_id in self.todo_service.selected_id:  # weird or what
                        self.todo_service.delete_todo(int(selected_id))
                        self.todo_service.last_id = self.todo_service.selected_id[0]
                        print("Deleted")
                    else:
                        self.todo_service.last_id = self.todo_service.selected_id[0]
                        print('please select a number from above list\n')
            except Exception as error:
                print(error)

            self.menu()
