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
         self.nombre = input("Introduce el nombre del contacto: ")
    def getnombre(self):
        return self.nombre
    
    def setapellido(self):
        self.apellido = input("Introduce el apellido del contacto: ")
    def getapellido(self):
        return self.apellido

    def settelefono(self):
        self.telefono = int(input("Introduce el teléfono del contacto: "))
    def gettelefono(self):
        return self.telefono

    def setdireccion(self):
        self.direccion = input("Introduce la dirección del contacto: ")      
    def getdireccion(self):
        return self.direccion
    
#____________________________________________________________________________________________________________________
class Agenda:
    def __init__(self):
        self.listado=[]
    
    def agregarlistado(self):
        #self.listado.append(persona)
        
        contacto = "INSERT INTO contactos (nombre, apellido, telefono, direccion) VALUES (%s,%s,%s,%s)"#Inserta en  la tabla creada (create table contactos[MYSQL]), le asigamos los 4 valores vacios
        nombre = input("Ingresar NOMBRE :")
        apellido=input("Ingresar APELLIDO:")
        telefono=input("ahora TELEFONO:")
        direccion=input("Y por ultimo DIRECION:")
        mi_cursor.execute(contacto, (nombre,apellido,telefono,direccion))
        base_datos.commit()
        print(" ______________________________")
        print("|+        CONTACTO CREADO     +|")
        print("|______________________________|")

    
    def mostrarcontactos(self):
        print(" ________________________________________________________")
        print("|                       CONTACTOS                        |")
        print("|________________________________________________________|")
        print("| ID|   NOMBRE   |   APELLIDO   | TELEFONO |  DIRECCION  |")
        print("|___|____________|______________|__________|_____________|")
        #VINCULACION PYTHON7MYSQL
        # traemos todos los datos de la tabla atletas
        consulta_motrar_datos="SELECT * FROM contactos"#selecciona la tabla creada (create table contactos[MYSQL])
        mi_cursor.execute(consulta_motrar_datos)
        tabla_contactos = mi_cursor.fetchall()
        for contacto in tabla_contactos:
            print ("|",contacto[0],"|",contacto[1],"|",contacto[2],"|",contacto[3],"|",contacto[4])
            print("|_______________________________________________________")

   
    def borrarcontacto(self):
   
            consulta_mostrar_dato = "SELECT * FROM contactos WHERE registro = %s AND nombre= %s "
            consulta_borrar = "DELETE FROM contactos WHERE registro = %s"   # espera un parámetro
            contacto_borrar = input("Ingrese el ID DE LA PERSONA A ELIMINAR:")#se elige el numero que se vincule con el registro
            print(" ______________________________ ")
            print("|            AGENDA            |")
            print("|                              |")
            print("|      ¿ELIMINAR CONTACTO?     |")
            print("|______________________________|")
            print("|            1- SI             |")
            print("|            2- NO             |")
            print("|______________________________|")
            self.opc=int(input(""))
            while self.opc>2:
                print("       ¡¡OPCION INVALIDA!!")
                self.opc=int(input(""))
            if self.opc==1:
                mi_cursor.execute(consulta_borrar, (contacto_borrar,)) #le pasamos el parámetro
                resultado=mi_cursor.fetchone()
                base_datos.commit() 
                print(" ______________________________")
                print("|-       CONTACTO ELIMINADO   -|")
                print("|______________________________|")
            
    def editarcontacto(self):
        consula_editar = "UPDATE contactos SET nombre = %s, apellido= %s,telefono= %s,direccion= %s WHERE registro = %s"  #espera 4 parámetros y usa REGISTRO para encontrarlos
        iden=int(input("INTRODUCE EL ID DEL CONTACTO A MODIFICAR:"))
        nuevonombre=input("INTRODUZCA EL NUEVO NOMBRE:")
        nuevoapellido=input("INTRODUZCA EL NUEVO APELLIDO:")
        nuevotelefono=input("INTRODUZCA EL NUEVO TELEFONO:")
        nuevodireccion=input("INTRODUZCA EL NUEVO DIRECCION:")
        parametros_editar=(nuevonombre,nuevoapellido,nuevotelefono,nuevodireccion,iden)
        mi_cursor.execute(consula_editar,parametros_editar)
        base_datos.commit()
        print(" ______________________________")
        print("|*      CONTACTO  EDITADO     *|")
        print("|______________________________|")

    def buscarcontacto(self):
        x=0
        consulta_mostrar_dato = "SELECT * FROM contactos WHERE nombre = %s " #AND apellido = %s" 
        nombre=input("Ingresar nombre Contacto:")
        mi_cursor.execute(consulta_mostrar_dato, (nombre,))
        resultado=mi_cursor.fetchall()# se utiliza fetchall() asi trae 2 o mas casos que tengan el mismo nombre,mi_cursor.fetchone() solo para 1 registro
        print(" ________________________________________________________")
        print("|                       RESULTADO                        |")
        print("|________________________________________________________|")
        print("| ID|   NOMBRE   |   APELLIDO   | TELEFONO |  DIRECCION  |")
        print("|___|____________|______________|__________|_____________|")
        for contacto in resultado:
                print("|",contacto[0],"|",contacto[1],"|",contacto[2],"|",contacto[3],"|",contacto[4])
                print("|________________________________________________________")
                x=1
        if x==0:
            print(" ________________________________________________________")
            print("|         NO HAY CONCIDENCIA CON",nombre)
            print("|________________________________________________________|")

        


#agenda = []


#main_______________________________________________________________________________________________________________________________


import mysql.connector;

base_datos = mysql.connector.connect(
  host="localhost",
  port="3305",#se tiene que utilizar el mismo puerto que utiliza mysql (default 3306)
  user="root",
  password="1234",
  database="agenda"
)
# mi_cursor es la representación de la base de datos en python
mi_cursor = base_datos.cursor()

#select nombre, from agenda;

agenda=Agenda()
i=2
while True:
    print(" ______________________________ ")
    print("|            AGENDA            |")
    print("|______________________________|")
    print("|      1- Agregar contacto     |")
    print("|      2-Mostrar Contactos     |")
    print("|      3- Borrar Contacto      |")
    print("|      4- Editar Contacto      |")
    print("|      5- Buscar Contacto      |")
    print("|           6-SALIR            |")
    print("|______________________________|")
    opcion = input("                ")
    if opcion == "1":
            agenda.agregarlistado()  
    elif opcion == "2":
        agenda.mostrarcontactos()
    elif opcion == "3":
        agenda.borrarcontacto()
    elif opcion=="4":
        agenda.editarcontacto()
    elif opcion=="5":
        agenda.buscarcontacto()#casi listo
    elif opcion=="6":
        print(" ______________________________ ")
        print("|***     ¡¡HASTA LUEGO!!    ***|")
        print("|______________________________|")
        break
    else:
        print("     ¡¡OPCION INVALIDA!!")
        print("_______________________________")
