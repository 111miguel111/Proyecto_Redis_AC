from Controller import Utiles,GestorBBDD



def alta():
    nombre=None
    tipoPieza=None
    armadura=None
    consumoEnergia=None
    peso=None
    precio=None
    
    print("ALTA")
    nombre=Utiles.check_campo("nombre", 25)
    if nombre is not None:
        piezaAux=GestorBBDD.buscarDato("Pieza"+nombre)#Comprobamos si ya existe un arma con ese nombre
        if piezaAux is None:
            tipoPieza=menuTipoPieza()
    if tipoPieza is not None:
        armadura=Utiles.check_numeros("valor de armadura", 25)
    if armadura is not None:
        consumoEnergia=Utiles.check_numeros("valor de consumo de energia", 25)
    if consumoEnergia is not None:
        peso=Utiles.check_numeros("peso de la pieza", 25)
    if peso is not None: 
        precio=Utiles.check_numeros("precio de la pieza", 25)
        if precio is not None:
            piezaPrueba = {#Aqui metemos en un diccionario los datos
                        "nombre":nombre,
                        "tipoPieza":tipoPieza,
                        "armadura":armadura,
                        "consumoEnergia":consumoEnergia,
                        "peso":peso,
                        "precio":precio
                        }
            #TODO-Aqui se meteria la nueva pieza a la bbdd
def menuTipoPieza():
    opcion=None
    while(opcion!="0"):
        print("--"*5+"MENU PRINCIPAL--"*5)
        print("1.Cabeza.\n2.Torso.\n3.Brazos.\n4.Piernas.\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            return "cabeza"
        elif(opcion=="2"):
            return "torso"
        elif(opcion=="3"):
            return "brazos"
        elif(opcion=="4"):
            return "piernas"
        elif(opcion=="0"):
            print("Saliendo del menu.")
            return None
        else:
            print("Opcion no valida.")
def baja():
    print("BAJA")
def modificar():
    print("MODIFICAR")
def buscar():
    print("BUSCAR")
def mostrarTodos():
    print("MOSTRAR TODOS")