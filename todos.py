from todo import Todo


class Todos():

    def __init__(self):
        self.todos = []

    def find_by_id(self, id):
        for t in self.todos:
            if int(t.id) == id:
                return t

        return Todo(-1, '', '', False)

    def append(self, todo):
        self.todos.append(todo)

    def is_exist(self, todo):
        exist = False

        for t in self.todos:
            if todo.is_Equal(t):
                exist = True

        return exist

    def getList(self):
        return self.todos

    def print(self):
        for t in self.todos:
            print(t.to_String())

    def get_todo(self, id):
        for todo in self.todos:
            if todo.id == id:
                return todo

        raise NameError

    def make_list(self, last_todo_Id: int, howmany: int):
        todo_list = Todo_List([], 0, len(self.todos))

        for t in todo_list.selected_id:
            print("Making list: " + str(t))

        if len(self.todos) == 0:
            print("LIST IS EMPTY")
            return

        first_todo = Todo(0, '', '', False)

        if last_todo_Id == 0:
            first_todo = self.todos[0]
        else:
            first_todo = self.find_by_id(int(last_todo_Id))
            if first_todo.id == -1:
                raise NotImplementedError("The Todo item not found")

        index = self.todos.index(first_todo)

        for _ in range(howmany):
            try:
                todo = self.todos[index]
                todo_list.last_id = int(todo.id)
                todo_list.todos.append(todo)
                todo_list.selected_id.append(todo.id)
                index = index + 1
            except:
                print("Warning: does not exist")
                break

        return todo_list


class Todo_List():
    def __init__(self, todos: [], last_id: int, count: int):
        self.todos = todos
        self.last_id = last_id
        self.total_todos = count
        # do i need this
        self.selected_id = []
