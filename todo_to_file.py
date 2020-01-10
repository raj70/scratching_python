import os

from todo import Todo
from todos import Todos


class Todo_To_File():

    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, todo):
        try:
            todos = self.read()
            newId = self.__generateId(todo)
            todo.id = newId

            with open(self.file_name, 'a') as file_obj:
                if todos.is_exist(todo) == False:
                    file_obj.write(todo.to_String() + "\n")

                file_obj.close()

        except FileNotFoundError as error:
            print(error)

    # not sure about this
    def write_todos(self, todos: []):
        os.remove(self.file_name)
        file_obj = open(self.file_name, 'a')
        for t in todos:
            file_obj.write(t.to_String() + "\n")

    def read(self):
        todos = Todos()
        try:
            flines = open(self.file_name, 'r')

            for line in flines:
                d = line.split(Todo.seperator())
                isCompleted = Todo.isCompletedBool(d[3])
                t = Todo(d[0], d[1], d[2], isCompleted)
                todos.append(t)

            flines.close()
        except FileNotFoundError as error:
            print(error)

        return todos

    def __generateId(self, todo):
        todos = self.read()
        list = todos.getList()

        if len(list) == 0:
            return 1

        lastTodo = list[-1]
        return int(lastTodo.id) + 1
