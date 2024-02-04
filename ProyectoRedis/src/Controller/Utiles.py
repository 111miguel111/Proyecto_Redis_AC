def confirmacion(contexto):
    '''
    Metodo para confirmar si se quiere confirmar una operacion
    :return Devuelve un un boolean. El valor sera True si escribe 'si' y False si escribe 'no'
    '''
    cont = 0
    while cont < 5:
        print(contexto, "(Si o No)")
        inputConfirmacion = input()
        if inputConfirmacion.lower() == 'si':
            return True
        elif inputConfirmacion.lower() == 'no':
            return False
        else:
            if cont < 4:
                print("\nValor incorrecto, pruebe otra vez (Si o No)." + "\n")
            cont += 1
    print("Has superado el numero de intentos." + "\n")
    return False


def entrada_teclado(contexto=""):
    """
    Funcion de apoyo que cerciora que la cadena que se introduce no este vacia
    :param contexto: informcacion sobre el campo
    :return: respuesta: si el campo es correcto
    :return: None: si el campo esta vacio
    """
    print(contexto.capitalize() + ": ")
    respuesta = input()
    if respuesta is not None and not respuesta.isspace():
        return respuesta.strip()
    else:
        print("El campo, " + contexto + " no puede estar vacio." + "\n")
        return None


# CHECKERS
def check_campo(contexto, long):
    """
    Funcion de apoyo que cerciora que la cadena que se introduce tiene como maximo una longitud y ademas es alfanumerica
    :param contexto: Explicacion del campo al que se refiere
    :param long: longitud maxima de la cadena
    :return: campo si este cumple las validaciones
    :return: None si se falla 5 veces en la introduccion del campo
    """
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado(contexto)
        if campo is not None:
            palabras = campo.split(" ")
            carac_no_valido = False
            for espacio in palabras:  # Comprobamos que en las posibles palabras del campo no haya componentes no alfanumericos
                if not espacio.isalnum():
                    carac_no_valido = True

            if not carac_no_valido:
                long = int(long)
                if 0 < len(campo) <= long:  # Verificamos la longitud del campo
                    print(contexto.capitalize() + " es valido.")
                    return campo.capitalize()
                else:
                    print(contexto + " tiene una longitud no valida, longitud maxima: " + str(long) + ".\n")
                    fallos += 1
            else:
                if len(campo) == 0:
                    print("El campo, " + contexto + " no puede estar vacio." + "\n")
                    fallos += 1
                else:
                    print(contexto + " contiene caracteres no validos." + "\n")
                    fallos += 1
        else:
            fallos += 1
        if fallos < 5:
            print("Fallos hasta salir", fallos, "/5")
    print("Se han producido 5 fallos.\nAbotortando proceso.\n")
    return None


def check_dni():
    """
    Funcion de apoyo que cerciora que se introduce un DNI valido
    :return: dni, si es valido
    :return: None, si se falla 5 veces en la introduccion de DNI
    """
    fallos = 0
    while fallos < 5:
        print("Recuerde el formato de un DNI valido es 00000000A.")
        dni = entrada_teclado("DNI")
        if dni is not None:
            if len(dni) == 9:
                if dni[0:8].isnumeric():  # Es cerrado por la izquierda abierto por la derecha
                    if dni[8].isalpha():  # Solo coge el noveno caracter
                        print("DNI es valido.")
                        return dni.upper()
                    else:
                        print("El ultimo caracter debe tratarse de una letra." + "\n")
                        fallos += 1
                else:
                    print("Los primeros 8 caracteres deben tratarse de numeros." + "\n")
                    fallos += 1
            else:
                print("El DNI debe de tener 9 caracteres." + "\n")
                fallos += 1
        else:
            fallos += 1
        if fallos < 5:
            print("Fallos hasta salir", fallos, "/5")
    print("Se han producido 5 fallos.\nAbotortando proceso" + "\n")
    return None


def check_telefono():
    """
    Funcion de apoyo que cerciora que se introduce un telefono valido
    :return: telefono, si esta es valida
    :return: None, si se falla 5 veces en la introduccion de un telefono
    """
    fallos = 0
    while fallos < 5:
        campo = entrada_teclado("telefono")
        if campo is not None:
            if campo.isnumeric():
                if len(campo) == 9:
                    print("Telefono es valido.")
                    return campo
                else:
                    print("Telefono tiene una longituz no valida, longitud debe ser: 9." + "\n")
                    fallos += 1
            else:
                print("Telefono contiene caracteres no validos." + "\n")
                fallos += 1
        else:
            fallos += 1
        if fallos < 5:
            print("Fallos hasta salir", fallos, "/5")
    print("Se han producido 5 fallos.\nAbotortando proceso." + "\n")
    return None


def escanerNumerico(contexto):
    """
    Funcion que cerciora que la cadena que se introduce no este vacia y sean numeros
    :param contexto: informcacion sobre el campo
    :return: respuesta: si el campo es correcto
    :return: None: si el campo esta vacio
    """
    # Se crea un contador de intentos para el bucle que solo iterara hasta 5 intentos
    intentos = 0
    while (intentos < 5):
        print(contexto.capitalize() + ": ")
        scan = input()
        # Se introduce la cadena y que ponga 1 o 2 si no te vuelve a preguntar y si fallas 5 veces devulve none
        if (scan.isspace() == False and scan.isnumeric()):
            return scan
        intentos += 1
        print('Porfavor introduce solo numeros no decimales.' + '\n')
        if intentos < 5:
            print("Fallos hasta salir", intentos, "/5")
    print("Has superado el numero de intentos.")
    return None
