from ProyectoRedis.src.Controller import Utiles, iGestores
from ProyectoRedis.src.Model import GestorBBDD


class GestionAC(iGestores.iGestores):
    @staticmethod
    def alta():
        '''
        Funcion encargada de dar de alta un AC pidiendo los nombres de las partes que lo componen
        '''
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
            cuerpoAux = GestorBBDD.buscarDato("AC_" + nombre)  # Te mando un tipo+nombre para que me devuelvas todods los datos dentro de un diccionario---------------
            if cuerpoAux is None:
                GestionAC.mostrarNombres("Pieza","cabeza")
                cabeza = Utiles.check_campo("nombre de la cabeza del AC", 25)

                #ESTO HAY QUE HACERLO PARA CADA PARTE, DE MOMENTO LO COMENTO CON PROPOSITOS DE TESTEO
                '''
                cabezaAux= GestorBBDD.buscarDato("Pieza_" + cabeza)
                if cabezaAux is None:
                    cabeza=None
                '''
            else:
                print("Ya existe un AC con ese nombre.")
        if cabeza is not None:
            GestionAC.mostrarNombres("Pieza", "torso")
            torso=Utiles.check_campo("nombre del torso del AC", 25)
        if torso is not None:
            GestionAC.mostrarNombres("Pieza", "brazos")
            brazos=Utiles.check_campo("nombre de los brazos del AC", 25)
        if brazos is not None:
            GestionAC.mostrarNombres("Pieza", "piernas")
            piernas=Utiles.check_campo("nombre de las piernas del AC", 25)
        if piernas is not None:
            GestionAC.mostrarNombres("Arma", "False")
            armaBDer=Utiles.check_campo("nombre del arma del brazo derecho del AC", 25)
        if armaBDer is not None:
            GestionAC.mostrarNombres("Arma", "False")
            armaBIzq=Utiles.check_campo("nombre del arma del brazo izquierdo del AC", 25)
        if armaBIzq is not None:
            GestionAC.mostrarNombres("Arma", "irrelevante")
            armaHDer = Utiles.check_campo("nombre del arma del hombro derecho del AC", 25)
        if armaHDer is not None:
            GestionAC.mostrarNombres("Arma", "irrelevante")
            armaHIzq = Utiles.check_campo("nombre del arma del hombro izquierdo del AC", 25)
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
            GestorBBDD.insertarDato(cuerpo)  # Te mando un diccionario con las clave valor del arma---------------------------------------------------
        if cuerpo is not None:
            print("AC creado.")
        else:
            print("Fallo en la creacion del AC.")



    @staticmethod
    def mostrarNombres(tipoDato,campo):
        datos = GestorBBDD.mostrarTodosDatos(tipoDato+"_")
        cont = 0
        if(tipoDato=="Pieza"):
            for x in datos:
                if (datos[x][x + "_TipoPieza"] == campo):
                    print("[-" + datos[x][x + "_Nombre"] + "-]" , end="")
                    cont += 1
                    if (cont == 3):
                        cont = 0
                        print("\n")
        elif(tipoDato=="Arma"):
            if(campo=="irrelevante"):
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
    def baja():
        print(5*"-"+"BAJA"+"-"*5)

    @staticmethod
    def modificar():
        print(5*"-"+"MODIFICAR"+"-"*5)

    @staticmethod
    def menuModificar(nombreOriginal, arma):
        print("QUITAME CUANDO HAYA CODIGO EN ESTA FUNCION")

    @staticmethod
    def buscar():
        print(5*"-"+"BUSCAR"+"-"*5)

    @staticmethod
    def mostrarTodos():
        print(5*"-"+"MOSTRAR TODOS"+"-"*5)
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
                "\n                ,*%(,//%-----------------------------------HD Arma:" +datos[x][x + "_ArmaHDer"]+
                "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
                "\n              (/#& ,(,%#%#&#../(,//((.(#% %#---------------HI Arma:" +datos[x][x + "_ArmaHIzq"] +
                "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
                "\n                  %&(#&   @%,,%///-------------------------Cabeza:" +datos[x][x + "_Cabeza"] +
                "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
                "\n                (&@/%%    &*&#@@%%#&-----------------------Torso:" +datos[x][x + "_Torso"] +
                "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
                "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##--------Brazos:" +datos[x][x + "_Brazos"] +
                "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
                "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
                "\n          (.%((%      *&(%&&          &&#&&     ##---------BI Arma:" +datos[x][x + "_ArmaBIzq"] +
                "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
                "\n          %%-----------------------------------------------BD Arma:" +datos[x][x + "_ArmaBDer"] +
                "\n        ,/%(       #((#&%(%            ##&#%#((             " +
                "\n       ,/&#       /(,/%#%%%            %&#%/---------------Piernas:" +datos[x][x + "_Piernas"] +
                "\n      ..%         (.*%&%                 %%,*..             " +
                "\n     ,,%        #*,(#&&                    %#* ./           " + "NOMBRE:" + datos[x][x + "_Nombre"] +
                "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + "ARMADURA: " + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "Armadura")) +
                "\n             %&@&&#%%%%                    *&&&&(@@/        " + "CONSUMO ENERGETICO:" + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "ConsumoEnergia")) +
                "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + "PESO:" + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "Peso")) +
                "\n         ,#%###                                 &&&%&(      " + "DPS:" + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "Dps")) +
                "\n                                                    ,,      " + "RPM:" + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "Rpm")) +
                "\n      ====================================================     PRECIO:" + str(GestorBBDD.datoAC( datos[x][x + "_Nombre"] , "Precio")) + "$"

            )
        if (datos == {}):
            print("No hay ACs creados.")

