from os import startfile, system
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

    def actualizar(self,fila,columna,valor):
        aux = self.eRows.primero
        while aux != None:
            actual = aux.acceso
            while actual != None:
                if actual.fila == fila and actual.columna == columna:
                    actual.valor = valor
                actual = actual.derecha
            aux = aux.siguiente

                

    #recorre por filas
    def imprimir(self):
        eFila=self.eRows.primero
        fila = ''
        while eFila != None:

            actual = eFila.acceso
            while actual != None:
                fila+='['+str(actual.fila+actual.columna)+']'
                actual = actual.derecha
                

            print(fila)
            fila=''
            eFila = eFila.siguiente
    
    #recorre por columna    
    def recorrerC(self):
        eColumna = self.eColumns.primero
        fila=''
        while eColumna != None:
            actual = eColumna.acceso
            while actual != None:
                fila+= '['+str(actual.fila+actual.columna)+']'
                actual = actual.abajo
            
            print(fila)
            fila=''
            eColumna = eColumna.siguiente

    #recorre por columna    
    def valores(self):
        eColumna = self.eColumns.primero
        fila=''
        while eColumna != None:
            actual = eColumna.acceso
            while actual != None:
                fila+= '['+str(actual.valor)+']'
                actual = actual.abajo
            
            print(fila)
            fila=''
            eColumna = eColumna.siguiente      


    def Graph(self,name):
        file = open(name+'.dot','w')
        grafo='digraph '+name+'''{\n
            label = \"'''+name+'\"'
        grafo+='''
            bgcolor = "#9DDEFC"
            node[shape=ellipse fillcolor="#E6D4BE" style =filled]
            fontsize="20"
            
        '''
        eColumna = self.eColumns.primero
        
        while eColumna != None:
            actual = eColumna.acceso
            while actual != None:
                
                grafo+='nodo'+str(actual.fila)+str(actual.columna)+'[label = '+str(actual.valor)+']\n\t\t'
                actual = actual.abajo
            
            eColumna = eColumna.siguiente 

        aux=self.eRows.primero
        while aux != None:
            actual=aux.acceso
            while actual != None and actual.derecha != None:
            
                grafo+='nodo'+str(actual.fila)+str(actual.columna)+'->nodo'+str(actual.derecha.fila)+str(actual.derecha.columna)+'[arrowhead = none]\n\t\t'

                actual = actual.derecha

            aux=aux.siguiente
        
        aux2=self.eColumns.primero
        while aux2 != None:
            actual=aux2.acceso
            while actual != None and actual.abajo != None:
                
                grafo+='rank = same{nodo'+str(actual.fila)+str(actual.columna)+'->nodo'+str(actual.abajo.fila)+str(actual.abajo.columna)+'[arrowhead = none]}\n\t\t'

                actual=actual.abajo
            aux2=aux2.siguiente 

        grafo+='}'
        file.write(grafo)
        file.close()

        system('cmd /c "dot.exe -Tpng ' + name + '.dot' + ' -o ' + name + '.png' + '"')
        startfile(name+'.png')



    