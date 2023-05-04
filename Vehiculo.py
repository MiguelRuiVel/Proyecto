import random


class Vehiculo():

    def __init__(self):
        pass
    def matricula(self):
        self.matricula = random.randint(0, 9999)

    def tiempo(self):
        # llamar a clock
        pass

    def estado(self):
        # menu con información
        print("Matricula: ", self.matricula)
