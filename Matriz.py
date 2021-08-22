from nodoM import NodoM, NodoEncabezado
from encabezados import ListaEncabezado

class Matriz:

    def __init__(self):
        self.eRows = ListaEncabezado()
        self.eColumns = ListaEncabezado()
    
    def insertar(self, fila, columna, valor):
        nuevo = NodoM(fila,columna,valor)

        eRows = self.eRows.getEncabezado(fila)

        if eRows == None:
            eRows = NodoEncabezado(fila)
            eRows.acceso = nuevo
            self.eRows.setEncabezado(eRows)
        else:
            if nuevo.columna < eRows.acceso.columna:
                nuevo.derecha = eRows.acceso
                eRows.acceso.izquierda = nuevo
                eRows.acceso = nuevo
            else:
                actual = eRows.acceso
                while actual.derecha !=None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        eColumna = self.eColumns.getEncabezado(columna)
        if eColumna == None:
            eColumna = NodoEncabezado(columna)
            eColumna.acceso = nuevo
            self.eColumns.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.acceso.fila:
                nuevo.abajo = eColumna.acceso
                eColumna.acceso.arriba = nuevo
                eColumna.acceso = nuevo
            else:
                actual = eColumna.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
            if actual.abajo == None:
                actual.abajo = nuevo
                nuevo.arriba = actual

    
    def imprimir(self):
        eFila=self.eRows.primero
        fila = ''
        while eFila != None:

            actual = eFila.acceso
            while actual != None:
                fila+='['+str(actual.valor)+']'
                actual = actual.derecha

            print(fila)
            fila=''
            eFila = eFila.siguiente
        
        
