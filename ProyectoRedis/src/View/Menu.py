from ProyectoRedis.src.Controller import Utiles,GestionPieza,GestionArma,GestionAC
from ProyectoRedis.src.Model import GestorBBDD

def menu():
    opcion=None
    while(opcion!="0"):
        print("\n"+Utiles.bcolors.Yellow+"[====="+"-"*5+"MENU PRINCIPAL"+"-"*5+"=====]"+Utiles.bcolors.White+"\n")
        print(Utiles.bcolors.Cyan+"1.Gestionar los AC(Mechas).\n2.Gestionar las Piezas.\n3.Gestionar las Armas.\n4.Agregar catalogo.\n5.Borrar base de datos.\n0.Salir."+Utiles.bcolors.White)
        opcion=Utiles.check_numerosMenu("Opcion", 25)
        if(opcion=="1"):
            gestor = GestionAC.GestionAC()
            submenu("AC", gestor)
        elif(opcion=="2"):
            gestor = GestionPieza.GestionPieza()
            submenu("PIEZA", gestor)
        elif(opcion=="3"):
            gestor = GestionArma.GestionArma()
            submenu("ARMA", gestor)
        elif (opcion == "4"):
            if Utiles.confirmacion("¿Esta seguro que quiere agregar catalogo?") == True:
                GestorBBDD.AgregarCatalogo()
        elif (opcion == "5"):
            if Utiles.confirmacion("¿Esta seguro que quiere borrar la base de datos?") == True:
                GestorBBDD.dropDatabase()
        elif(opcion=="0"):
            print("Saliendo del programa.")
        else:
            print("Opcion no valida.")


def submenu(tipoDato, gestor):
    opcion=None
    while(opcion!="0"):
        print(Utiles.bcolors.Purple+"[=====================GESTION DE "+tipoDato+"=====================]\n"+Utiles.bcolors.White)
        print(Utiles.bcolors.Cyan+"1.Crear "+tipoDato+".\n2.Eliminar "+tipoDato+".\n3.Modificar "+tipoDato+".\n4.Buscar "+tipoDato+".\n5.Mostrar todos los "+tipoDato+".\n0.Salir."+Utiles.bcolors.White)
        opcion=Utiles.check_numerosMenu("Opcion", 25)
        if(opcion=="1"):
            gestor.alta()
        elif(opcion=="2"):
            gestor.baja()
        elif(opcion=="3"):
            gestor.modificar()
        elif(opcion=="4"):
            gestor.buscar()
        elif(opcion=="5"):
            gestor.mostrarTodos()
        elif(opcion=="0"):
            print("\nSaliendo del menu.\n")
            
        else:
            print("Opcion no valida.")



