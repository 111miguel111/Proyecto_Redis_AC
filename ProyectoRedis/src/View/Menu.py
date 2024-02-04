from Controller import Utiles,GestionPieza,GestionArma,GestionAC

def menu():
    opcion=None
    while(opcion!="0"):
        print("--"*5+"MENU PRINCIPAL--"*5)
        print("1.Gestionar los AC(Mechas).\n2.Gestionar las piezas.\n3.Armas\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            menuAC()
        elif(opcion=="2"):
            print("")
            menuPiezas()
        elif(opcion=="3"):
            print("")
            menuArmas()
        elif(opcion=="0"):
            print("Saliendo del programa.")
        else:
            print("Opcion no valida.")


def menuAC():
    opcion=None
    while(opcion!="0"):
        print("\n--GESTION DEL AC--\n")
        print("1.Crear AC.\n2.Eliminar AC.\n3.Modificar AC.\n4.Buscar AC.\n5.Mostrar todos los AC.\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            GestionAC.alta()
        elif(opcion=="2"):
            print("")
            GestionAC.baja()
        elif(opcion=="3"):
            print("")
            GestionAC.modificar()
        elif(opcion=="4"):
            print("")
            GestionAC.buscar()
        elif(opcion=="5"):
            print("")
            GestionAC.mostrarTodos()
        elif(opcion=="0"):
            print("Saliendo del menu.\n")
            
        else:
            print("Opcion no valida.")



def menuPiezas():
    opcion=None
    while(opcion!="0"):
        print("\n--GESTION DE LAS PIEZAS--\n")
        print("1.Crear pieza.\n2.Eliminar pieza.\n3.Modificar pieza.\n4.Buscar pieza.\n5.Mostrar todos las pieza.\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            GestionPieza.alta()
        elif(opcion=="2"):
            print("")
            GestionPieza.baja()
            
        elif(opcion=="3"):
            print("")
            GestionPieza.modificar()
            
        elif(opcion=="4"):
            print("")
            GestionPieza.buscar()
            
        elif(opcion=="5"):
            print("")
            GestionPieza.mostrarTodos()
            
        elif(opcion=="0"):
            print("Saliendo del menu.\n")
            
        else:
            print("Opcion no valida.")
def menuArmas():
    opcion=None
    while(opcion!="0"):
        print("\n--GESTION DE LAS ARMAS--\n")
        print("1.Crear arma.\n2.Eliminar arma.\n3.Modificar arma.\n4.Buscar arma.\n5.Mostrar todos las armas.\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            GestionArma.alta()
        elif(opcion=="2"):
            print("")
            GestionArma.baja()
            
        elif(opcion=="3"):
            print("")
            GestionArma.modificar()
            
        elif(opcion=="4"):
            print("")
            GestionArma.buscar()
            
        elif(opcion=="5"):
            print("")
            GestionArma.mostrarTodos()
            
        elif(opcion=="0"):
            print("Saliendo del menu.\n")
            
        else:
            print("Opcion no valida.")
            
            
            
            
            