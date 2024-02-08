from ProyectoRedis.src.Controller import Utiles, iGestores
from ProyectoRedis.src.Model import GestorBBDD


class GestionArma(iGestores):
    @staticmethod
    def alta():
        nombre = None
        tipoDamage = None
        dps = None
        rpm = None
        municion = None
        armaHombro = None
        precio = None

        print("ALTA")
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            armaAux = GestorBBDD.buscarDato("Arma_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
            if armaAux is None:
                tipoDamage = Utiles.check_letras("tipo de damage", 25)
        if tipoDamage is not None:
            dps = Utiles.check_numeros("damage por segundo", 25)
        if dps is not None:
            rpm = Utiles.check_numeros("rondas por minuto", 25)
        if rpm is not None:
            municion = Utiles.check_numeros("rondas maximas", 25)
        if municion is not None:
            armaHombro = Utiles.confirmacion("¿Es un arma de hombro?")
        if armaHombro is not None:
            precio = Utiles.check_numeros("precio del arma", 25)
        if precio is not None:
            arma = {  # Aqui metemos en un diccionario los datos
                "Arma_"+str(nombre)+"_Nombre": str(nombre),
                "Arma_"+str(nombre)+"_TipoDamage": str(tipoDamage),
                "Arma_"+str(nombre)+"_Dps": str(dps),
                "Arma_"+str(nombre)+"_Rpm": str(rpm),
                "Arma_"+str(nombre)+"_Municion": str(municion),
                "Arma_"+str(nombre)+"_ArmaHombro": str(armaHombro),
                "Arma_"+str(nombre)+"_Precio": str(precio)
                }
            GestorBBDD.insertarDato(arma)#Te mando un diccionario con las clave valor del arma---------------------------------------------------

    @staticmethod
    def baja():
        print("BAJA")
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            armaAux =GestorBBDD.buscarDato("Arma_" + nombre)
            if armaAux is not None:
                if Utiles.confirmacion("¿Seguro que quiere eliminar este arma?") is True:
                    GestorBBDD.borrarDato("Arma_"+nombre)

    @staticmethod
    def modificar():
        print("MODIFICAR")
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            armaAux = GestorBBDD.buscarDato("Arma_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
            if armaAux is not None:
                menuModificar(nombre,armaAux)


    @staticmethod
    def menuModificar(nombreOriginal,arma):
        opcion = None
        while (opcion != "0"):
            cambio=False
            print("¿Que campo quieres modificar?")
            print("1.Nombre.\n2.Tipo de damage.\n3.Damage por segundo."
                  "\n4.Rondas por minuto.\n5.Municion maxima.\n6.Puede ponerse en el hombro.\n7.Precio.\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    armaAux = GestorBBDD.buscarDato("Arma_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                    if armaAux is None:
                        if Utiles.confirmacion("Seguro que quiere cambiar el nombre del arma: "+nombreOriginal+" a: "+nombre):
                            GestorBBDD.borrarDato("Arma_"+nombreOriginal)
                            armaAux2 = {
                                "Arma_" + nombre + "_Nombre": nombre,
                                "Arma_" + nombre + "_TipoDamage": arma["Arma_" + nombreOriginal + "_TipoDamage"],
                                "Arma_" + nombre + "_Dps": arma["Arma_" + nombreOriginal + "_Dps"],
                                "Arma_" + nombre + "_Rpm": arma["Arma_" + nombreOriginal + "_Rpm"],
                                "Arma_" + nombre + "_Municion": arma["Arma_" + nombreOriginal + "_Municion"],
                                "Arma_" + nombre + "_ArmaHombro": arma["Arma_" + nombreOriginal + "_ArmaHombro"],
                                "Arma_" + nombre + "_Precio": arma["Arma_" + nombreOriginal + "_Precio"]
                            }
                            arma=armaAux2
                            nombreOriginal=nombre
                            cambio = True
                    else:
                        print("Ya existe un arma con el mismo nombre.")
            elif (opcion == "2"):
                tipoDamage = Utiles.check_letras("tipo de damage", 25)
                if tipoDamage is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el tipo de damage del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + tipoDamage):
                        arma["Arma_" + nombreOriginal + "_TipoDamage"] = tipoDamage
                        cambio = True
            elif (opcion == "3"):
                dps = Utiles.check_numeros("damage por segundo", 25)
                if dps is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el damage por segundo del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + dps):
                        arma["Arma_" + nombreOriginal + "_Dps"] = dps
                        cambio = True
            elif (opcion == "4"):
                rpm = Utiles.check_numeros("rondas por minuto", 25)
                if rpm is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el rondas por minuto del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + rpm):
                        arma["Arma_" + nombreOriginal + "_Rpm"] = rpm
                        cambio = True
            elif (opcion == "5"):
                municion = Utiles.check_numeros("rondas maximas", 25)
                if municion is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar las rondas maximas del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + municion):
                        arma["Arma_" + nombreOriginal + "_Municion"] = municion
                        cambio = True
            elif (opcion == "6"):
                armaHombro = Utiles.confirmacion("¿Es un arma de hombro?")
                if armaHombro is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar si el arma es de hombro de: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + armaHombro):
                        arma["Arma_" + nombreOriginal + "_ArmaHombro"] = armaHombro
                        cambio = True
            elif (opcion == "7"):
                precio = Utiles.check_numeros("precio del arma", 25)
                if precio is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el precio del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + precio):
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
    def buscar(nombre):
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            datos = GestorBBDD.buscarDato("Arma_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
            if datos is not None:
                print("\n[-" + datos["Arma_"+nombre+"_Nombre"] + "-]")
                print("  Tipo de damage:" + datos["Arma_"+nombre+"_TipoDamage"] + "  ")
                print("  Damage por segundo:" + datos["Arma_"+nombre+"_Dps"] + "  ")
                print("  Rondas por minuto:" + datos["Arma_"+nombre+"_Rpm"] + "  ")
                print("  Municion maxima:" + datos["Arma_"+nombre+"_Municion"] + "  ")
                print("  Puede ponerse en el hombro:" + datos["Arma_"+nombre+"_ArmaHombro"] + "  ")
                print("  Precio:" + datos["Arma_"+nombre+"_Precio"] + "$  ")
                return datos
            else:
                print("No se ha encontrado el arma.")
                return None
        else:
            return None
    @staticmethod
    def mostrarTodos():
        print("MOSTRAR TODOS")
        datos = GestorBBDD.mostrarTodosDatos("Arma")# Te mando la categoria para que me devuelvas un diccionario con diccionarios que contengan los datos de una pieza
        for x in datos:
            print("\n[-" + datos[x][x+"_Nombre"] + "-]")
            print("  Tipo de damage:" + datos[x][x+"_TipoDamage"] + "  ")
            print("  Damage por segundo:" + datos[x][x+"_Dps"] + "  ")
            print("  Rondas por minuto:" + datos[x][x+"_Rpm"] + "  ")
            print("  Municion maxima:" + datos[x][x+"_Municion"] + "  ")
            print("  Puede ponerse en el hombro:" + datos[x][x+"_ArmaHombro"] + "  ")
            print("  Precio:" + datos[x][x+"_Precio"] + "$  ")
