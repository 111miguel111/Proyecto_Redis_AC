class Pieza:
    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.tipoPieza = datos["tipoPieza"]
        self.armadura = datos["armadura"]
        self.consumoEnergia = datos["consumoEnergia"]
        self.peso = datos["peso"]
        self.precio = datos["precio"]
