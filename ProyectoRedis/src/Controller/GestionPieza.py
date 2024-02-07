from ProyectoRedis.src.Controller import Utiles
from ProyectoRedis.src.Model import GestorBBDD

class GestionPieza(iGestores):


    @staticmethod
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
            piezaAux= GestorBBDD.buscarDato("Pieza_" + nombre)#Comprobamos si ya existe un arma con ese nombre
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
            pieza = {#Aqui metemos en un diccionario los datos
                "Pieza_"+str(nombre)+"_nombre":str(nombre),
                "Pieza_"+str(nombre)+"_tipoPieza":str(tipoPieza),
                "Pieza_"+str(nombre)+"_armadura":str(armadura),
                "Pieza_"+str(nombre)+"_consumoEnergia":str(consumoEnergia),
                "Pieza_"+str(nombre)+"_peso":str(peso),
                "Pieza_"+str(nombre)+"_precio":str(precio)
                }
            GestorBBDD.insertarDato(pieza)


    @staticmethod
    def menuTipoPieza():
        opcion = None
        while (opcion != "0"):
            print("Tipo de pieza:")
            print("1.Cabeza.\n2.Torso.\n3.Brazos.\n4.Piernas.\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                return "cabeza"
            elif (opcion == "2"):
                return "torso"
            elif (opcion == "3"):
                return "brazos"
            elif (opcion == "4"):
                return "piernas"
            elif (opcion == "0"):
                print("Saliendo del menu.")
                return None
            else:
                print("Opcion no valida.")


    @staticmethod
    def baja():
        print("BAJA")
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            piezaAux = GestorBBDD.buscarDato("Pieza_" + nombre)
            if piezaAux is not None:
                if Utiles.confirmacion("¿Seguro que quiere eliminar esta pieza?") is True:
                    GestorBBDD.borrarDato("Pieza_" + nombre)


    @staticmethod
    def modificar():
        print("MODIFICAR")


    @staticmethod
    def menuModificar(nombreOriginal, arma):#Metodo placeholder
        opcion = None
        while (opcion != "0"):
            cambio = False
            print("¿Que campo quieres modificar?")
            print("1.Nombre.\n2.Tipo de damage.\n3.Damage por segundo."
                  "\n4.Rondas por minuto.\n5.Municion maxima."
                  "\n6.Puede ponerse en el hombro.\n7.Precio."
                  "\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    armaAux = GestorBBDD.buscarDato(
                        "Arma_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                    if armaAux is None:
                        if Utiles.confirmacion(
                                "Seguro que quiere cambiar el nombre del arma: " + nombreOriginal + " a: " + nombre):
                            GestorBBDD.borrarDato("Arma_" + nombreOriginal)
                            armaAux2 = {
                                "Arma_" + nombre + "_Nombre": nombre,
                                "Arma_" + nombre + "_TipoDamage": arma["Arma_" + nombreOriginal + "_TipoDamage"],
                                "Arma_" + nombre + "_Dps": arma["Arma_" + nombreOriginal + "_Dps"],
                                "Arma_" + nombre + "_Rpm": arma["Arma_" + nombreOriginal + "_Rpm"],
                                "Arma_" + nombre + "_Municion": arma["Arma_" + nombreOriginal + "_Municion"],
                                "Arma_" + nombre + "_ArmaHombro": arma["Arma_" + nombreOriginal + "_ArmaHombro"],
                                "Arma_" + nombre + "_Precio": arma["Arma_" + nombreOriginal + "_Precio"]
                            }
                            arma = armaAux2
                            cambio = True
                else:
                    print("Ya existe un arma con el mismo nombre.")
            elif (opcion == "2"):
                tipoDamage = Utiles.check_letras("tipo de damage", 25)
                if tipoDamage is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el tipo de damage del arma: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + tipoDamage):
                        arma["Arma_" + nombreOriginal + "_TipoDamage"] = tipoDamage
                        cambio = True
            elif (opcion == "3"):
                dps = Utiles.check_numeros("damage por segundo", 25)
                if dps is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el damage por segundo del arma: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + dps):
                        arma["Arma_" + nombreOriginal + "_Dps"] = dps
                        cambio = True
            elif (opcion == "4"):
                rpm = Utiles.check_numeros("rondas por minuto", 25)
                if rpm is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el rondas por minuto del arma: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + rpm):
                        arma["Arma_" + nombreOriginal + "_Rpm"] = rpm
                        cambio = True
            elif (opcion == "5"):
                municion = Utiles.check_numeros("rondas maximas", 25)
                if municion is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar las rondas maximas del arma: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + municion):
                        arma["Arma_" + nombreOriginal + "_Municion"] = municion
                        cambio = True
            elif (opcion == "6"):
                armaHombro = Utiles.confirmacion("¿Es un arma de hombro?")
                if armaHombro is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar si el arma es de hombro de: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + armaHombro):
                        arma["Arma_" + nombreOriginal + "_ArmaHombro"] = armaHombro
                        cambio = True
            elif (opcion == "7"):
                precio = Utiles.check_numeros("precio del arma", 25)
                if precio is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el precio del arma: " + arma[
                        "Arma_" + nombreOriginal + "_Nombre"] + " a: " + precio):
                        arma["Arma_" + nombreOriginal + "_Precio"] = precio
                        cambio = True
            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                return None
            else:
                print("Opcion no valida.")
            if cambio is True:
                GestorBBDD.insertarDato(arma)


    @staticmethod
    def buscar():
        print("BUSCAR")
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            datos = GestorBBDD.buscarDato(
                "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
            if datos is not None:
                print("\n[-" + datos["*Nombre"] + "-]")
                print("  Tipo de pieza:" + datos["*TipoPieza"] + "  ")
                print("  Armadura:" + datos["*Armadura"] + "  ")
                print("  Consumo de energia:" + datos["*ConsumoEnergia"] + "  ")
                print("  Peso:" + datos["*Peso"] + "  ")
                print("  Precio:" + datos["*Precio"] + "$  ")
                return datos
            else:
                print("No se ha encontrado la pieza.")
                return None
        else:
            return None

    @staticmethod
    def mostrarTodos():
        print("MOSTRAR TODOS")
        datos= GestorBBDD.mostrarTodosDatos("Pieza")
        for x in datos:
            print("\n[-"+datos[x]["*Nombre"]+"-]")
            print("  Tipo de pieza:"+datos[x]["*TipoPieza"]+"  ")
            print("  Armadura:"+datos[x]["*Armadura"]+"  ")
            print("  Consumo de energia:"+datos[x]["*ConsumoEnergia"]+"  ")
            print("  Peso:"+datos[x]["*Peso"]+"  ")
            print("  Precio:"+datos[x]["*Precio"]+"$  ")
    
    
    
    