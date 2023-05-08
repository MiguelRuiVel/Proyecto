import pygame
from pygame.locals import*
from Parking import IMG_DIR, SCREEN_WIDTH, SCREEN_HEIGHT
from funciones import cargar_imagen

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
        if keys[K_LEFT]:
            self.imagen = cargar_imagen("coche4.png", IMG_DIR, alpha=True)
            self.rect.centerx -= self.speed
        if keys[K_UP]:
            self.imagen = cargar_imagen("coche3.png", IMG_DIR, alpha=True)
            self.rect.centery -= self.speed
        if keys[K_DOWN]:
            self.imagen = cargar_imagen("coche2.png", IMG_DIR, alpha=True)
            self.rect.centery += self.speed
        if keys[K_SPACE]:
            pass





    def cliente(self):
        # Controlar que la vehiculo no salga de la pantalla
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.left <= 0:
            self.rect.left = 0




