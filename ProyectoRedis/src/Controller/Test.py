from ProyectoRedis.src.Model import Arma
from ProyectoRedis.src.Model import Cuerpo
from ProyectoRedis.src.Model import Pieza

armaPrueba = {#Aqui metemos en un diccionario los datos
    "nombre":input("Introduzca el nombre"),
    "tipoDamage":input("Introduzca el tipo de damage"),
    "dps":input("Introduzca el damage por segundo"),
    "rpm":input("Introduzca las rondas por minuto"),
    "municion":input("Introduzca las rondas maximas"),
    "armaHombro":input("¿Es un arma de hombro? (Si o No)"),
    "precio":input("Introduzca el precio del arma")
}

a = Arma.Arma(armaPrueba)#Para construir el objeto por alguna razon tienes que usar un metodo que se llama igual que la clase de esta forma

cuerpoPrueba = {#Aqui metemos en un diccionario los datos
    "nombre":input("Introduzca el nombre"),
    "cabeza":input("Introduzca el modelo de cabeza"),
    "cuerpo":input("Introduzca el modelo del cuerpo"),
    "brazos":input("Introduzca el modelo de los brazos"),
    "piernas":input("Introduzca el modelo de las piernas"),
    "armaBDer":input("Introduzca el modelo de arma del brazo derecho"),
    "armaBIzq":input("Introduzca el modelo de arma del brazo izquierdo"),
    "armaHDer":input("Introduzca el modelo de arma del hombro derecho"),
    "armaHIzq":input("Introduzca el modelo de arma del hombro izquierdo")
}

b = Cuerpo.Cuerpo(cuerpoPrueba)

piezaPrueba = {#Aqui metemos en un diccionario los datos
    "nombre":input("Introduzca el nombre"),
    "tipoPieza":input("Introduzca el tipo de la pieza"),
    "armadura":input("Introduzca el valor de armadura"),
    "consumoEnergia":input("Introduzca el valor de consumo de energia"),
    "peso":input("Introduzca el peso de la pieza"),
    "precio":input("Introduzca el precio de la pieza")
}

c = Pieza.Pieza(piezaPrueba)