FILEPATH = "/Users/jerry/Desktop/megacourse/todopy/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
         todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list inm the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
         
print("Hell from functions")