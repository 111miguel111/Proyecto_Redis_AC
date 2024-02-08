#from ProyectoRedis.src.Model import Arma
from ProyectoRedis.src.Model import Cuerpo
from ProyectoRedis.src.Model import Pieza
from ProyectoRedis.src.Model import GestorBBDD

GestorBBDD.borrarDato("Arma")
armaPrueba = {#Aqui metemos en un diccionario los datos
    "Arma_Ejemplo_Nombre":input("Introduzca el nombre"),
    "Arma_Ejemplo_TipoDamage":input("Introduzca el tipo de damage"),
    "Arma_Ejemplo_Dps":input("Introduzca el damage por segundo"),
    "Arma_Ejemplo_Rpm":input("Introduzca las rondas por minuto"),
    "Arma_Ejemplo_Municion":input("Introduzca las rondas maximas"),
    "Arma_Ejemplo_ArmaHombro":input("¿Es un arma de hombro? (Si o No)"),
    "Arma_Ejemplo_Precio":input("Introduzca el precio del arma")
}
GestorBBDD.insertarDato(armaPrueba)
print(GestorBBDD.mostrarTodosFiltro("Arma","_Nombre","8","<"))


#a = Arma.Arma(armaPrueba)#Para construir el objeto por alguna razon tienes que usar un metodo que se llama igual que la clase de esta forma

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