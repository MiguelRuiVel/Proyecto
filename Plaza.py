import pygame

import funciones
from funciones import cargar_imagen

class Plaza(pygame.sprite.Sprite):

    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = cargar_imagen(imagen, "imagenes", alpha=False)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 580 / 1.95
        self.rect.centery = 474 / 6

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


