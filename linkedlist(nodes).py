class node:
    def __init__(self, value):
        self.value = value
        self.pointer = None
    def insert(self, item):
        if self.pointer == None:
            self.pointer = node(item)
        else:
            self.pointer.insert(item)
    def delete(self):
        if self.pointer == None:
            self.value = 0
        else:
            self.pointer.delete()
    def search(self, item):
        found = False
        if self.value == item:
            found = True
            print("value found")    
        elif found != False and self.pointer == None:
            found = False
        else:
            self.pointer.search(item)
    def show_detail(self):
        i = ""
        if self.pointer != None:
            print( self.value)
            self.pointer.show_detail()
        else:
            print(self.value)

list = node(20)
list.insert(50)
list.insert(30)
list.show_detail()
list.search(30)