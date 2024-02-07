#from ProyectoRedis.src.Model import Arma
from ProyectoRedis.src.Model import Cuerpo
from ProyectoRedis.src.Model import Pieza
from ProyectoRedis.src.Model import GestorBBDD

armaPrueba = {#Aqui metemos en un diccionario los datos
    "Arma_Ejemplo_nombre":input("Introduzca el nombre"),
    "Arma_Ejemplo_tipoDamage":input("Introduzca el tipo de damage"),
    "Arma_Ejemplo_dps":input("Introduzca el damage por segundo"),
    "Arma_Ejemplo_rpm":input("Introduzca las rondas por minuto"),
    "Arma_Ejemplo_municion":input("Introduzca las rondas maximas"),
    "Arma_Ejemplo_armaHombro":input("¿Es un arma de hombro? (Si o No)"),
    "Arma_Ejemplo_precio":input("Introduzca el precio del arma")
}
#GestorBBDD.borrarDato("Arma")
GestorBBDD.insertarDato(armaPrueba)
aux = GestorBBDD.buscarDato("ArmaEjemplo")
print(aux)
print(GestorBBDD.mostrarTodosDatos("Arma"))

if aux is not None:
    for campo in aux:
        print(campo,aux[str(campo)])
else:
    print("Esta None")

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