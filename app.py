class Todo():
    def __init__(self):
        self.todos = []
        self.warn_ui = """<div class="alert alert-warning alert-dismissible fade show" role="alert">
            Please Enter Something Before Add
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>"""

    def add_todo(self, item):
        if len(item.strip()) == 0:
            alertBox = Element('alert')
            alertBox.write(self.warn_ui)
            return 

        self.todos.append(item)
    
    def remove_todo(self, item):
        tmp = []
        for i in self.todos:
            if (i != item):
                tmp.append(i)
        self.todos = tmp
    
    def render(self):
        items = ''
        for i in self.todos:
            items += (f'<li pys  class="list-group-item">{i}</li>')
        return items
        

todoHandler = Todo()

def getTodo(*args, **kwargs):
    outputbox = Element('output')
    inputBox = Element('todoTextInput')
    data =  inputBox.value
    todoHandler.add_todo(data)
    items = todoHandler.render()
    outputbox.write(items)

