
class bcolors:
    NC = '\033[0m'  # No Color, reset all

    Bold = '\033[1m'
    Underlined = '\033[4m'
    Blink = '\033[5m'
    Inverted = '\033[7m'
    Hidden = '\033[8m'

    Black = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Purple = '\033[35m'
    Cyan = '\033[36m'
    LightGray = '\033[37m'
    DarkGray = '\033[30m'
    LightRed = '\033[31m'
    LightGreen = '\033[32m'
    LightYellow = '\033[93m'
    LightBlue = '\033[34m'
    LightPurple = '\033[35m'
    LightCyan = '\033[36m'
    White = '\033[97m'

    BckgrDefault = '\033[49m'
    BckgrBlack = '\033[40m'
    BckgrRed = '\033[41m'
    BckgrGreen = '\033[42m'
    BckgrYellow = '\033[43m'
    BckgrBlue = '\033[44m'
    BckgrPurple = '\033[45m'
    BckgrCyan = '\033[46m'
    BckgrLightGray = '\033[47m'
    BckgrDarkGray = '\033[100m'
    BckgrLightRed = '\033[101m'
    BckgrLightGreen = '\033[102m'
    BckgrLightYellow = '\033[103m'
    BckgrLightBlue = '\033[104m'
    BckgrLightPurple = '\033[105m'
    BckgrLightCyan = '\033[106m'
    BckgrWhite = '\033[107m'

    # Typical format
    Achtung = LightRed + Bold + Blink
    Error = LightRed + Bold

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
    print(contexto.upper() + ": ")
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
                    return campo.upper()
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
                    return campo.upper()
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


