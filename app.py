
warn_ui = """
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        {}
        <button 
            type="button" 
            class="btn-close" data-bs-dismiss="alert" 
            aria-label="Close">
        </button>
    </div>"""


class Todo():
    def __init__(self):
        self.todos = []

    def add_todo(self, item):
        if len(item.strip()) == 0:
            alertBox.write(warn_ui.format("Please Enter Something Before Add"))
            return 

        self.todos.append(item)
    
    def remove_todo(self, item_idx):
        if (len(item_idx.strip())==0 or int(item_idx)-1 < len(self.todos)):
            alertBox.write(warn_ui.format("Item is not found"))
        item_idx = int(item_idx)
        tmp = []
        item = self.todos.pop(item_idx-1)
        console.log(f'{item} has been deleted')
        return item
    
    def render(self):
        #This will return a ui string
        items = ''
        template_item = '<li class="list-group-item d-flex justify-content-between"><span>{}</span> <button pys-onClick="removeItem" class="rm-btn"  > | Erase</button> </li>'

        for i in self.todos:
            items += (template_item.format(i))
        return items
        

todoHandler = Todo()
alertBox = Element('alert')
outputbox = Element('output')
inputBox = Element('todoTextInput')
deleteBox =  Element('deleteIdxInput')

def getTodo(*args, **kwargs):
    data =  inputBox.value
    todoHandler.add_todo(data)
    items = todoHandler.render()
    outputbox.write(items)

def removeItem(*args, **kwargs):
    items = todoHandler.render()
    if len(items.strip()) == 0:
        alertBox.write(warn_ui.format("Nothing Found To Delete"))
        return
    deleteIdx =deleteBox.value
    getDeletedItem = todoHandler.remove_todo(deleteIdx)
    items = todoHandler.render()
    alertBox.write(warn_ui.format(f'Items <strong>{getDeletedItem}</strong> Has Been Deleted'))
    outputbox.write(items)





