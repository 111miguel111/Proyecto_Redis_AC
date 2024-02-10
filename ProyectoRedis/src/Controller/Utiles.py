def confirmacion(contexto):
    '''
    Metodo para confirmar si se quiere confirmar una operacion
    :return Devuelve un un boolean. El valor sera True si escribe 'si' y False si escribe 'no'
    '''
    cont = 0
    while cont < 5:
        print(contexto, "(Si o No)")
        inputConfirmacion = input("→")
        print("")
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
    respuesta = input("→")
    print("")
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
def check_numeros(contexto, long):
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
                if not espacio.isnumeric():
                    carac_no_valido = True

            if not carac_no_valido:
                long = int(long)
                if 0 < len(campo) <= long:  # Verificamos la longitud del campo
                    return campo
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


def check_letras(contexto, long):
    """
    Funcion de apoyo que cerciora que la cadena que se introduce tiene como maximo una longitud y ademas es alfabetica
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
                if not espacio.isalpha():
                    carac_no_valido = True

            if not carac_no_valido:
                long = int(long)
                if 0 < len(campo) <= long:  # Verificamos la longitud del campo
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


