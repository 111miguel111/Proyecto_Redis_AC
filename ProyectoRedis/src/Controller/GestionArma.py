from Controller import Utiles, iGestores
from Model import GestorBBDD


class GestionArma(iGestores.iGestores):
    @staticmethod
    def alta():
        '''
        Funcion encargada de pedir los datos necesarios y validarlos pra la creacion de un arma
        '''
        nombre = None
        tipoDamage = None
        dps = None
        rpm = None
        municion = None
        armaHombro = None
        precio = None
        arma=None
        print(Utiles.bcolors.Green+5*"-"+"ALTA"+"-"*5+Utiles.bcolors.White)
        nombre = Utiles.check_campo("nombre", 25)
        if nombre is not None:
            armaAux = GestorBBDD.buscarDatoPorClave("Arma_" + nombre)#Confirmamos que no haya otro arma con el mismo nombre
            if armaAux is None:
                tipoDamage = GestionArma.menuTipoDamage()#Lamamos a un menu que te permita elegir entre los tipos de daño
            else:
                print("Ya existe un arma con ese nombre.")
        if tipoDamage is not None:
            dps = Utiles.check_numeros("damage por segundo", 25)
        if dps is not None:
            rpm = Utiles.check_numeros("rondas por minuto", 25)
        if rpm is not None:
            municion = Utiles.check_numeros("rondas maximas", 25)
        if municion is not None:
            armaHombro = Utiles.confirmacionArmaHombro("¿Es un arma de hombro?")
        if armaHombro is not None:
            precio = Utiles.check_numeros("precio del arma", 25)
        if precio is not None:
            arma = {  # Aqui metemos en un diccionario los datos
                "Arma_"+str(nombre)+"_Nombre": str(nombre),
                "Arma_"+str(nombre)+"_TipoDamage": str(tipoDamage),
                "Arma_"+str(nombre)+"_Dps": str(dps),
                "Arma_"+str(nombre)+"_Rpm": str(rpm),
                "Arma_"+str(nombre)+"_Municion": str(municion),
                "Arma_"+str(nombre)+"_ArmaHombro": str(armaHombro).upper(),
                "Arma_"+str(nombre)+"_Precio": str(precio)
                }
            GestorBBDD.insertarDato(arma)#Mandamos el diccionario que acabamos de crear para guardarlo en la base de datos
        if arma is not None:
            print("Arma creada.")
        else:
            print("Fallo en la creacion del arma.")

    @staticmethod
    def menuTipoDamage():
        '''
        Funcion encargada de permitirte elegir entre los tipos de damage que puede hacer el arma
        return El tipo de damage que hace el arma
        '''
        opcion = None
        while (opcion != "0"):
            print("Tipo de damage:")
            print("1.Cinetico.\n2.Explosivo.\n3.Energia.\n4.Fuego.\n0.Salir.")
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                print("Se ha seleccionado CINETICO\n")
                return "CINETICO"
            elif (opcion == "2"):
                print("Se ha seleccionado EXPLOSIVO\n")
                return "EXPLOSIVO"
            elif (opcion == "3"):
                print("Se ha seleccionado ENERGIA\n")
                return "ENERGIA"
            elif (opcion == "4"):
                print("Se ha seleccionado FUEGO\n")
                return "FUEGO"
            elif (opcion == "5"):
                print("Se ha seleccionado ELECTRICO\n")
                return "ELECTRICO"
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
        Funcion encargada de pedir los datos necesarios para borrar un arma de la base de datos
        '''
        if(GestorBBDD.mostrarTodosDatos("Arma_")!={}):#Confirmamos que haya armas creadas
            print(Utiles.bcolors.Green+5*"-"+"BAJA"+"-"*5+Utiles.bcolors.White)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                armaAux =GestorBBDD.buscarDatoPorClave("Arma_" + nombre)#Confirmamos que el nombre introducido es un arma
                if armaAux is not None:
                    if Utiles.confirmacion("¿Seguro que quiere eliminar este arma?") is True:
                        GestorBBDD.borrarDato("Arma_"+nombre)
                        GestorBBDD.cascada(nombre, "Sin equipar")#Nos aseguramos de que si algun AC tiene este arma equipada ya no la tenga
                        print("Arma eliminada.")
                    else:
                        print("Arma no eliminada.")
            else:
                print("No se ha encontrado el arma.")
        else:
            print("No hay armas creadas.")

    @staticmethod
    def modificar():
        '''
        Funcion encargada de pedir y validar los datos necesarios para poder modificar un arma
        '''
        if (GestorBBDD.mostrarTodosDatos("Arma_") != {}):#Confirmamos que haya armas creadas
            print(Utiles.bcolors.Green+5*"-"+"MODIFICAR"+"-"*5+Utiles.bcolors.White)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                armaAux = GestorBBDD.buscarDatoPorClave("Arma_" + nombre)#Confirmamos que el nombre dado es un arma existente
                if armaAux is not None:
                    GestionArma.menuModificar(nombre,armaAux)#Llamamos a la funcion encargada de modificar los datos del arma
                else:
                    print("Pieza no encontrada.")
        else:
            print("No hay armas creadas.")

    @staticmethod
    def menuModificar(nombreOriginal,arma):
        '''
        Funcion encargada de pedir y verificar los datos para que sean actualizados en el arma
        nombreOriginal Es el nombre original del arma que facilitara la modifcacion de los datos de esta
        arma Es el arma que vamos a modificar
        '''
        opcion = None
        while (opcion != "0"):
            cambio=False
            print("¿Que campo quieres modificar?")
            print(Utiles.bcolors.Cyan+"1.Nombre.\n2.Tipo de damage.\n3.Damage por segundo."
                  "\n4.Rondas por minuto.\n5.Municion maxima.\n6.Precio.\n0.Salir."+Utiles.bcolors.White)
            opcion = Utiles.check_numeros("Opcion", 25)
            if (opcion == "1"):
                nombre = Utiles.check_campo("nombre", 25)
                if nombre is not None:
                    armaAux = GestorBBDD.buscarDatoPorClave("Arma_" + nombre)#Comprobamos que el nombre dado es un arma que existe
                    if armaAux is None:
                        if Utiles.confirmacion("Seguro que quiere cambiar el nombre del arma: "+nombreOriginal+" a: "+nombre):
                            GestorBBDD.cascada(nombreOriginal, nombre)#Nos encargamos de cambiar el nombre del arma en todos los AC que la tengan equipada
                            GestorBBDD.borrarDato("Arma_"+nombreOriginal)#Borramos los datos de este arma de la base de datos
                            #Creamos una copia del arma con el nuevo nombre(el nombre es parte de la clave) y los mismos datos(menos el nombre)
                            armaAux2 = {
                                "Arma_" + nombre + "_Nombre": nombre,
                                "Arma_" + nombre + "_TipoDamage": arma["Arma_" + nombreOriginal + "_TipoDamage"],
                                "Arma_" + nombre + "_Dps": arma["Arma_" + nombreOriginal + "_Dps"],
                                "Arma_" + nombre + "_Rpm": arma["Arma_" + nombreOriginal + "_Rpm"],
                                "Arma_" + nombre + "_Municion": arma["Arma_" + nombreOriginal + "_Municion"],
                                "Arma_" + nombre + "_ArmaHombro": arma["Arma_" + nombreOriginal + "_ArmaHombro"],
                                "Arma_" + nombre + "_Precio": arma["Arma_" + nombreOriginal + "_Precio"]
                            }
                            #Actualizamos el arma con el que estamos trabajando y el nombre original
                            arma=armaAux2
                            nombreOriginal=nombre
                            cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
                    else:
                        print("Ya existe un arma con el mismo nombre.")
            elif (opcion == "2"):
                tipoDamage = GestionArma.menuTipoDamage()#Llamamos a un sub menu para que el usuario pueda elegir el tipo de damage del arma
                if tipoDamage is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el tipo de damage del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + tipoDamage):
                        arma["Arma_" + nombreOriginal + "_TipoDamage"] = tipoDamage
                        cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
            elif (opcion == "3"):
                dps = Utiles.check_numeros("damage por segundo", 25)
                if dps is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el damage por segundo del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + dps):
                        arma["Arma_" + nombreOriginal + "_Dps"] = dps
                        cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
            elif (opcion == "4"):
                rpm = Utiles.check_numeros("rondas por minuto", 25)
                if rpm is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el rondas por minuto del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + rpm):
                        arma["Arma_" + nombreOriginal + "_Rpm"] = rpm
                        cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
            elif (opcion == "5"):
                municion = Utiles.check_numeros("rondas maximas", 25)
                if municion is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar las rondas maximas del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + municion):
                        arma["Arma_" + nombreOriginal + "_Municion"] = municion
                        cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
            elif (opcion == "6"):
                precio = Utiles.check_numeros("precio del arma", 25)
                if precio is not None:
                    if Utiles.confirmacion("Seguro que quiere cambiar el precio del arma: " + arma["Arma_"+nombreOriginal+"_Nombre"] + " a: " + precio):
                        arma["Arma_" + nombreOriginal + "_Precio"] = precio
                        cambio = True#Informamos al programa de que se ha realizado un cambio en el arma
            elif (opcion == "0"):
                print("Saliendo del subMenu.")
                opcion="0"
            else:
                print("Opcion no valida.")
            if cambio is True:#Si cambio esta en true significa que el AC a sido modificado po lo que lo actualizaremos en la base de datos
                GestorBBDD.insertarDato(arma)
                print("Arma modificada.")

    @staticmethod
    def buscar():
        '''
        Funcion encargada de pedir los datos necesarios para mostrar un arma y mostrarla
        '''
        if (GestorBBDD.mostrarTodosDatos("Arma_") != {}):#Confirmamos que haya armas creadas
            print(Utiles.bcolors.Green+5*"-"+"BUSCAR"+"-"*5+Utiles.bcolors.White)
            nombre = Utiles.check_campo("nombre", 25)
            if nombre is not None:
                datos = GestorBBDD.buscarDatoPorClave("Arma_" + nombre)#Nos aseguramos de que el arma exista
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
        else:
            print("No hay armas creadas.")


    @staticmethod
    def mostrarTodos():
        if (GestorBBDD.mostrarTodosDatos("Pieza_") != {}):#Confirmamos que haya armas creadas
            print(Utiles.bcolors.Green+5*"-"+"MOSTRAR TODOS"+"-"*5+Utiles.bcolors.White)
            datos = GestorBBDD.mostrarTodosDatos("Arma_")
            for x in datos:
                print("\n[-" + datos[x][x+"_Nombre"] + "-]")
                print("  Tipo de damage:" + datos[x][x+"_TipoDamage"] + "  ")
                print("  Damage por segundo:" + datos[x][x+"_Dps"] + "  ")
                print("  Rondas por minuto:" + datos[x][x+"_Rpm"] + "  ")
                print("  Municion maxima:" + datos[x][x+"_Municion"] + "  ")
                print("  Puede ponerse en el hombro:" + datos[x][x+"_ArmaHombro"] + "  ")
                print("  Precio:" + datos[x][x+"_Precio"] + "$  ")
        else:
            print("No hay armas creadas.")
