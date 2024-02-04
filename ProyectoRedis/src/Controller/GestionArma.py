
from Controller import Utiles,GestorBBDD


def alta():
    nombre=None
    tipoDamage=None
    dps=None
    rpm=None
    municion=None
    armaHombro=None
    precio=None
    
    print("ALTA")
    nombre=Utiles.check_campo("nombre", 25)
    if nombre is not None:
        armaAux=GestorBBDD.buscarDato("Arma"+nombre)#Comprobamos si ya existe un arma con ese nombre
        if armaAux is None:
            tipoDamage=Utiles.check_letras("tipo de damage", 25)
    if tipoDamage is not None:
        dps=Utiles.check_numeros("damage por segundo",25)
    if dps is not None:
        rpm=Utiles.check_numeros("rondas por minuto",25)
    if rpm is not None:
        municion=Utiles.check_numeros("rondas maximas", 25)
    if municion is not None:
        armaHombro=Utiles.confirmacion("¿Es un arma de hombro?")
    if armaHombro is not None: 
        precio=Utiles.check_numeros("precio del arma", 25)
        if precio is not None:
            armaPrueba = {#Aqui metemos en un diccionario los datos
                        "nombre":str(nombre),
                        "tipoDamage":str(tipoDamage),
                        "dps":str(dps),
                        "rpm":str(rpm),
                        "municion":str(municion),
                        "armaHombro":str(armaHombro),
                        "precio":str(precio)
                        }
            GestorBBDD.insertarDato("Arma", armaPrueba)
            
    
def baja():
    print("BAJA")
def modificar():
    print("MODIFICAR")
def buscar():
    print("BUSCAR")
def mostrarTodos():
    print("MOSTRAR TODOS")
    datos=GestorBBDD.mostrarTodosDatos("Arma")
    print(datos, type(datos))
    
    for x in datos:
        print(datos[x])






