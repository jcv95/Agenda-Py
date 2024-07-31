from abc import ABC, abstractmethod

class Persona(ABC):
    def _init_(self):
        self.nombre = ""
        self.apellido = ""
        self.telefono=0
        self.direccion=""
        self.num=1
       


    def setnum(self, num):
        self.num = num
       
    def getnum(self):
        return self.num
       
    def setnombre(self):
        print(" ______________________________ ")
        print("|      INTRODUCIR NOMBRE       |")
        print("|______________________________|")
        self.nombre = input("                ")
    def getnombre(self):
        return self.nombre
   
    def setapellido(self):
        print(" ______________________________ ")
        print("|     INTRODUCIR APELLIDO      |")
        print("|______________________________|")
        self.apellido = input("                ")
    def getapellido(self):
        return self.apellido

    def settelefono(self):
        print(" ______________________________ ")
        print("|     INTRODUCIR TELEFONO      |")
        print("|______________________________|")
        self.telefono = input("                ")
    def gettelefono(self):
        return self.telefono

    def setdireccion(self):
        print(" ______________________________ ")
        print("|     INTRODUCIR DIRECCION     |")
        print("|______________________________|")
        self.direccion = input("                ")      
    def getdireccion(self):
        return self.direccion
        
   
#____________________________________________________________________________________________________________________
class Agenda:
    def __init__(self):
        self.listado=[]
   
    def agregarlistado(self,persona):
        self.listado.append(persona)
   
    def mostrarcontactos(self):
        print(" ________________________________________________________")
        print("|                       CONTACTOS                        |")
        print("|________________________________________________________|")
        print("| ID|   NOMBRE   |   APELLIDO   | TELEFONO |  DIRECCION  |")
        print("|___|____________|______________|__________|_____________|")
        for contacto in self.listado:
            print("|",contacto.getnum(),"|",contacto.getnombre(),"|",contacto.getapellido(),"|",contacto.gettelefono(),"|",contacto.getdireccion())
            print("|________________________________________________________|")
   
    def borrarcontacto(self):
        print(" ______________________________ ")
        print("|     INTRODUCIR ID/BORRAR     |")
        print("|______________________________|")
        numero = int(input("                "))
        for contacto in self.listado:
            if (contacto.getnum()== numero):
                self.listado.remove(contacto)
                print(" ______________________________ ")
                print("| El contacto",contacto.getnombre(),contacto.getapellido())
                print("|  FUE ELIMINADO DE LA AGENDA  |")
                print("|______________________________|")
        else:
                print(" ______________________________ ")
                print("|    NO SE ENCONTRO CONTACTO   |")
                print("|______________________________|")

    def editarcontacto(self):
        print(" ______________________________ ")
        print("|     INTRODUCIR ID/MODIF      |")
        print("|______________________________|")
        numero = int(input("                "))
        for contacto in self.listado:
            if (contacto.getnum()== numero):
                print(" ______________________________ ")
                print("|    MODIFICAR CONTACTO",contacto.getnombre())
                print("|______________________________|")
                print("|       SELECCIONE OPCION      |")
                print("|          1- NOMBRE           |")
                print("|          2- APELLIDO         |")
                print("|          3- TELEFONO         |")
                print("|          4- DIRECCION        |")
                print("|______________________________|")
                opcion=int(input("                "))
                if opcion==1:
                    contacto.setnombre()
                elif opcion==2:
                    contacto.setapellido()
                elif opcion==3:
                    contacto.settelefono()
                elif opcion==4:
                    contacto.setdireccion()
                print(" ______________________________ ")
                print("|    MODIFICACION COMPLETADA   |")
                print("|______________________________|")
        else:
                print(" ______________________________ ")
                print("|    NO SE ENCONTRO CONTACTO   |")
                print("|______________________________|")

    def buscarcontacto(self):
        print(" ______________________________ ")
        print("|  INTRODUCIR NOMBRE/APELLIDO  |")
        print("|         PARA BUSCAR          |")
        print("|______________________________|")
        nombre_apellido = input("                ")
        coincidencias = []
        for contacto in self.listado:
            if (contacto.getnombre()== nombre_apellido) or (contacto.getapellido()== nombre_apellido):
                coincidencias.append(contacto)        
               
        if len(coincidencias)>0:
            print(" ________________________________________________________")
            print("|                       RESULTADO                        |")
            print("|________________________________________________________|")
            print("| ID|   NOMBRE   |   APELLIDO   | TELEFONO |  DIRECCION  |")
            print("|___|____________|______________|__________|_____________|")
            for i in coincidencias:
                 print("|",i.getnum(),"|",i.getnombre(),"|",i.getapellido(),"|",i.gettelefono(),"|",i.getdireccion())
        else:
            print(" ______________________________ ")
            print("|    NO SE ENCONTRO CONTACTO   |")
            print("|______________________________|")

       


#agenda = []


#main_______________________________________________________________________________________________________________________________
agenda=Agenda()
i=1
while True:
    print(" ______________________________ ")
    print("|*            AGENDA          *|")
    print("|______________________________|")
    print("|      1- Agregar Contacto     |")
    print("|      2- Lista  Contactos     |")
    print("|      3- Borrar Contacto      |")
    print("|      4- Editar Contacto      |")
    print("|      5- Buscar Contacto      |")
    print("|*          6- SALIR          *|")
    print("|______________________________|")
    opcion = input("                ")
    if opcion == "1":
            persona=Persona()
            persona.setnum(i)
            persona.setnombre()
            persona.setapellido()
            persona.settelefono()
            persona.setdireccion()
            agenda.agregarlistado(persona)
            print(" ______________________________ ")
            print("|     NUEVO CONTACTO CREADO    |")
            print("|______________________________|")
            i=i+1
    elif opcion == "2": 
        agenda.mostrarcontactos()      
    elif opcion == "3":
        agenda.borrarcontacto()
    elif opcion=="4":
        agenda.editarcontacto()
    elif opcion=="5":
        agenda.buscarcontacto()
    elif opcion=="6":
        print("¡¡HASTA LUEGO!!")
        break
    else:
        print(" ______________________________ ")
        print("|     ¡¡OPCION INVALIDA!!      |")
        print("|______________________________|")
