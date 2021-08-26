import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
from Matriz import Matriz
from terreno import terreno
from lista import dlinkedlist
from ruta import Camino

def read_xml(root):
    mytree = ET.parse(root)
    myroot = mytree.getroot()
    return myroot

def nodos(file,n):
    Nodos=Matriz()
    
    for x in file[n].findall('posicion'):
        Nodos.insertar(x.attrib.get('x'),x.attrib.get('y'),int(x.text))
        
    return Nodos

def crear_terreno(file):
    nombre=[]
    m=[]
    n=[]
    Px=[]
    Py=[]
    Fx=[]
    Fy=[]

    for child in file:
        nombre.append(child.attrib.get('nombre'))
    
    for c in archivo.findall('./terreno/dimension/m'):
        m.append(c.text)

    for c in archivo.findall('./terreno/dimension/n'):
        n.append(c.text)

    for c in archivo.findall('./terreno/posicioninicio/x'):
        Px.append(c.text)
    
    for c in archivo.findall('./terreno/posicioninicio/y'):
        Py.append(c.text)

    for c in archivo.findall('./terreno/posicionfin/x'):
        Fx.append(c.text)
    
    for c in archivo.findall('./terreno/posicionfin/y'):
        Fy.append(c.text)

    datos = dlinkedlist()

    for i in range(len(archivo)):
        t = terreno(nombre[i],m[i],n[i],Px[i],Py[i],Fx[i],Fy[i],nodos(file,i),gas=[],Rx=[],Ry=[])
        datos.append(t)

    return datos
    
def recorrido(file,pos,dato):
    g = Camino()
    coordenadas=[]
    valor=[]
    prueba=[]

    print('filas= '+str(dato.getDimM()))
    print('columnas= '+str(dato.getDimN()))
    for c in file[pos].findall('posicion'):
        coordenadas.append(c.attrib.get('x')+c.attrib.get('y'))
        valor.append(int(c.text))

    ruta=dict(zip(coordenadas,valor))
    
    for c in coordenadas:
        g.agregarVertice(c)

    aux=dato.getNodos().eRows.primero
    while aux != None:
        actual=aux.acceso
        while actual != None and actual.derecha != None:
            
            g.agregarArista(str(actual.fila+actual.columna),str(actual.derecha.fila+actual.derecha.columna),int(actual.valor)+int(actual.derecha.valor))
            actual = actual.derecha

        aux=aux.siguiente
    print('')
    print('')
    aux2=dato.getNodos().eColumns.primero
    while aux2 != None:
        actual=aux2.acceso
        while actual != None and actual.abajo != None:
            g.agregarArista(str(actual.fila+actual.columna),str(actual.abajo.fila+actual.abajo.columna),int(actual.valor)+int(actual.abajo.valor))
            actual=actual.abajo
        aux2=aux2.siguiente

    inicio=dato.getIniciox()+dato.getInicioy()
    final=dato.getFinx()+dato.getFiny()

    g.dijkstra(inicio)
    print(g.camino(inicio,final))

    ruta_C=g.camino(inicio,final)

    ruta_F=[]

    for c in ruta_C:
        ruta_F.append(ruta.get(c))

    print(ruta_F)
    dato.setGas(ruta_F)
    gas=0
    for c in ruta_F:
        gas+=int(c)
    mostrar_recorrido(ruta_C,gas,dato)
    return prueba

    
def mostrar_recorrido(ruta_C,gas,obj):
    R = Matriz()
    auxiliarX=[]
    coordenadaX=[]
    coordenaday=[]


    filas=int(obj.getDimM())
    columnas=int(obj.getDimN())

    for c in ruta_C:
        for x in c:
            auxiliarX.append(x)

    for i in range(len(auxiliarX)):
        if i%2==0:
            coordenadaX.append(auxiliarX[i])
        else:
            coordenaday.append(auxiliarX[i])
    print(coordenadaX)
    print(coordenaday)
    print('')
    print('filas= '+str(filas))
    print('columnas= '+str(columnas))

    obj.setRX(coordenadaX)
    obj.setRY(coordenaday)


    aux2=obj.getNodos().eColumns.primero
    while aux2 != None:
        actual=aux2.acceso
        while actual != None:
            R.insertar(actual.fila,actual.columna,'0')
            actual=actual.abajo
        aux2=aux2.siguiente

    for i in range(len(coordenadaX)):
        R.actualizar(coordenadaX[i],coordenaday[i],'1')

    print('')
    R.recorrerC()
    print('')
    R.valores()

    

    
def write_xml(obj):
    gas=0
    for g in obj.getGas():
        gas+=g
    
    if gas == 0:
        return print('AUN NO SE HA PROCESADO EL TERRENO')
    else:
        raiz=ET.Element('terreno',name=obj.getNombre())
        PI=ET.SubElement(raiz,'posicioninicio')
        ET.SubElement(PI,'x').text=str(obj.getIniciox())
        ET.SubElement(PI,'y').text=str(obj.getInicioy())
        PF=ET.SubElement(raiz,'posicionfin')
        ET.SubElement(PF,'x').text=str(obj.getFinx())
        ET.SubElement(PF,'y').text=str(obj.getFiny())
        
        combustible=ET.SubElement(raiz,'combustible')
        combustible.text = str(gas)

        for i in range(len(obj.getRX())):
            R = ET.SubElement(raiz,'posicion',x=str(obj.getRX()[i]),y=str(obj.getRY()[i]))
            R.text = str(obj.getGas()[i])
    
        estructura(raiz)
        doc = ET.ElementTree(raiz)
        guardar = input('INGRESE RUTA PARA GUARDAR EL ARCHIVO: ')

        try:
            doc.write(guardar)
        except IOError as e:
            print(e)


def estructura(root, tab='  '):
    aux = [(0, root)]
    while aux:
        line, e = aux.pop(0)
        lista = [(line + 1, c) for c in list(e)]
        if lista:
            e.text = '\n' + tab * (line+1)
        if aux:
            e.tail = '\n' + tab * aux[0][0]
        else:
            e.tail = '\n' + tab * (line-1) 
        aux[0:0] = lista 


if __name__ == '__main__':
    auxiliar=False
    global archivo
    global ter
    while auxiliar==False:
        print('------------------MENÚ------------------')
        print('|    1. CARGAR ARCHIVO                 |')
        print('|    2. PROCESAR ARCHIVO               |')
        print('|    3. ESCRIBIR ARCHIVO SALIDA        |')
        print('|    4. DATOS DEL ESTUDIANTE           |')
        print('|    5. GENERAR GRAFICA                |')
        print('|    6. CERRAR PROGRAMA                |')

        opcion=input("Elija una Opción dentro del menú: \n")

        if opcion == '1':
            root=input('INGRRESE LA RUTA DEL ARCHIVO:\n')
            archivo=read_xml(root)
            
            for child in archivo:
                print(child.tag, child.attrib.get('nombre'))
            
            ter = crear_terreno(archivo)
            
            print(ter.size)
            
            

        elif opcion == '2':
            c = input('ingrese el nombre del terreno: ')
            aux=ter.first
            index=0
            while aux:
                if aux.dato.getNombre() == c:
                    #aux.dato.getNodos().imprimir()
                    print('')
                    aux.dato.getNodos().recorrerC()
                    print('')
                    aux.dato.getNodos().valores()
                    print('')
                    prueba=recorrido(archivo,index,aux.dato)
                    #for p in prueba:
                        #print(p)

                    break
                

                index+=1
                aux=aux.next
            else:
                    print('TERRENO NO ENCONTRADO')

        elif opcion == '3':
            c = input('ingrese el nombre del terreno: ')
            aux=ter.first
            index=0
            while aux:
                if aux.dato.getNombre() == c:
                    write_xml(aux.dato)
                    break
                index+=1
                aux=aux.next


        elif opcion == '4':
            print('---------------------------------------------')
            print('HENRY RONELY MENDOZA AGUILAR')
            print('202004810')
            print('INTRODUCCIÓN A LA PROGRAMACIÓN Y COMPUTACIÓN 2 SECCIÓN \"A\"')
            print('INGENIERIA EN CIENCIAS Y SISTEMAS')
            print('4TO SEMESTRE')
            print('---------------------------------------------')

        elif opcion == '5':
            c = input('ingrese el nombre del terreno: ')
            aux=ter.first
        
            while aux:
                if aux.dato.getNombre() == c:

                    aux.dato.getNodos().Graph(c)

                    break
                aux=aux.next
            else:
                print('TERRENO NO ENCONTRADO')
            


        elif opcion == '6':
            print('PROGRAMA FINALIZADO')
            auxiliar=True
        else:
            print('Por favor ingrese un número')
        