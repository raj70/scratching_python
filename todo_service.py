import app_constant as constant
from todo import Todo

from todo_to_file import Todo_To_File


class Todo_Service:
    def __init__(self):
        self.last_id = 0
        self.number_of_todo = constant.number_of_todo_list
        self.total_of_todos = 0
        self.history = [self.last_id]
        self.selected_id = []
        self.selected_todos = []

    def get_todo_list(self):
        tofile = Todo_To_File(constant.file_name)
        ts = tofile.read()

        if len(ts.todos) == 0:
            return

        todo_list = ts.make_list(self.last_id, self.number_of_todo)
        self.total_of_todos = todo_list.total_todos
        self.selected_id = todo_list.selected_id
        self.selected_todos = todo_list.todos
        # next id
        self.last_id = todo_list.last_id

        print('---------------App: Selected Todos-----------------------')
        for t in todo_list.todos:
            print(t.to_String())  # TODO: fixed this

    def balance_history(self, id):
        if not id in self.history:
            self.history.append(id)

    def last_last_id(self):
        self.last_id = self.history[-1]

        if self.last_id in self.history and len(self.history) > 1:
            self.history.remove(self.last_id)

        # actually this is last id we need
        self.last_id = self.history[-1]

    def get_todo(self, id) -> Todo:
        for todo in self.selected_todos:
            if int(todo.id) == int(id):
                return todo

        raise NameError("Todo not found for given id: " + str(id))

    def update_todo(self, todo: Todo):
        tofile = Todo_To_File(constant.file_name)
        ts = tofile.read()

        newTodos = []
        for t in ts.todos:
            if int(t.id) == int(todo.id):
                t.title = todo.title
                t.description = todo.description
                t.is_completed = todo.is_completed

            newTodos.append(t)

        tofile.write_todos(newTodos)

    def delete_todo(self, id: int):
        tofile = Todo_To_File(constant.file_name)
        ts = tofile.read()

        newTodos = []

        for t in ts.todos:
            if int(id) != int(t.id):
                newTodos.append(t)
            elif int(id) == int(t.id):
                print("Delete: Found")
            else:
                print("Delete: Not Found")

        if len(newTodos) > 0:

            tofile.write_todos(newTodos)
        else:
            print("Deleted: empty")

    def add_todo(self, todo: Todo):
        tofile = Todo_To_File(constant.file_name)
        tofile.write_line(todo)

    def reset(self, id):
        self.last_id = id
