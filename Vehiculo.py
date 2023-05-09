import pygame
from pygame.locals import *
from Parking import *
from Funciones import cargar_imagen


class Vehiculo(pygame.sprite.Sprite):

    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = cargar_imagen(imagen, IMG_DIR, alpha=True)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 10
        self.rect.centery = SCREEN_HEIGHT / 1.65
        self.speed = 4

    def movimiento_coche(self):
        keys = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        clock.tick(60)
        if keys[K_RIGHT]:
            self.imagen = cargar_imagen("coche1.png", IMG_DIR, alpha=True)
            self.rect.centerx += self.speed
        elif keys[K_LEFT]:
            self.imagen = cargar_imagen("coche4.png", IMG_DIR, alpha=True)
            self.rect.centerx -= self.speed
        elif keys[K_UP]:
            self.imagen = cargar_imagen("coche3.png", IMG_DIR, alpha=True)
            self.rect.centery -= self.speed
        elif keys[K_DOWN]:
            self.imagen = cargar_imagen("coche2.png", IMG_DIR, alpha=True)
            self.rect.centery += self.speed
        elif keys[K_SPACE]:
            # añadir nuevo coche
            pass

    def limites(self):
        # Controlar que la vehiculo no salga de la pantalla
        # Abajo
        if self.rect.centery > SCREEN_HEIGHT:
            self.rect.centery = SCREEN_HEIGHT
        # Arriba
        if self.rect.centery < 0:
            self.rect.centery = 0
        # Derecha
        if self.rect.centerx > SCREEN_WIDTH:
            self.rect.centerx = SCREEN_WIDTH
        # Izquierda
        if self.rect.centerx < 0:
            self.rect.centerx = 0

