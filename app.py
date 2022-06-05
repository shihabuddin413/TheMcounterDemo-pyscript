class Todo():
    def __init__(self):
        self.todos = []

    def add_todo(self, item):
        if (item in self.todos):
            return "This item exist"
        self.todos.add(item)
    
    def remove_todo(self, item):
        tmp = []
        for i in self.todos:
            if (i != item):
                tmp.append(i)
        self.todos = tmp


mTodoHandler = Todo()

