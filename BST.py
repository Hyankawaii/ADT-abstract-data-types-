class node:
    def __init__(self, value):
        self.nodeval = value
        self.Rpointer = -1
        self.Lpointer = -1
Tree = [node(None) for i in range(10)]

root = -1
current_pointer = root
def search(item):
    current_pointer = root
    while root != -1 and Tree[current_pointer].nodeval != item:
       if item > Tree[current_pointer].nodeval:
            current_pointer <-- Tree[current_pointer].Rpointer
       else:
            current_pointer <-- Tree[current_pointer].Lpointer
    return current_pointer
def insert(item):
    global root
    root = 0
    