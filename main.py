
import xml.etree.ElementTree as ET
from Matriz import Matriz
def read_xml(root):
    mytree = ET.parse(root)
    myroot = mytree.getroot()
    return myroot

def nodos(file,n):
    Nodos=Matriz()
    for x in file[n].findall('posicion'):
        Nodos.insertar(x.attrib.get('x'),x.attrib.get('y'),x.text)
        
    return Nodos






if __name__ == '__main__':
    auxiliar=False
    global archivo
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
                print(child.tag, child.attrib)
               
            #for x in archivo[0].findall('posicion'):
                #print(x.text)
                
            Lista=nodos(archivo,0)
            
            Lista.imprimir()
            

           

        elif opcion == '2':
            print('aqui el dolor de cabeza')
        elif opcion == '3':
            print('aqui lo ultimo')
        elif opcion == '4':
            print('---------------------------------------------')
            print('HENRY RONELY MENDOZA AGUILAR')
            print('202004810')
            print('INTRODUCCIÓN A LA PROGRAMACIÓN Y COMPUTACIÓN 2 SECCIÓN \"A\"')
            print('INGENIERIA EN CIENCIAS Y SISTEMAS')
            print('4TO SEMESTRE')
            print('---------------------------------------------')

        elif opcion == '5':
            print('AQUI HAGO ESO DE GRAPHZLI')
        elif opcion == '6':
            print('PROGRAMA FINALIZADO')
            auxiliar=True
        else:
            print('Por favor ingrese un número')
        