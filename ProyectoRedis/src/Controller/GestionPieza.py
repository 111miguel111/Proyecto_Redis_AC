from Controller import Utiles, iGestores
from Model import GestorBBDD


class GestionPieza(iGestores.iGestores):

    @staticmethod
    def alta():
        '''
        Metodo que da de alta una pieza en la base de datos
        '''
        #Se definen variables que se van a comprobar mas adelante
        nombre = None
        tipoPieza = None
        armadura = None
        consumoEnergia = None
        peso = None
        precio = None
        pieza=None

        print(Utiles.bcolors.Green+5*"-"+"ALTA"+"-"*5+Utiles.bcolors.White)
        #Se comprueba que el campo introducido es un campo valido y si lo es comprobamos si existe. Si no existe se continua
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            piezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + nombre)
            if piezaAux is None:
                tipoPieza = GestionPieza.menuTipoPieza()
            else:
                print("Ya existe una pieza con ese nombre.")
        # Se comprueba que el campo introducido es un campo valido y si lo es se continua
        if tipoPieza is not None:
            armadura = Utiles.check_numeros("valor de armadura", 25)
        # Se comprueba que el campo introducido es un campo valido y si lo es se continua
        if armadura is not None:
            consumoEnergia = Utiles.check_numeros("valor de consumo de energia", 25)
        # Se comprueba que el campo introducido es un campo valido y si lo es se continua
        if consumoEnergia is not None:
            peso = Utiles.check_numeros("peso de la pieza", 25)
        # Se comprueba que el campo introducido es un campo valido y si lo es se continua
        if peso is not None:
            precio = Utiles.check_numeros("precio de la pieza", 25)
        # Si todos los campos son correctos se crea un diccionario con ellos y se inserta en la base de datos
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
            print("Fallo en la creacion de la pieza.")

    @staticmethod
    def menuTipoPieza():
        '''
        Metodo para seleccionar el tipo de pieza que es la pieza a crear o modificar
        :return String con tipo de pieza o None si no se selecciona ninguno
        '''
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
            elif (opcion == None):
                return None
            else:
                print("Opcion no valida.")

    @staticmethod
    def baja():
        '''
        Metodo para borrar todos los campos de una pieza de la base de datos
        '''
        #Se buscan todos los datos de las piezas y si el diccionario que devuelve es vacio sale del metodo
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(Utiles.bcolors.Green+5*"-"+"BAJA"+"-"*5+Utiles.bcolors.White)
            #Se comprueba que el nombre introducido es correcto y luego se comprueba si existe esa pieza
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                piezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + nombre)
                if piezaAux is not None:
                    #Si ambas condiciones se cumplen se borra la pieza y se modifica en cascada en los AC a "Sin equipar"
                    if Utiles.confirmacion("¿Seguro que quiere eliminar esta pieza?") is True:
                        GestorBBDD.borrarDato("Pieza_" + nombre)
                        GestorBBDD.cascada(nombre, "Sin equipar")
                        print("Pieza eliminada.")
                    else:
                        print("Pieza no eliminada.")
                else:
                    print("Pieza no encontrada.")
        else:
            print("No hay piezas creadas.")

    @staticmethod
    def modificar():
        '''
        Metodo para modificar los campos de una pieza
        '''
        #Se mira si hay datos de tipo pieza y si los hay continua
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(Utiles.bcolors.Green+5*"-"+"MODIFICAR"+"-"*5+Utiles.bcolors.White)
            # Se comprueba que el nombre introducido es correcto y luego se comprueba si existe esa pieza
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                piezaAux = GestorBBDD.buscarDatoPorClave(
                    "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                if piezaAux is not None:
                    #Si no existe la pieza se llama al menu de la modificacion de piezas
                    GestionPieza.menuModificar(nombre, piezaAux)
                else:
                    print("Pieza no encontrada.")

        else:
            print("No hay piezas creadas.")

    @staticmethod
    def menuModificar(nombreOriginal, pieza):
        '''
        Metodo que gestiona la modificacion de las piezas
        :param nombreOriginal: String que contiene el nombre de la pieza antes de la modificacion
        :param pieza: Diccionario con los campos de la pieza a modificar
        '''
        #Se crea un bucle con distintas opciones con los campos a eliminar
        opcion = None
        while (opcion != "0"):
            cambio = False
            print("¿Que campo quieres modificar?")
            print(Utiles.bcolors.Cyan+"1.Nombre.\n2.Armadura."
                  "\n3.Consumo de energia.\n4.Peso."
                  "\n5.Precio."
                  "\n0.Salir."+Utiles.bcolors.White)
            opcion = Utiles.check_numerosMenu("Opcion", 25)
            #Modificar el nombre
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    piezaAux = GestorBBDD.buscarDatoPorClave(
                        "Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario
                    if piezaAux is None:
                        if Utiles.confirmacion("Seguro que quiere cambiar el nombre de la pieza: " + nombreOriginal + " a: " + nombre):
                            #Se modifica en cascada los datos del AC el nuevo nombre con el viejo y luego se borra el dato original
                            GestorBBDD.cascada(nombreOriginal, nombre)
                            GestorBBDD.borrarDato("Pieza_" + nombreOriginal)
                            #Ahora se inserta el dato con el nuevo nombre
                            piezaAux2 = {
                                "Pieza_" + nombre + "_Nombre": nombre,
                                "Pieza_" + nombre + "_TipoPieza": pieza["Pieza_" + nombreOriginal + "_TipoPieza"],
                                "Pieza_" + nombre + "_Armadura": pieza["Pieza_" + nombreOriginal + "_Armadura"],
                                "Pieza_" + nombre + "_ConsumoEnergia": pieza["Pieza_" + nombreOriginal + "_ConsumoEnergia"],
                                "Pieza_" + nombre + "_Peso": pieza["Pieza_" + nombreOriginal + "_Peso"],
                                "Pieza_" + nombre + "_Precio": pieza["Pieza_" + nombreOriginal + "_Precio"]
                            }
                            #Se actualizan las variables del metodo
                            pieza = piezaAux2
                            nombreOriginal=nombre
                            cambio = True
                    else:
                        print("Ya existe una pieza con el mismo nombre.")

            #Modificar armadura
            elif (opcion == "2"):
                armadura = Utiles.check_numeros("valor de armadura", 25)
                if armadura is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar la armadura de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + armadura):
                        pieza["Pieza_" + nombreOriginal + "_Armadura"] = armadura
                        cambio = True

            #Modificar consumo energetico
            elif (opcion == "3"):
                consumoEnergia = Utiles.check_numeros("valor de consumo de energia", 25)
                if consumoEnergia is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el consumo energetico de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + consumoEnergia):
                        pieza["Pieza_" + nombreOriginal + "_ConsumoEnergia"] = consumoEnergia
                        cambio = True

            #Modifica el peso
            elif (opcion == "4"):
                peso = Utiles.check_numeros("peso de la pieza", 25)
                if peso is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el peso de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + peso):
                        pieza["Pieza_" + nombreOriginal + "_Peso"] = peso
                        cambio = True

            #Modifica el precio
            elif (opcion == "5"):
                precio = Utiles.check_numeros("precio de la pieza", 25)
                if precio is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el precio de la pieza: " + pieza[
                        "Pieza_" + nombreOriginal + "_Nombre"] + " a: " + precio):
                        pieza["Pieza_" + nombreOriginal + "_Precio"] = precio
                        cambio = True

            #Salir del menu
            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                opcion = "0"
            else:
                print("Opcion no valida.")

            #Si se ha realizado un cambio se sobrescribe la pieza
            if cambio is True:
                GestorBBDD.insertarDato(pieza)
                print("Pieza modificada.")

    @staticmethod
    def buscar():
        '''
        Metodo para buscar una pieza y todos sus campos
        '''
        # Se comprueba si hay piezas y si las hay continua
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(Utiles.bcolors.Green+5*"-"+"BUSCAR"+"-"*5+Utiles.bcolors.White)
            #Se comprueba que el nombre es un campo valido y si lo es lo busca en la base de datos y lo imprime
            nombre = Utiles.check_campo("nombre", 25)

            if nombre is not None:
                datos = GestorBBDD.buscarDatoPorClave("Pieza_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario

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
        '''
        Metodo para mostrar todas las piezas
        '''
        #Se comprueba si hay piezas y si las hay busca todas las piezas y las imprime
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):
            print(Utiles.bcolors.Green+5*"-"+"MOSTRAR TODOS"+"-"*5+Utiles.bcolors.White)
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