import pygame
from pygame.locals import *
from Parking import *
from Funciones import cargar_imagen
from Parking import SCREEN_WIDTH,SCREEN_HEIGHT


class Vehiculo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = cargar_imagen("car.png", "imagenes", alpha=True)
        self.sheet.set_clip(pygame.Rect(0, 132, 66, 66))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = 30, 230
        self.frame = 0
        self.left_states = {0: (0, 66, 66, 66), 1: (66, 66, 66, 66), 2: (132, 66, 66, 66)}
        self.right_states = {0: (0, 132, 66, 66), 1: (66, 132, 66, 66), 2: (132, 132, 66, 66)}
        self.up_states = {0: (0, 198, 66, 66), 1: (66, 198, 66, 66), 2: (132, 198, 66, 66)}
        self.down_states = {0: (0, 0, 66, 66), 1: (66, 0, 52, 76), 2: (132, 0, 66, 66)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self):
        keys = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        clock.tick(60)
        if keys[K_RIGHT]:
            self.clip(self.right_states)
            self.rect.x += 3
        elif keys[K_LEFT]:
            self.clip(self.left_states)
            self.rect.x -= 3
        elif keys[K_UP]:
            self.clip(self.up_states)
            self.rect.y -= 3
        elif keys[K_DOWN]:
            self.clip(self.down_states)
            self.rect.y += 3
        elif keys[K_SPACE]:
            # añadir nuevo coche
            pass

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def limites(self):
        # Controlar que la vehiculo no salga de la pantalla
        # Abajo
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def puntuacion(self, objeto):
        if self.rect.colliderect(objeto.rect):
            self.puntos += 1


"""
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            elif event.key == pygame.K_RIGHT:
                self.update('right')
            elif event.key == pygame.K_UP:
                self.update('up')
            elif event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            elif event.key == pygame.K_RIGHT:
                self.update('stand_right')
            elif event.key == pygame.K_UP:
                self.update('stand_up')
            elif event.key == pygame.K_DOWN:
                self.update('stand_down')
"""
