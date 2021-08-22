class NodoM:
    def __init__(self,fila,columna,valor):
        self.fila=fila
        self.columna=columna
        self.valor = valor
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None

class NodoEncabezado:
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None
