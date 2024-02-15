from ProyectoRedis.src.Controller import Utiles, iGestores
from ProyectoRedis.src.Model import GestorBBDD


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

            print(5 * "-" + "ALTA" + "-" * 5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                cuerpoAux = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------

                if cuerpoAux is None:
                    cont = 0
                    while cont < 5:
                        print("Cabezas disponibles:")
                        GestionAC.mostrarNombres("Pieza", "CABEZA")
                        cabeza = Utiles.check_campo("introduzca el nombre de la cabeza del AC", 25)

                        if cabeza is not None:
                            cabezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + cabeza)
                            if cabezaAux is None:
                                cabeza = None
                                print("No existe esa cabeza "+str(cont+1)+"/5\n")
                            else:
                                cont = 5
                            cont += 1
                        else:
                            cont = 5

                else:
                    print("Ya existe un AC con ese nombre.")

            if cabeza is not None:
                cont = 0
                while cont < 5:
                    print("Torsos disponibles:")
                    GestionAC.mostrarNombres("Pieza", "TORSO")
                    torso = Utiles.check_campo("introduzca el nombre del torso del AC", 25)
                    if torso is not None:
                        torsoAux = GestorBBDD.buscarDatoPorClave("Pieza_" + torso)
                        if torsoAux is None:
                            torso = None
                            print("No existe ese torso "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if torso is not None:
                cont = 0
                while cont < 5:
                    print("Brazos disponibles:")
                    GestionAC.mostrarNombres("Pieza", "BRAZOS")
                    brazos = Utiles.check_campo("Introduzca el nombre de los brazos del AC", 25)
                    if brazos is not None:
                        brazosAux = GestorBBDD.buscarDatoPorClave("Pieza_" + brazos)
                        if brazosAux is None:
                            brazos = None
                            print("No existen esos brazos "+str(cont+1)+"/5\n")
                            cont += 1
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if brazos is not None:
                cont = 0
                while cont < 5:
                    print("Piernas disponibles:")
                    GestionAC.mostrarNombres("Pieza", "PIERNAS")
                    piernas = Utiles.check_campo("Introduzca el nombre de las piernas del AC", 25)
                    if piernas is not None:
                        piernasAux = GestorBBDD.buscarDatoPorClave("Pieza_" + piernas)
                        if piernasAux is None:
                            piernas = None
                            print("No existen esas piernas "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if piernas is not None:
                cont = 0
                while cont < 5:
                    print("Armas para brazo disponibles:")
                    GestionAC.mostrarNombres("Arma", "False")
                    armaBDer = Utiles.check_campo("Introduzca el nombre del arma del brazo derecho del AC", 25)
                    if armaBDer is not None:
                        armaBDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBDer)
                        if armaBDerAux is None:
                            armaBDer = None
                            print("No existe ese arma del brazo derecho "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if armaBDer is not None:
                cont = 0
                while cont < 5:
                    print("Armas para brazo disponibles:")
                    GestionAC.mostrarNombres("Arma", "False")
                    armaBIzq = Utiles.check_campo("Introduzca el nombre del arma del brazo izquierdo del AC", 25)
                    if armaBIzq is not None:
                        armaBIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBIzq)
                        if armaBIzqAux is None:
                            armaBIzq = None
                            print("No existe ese arma del brazo izquierdo "+str(cont+1)+"/5\n")
                        else:
                            cont = 5
                        cont += 1
                    else:
                        cont = 5

            if armaBIzq is not None:
                cont = 0
                while cont < 5:
                    print("Armas para  disponibles:")
                    GestionAC.mostrarNombres("Arma", "irrelevante")
                    armaHDer = Utiles.check_campo("nombre del arma del hombro derecho del AC", 25)
                    if armaHDer is not None:
                        armaHDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHDer)
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
                    GestionAC.mostrarNombres("Arma", "irrelevante")
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
                    cuerpo)  # Te mando un diccionario con las clave valor del arma---------------------------------------------------
            if cuerpo is not None:
                print("AC creado.")
            else:
                print("Fallo en la creacion del AC.")
        else:
            print("No hay suficientes piezas para montar un AC.")

    @staticmethod
    def mostrarNombres(tipoDato, campo):
        datos = GestorBBDD.mostrarTodosDatos(tipoDato + "_")
        cont = 0
        if (tipoDato == "Pieza"):
            for x in datos:
                if (datos[x][x + "_TipoPieza"] == campo):
                    print("[-" + datos[x][x + "_Nombre"] + "-]", end="")
                    cont += 1
                    if (cont == 3):
                        cont = 0
                        print("\n")
        elif (tipoDato == "Arma"):
            if (campo == "irrelevante"):
                for x in datos:
                    print("[-" + datos[x][x + "_Nombre"] + "-]", end="")
                    cont += 1
                    if (cont == 3):
                        cont = 0
                        print("\n")
            else:
                for x in datos:
                    if (datos[x][x + "_ArmaHombro"] == campo):
                        print("[-" + datos[x][x + "_Nombre"] + "-]", end="")
                        cont += 1
                        if (cont == 3):
                            cont = 0
                            print("\n")
        print("")

    @staticmethod
    def confirmarStock(tipoDato, campo):
        datos = GestorBBDD.mostrarTodosDatos(tipoDato + "_")
        datosAux = {}
        if (tipoDato == "Pieza"):
            for x in datos:
                if (datos[x][x + "_TipoPieza"] == campo):
                    datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            return datosAux
        elif (tipoDato == "Arma"):
            if (campo == "irrelevante"):
                for x in datos:
                    datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            else:
                for x in datos:
                    if (datos[x][x + "_ArmaHombro"] == campo):
                        datosAux[x + "_Nombre"] = datos[x][x + "_Nombre"]
            return datosAux

    @staticmethod
    def baja():
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):
            print(5 * "-" + "BAJA" + "-" * 5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                acAux = GestorBBDD.buscarDatoPorClave("AC_" + nombre)
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
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):
            print(5 * "-" + "MODIFICAR" + "-" * 5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                acAux = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                if acAux is not None:
                    GestionAC.menuModificar(nombre, acAux)
                else:
                    print("No se ha encontrado ese AC")
        else:
            print("No hay ACs creados.")

    @staticmethod
    def menuModificar(nombreOriginal, ac):
        opcion = None
        while (opcion != "0"):
            cambio = False
            print("¿Que campo quieres modificar?")
            print("1.Nombre.\n2.Cabeza.\n3.Torso."
                  "\n4.Brazos.\n5.Piernas.\n6.Arma brazo derecho."
                  "\n7.Arma Brazo Izquierdo.\n8.Arma Hombro Derecho."
                  "\n9.Arma Hombro Izquierdo.\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    acAux = GestorBBDD.buscarDatoPorClave(
                        "AC_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
                    if acAux is None:
                        if Utiles.confirmacion(
                                "Seguro que quiere cambiar el nombre del AC: " + nombreOriginal + " a: " + nombre):
                            GestorBBDD.borrarDato("AC_" + nombreOriginal)
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
                            ac = acAux2
                            nombreOriginal = nombre
                            cambio = True
                    else:
                        print("Ya existe un AC con el mismo nombre.\n")

            elif (opcion == "2"):
                GestionAC.mostrarNombres("Pieza", "CABEZA")
                cabeza = Utiles.check_campo("cabeza", 25)

                if cabeza is not None:
                    cabezaAux = GestorBBDD.buscarDatoPorClave("Pieza_" + cabeza)
                    if cabezaAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la cabeza del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + cabeza):
                            ac["AC_" + nombreOriginal + "_Cabeza"] = cabeza
                            cambio = True
                    else:
                        print("No se ha encontrado esa cabeza\n")

            elif (opcion == "3"):
                GestionAC.mostrarNombres("Pieza", "TORSO")
                torso = Utiles.check_campo("torso", 25)

                if torso is not None:
                    torsoAux = GestorBBDD.buscarDatoPorClave("Pieza_" + torso)
                    if torsoAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar el torso del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + torso):
                            ac["AC_" + nombreOriginal + "_Torso"] = torso
                            cambio = True
                    else:
                        print("No se ha encontrado ese torso\n")

            elif (opcion == "4"):
                GestionAC.mostrarNombres("Pieza", "BRAZOS")
                brazos = Utiles.check_campo("brazos", 25)

                if brazos is not None:
                    brazosAux = GestorBBDD.buscarDatoPorClave("Pieza_" + brazos)
                    if brazosAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la brazos del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + brazos):
                            ac["AC_" + nombreOriginal + "_Brazos"] = brazos
                            cambio = True
                    else:
                        print("No se han encontrado esos brazos\n")

            elif (opcion == "5"):
                GestionAC.mostrarNombres("Pieza", "PIERNAS")
                piernas = Utiles.check_campo("piernas", 25)

                if piernas is not None:
                    piernasAux = GestorBBDD.buscarDatoPorClave("Pieza_" + piernas)
                    if piernasAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la piernas del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + piernas):
                            ac["AC_" + nombreOriginal + "_Piernas"] = piernas
                            cambio = True
                    else:
                        print("No se han encontrado esas piernas\n")

            elif (opcion == "6"):
                GestionAC.mostrarNombres("Arma", "False")
                armaBDer = Utiles.check_campo("armaBDer", 25)

                if armaBDer is not None:
                    armaBDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBDer)
                    if armaBDerAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaBDer del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaBDer):
                            ac["AC_" + nombreOriginal + "_ArmaBDer"] = armaBDer
                            cambio = True
                    else:
                        print("No se ha encontrado ese arma del brazo derecho\n")

            elif (opcion == "7"):
                GestionAC.mostrarNombres("Arma", "False")
                armaBIzq = Utiles.check_campo("armaBIzq", 25)

                if armaBIzq is not None:
                    armaBIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaBIzq)
                    if armaBIzqAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaBIzq del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaBIzq):
                            ac["AC_" + nombreOriginal + "_ArmaBIzq"] = armaBIzq
                            cambio = True
                    else:
                        print("No se ha encontrado ese arma del brazo izquierdo\n")

            elif (opcion == "8"):
                GestionAC.mostrarNombres("Arma", "irrelevante")
                armaHDer = Utiles.check_campo("armaHDer", 25)

                if armaHDer is not None:
                    armaHDerAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHDer)
                    if armaHDerAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaHDer del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaHDer):
                            ac["AC_" + nombreOriginal + "_ArmaHDer"] = armaHDer
                            cambio = True
                    else:
                        print("No se ha encontrado ese arma del hombro derecho\n")

            elif (opcion == "9"):
                GestionAC.mostrarNombres("Arma", "irrelevante")
                armaHIzq = Utiles.check_campo("armaHIzq", 25)

                if armaHIzq is not None:
                    armaHIzqAux = GestorBBDD.buscarDatoPorClave("Arma_" + armaHIzq)
                    if armaHIzqAux is not None:
                        # Este if va dentro del de justo arriba
                        if Utiles.confirmacion("Seguro que quiere cambiar la armaHIzq del AC: " + ac[
                            "AC_" + nombreOriginal + "_Nombre"] + " a: " + armaHIzq):
                            ac["AC_" + nombreOriginal + "_ArmaHIzq"] = armaHIzq
                            cambio = True
                    else:
                        print("No se ha encontrado ese arma del hombro izquierdo\n")

            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                return None
            else:
                print("Opcion no valida.")

            if cambio is True:
                GestorBBDD.insertarDato(ac)
                print("AC modificado.")

    @staticmethod
    def buscar():
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):
            print(5 * "-" + "BUSCAR" + "-" * 5)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                datos = GestorBBDD.buscarDatoPorClave(
                    "AC_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
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

                    print(

                        "\n                                         *(                 " +
                        "\n                    /  *,,               (#(                " +
                        "\n                   (#,....#  .       *   /%@(               " +
                        "\n                ,*%(,//%-----------------------------------HD Arma:" + datos[
                            "AC_" + nombre + "_ArmaHDer"] +
                        "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
                        "\n              (/#& ,(,%#%#&#../(,//((.(#% %#---------------HI Arma:" + datos[
                            "AC_" + nombre + "_ArmaHIzq"] +
                        "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
                        "\n                  %&(#&   @%,,%///-------------------------Cabeza:" + datos[
                            "AC_" + nombre + "_Cabeza"] +
                        "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
                        "\n                (&@/%%    &*&#@@%%#&-----------------------Torso:" + datos[
                            "AC_" + nombre + "_Torso"] +
                        "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
                        "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##--------Brazos:" + datos[
                            "AC_" + nombre + "_Brazos"] +
                        "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
                        "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
                        "\n          (.%((%      *&(%&&          &&#&&     ##---------BI Arma:" + datos[
                            "AC_" + nombre + "_ArmaBIzq"] +
                        "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
                        "\n          %%-----------------------------------------------BD Arma:" + datos[
                            "AC_" + nombre + "_ArmaBDer"] +
                        "\n        ,/%(       #((#&%(%            ##&#%#((             " +
                        "\n       ,/&#       /(,/%#%%%            %&#%/---------------Piernas:" + datos[
                            "AC_" + nombre + "_Piernas"] +
                        "\n      ..%         (.*%&%                 %%,*..             " +
                        "\n     ,,%        #*,(#&&                    %#* ./           " + "NOMBRE:" + datos[
                            "AC_" + nombre + "_Nombre"] +
                        "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + "ARMADURA: " + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "Armadura")) +
                        "\n             %&@&&#%%%%                    *&&&&(@@/        " + "CONSUMO ENERGETICO:" + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "ConsumoEnergia")) +
                        "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + "PESO:" + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "Peso")) +
                        "\n         ,#%###                                 &&&%&(      " + "DPS:" + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "Dps")) +
                        "\n                                                    ,,      " + "RPM:" + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "Rpm")) +
                        "\n      ====================================================     PRECIO:" + str(
                            datoAC(datos["AC_" + nombre + "_Nombre"], "Precio")) + "$"
                    )
                else:
                    print("No se ha encontrado ese AC.")
        else:
            print("No hay ACs creados.")

    @staticmethod
    def mostrarTodos():
        if (GestorBBDD.mostrarTodosDatos("AC_") != {}):
            print(5 * "-" + "MOSTRAR TODOS" + "-" * 5)
            datos = GestorBBDD.mostrarTodosDatos(
                "AC_")  # Te mando la categoria para que me devuelvas un diccionario con diccionarios que contengan los datos de una pieza
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

                print(

                    "\n                                         *(                 " +
                    "\n                    /  *,,               (#(                " +
                    "\n                   (#,....#  .       *   /%@(               " +
                    "\n                ,*%(,//%-----------------------------------HD Arma:" + datos[x][
                        x + "_ArmaHDer"] +
                    "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
                    "\n              (/#& ,(,%#%#&#../(,//((.(#% %#---------------HI Arma:" + datos[x][
                        x + "_ArmaHIzq"] +
                    "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
                    "\n                  %&(#&   @%,,%///-------------------------Cabeza:" + datos[x][x + "_Cabeza"] +
                    "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
                    "\n                (&@/%%    &*&#@@%%#&-----------------------Torso:" + datos[x][x + "_Torso"] +
                    "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
                    "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##--------Brazos:" + datos[x][x + "_Brazos"] +
                    "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
                    "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
                    "\n          (.%((%      *&(%&&          &&#&&     ##---------BI Arma:" + datos[x][
                        x + "_ArmaBIzq"] +
                    "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
                    "\n          %%-----------------------------------------------BD Arma:" + datos[x][
                        x + "_ArmaBDer"] +
                    "\n        ,/%(       #((#&%(%            ##&#%#((             " +
                    "\n       ,/&#       /(,/%#%%%            %&#%/---------------Piernas:" + datos[x][x + "_Piernas"] +
                    "\n      ..%         (.*%&%                 %%,*..             " +
                    "\n     ,,%        #*,(#&&                    %#* ./           " + "NOMBRE:" + datos[x][
                        x + "_Nombre"] +
                    "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + "ARMADURA: " + str(
                        datoAC(datos[x][x + "_Nombre"], "Armadura")) +
                    "\n             %&@&&#%%%%                    *&&&&(@@/        " + "CONSUMO ENERGETICO:" + str(
                        datoAC(datos[x][x + "_Nombre"], "ConsumoEnergia")) +
                    "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + "PESO:" + str(
                        datoAC(datos[x][x + "_Nombre"], "Peso")) +
                    "\n         ,#%###                                 &&&%&(      " + "DPS:" + str(
                        datoAC(datos[x][x + "_Nombre"], "Dps")) +
                    "\n                                                    ,,      " + "RPM:" + str(
                        datoAC(datos[x][x + "_Nombre"], "Rpm")) +
                    "\n      ====================================================  PRECIO:" + str(
                        datoAC(datos[x][x + "_Nombre"], "Precio")) + "$"
                )
        else:
            print("No hay ACs creados.")


def datoAC(nombreAC, tipoDato):  # Este metodo no va aqui
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
