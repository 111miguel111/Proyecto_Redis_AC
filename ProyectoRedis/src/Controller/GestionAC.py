from Controller import Utiles, iGestores
from Model import GestorBBDD


class GestionAC(iGestores.iGestores):
    @staticmethod
    def alta():
        '''
        Funcion encargada de dar de alta un AC pidiendo los nombres de las partes que lo componen
        '''
        if (GestionAC.confirmarStock("Pieza", "CABEZA") != {}
                and GestionAC.confirmarStock("Pieza", "TORSO") != {}
                and GestionAC.confirmarStock("Pieza", "BRAZOS") != {}
                and GestionAC.confirmarStock("Pieza", "PIERNAS") != {}
                and GestionAC.confirmarStock("Arma", "FALSE") != {}
                and GestionAC.confirmarStock("Arma", "irrelevante") != {}):
            nombre = None
            cabeza = None
            torso = None
            brazos = None
            piernas = None
            armaBDer = None
            armaBIzq = None
            armaHDer = None
            armaHIzq = None
            cuerpo = None

            print(Utiles.bcolors.Green+5 * "-" + "ALTA" + "-" * 5+Utiles.bcolors.White)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                cuerpoAux = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre)  #Nos aseguramos de que no exista un AC con el mismo nombre

                if cuerpoAux is None:
                    cont = 0
                    while cont < 5:
                        print("Cabezas disponibles:")
                        GestionAC.mostrarNombres("Pieza", "CABEZA")#Mostramos las piezas del tipo que pedimos
                        cabeza = Utiles.check_campo("introduzca el nombre de la cabeza del AC", 25)

                        if cabeza is not None:
                            cabezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + cabeza)#Nos aseguramos de que has metido el nombre de una pieza
                            if cabezaAux is None:
                                cabeza = None
                                print("No existe esa cabeza "+str(cont+1)+"/5\n")
                            else:
                                if cabezaAux["Pieza_" + cabeza + "_TipoPieza"] == "CABEZA":#Confirmamos de que la pieza introducida sea del tipo correcto
                                    cont = 5
                                else:
                                    cabeza = None
                                    print("No existe esa cabeza " + str(cont + 1) + "/5\n")
                        else:
                            cont = 5

                else:
                    print("Ya existe un AC con ese nombre.")

            if cabeza is not None:
                cont = 0
                while cont < 5:
                    print("Torsos disponibles:")
                    GestionAC.mostrarNombres("Pieza", "TORSO")#Mostramos las piezas del tipo que pedimos
                    torso = Utiles.check_campo("introduzca el nombre del torso del AC", 25)
                    if torso is not None:
                        torsoAux = GestorBBDD.buscarDatoPorClave("Pieza_" + torso)#Nos aseguramos de que has metido el nombre de una pieza
                        if torsoAux is None:
                            torso = None
                            print("No existe ese torso "+str(cont+1)+"/5\n")
                        else:
                            if torsoAux["Pieza_" + torso + "_TipoPieza"] == "TORSO":#Confirmamos de que la pieza introducida sea del tipo correcto
                                cont = 5
                            else:
                                torso = None
                                print("No existe ese torso " + str(cont + 1) + "/5\n")
                    else:
                        cont = 5

            if torso is not None:
                cont = 0
                while cont < 5:
                    print("Brazos disponibles:")
                    GestionAC.mostrarNombres("Pieza", "BRAZOS")#Mostramos las piezas del tipo que pedimos
                    brazos = Utiles.check_campo("Introduzca el nombre de los brazos del AC", 25)
                    if brazos is not None:
                        brazosAux = GestorBBDD.buscarDatoPorClave("Pieza_" + brazos)#Nos aseguramos de que has metido el nombre de una pieza
                        if brazosAux is None:
                            brazos = None
                            print("No existen esos brazos "+str(cont+1)+"/5\n")
                            cont += 1
                        else:
                            if brazosAux["Pieza_" + brazos + "_TipoPieza"] == "BRAZOS":#Confirmamos de que la pieza introducida sea del tipo correcto
                                cont = 5
                            else:
                                brazos = None
                                print("No existen esos brazos " + str(cont + 1) + "/5\n")
                    else:
                        cont = 5

            if brazos is not None:
                cont = 0
                while cont < 5:
                    print("Piernas disponibles:")
                    GestionAC.mostrarNombres("Pieza", "PIERNAS")#Mostramos las piezas del tipo que pedimos
                    piernas = Utiles.check_campo("Introduzca el nombre de las piernas del AC", 25)
                    if piernas is not None:
                        piernasAux = GestorBBDD.buscarDatoPorClave("Pieza_" + piernas)#Nos aseguramos de que has metido el nombre de una pieza
                        if piernasAux is None:
                            piernas = None
                            print("No existen esas piernas "+str(cont+1)+"/5\n")
                        else:
                            if piernasAux["Pieza_" + piernas + "_TipoPieza"] == "PIERNAS":#Confirmamos de que la pieza introducida sea del tipo correcto
                                cont = 5
                            else:
                                piernas = None
                                print("No existen esas piernas " + str(cont + 1) + "/5\n")
                    else:
                        cont = 5

            if piernas is not None:
                cont = 0
                while cont < 5:
                    print("Armas para brazo disponibles:")
                    GestionAC.mostrarNombres("Arma", "FALSE")#Mostramos las armas del tipo que pedimos
                    armaBDer = Utiles.check_campo("Introduzca el nombre del arma del brazo derecho del AC", 25)
                    if armaBDer is not None:
                        armaBDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBDer)#Nos aseguramos de que has metido el nombre de un arma
                        if armaBDerAux is None:
                            armaBDer = None
                            print("No existe ese arma del brazo derecho "+str(cont+1)+"/5\n")
                        else:
                            if armaBDerAux["Arma_" + armaBDer + "_ArmaHombro"] == "FALSE":#Confirmamos de que el arma introducida sea del tipo correcto
                                cont = 5
                            else:
                                armaBDer = None
                                print("No existe ese arma de brazo " + str(cont + 1) + "/5\n")
                    else:
                        cont = 5

            if armaBDer is not None:
                cont = 0
                while cont < 5:
                    print("Armas para brazo disponibles:")
                    GestionAC.mostrarNombres("Arma", "FALSE")#Mostramos las armas del tipo que pedimos
                    armaBIzq = Utiles.check_campo("Introduzca el nombre del arma del brazo izquierdo del AC", 25)
                    if armaBIzq is not None:
                        armaBIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBIzq)#Nos aseguramos de que has metido el nombre de un arma
                        if armaBIzqAux is None:
                            armaBIzq = None
                            print("No existe ese arma del brazo izquierdo "+str(cont+1)+"/5\n")
                        else:
                            if armaBIzqAux["Arma_" + armaBIzq + "_ArmaHombro"] == "FALSE":#Confirmamos de que el arma introducida sea del tipo correcto
                                cont = 5
                            else:
                                armaBIzq = None
                                print("No existe ese arma de brazo " + str(cont + 1) + "/5\n")
                    else:
                        cont = 5

            if armaBIzq is not None:
                cont = 0
                while cont < 5:
                    print("Armas para hombros disponibles:")
                    GestionAC.mostrarNombres("Arma", "irrelevante")#Mostramos las armas del tipo que pedimos
                    armaHDer = Utiles.check_campo("nombre del arma del hombro derecho del AC", 25)
                    if armaHDer is not None:
                        armaHDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHDer)#Nos aseguramos de que has metido el nombre de un arma
                        if armaHDerAux is None:
                            armaHDer = None
                            print("No existe ese arma del hombro derecho "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if armaHDer is not None:
                cont = 0
                while cont < 5:
                    print("Armas para hombros disponibles:")
                    GestionAC.mostrarNombres("Arma", "irrelevante")#Mostramos las armas del tipo que pedimos
                    armaHIzq = Utiles.check_campo("nombre del arma del hombro izquierdo del AC", 25)
                    if armaHIzq is not None:
                        armaHIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHIzq)
                        if armaHIzqAux is None:
                            armaHIzq = None
                            print("No existe ese arma del hombro izquierdo "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if armaHIzq is not None:
                cuerpo = {  # Aqui metemos en un diccionario los datos
                    "AC_" + str(nombre) + "_Nombre": str(nombre),
                    "AC_" + str(nombre) + "_Cabeza": str(cabeza),
                    "AC_" + str(nombre) + "_Torso": str(torso),
                    "AC_" + str(nombre) + "_Brazos": str(brazos),
                    "AC_" + str(nombre) + "_Piernas": str(piernas),
                    "AC_" + str(nombre) + "_ArmaBDer": str(armaBDer),
                    "AC_" + str(nombre) + "_ArmaBIzq": str(armaBIzq),
                    "AC_" + str(nombre) + "_ArmaHDer": str(armaHDer),
                    "AC_" + str(nombre) + "_ArmaHIzq": str(armaHIzq)
                }
                GestorBBDD.insertarDato(
                    cuerpo)  # Insertamos el nuevo AC en la base de datos
            if cuerpo is not None:
                print("AC creado.")
            else:
                print("Fallo en la creacion del AC.")
        else:
            print("No hay suficientes piezas para montar un AC.")

    @staticmethod
    def mostrarNombres(tipoDato, campo):
        '''
        Funcion encargada de mostrar solo nos nombres de piezas, armas o Acs
        tipoDato La categoria que queremos mostrar(Pieza,Arma,AC)
        campo El campo que queremos tener en cuenta es decir que la pieza sea una cabeza, torso,etc. o que el arma no sea de hombro, etc.
        '''
        datos = GestorBBDD.mostrarTodosDatos(tipoDato + "_")#Obtenemos todos los datos de la categoria deseada
        cont = 0
        if (tipoDato == "Pieza"):
            for x in datos:
                if (datos[x][x + "_TipoPieza"] == campo):#Filtramos los datos para mostrar solo los que nos interesa
                    print(Utiles.bcolors.Cyan+"[-" + datos[x][x + "_Nombre"] + "-]"+Utiles.bcolors.White, end="")
                    cont += 1
                    if (cont == 3):
                        cont = 0
                        print("\n")
        elif (tipoDato == "Arma"):
            if (campo == "irrelevante"):#Filtramos los datos para mostrar solo los que nos interesa
                for x in datos:
                    print(Utiles.bcolors.Cyan+"[-" + datos[x][x + "_Nombre"] + "-]"+Utiles.bcolors.White, end="")
                    cont += 1
                    if (cont == 3):
                        cont = 0
                        print("\n")
            else:
                for x in datos:
                    if (datos[x][x + "_ArmaHombro"] == campo):#Filtramos los datos para mostrar solo los que nos interesa
                        print(Utiles.bcolors.Cyan+"[-" + datos[x][x + "_Nombre"] + "-]"+Utiles.bcolors.White, end="")
                        cont += 1
                        if (cont == 3):
                            cont = 0
                            print("\n")
        elif (tipoDato == "AC"):
            for x in datos:
                print(Utiles.bcolors.Cyan+"[-" + datos[x][x + "_Nombre"] + "-]"+Utiles.bcolors.White, end="")
                cont += 1
                if (cont == 3):
                    cont = 0
                    print("\n")
        print("")

    @staticmethod
    def confirmarStock(tipoDato, campo):
        '''
        Funcion que se encarga de comprobar que haya piezas o armas de una categoria en concreto con el objetivo de verificar que hay suficientes piezas para crear un AC
        tipoDato La categoria que queremos comprobar(Pieza,Arma)
        campo El campo que queremos tener en cuenta es decir que la pieza sea una cabeza, torso,etc. o que el arma no sea de hombro, etc.
        return Devolvera las piezas que encuentre de la categoria con el campo que le indiquemos
        '''
        datos = GestorBBDD.mostrarTodosDatos(tipoDato + "_")#Obtenemos todos los datos de la categoria deseada
        datosAux = {}
        if (tipoDato == "Pieza"):
            for x in datos:
                if (datos[x][x + "_TipoPieza"] == campo):#Filtramos los datos para mostrar solo los que nos interesa
                    datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            return datosAux
        elif (tipoDato == "Arma"):
            if (campo == "irrelevante"):#Filtramos los datos para mostrar solo los que nos interesa
                for x in datos:
                    datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            else:
                for x in datos:
                    if (datos[x][x + "_ArmaHombro"] == campo):#Filtramos los datos para mostrar solo los que nos interesa
                        datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            return datosAux

    @staticmethod
    def baja():
        '''
        Funcion encargada de eliminar un AC de la base de datos
        '''
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):#Confirmamos que haya al menus un AC
            print(Utiles.bcolors.Green+5 * "-" + "BAJA" + "-" * 5+Utiles.bcolors.White)
            print("ACs disponibles:")
            GestionAC.mostrarNombres("AC", "")#Mostramos los nombres de todos los AC
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                acAux = GestorBBDD.buscarDatoPorClave("AC_" + nombre)#Nos aseguramos que el nombre que has puesto es el de un AC
                if acAux is not None:
                    if Utiles.confirmacion("¿Seguro que quiere eliminar este AC?") is True:
                        GestorBBDD.borrarDato("AC_" + nombre)
                        print("AC eliminado.")
                else:
                    print("No se ha encontrado ese AC.")
        else:
            print("No hay ACs creados.")

    @staticmethod
    def modificar():
        '''
        Funcion encargada de pedir los datos necesarios para realizar la modificacion de un AC
        '''
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):#Confirmamos que haya al menus un AC
            print(Utiles.bcolors.Green+5 * "-" + "MODIFICAR" + "-" * 5+Utiles.bcolors.White)
            print("ACs disponibles:")
            GestionAC.mostrarNombres("AC", "")#Mostramos los AC disponibles
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                acAux = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre) #Comprobamos que el nombre que has puesto sea una palabra
                if acAux is not None:
                    GestionAC.menuModificar(nombre, acAux)#Llamamos al menu que se va a encargar de modificar el AC
                else:
                    print("No se ha encontrado ese AC")
        else:
            print("No hay ACs creados.")

    @staticmethod
    def menuModificar(nombreOriginal, ac):
        '''
        Funcion encargada de preguntar que quieres modificar y tras pedir los datos y confirmar que estos son validos realizar el cambio
        nombreOriginal Variable con el nombre original del AC para poder buscar los datos de este mas facilmente (el nombre es parte de la clave)
        ac Un diccionario que contiene los datos del AC
        '''
        opcion = None
        while (opcion != "0"):
            cambio = False
            print("¿Que campo quieres modificar?")
            print(Utiles.bcolors.Cyan+"1.Nombre.\n2.Cabeza.\n3.Torso."
                  "\n4.Brazos.\n5.Piernas.\n6.Arma brazo derecho."
                  "\n7.Arma Brazo Izquierdo.\n8.Arma Hombro Derecho."
                  "\n9.Arma Hombro Izquierdo.\n0.Salir."+Utiles.bcolors.White)
            opcion = Utiles.check_numerosMenu("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    acAux = GestorBBDD.buscarDatoPorClave(
                        "AC_" + nombre)  #Nos aseguramos de que el nombre introducido no lo tenga ya otro AC
                    if acAux is None:
                        if Utiles.confirmacion(
                                "Seguro que quiere cambiar el nombre del AC: " + nombreOriginal + " a: " + nombre):
                            GestorBBDD.borrarDato("AC_" + nombreOriginal)#Borramos los datos de AC con el nombre antiguo de la base de datos
                            #Creamos un nuevo AC que tenga el nuevo nombre(es parte de la clave) pero los mismos datos que el AC original(menos el nombre)
                            acAux2 = {
                                "AC_" + nombre + "_Nombre": nombre,
                                "AC_" + nombre + "_Cabeza": ac["AC_" + nombreOriginal + "_Cabeza"],
                                "AC_" + nombre + "_Torso": ac["AC_" + nombreOriginal + "_Torso"],
                                "AC_" + nombre + "_Brazos": ac["AC_" + nombreOriginal + "_Brazos"],
                                "AC_" + nombre + "_Piernas": ac["AC_" + nombreOriginal + "_Piernas"],
                                "AC_" + nombre + "_ArmaBDer": ac["AC_" + nombreOriginal + "_ArmaBDer"],
                                "AC_" + nombre + "_ArmaBIzq": ac["AC_" + nombreOriginal + "_ArmaBIzq"],
                                "AC_" + nombre + "_ArmaHDer": ac["AC_" + nombreOriginal + "_ArmaHDer"],
                                "AC_" + nombre + "_ArmaHIzq": ac["AC_" + nombreOriginal + "_ArmaHIzq"]
                            }
                            #Actualizamos el AC con el que estamos trabajando y el nuevo nombre original del AC
                            ac = acAux2
                            nombreOriginal = nombre
                            cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                    else:
                        print("Ya existe un AC con el mismo nombre.\n")

            elif (opcion == "2"):
                GestionAC.mostrarNombres("Pieza", "CABEZA")
                cabeza = Utiles.check_campo("cabeza", 25)

                if cabeza is not None:
                    cabezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + cabeza)
                    if cabezaAux is not None:
                        if cabezaAux["Pieza_" + cabeza + "_TipoPieza"] == "CABEZA":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar la cabeza del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + cabeza):
                                ac["AC_" + nombreOriginal + "_Cabeza"] = cabeza
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se ha encontrado esa cabeza\n")
                    else:
                        print("No se ha encontrado esa cabeza\n")

            elif (opcion == "3"):
                GestionAC.mostrarNombres("Pieza", "TORSO")
                torso = Utiles.check_campo("torso", 25)

                if torso is not None:
                    torsoAux = GestorBBDD.buscarDatoPorClave("Pieza_" + torso)
                    if torsoAux is not None:
                        if torsoAux["Pieza_" + torso + "_TipoPieza"] == "TORSO":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar el torso del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + torso):
                                ac["AC_" + nombreOriginal + "_Torso"] = torso
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se ha encontrado ese torso\n")

                    else:
                        print("No se ha encontrado ese torso\n")

            elif (opcion == "4"):
                GestionAC.mostrarNombres("Pieza", "BRAZOS")
                brazos = Utiles.check_campo("brazos", 25)

                if brazos is not None:
                    brazosAux = GestorBBDD.buscarDatoPorClave("Pieza_" + brazos)
                    if brazosAux is not None:
                        if brazosAux["Pieza_" + brazos + "_TipoPieza"] == "BRAZOS":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar la brazos del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + brazos):
                                ac["AC_" + nombreOriginal + "_Brazos"] = brazos
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se han encontrado esos brazos\n")
                    else:
                        print("No se han encontrado esos brazos\n")

            elif (opcion == "5"):
                GestionAC.mostrarNombres("Pieza", "PIERNAS")
                piernas = Utiles.check_campo("piernas", 25)

                if piernas is not None:
                    piernasAux = GestorBBDD.buscarDatoPorClave("Pieza_" + piernas)
                    if piernasAux is not None:
                        if piernasAux["Pieza_" + piernas + "_TipoPieza"] == "PIERNAS":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar la piernas del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + piernas):
                                ac["AC_" + nombreOriginal + "_Piernas"] = piernas
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se han encontrado esas piernas\n")
                    else:
                        print("No se han encontrado esas piernas\n")

            elif (opcion == "6"):
                GestionAC.mostrarNombres("Arma", "FALSE")
                armaBDer = Utiles.check_campo("armaBDer", 25)

                if armaBDer is not None:
                    armaBDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBDer)
                    if armaBDerAux is not None:
                        if armaBDerAux["Arma_" + armaBDer + "_ArmaHombro"] == "FALSE":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar la armaBDer del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaBDer):
                                ac["AC_" + nombreOriginal + "_ArmaBDer"] = armaBDer
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se ha encontrado ese arma del brazo derecho\n")
                    else:
                        print("No se ha encontrado ese arma del brazo derecho\n")

            elif (opcion == "7"):
                GestionAC.mostrarNombres("Arma", "FALSE")
                armaBIzq = Utiles.check_campo("armaBIzq", 25)

                if armaBIzq is not None:
                    armaBIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBIzq)
                    if armaBIzqAux is not None:
                        if armaBIzqAux["Arma_" + armaBIzq + "_ArmaHombro"] == "FALSE":#Confirmamos que el nombre dado referencie el tipo correcto
                            if Utiles.confirmacion("Seguro que quiere cambiar la armaBIzq del AC: " + ac[
                                "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaBIzq):
                                ac["AC_" + nombreOriginal + "_ArmaBIzq"] = armaBIzq
                                cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                        else:
                            print("No se ha encontrado ese arma del brazo izquierdo\n")
                    else:
                        print("No se ha encontrado ese arma del brazo izquierdo\n")

            elif (opcion == "8"):
                GestionAC.mostrarNombres("Arma", "irrelevante")
                armaHDer = Utiles.check_campo("armaHDer", 25)

                if armaHDer is not None:
                    armaHDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHDer)#Confirmamos que el nombre dado es un arma
                    if armaHDerAux is not None:
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaHDer del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaHDer):
                            ac["AC_" + nombreOriginal + "_ArmaHDer"] = armaHDer
                            cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                    else:
                        print("No se ha encontrado ese arma del hombro derecho\n")

            elif (opcion == "9"):
                GestionAC.mostrarNombres("Arma", "irrelevante")
                armaHIzq = Utiles.check_campo("armaHIzq", 25)

                if armaHIzq is not None:
                    armaHIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHIzq)#Confirmamos que el nombre dado es un arma
                    if armaHIzqAux is not None:
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaHIzq del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaHIzq):
                            ac["AC_" + nombreOriginal + "_ArmaHIzq"] = armaHIzq
                            cambio = True#Informamos al programa con esta variable de que se ha realizado un cambio en el AC
                    else:
                        print("No se ha encontrado ese arma del hombro izquierdo\n")

            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                return None
            else:
                print("Opcion no valida.")

            if cambio is True:#Si cambio esta en true significa que el AC a sido modificado po lo que lo actualizaremos en la base de datos
                GestorBBDD.insertarDato(ac)
                print("AC modificado.")

    @staticmethod
    def buscar():
        '''
        Funcion encargada de buscar y mostrar un AC
        '''
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):#Confirmamos que haya al menus un AC
            print(Utiles.bcolors.Green+5 * "-" + "BUSCAR" + "-" * 5+Utiles.bcolors.White)
            print("ACs disponibles:")
            GestionAC.mostrarNombres("AC", "")#Mostramos los nombres de los AC disponibles
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                datos = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre)
                if datos is not None:
                    print("\n[-" + datos["AC_" + nombre + "_Nombre"] + "-]")
                    print("  Cabeza:" + datos["AC_" + nombre + "_Cabeza"] + "  ")
                    print("  Torso:" + datos["AC_" + nombre + "_Torso"] + "  ")
                    print("  Brazos:" + datos["AC_" + nombre + "_Brazos"] + "  ")
                    print("  Piernas:" + datos["AC_" + nombre + "_Piernas"] + "  ")
                    print("  Arma brazo derecho:" + datos["AC_" + nombre + "_ArmaBDer"] + "  ")
                    print("  Arma brazo izquierdo:" + datos["AC_" + nombre + "_ArmaBIzq"] + "  ")
                    print("  Arma hombro derecho:" + datos["AC_" + nombre + "_ArmaHDer"] + "  ")
                    print("  Arma hombro izquierdo:" + datos["AC_" + nombre + "_ArmaHIzq"] + "  ")

                    print(Utiles.bcolors.Green +

                          "\n                                         *(                 " +
                          "\n                    /  *,,               (#(                " +
                          "\n                   (#,....#  .       *   /%@(               " +
                          "\n                ,*%(,//%" + Utiles.bcolors.Purple + "------------------------------------HD Arma:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_ArmaHDer"] + Utiles.bcolors.Green +
                          "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
                          "\n              (/#& ,(,%#%#&#../(,//((.(#% %#" + Utiles.bcolors.Purple + "----------------HI Arma:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_ArmaHIzq"] + Utiles.bcolors.Green +
                          "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
                          "\n                  %&(#&   @%,,%///" + Utiles.bcolors.Purple + "--------------------------Cabeza:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_Cabeza"] + Utiles.bcolors.Green +
                          "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
                          "\n                (&@/%%    &*&#@@%%#&" + Utiles.bcolors.Purple + "------------------------Torso:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_Torso"] + Utiles.bcolors.Green +
                          "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
                          "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##" + Utiles.bcolors.Purple + "---------Brazos:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_Brazos"] + Utiles.bcolors.Green +
                          "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
                          "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
                          "\n          (.%((%      *&(%&&          &&#&&     ##" + Utiles.bcolors.Purple + "----------BI Arma:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_ArmaBIzq"] + Utiles.bcolors.Green +
                          "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
                          "\n          %%" + Utiles.bcolors.Purple + "------------------------------------------------BD Arma:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_ArmaBDer"] + Utiles.bcolors.Green +
                          "\n        ,/%(       #((#&%(%            ##&#%#((             " +
                          "\n       ,/&#       /(,/%#%%%            %&#%/" + Utiles.bcolors.Purple + "----------------Piernas:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_Piernas"] + Utiles.bcolors.Green +
                          "\n      ..%         (.*%&%                 %%,*..             " +
                          "\n     ,,%        #*,(#&&                    %#* ./           " + Utiles.bcolors.Purple + "NOMBRE:" + Utiles.bcolors.Cyan +
                          datos[
                              "AC_" + nombre + "_Nombre"] + Utiles.bcolors.Green +
                          "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + Utiles.bcolors.Purple + "ARMADURA: " + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "Armadura")) + Utiles.bcolors.Green +
                          "\n             %&@&&#%%%%                    *&&&&(@@/        " + Utiles.bcolors.Purple + "CONSUMO ENERGETICO:" + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "ConsumoEnergia")) + Utiles.bcolors.Green +
                          "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + Utiles.bcolors.Purple + "PESO:" + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "Peso")) + Utiles.bcolors.Green +
                          "\n         ,#%###                                 &&&%&(      " + Utiles.bcolors.Purple + "DPS:" + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "Dps")) + Utiles.bcolors.Green +
                          "\n                                                    ,,      " + Utiles.bcolors.Purple + "RPM:" + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "Rpm")) + Utiles.bcolors.Green +
                          "\n   =======================================================  " + Utiles.bcolors.Purple + "PRECIO:" + Utiles.bcolors.Cyan + str(
                        datoAC(datos["AC_" + nombre + "_Nombre"], "Precio")) + "$\n"
                          + Utiles.bcolors.White)
                else:
                    print("No se ha encontrado ese AC.")
        else:
            print("No hay ACs creados.")

    @staticmethod
    def mostrarTodos():
        '''
        Funcion encargada de mostrar los datos de todos los AC
        '''
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):#Confirmamos que haya al menus un AC
            print(Utiles.bcolors.Green+5 * "-" + "MOSTRAR TODOS" + "-" * 5+Utiles.bcolors.White)
            datos = GestorBBDD.mostrarTodosDatos(
                "AC_")
            for x in datos:
                print("\n[-" + datos[x][x + "_Nombre"] + "-]")
                print("  Cabeza:" + datos[x][x + "_Cabeza"] + "  ")
                print("  Torso:" + datos[x][x + "_Torso"] + "  ")
                print("  Brazos:" + datos[x][x + "_Brazos"] + "  ")
                print("  Piernas:" + datos[x][x + "_Piernas"] + "  ")
                print("  Arma brazo derecho:" + datos[x][x + "_ArmaBDer"] + "  ")
                print("  Arma brazo izquierdo:" + datos[x][x + "_ArmaBIzq"] + "  ")
                print("  Arma hombro derecho:" + datos[x][x + "_ArmaHDer"] + "  ")
                print("  Arma hombro izquierdo:" + datos[x][x + "_ArmaHIzq"] + "  ")

                print(Utiles.bcolors.Green +

                      "\n                                         *(                 " +
                      "\n                    /  *,,               (#(                " +
                      "\n                   (#,....#  .       *   /%@(               " +
                      "\n                ,*%(,//%" + Utiles.bcolors.Purple + "------------------------------------HD Arma:" + Utiles.bcolors.Cyan +
                      datos[x][
                          x + "_ArmaHDer"] + Utiles.bcolors.Green +
                      "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
                      "\n              (/#& ,(,%#%#&#../(,//((.(#% %#" + Utiles.bcolors.Purple + "----------------HI Arma:" + Utiles.bcolors.Cyan +
                      datos[x][
                          x + "_ArmaHIzq"] + Utiles.bcolors.Green +
                      "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
                      "\n                  %&(#&   @%,,%///" + Utiles.bcolors.Purple + "--------------------------Cabeza:" + Utiles.bcolors.Cyan +
                      datos[x][x + "_Cabeza"] + Utiles.bcolors.Green +
                      "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
                      "\n                (&@/%%    &*&#@@%%#&" + Utiles.bcolors.Purple + "------------------------Torso:" + Utiles.bcolors.Cyan +
                      datos[x][x + "_Torso"] + Utiles.bcolors.Green +
                      "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
                      "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##" + Utiles.bcolors.Purple + "---------Brazos:" + Utiles.bcolors.Cyan +
                      datos[x][x + "_Brazos"] + Utiles.bcolors.Green +
                      "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
                      "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
                      "\n          (.%((%      *&(%&&          &&#&&     ##" + Utiles.bcolors.Purple + "----------BI Arma:" + Utiles.bcolors.Cyan +
                      datos[x][
                          x + "_ArmaBIzq"] + Utiles.bcolors.Green +
                      "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
                      "\n          %%" + Utiles.bcolors.Purple + "------------------------------------------------BD Arma:" + Utiles.bcolors.Cyan +
                      datos[x][
                          x + "_ArmaBDer"] + Utiles.bcolors.Green +
                      "\n        ,/%(       #((#&%(%            ##&#%#((             " +
                      "\n       ,/&#       /(,/%#%%%            %&#%/" + Utiles.bcolors.Purple + "----------------Piernas:" + Utiles.bcolors.Cyan +
                      datos[x][x + "_Piernas"] + Utiles.bcolors.Green +
                      "\n      ..%         (.*%&%                 %%,*..             " +
                      "\n     ,,%        #*,(#&&                    %#* ./           " + Utiles.bcolors.Purple + "NOMBRE:" + Utiles.bcolors.Cyan +
                      datos[x][
                          x + "_Nombre"] + Utiles.bcolors.Green +
                      "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + Utiles.bcolors.Purple + "ARMADURA: " + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "Armadura")) + Utiles.bcolors.Green +
                      "\n             %&@&&#%%%%                    *&&&&(@@/        " + Utiles.bcolors.Purple + "CONSUMO ENERGETICO:" + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "ConsumoEnergia")) + Utiles.bcolors.Green +
                      "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + Utiles.bcolors.Purple + "PESO:" + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "Peso")) + Utiles.bcolors.Green +
                      "\n         ,#%###                                 &&&%&(      " + Utiles.bcolors.Purple + "DPS:" + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "Dps")) + Utiles.bcolors.Green +
                      "\n                                                    ,,      " + Utiles.bcolors.Purple + "RPM:" + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "Rpm")) + Utiles.bcolors.Green +
                      "\n   =======================================================  " + Utiles.bcolors.Purple + "PRECIO:" + Utiles.bcolors.Cyan + str(
                    datoAC(datos[x][x + "_Nombre"], "Precio")) + "$"
                      + Utiles.bcolors.White)
                print("")
        else:
            print("No hay ACs creados.")


def datoAC(nombreAC, tipoDato):
    '''
    Esta clase se encarga de devolver la suma de valores numericos del mecha
    ac: diccionario del mecha
    tipoDato: String del tipo de dato del que se quieren obtener datos
    nombreAC: Nombre del AC del que se quiere saber los datos
    '''

    # Se comprueba si los datos a buscar son de una pieza
    if tipoDato == "Armadura" or tipoDato == "ConsumoEnergia" or tipoDato == "Peso":
        # Se define que se quieren piezas
        tipoComponente = "Pieza_"
        # Se crea una lista con los campos a comprobar de la pieza
        listaCampos = ["_Cabeza", "_Torso", "_Brazos", "_Piernas"]
        # Se calcula el valor de la suma de la estadistica
        valor = GestorBBDD.sumaDatosAC(listaCampos, tipoComponente, nombreAC, tipoDato)

    # Se comprueba si los datos son de las armas
    elif tipoDato == "Dps" or tipoDato == "Rpm":
        # Se define que se quieren armas
        tipoComponente = "Arma_"
        # Se crea una lista con los campos a comprobar del arma
        listaCampos = ["_ArmaBDer", "_ArmaBIzq", "_ArmaHDer", "_ArmaHIzq"]
        # Se calcula el valor de la suma de la estadistica
        valor = GestorBBDD.sumaDatosAC(listaCampos, tipoComponente, nombreAC, tipoDato)

    # Se comprueba si el dato es el precio
    elif tipoDato == "Precio":
        # Se define que se quieren piezas
        tipoComponente = "Pieza_"
        # Se crea una lista con los campos a comprobar
        listaCampos = ["_Cabeza", "_Torso", "_Brazos", "_Piernas"]
        # Se calcula el valor de la suma de la estadistica
        valor = GestorBBDD.sumaDatosAC(listaCampos, tipoComponente, nombreAC, tipoDato)

        # Se define que se quieren armas
        tipoComponente = "Arma_"
        # Se crea una lista con los campos a comprobar del arma
        listaCampos = ["_ArmaBDer", "_ArmaBIzq", "_ArmaHDer", "_ArmaHIzq"]
        # Se calcula el valor de la suma de la estadistica
        valor += GestorBBDD.sumaDatosAC(listaCampos, tipoComponente, nombreAC, tipoDato)

    else:
        # Si no es ningun valor conocido devuelve None
        valor = None

    return valor
