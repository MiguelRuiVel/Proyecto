import pygame

from Parking import *
from Funciones import cargar_imagen


class Plaza(pygame.sprite.Sprite):

    def __init__(self, image, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Plazaocupada.png", "imagenes", alpha=False)
        self.rect = self.image.get_rect()

    def plazaprueba(self):
        self.imagen = cargar_imagen("Plazaprueba.png ", "imagenes", alpha=False)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 580 / 1.95
        self.rect.centery = 474 / 4

    def plazadisponible(self):
        self.imagen = cargar_imagen("Plazadisponible.png ", "imagenes", alpha=False)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 580 / 1.95
        self.rect.centery = 474 / 20

    def plazaocupada(self):
        self.imagen = cargar_imagen("Plazaocupada.png", "imagenes", alpha=False)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 580 / 1.95
        self.rect.centery = 470 / 20

    def colision(self, objeto):
        if self.rect.colliderect(objeto.rect):
            self.plazaocupada()

        else:
            self.plazadisponible()

    """
        def posicion(self):
        x=100
        y=30
        for i in range(4):
            estacion=Plaza()
            estacion.rect.x=x
            x+=150
            estacion.rect.y=y
    """
