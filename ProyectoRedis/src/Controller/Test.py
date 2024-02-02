from ProyectoRedis.src.Model import Arma

armaPrueba = {
    "nombre":input("Introduzca el nombre"),
    "tipoDamage":input("Introduzca el tipo de damage"),
    "dps":input("Introduzca el damage por segundo"),
    "rpm":input("Introduzca las rondas por minuto"),
    "municion":input("Introduzca las rondas maximas"),
    "armaHombro":input("¿Es un arma de hombro? (Si o No)"),
    "precio":input("Introduzca el precio del arma")
}

a = Arma(armaPrueba)

print(a)