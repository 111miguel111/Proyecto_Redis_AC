import configparser
import traceback
from os import remove
import sys
import redis
from ProyectoRedis.src.Controller import Utiles


def iniciarFicheroConfiguracion():
    '''
    Funcion que se encarga de crear el fichero de configuracion con valores predeterminados
    '''
    try:
        # Creamos un fichero .ini en el cual se guardan datos para la configuracion del programa
        config = configparser.ConfigParser()  # Creamos la variable que contiene los datos de configuracion
        config['SERVER'] = {'host': 'localhost',
                            'port': '6380'}
        with open('config.ini', 'w') as configfile:  # Escribimos el fichero de configuracion
            config.write(configfile)
        print("Se ha creado el fichero de configuracion.")
    except:
        print('No se ha podido crear el fichero de configuracion, el programa se cerrara. ')
        sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
    return 0


def iniciarFicheroConfiguracionManulamente():
    '''
    Funcion que se encarga de crear el fichero de configuracion con valores que se le pediran al usuario
    '''
    host = None
    port = None
    # Pedimos los datos para crear el ficheo de configuracion
    print("El fichero de configuracion no existe porfavor introduce los campos a poner en el fichero.")
    host = Utiles.check_campo("host", 25)
    if host is not None:
        port = Utiles.check_numeros("port", 25)
    if port is not None:
        try:
            # Creamos un fichero .ini en el cual se guardan datos para la configuracion del programa
            config = configparser.ConfigParser()  # Creamos la variable que contiene los datos de configuracion
            config['SERVER'] = {'host': str(host).lower(),
                                'port': str(port).lower()}
            with open('config.ini', 'w') as configfile:  # Escribimos el fichero de configuracion
                config.write(configfile)
            print("Se ha creado el fichero de configuracion.")
        except:
            print(
                'No se ha podido crear el fichero de configuracion, el programa se cerrara. \nComprueba que has introducido bien los datos.\nEl fichero se llama "config.ini". ')
            sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
    else:
        print('No se ha podido crear el fichero de configuracion, el programa se cerrara. ')
        sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
    return 0


def checkFileExistance(filePath):
    '''
    Comprueba que el fichero de configuracion existe
    :param filePath: El nombre del fichero
    :return Devuelve True si el fichero existe y False si no existe
    '''
    # Comprobamos que el fichero exista si no es el caso devolvemos false
    try:
        with open(filePath, "r"):
            print("El fichero de configuracion existe.")
            return True

    except FileNotFoundError:
        print("El fichero de configuracion no existe.")
        return False

    except IOError:
        return False


def checkConfigBien(filePath):
    '''
    Funcion encargada de comprobar que el fichero de configuracion esta completo y no tenga errores
    :param filePath: El nombre del fichero
    :return Devuelve False si hay algun problema al leer el fichero de configuracion y si todos los campos estan bien devuelve True
    '''
    campo = ''
    # Comprobamos que el fichero tiene todas sus secciones y categorias en orden
    try:
        print("Comprobando estado del fichero de configuracion.")
        config = configparser.ConfigParser()
        config.read(filePath)
        campo = 'host'
        # Comprobamos que la categoria existe solicitando el dato que hay dentro
        host_variable = str(config['SERVER']['host'])
        if (host_variable.isspace() or len(
                host_variable) == 0):  # Si esta categoria esta mal devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo " + campo + " no puede estar vacio.\n")
            return False
        campo = 'port'
        # Comprobamos que la categoria existe solicitando el dato que hay dentro
        port_variable = int(config['SERVER']['port'])
        if (str(port_variable).isspace() or str(port_variable).isnumeric() == False or len(
                str(port_variable)) == 0):  # Si esta categoria esta mal o esta vacia devolveremos false y se entendera que el fichero de configuracion esta mal
            print("El campo " + campo + " tiene que ser numeros.\n")
            return False
        print("El fichero de configuracion esta bien.")
        print(
            'Si quieres configurar los datos de conexion del sistema gestor de base de datos, modifique la informacion el fichero "config.ini".')
        return True
    except FileNotFoundError:
        print("El campo " + campo + " falta o esta mal.\n")
        return False
    except IOError:
        print("El campo " + campo + " falta o esta mal.\n")
        return False
    except:
        print("El campo " + campo + " falta o esta mal.\n")
        return False


def AgregarCatalogo():
    try:
        with open("../../catalogo.txt", "r") as fichero:
            for linea in fichero:
                linea=linea.replace("\n","")
                claveValor=linea.split(":")
                conn.set(claveValor[0],claveValor[1])
            print("Se ha agregado el catalogo es decir 2 piezas de cada tipo y 2 armas de cada tipo.")
    except:
        print("No se ha podido agregar catalogo.")

    return 0


def conectarse():
    '''
    Funcion encargada de conectar redis a la base de datos
    :return devolveremos una conexion 
    '''
    try:

        # Obtenemos la informacion del fichero de oniguracion
        config = configparser.ConfigParser()
        config.read('config.ini')
        host_variable = str(config['SERVER']['host'])
        port_variable = int(config['SERVER']['port'])
        # Una vez ya tenemos las variables con los datos para la conexion nos conectamos con redis
        conn = redis.Redis(host=host_variable,
                           port=port_variable,
                           decode_responses=True)

        return conn
    # Si la conexion no se puede realizar nos informara
    except:
        print(
            "Hay un error en la conexion. \n1.Quieres restablecer el fichero con los valores por defecto \n2.Quieres cerrar el programa. ")
        opcion = Utiles.check_numeros("Opcion", 25)
        if (opcion == '1'):
            print("El fichero de configuracion sera restablecido y el programa se cerrara.")
            iniciarFicheroConfiguracion()
            print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini". ')
            sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
        elif (opcion == '2'):
            print("El programa se cerrara.")
            sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
        else:
            print("Opcion no valida, el programa se cerrara.")
            sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error


def cerrarBD():
    try:
        print("Desconectando la base de datos.")
        conn.close()
    except:
        # print(traceback.format_exc())
        return None


def iniciar():
    '''
    Funcion encargada de crear la conexion y confirmar que el fichero de configuracion va bien etc.
    :return Si la base de datos se realiza con exito devolveremos True en caso de que suceda algun problema devolveremos False
    '''
    # Funcion que inicia lo relacionado con la base de datos, comprueba el fichero de datos, comprueba la conexion y si esta bien procede a crear una base de datos
    try:
        # Primero confirmamos que el fichero de configuracion existe y no esta corrupto
        if (checkFileExistance(
                "config.ini") == True):  # Comprobamos que el fichero de configuracion existe, si no es el caso lo creamos con los datos por defecto
            if (checkConfigBien("config.ini") == False):  # Comprobamos que el fichero de configuracion esta bien
                # Si hay algun error informamos al usuario
                print(
                    "Hay un error en el fichero de configuracion: \n1.Quieres restablecer el fichero con los valores por defecto. \n2.Quieres cerrar el programa.\n3.Quieres borrar el fichero de configuracion.")

                opcion = Utiles.check_numeros("Opcion", 25)
                if (opcion == '1'):
                    print("El fichero de configuracion sera restablecido y el programa se cerrara.")
                    iniciarFicheroConfiguracion()
                    print('Si quieres hacer cambios en la conexion mire el archivo de configuracion "config.ini". ')
                    sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
                elif (opcion == '2'):
                    print("El programa se cerrara.")
                    sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
                elif (opcion == '3'):
                    print("El fichero de configuracion sera borrado.")
                    remove("config.ini")
                    print("El programa se cerrara.")
                    sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
                else:
                    print("El programa se cerrara.")
                    sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error
        else:
            iniciarFicheroConfiguracionManulamente()
        return True
    except:
        return False


# ------------------------------------------------------------------------------------------------------------
# Creamos la variable conn para inicializarla
conn = None
# Comprobamos que la conexion esta bien y si este es el caso rrreaalizamos la conexion con peewee si no cerramos el programa
if (iniciar()):
    conn = conectarse()
else:
    sys.exit()  # Cerramos el programa ya que no deberia continuar tras este error


# -------------------------------------------
# Metodos redis

# Crud
def insertarDato(datos):
    try:
        for campo in datos:
            conn.set(campo, datos[campo])
    except:
        print("Se ha cometido un error en la insercion")


def buscarDato(busqueda):
    datos = {}
    for campo in conn.keys(busqueda + "*"):
        datos[campo] = conn.get(campo)
    if (datos == {}):
        datos = None
    return datos

def buscarDatoPorClave(clave):
    datos = {}
    for campo in conn.keys(clave +"_"+"*"):
        datos[campo] = conn.get(campo)
    if (datos == {}):
        datos = None
    return datos


def borrarDato(clave):
    datos = buscarDato(clave)
    for campo in datos:
        conn.delete(campo)

def dropDatabase():
    datos = buscarDato("*")
    for campo in datos:
        conn.delete(campo)


def mostrarTodosDatos(tipoDato):  # Diccionario de diccionarios
    datos = conn.keys(tipoDato + "*")  # Ayuda
    datosOut = {}
    stringAux = ""
    for key in datos:
        if (str(key).split("_")[0] + "_" + str(key).split("_")[1]) != stringAux:
            stringAux = str(key).split("_")[0] + "_" + str(key).split("_")[1]
            datosAux = {}
            for key in conn.keys(stringAux + "*"):
                datosAux[key] = conn.get(key)
            datosOut[stringAux] = datosAux
    return datosOut


def cascada(nombreOriginal, nombre):
    datos = mostrarTodosDatos(
        "AC_")  # Te mando la categoria para que me devuelvas un diccionario con diccionarios que contengan los datos de una pieza
    for x in datos:
        for campo in datos[x]:
            if (datos[x][campo] == nombreOriginal):
                datos[x][campo] = nombre
                borrarDato(campo)
                conn.set(campo, nombre)


# Queries
def sumaDatosAC(listaCampos, tipoComponente, nombreAC, tipoDato):
    '''
    Metodo que suma los valores de un campo de cada pieza o arma
    listaCampos: Lista con los campos a comprobar de la pieza
    tipoComponente: String que define si se quieren buscar piezas o armas
    nombreAC: Nombre del AC del que se quiere saber los datos
    tipoDato: String del tipo de dato del que se quieren obtener datos
    '''
    # Se crea un valor 0 sobre el que se sumaran las estadisticas
    valor = 0
    # Se suma campo a campo el valor a calcular
    for campos in listaCampos:
        # Se obtiene el nombre de la pieza de la parte correspondiente en el AC
        nombrePieza = tipoComponente + buscarDato("AC_" + nombreAC + campos)["AC_" + nombreAC + campos] + "_" + tipoDato
        # Se busca ahora el parametro de la pieza en la base de datos y se suma a valor
        # Si el campo no existe se pone 0
        try:
            valor += int(buscarDato(nombrePieza)[nombrePieza])
        except:
            valor = 0
    return valor


def mostrarTodosFiltro(tipoDato, campo, valor, rango):  # Diccionario de diccionarios
    '''
    Metodo que busca todas las instancias de datos con los parametros elegidos.
    Si los parametros elegidos no son correctos se devuelve none
    tipoDato: String con el tipo de dato a buscar, se le puede concatenar caracteres
    del nombre del dato para una busqueda por nombre mas exhaustiva
    campo: String del parametro del dato por el que se desea filtrar
    valor: String del valor por el que se desea filtrar. En el caso de buscar por nombre
    se puede hacer busqueda parcial terminando con un *
    rango: String con "=", "<", o ">" para hacer que busque por mayor que, menor que o igual.
    El caso de que se quiera buscar un campo con letras solo "=" sera valido
    '''
    # Se crea el diccionario en el que se van a guardar los datos
    datosAux = {}

    datos = mostrarTodosDatos(tipoDato)
    # El for each recorre la BBDD en funcion a la cadena del tipo de dato introducida
    for key in datos:
        try:
            # Se comprueba que se quiere hacer con el tipo de dato
            if (rango == "="):
                if valor == "" or conn.get(key + campo) == valor:
                    datosAux[key] = datos[key]
            elif (rango == ">"):
                if valor == "" or int(conn.get(key + campo)) > int(valor):
                    datosAux[key] = datos[key]
            elif (rango == "<"):
                if valor == "" or int(conn.get(key + campo)) < int(valor):
                    datosAux[key] = datos[key]
            else:
                print('Introduzca que con que rango se quieren filtrar los datos. Si no esta seguro ponga "')
        except:
            print("Error al buscar dato. Compruebe que los parametros de busqueda son correctos")
            return None

    return datosAux
