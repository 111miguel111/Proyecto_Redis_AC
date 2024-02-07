from ProyectoRedis.src.Controller import Utiles, GestorBBDD, iGestores

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
            armaAux = GestorBBDD.buscarDato("Arma" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
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
                armaPrueba = {  # Aqui metemos en un diccionario los datos
                    "Arma"+str(nombre)+"Nombre": str(nombre),
                    "Arma"+str(nombre)+"TipoDamage": str(tipoDamage),
                    "Arma"+str(nombre)+"Dps": str(dps),
                    "Arma"+str(nombre)+"Rpm": str(rpm),
                    "Arma"+str(nombre)+"Municion": str(municion),
                    "Arma"+str(nombre)+"ArmaHombro": str(armaHombro),
                    "Arma"+str(nombre)+"Precio": str(precio)
                }
                GestorBBDD.insertarDato("Arma", armaPrueba)#Te mando un diccionario con las clave valor del arma---------------------------------------------------

    @staticmethod
    def baja():
        print("BAJA")

    @staticmethod
    def modificar():
        print("MODIFICAR")

    @staticmethod
    def buscar():
        print("BUSCAR")

    @staticmethod
    def mostrarTodos():
        print("MOSTRAR TODOS")
        datos = GestorBBDD.mostrarTodosDatos("Arma")# Te mando la categoria para que me devuelvas un diccionario con diccionarios que contengan los datos de una pieza
        for x in datos:
            print("\n[-" + datos[x]["*Nombre"] + "-]")
            print("  Tipo de damage:" + datos[x]["*TipoDamage"] + "  ")
            print("  Damage por segundo:" + datos[x]["*Dps"] + "  ")
            print("  Rondas por minuto:" + datos[x]["*Rpm"] + "  ")
            print("  Municion maxima:" + datos[x]["*Municion"] + "  ")
            print("  Puede ponerse en el hombro:" + datos[x]["*ArmaHombro"] + "  ")
            print("  Precio:" + datos[x]["*Precio"] + "$  ")
