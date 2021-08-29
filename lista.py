from nodo import nodo

class dlinkedlist:
 
    def __init__(self):
        self.first=None
        self.last=None
        self.size=0

    def empty(self):
        return self.first == None
    
    def append(self,dato):
        if self.empty():
            self.first = self.last = nodo(dato)
        else: 
            aux = self.last
            self.last = aux.next = nodo(dato)
            self.last.preview = aux
        self.size+=1
