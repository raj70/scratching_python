class Todo:

    def __init__(self, id:int, title, description, is_completed:bool):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed

    def isCompleted(self):
        return self.is_completed

    def __completedToString(self):
        if self.is_completed:
            return "Completed"
        else:
            return "Pending"
    
    def to_String(self):        
        return str(self.id) + Todo.seperator() + self.title + Todo.seperator() + self.description + Todo.seperator() + self.__completedToString()
    
    def is_Equal(self, todo):
        equal = False

        if self.title == todo.title and self.description == todo.description:
            equal = True

        return equal    
        

    @staticmethod
    def isCompletedBool(chars):
        if chars.upper().replace("\n", "") == "Completed".upper():
            return True
        else:
            return False

    @staticmethod
    def seperator():
        return ":"
    
