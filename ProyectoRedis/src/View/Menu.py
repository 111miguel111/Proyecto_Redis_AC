from ProyectoRedis.src.Controller import Utiles,GestionPieza,GestionArma,GestionAC


def menu():
    opcion=None
    while(opcion!="0"):
        print("\n"+"--"*5+"MENU PRINCIPAL"+"--"*5+"\n")
        print("1.Gestionar los AC(Mechas).\n2.Gestionar las piezas.\n3.Armas\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            gestor = GestionAC.GestionAC()
            submenu("AC", gestor)
        elif(opcion=="2"):
            print("")
            gestor = GestionPieza.GestionPieza()
            submenu("PIEZA", gestor)
        elif(opcion=="3"):
            print("")
            gestor = GestionArma.GestionArma()
            submenu("ARMA", gestor)
        elif(opcion=="0"):
            print("Saliendo del programa.")
        else:
            print("Opcion no valida.")


def submenu(tipoDato, gestor):
    opcion=None
    while(opcion!="0"):
        print("\n--GESTION DE "+tipoDato+"--\n")
        print("1.Crear "+tipoDato+".\n2.Eliminar "+tipoDato+".\n3.Modificar "+tipoDato+".\n4.Buscar "+tipoDato+".\n5.Mostrar todos los "+tipoDato+".\n0.Salir.")
        opcion=Utiles.check_numeros("Opcion", 25)
        if(opcion=="1"):
            print("")
            gestor.alta()
        elif(opcion=="2"):
            print("")
            gestor.baja()
        elif(opcion=="3"):
            print("")
            gestor.modificar()
        elif(opcion=="4"):
            print("")
            gestor.buscar()
        elif(opcion=="5"):
            print("")
            gestor.mostrarTodos()
        elif(opcion=="0"):
            print("Saliendo del menu.\n")
            
        else:
            print("Opcion no valida.")



