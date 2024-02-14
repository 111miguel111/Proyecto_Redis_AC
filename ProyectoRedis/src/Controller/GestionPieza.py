from ProyectoRedis.src.Controller import Utiles, iGestores
from ProyectoRedis.src.Model import GestorBBDD


class GestionPieza(iGestores.iGestores):

    @staticmethod
    def alta():
        nombre = None
        tipoPieza = None
        armadura = None
        consumoEnergia = None
        peso = None
        precio = None
        pieza=None
        print(5*"-"+"ALTA"+"-"*5)
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            piezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + nombre)  # Comprobamos si ya existe un arma con ese nombre
            if piezaAux is None:
                tipoPieza = GestionPieza.menuTipoPieza()
            else:
                print("Ya existe una pieza con ese nombre.")
        if tipoPieza is not None:
            armadura = Utiles.check_numeros("valor de armadura", 25)
        if armadura is not None:
            consumoEnergia = Utiles.check_numeros("valor de consumo de energia", 25)
        if consumoEnergia is not None:
            peso = Utiles.check_numeros("peso de la pieza", 25)
        if peso is not None:
            precio = Utiles.check_numeros("precio de la pieza", 25)
        if precio is not None:
            pieza = {  # Aqui metemos en un diccionario los datos
                "Pieza_" + str(nombre) + "_Nombre": str(nombre),
                "Pieza_" + str(nombre) + "_TipoPieza": str(tipoPieza),
                "Pieza_" + str(nombre) + "_Armadura": str(armadura),
                "Pieza_" + str(nombre) + "_ConsumoEnergia": str(consumoEnergia),
                "Pieza_" + str(nombre) + "_Peso": str(peso),
                "Pieza_" + str(nombre) + "_Precio": str(precio)
            }
            GestorBBDD.insertarDato(pieza)
        if pieza is not None:
            print("Pieza creada.")
        else:
            print("Fallo en la creacion de la pieza")
    @staticmethod
    def menuTipoPieza():
        opcion = None
        while (opcion != "0"):
            print("Tipo de pieza:")
            print("1.Cabeza.\n2.Torso.\n3.Brazos.\n4.Piernas.\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                return "CABEZA"
            elif (opcion == "2"):
                return "TORSO"
            elif (opcion == "3"):
                return "BRAZOS"
            elif (opcion == "4"):
                return "PIERNAS"
            elif (opcion == "0"):
                print("Saliendo del menu.")
                return None
            else:
                print("Opcion no valida.")

    @staticmethod
    def baja():
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(5*"-"+"BAJA"+"-"*5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                piezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + nombre)
                if piezaAux is not None:
                    if Utiles.confirmacion("¿Seguro que quiere eliminar esta pieza?") is True:
                        GestorBBDD.borrarDato("Pieza_" + nombre)
                        GestorBBDD.cascada(nombre, "Sin equipar")
        else:
            print("No hay piezas creadas.")

    @staticmethod
    def modificar():
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(5*"-"+"MODIFICAR"+"-"*5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                piezaAux = GestorBBDD.buscarDatoPorClave(
                    "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                if piezaAux is not None:
                    GestionPieza.menuModificar(nombre, piezaAux)
        else:
            print("No hay piezas creadas.")

    @staticmethod
    def menuModificar(nombreOriginal, pieza):  # Metodo placeholder
        opcion = None
        while (opcion != "0"):
            cambio = False
            print("¿Que campo quieres modificar?")
            print("1.Nombre.\n2.Tipo de pieza.\n3.Armadura."
                  "\n4.Consumo de energia.\n5.Peso."
                  "\n6.Precio."
                  "\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    piezaAux = GestorBBDD.buscarDatoPorClave(
                        "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                    if piezaAux is None:
                        if Utiles.confirmacion("Seguro que quiere cambiar el nombre de la pieza: " + nombreOriginal + " a: " + nombre):
                            GestorBBDD.cascada(nombreOriginal, nombre)
                            GestorBBDD.borrarDato("Pieza_" + nombreOriginal)
                            piezaAux2 = {
                                "Pieza_" + nombre + "_Nombre": nombre,
                                "Pieza_" + nombre + "_TipoPieza": pieza["Pieza_" + nombreOriginal + "_TipoPieza"],
                                "Pieza_" + nombre + "_Armadura": pieza["Pieza_" + nombreOriginal + "_Armadura"],
                                "Pieza_" + nombre + "_ConsumoEnergia": pieza["Pieza_" + nombreOriginal + "_ConsumoEnergia"],
                                "Pieza_" + nombre + "_Peso": pieza["Pieza_" + nombreOriginal + "_Peso"],
                                "Pieza_" + nombre + "_Precio": pieza["Pieza_" + nombreOriginal + "_Precio"]
                            }
                            pieza = piezaAux2
                            cambio = True
                    else:
                        print("Ya existe una pieza con el mismo nombre.")
            elif (opcion == "2"):
                tipoPieza = GestionPieza.menuTipoPieza()
                if tipoPieza is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el tipo de pieza de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + tipoPieza):
                        pieza["Pieza_" + nombreOriginal + "_TipoPieza"] = tipoPieza
                        cambio = True
            elif (opcion == "3"):
                armadura = Utiles.check_numeros("valor de armadura", 25)
                if armadura is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar la armadura de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + armadura):
                        pieza["Pieza_" + nombreOriginal + "_Armadura"] = armadura
                        cambio = True
            elif (opcion == "4"):
                consumoEnergia = Utiles.check_numeros("valor de consumo de energia", 25)
                if consumoEnergia is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el consumo energetico de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + consumoEnergia):
                        pieza["Pieza_" + nombreOriginal + "_ConsumoEnergia"] = consumoEnergia
                        cambio = True
            elif (opcion == "5"):
                peso = Utiles.check_numeros("peso de la pieza", 25)
                if peso is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el peso de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + peso):
                        pieza["Pieza_" + nombreOriginal + "_Peso"] = peso
                        cambio = True
            elif (opcion == "6"):
                precio = Utiles.check_numeros("precio de la pieza", 25)
                if precio is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el precio de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + precio):
                        pieza["Pieza_" + nombreOriginal + "_Precio"] = precio
                        cambio = True
            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                return None
            else:
                print("Opcion no valida.")
            if cambio is True:
                GestorBBDD.insertarDato(pieza)

    @staticmethod
    def buscar():
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(5*"-"+"BUSCAR"+"-"*5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                datos = GestorBBDD.buscarDatoPorClave(
                    "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                if datos is not None:
                    print("\n[-" + datos["Pieza_" + nombre + "_Nombre"] + "-]")
                    print("  Tipo de pieza:" + datos["Pieza_" + nombre + "_TipoPieza"] + "  ")
                    print("  Armadura:" + datos["Pieza_" + nombre + "_Armadura"] + "  ")
                    print("  Consumo de energia:" + datos["Pieza_" + nombre + "_ConsumoEnergia"] + "  ")
                    print("  Peso:" + datos["Pieza_" + nombre + "_Peso"] + "  ")
                    print("  Precio:" + datos["Pieza_" + nombre + "_Precio"] + "$  ")
                    return datos
                else:
                    print("No se ha encontrado la pieza.")
                    return None
            else:
                return None
        else:
            print("No hay piezas creadas.")

    @staticmethod
    def mostrarTodos():
        if (GestorBBDD.mostrarTodosDatos("Arma_") != {}):
            print(5*"-"+"MOSTRAR TODOS"+"-"*5)
            datos = GestorBBDD.mostrarTodosDatos("Pieza_")
            for x in datos:
                print("\n[-" + datos[x][x + "_Nombre"] + "-]")
                print("  Tipo de pieza:" + datos[x][x + "_TipoPieza"] + "  ")
                print("  Armadura:" + datos[x][x + "_Armadura"] + "  ")
                print("  Consumo de energia:" + datos[x][x + "_ConsumoEnergia"] + "  ")
                print("  Peso:" + datos[x][x + "_Peso"] + "  ")
                print("  Precio:" + datos[x][x + "_Precio"] + "$  ")
        else:
            print("No hay piezas creadas.")