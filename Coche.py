#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, random
import sys
import os


# -----------
# Constantes
# -----------

SCREEN_WIDTH = 580
SCREEN_HEIGHT = 470
IMG_DIR = "imagenes"
game_over = False


# -----------
# Funciones
# -----------
def cargar_imagen(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def mostrartexto(cadena, tipoFuente, tamaño, colorTexto):
    fuente = pygame.font.SysFont(tipoFuente, tamaño)
    texto = fuente.render(cadena, True, colorTexto)
    return texto


# -----------
# Clases
# -----------
class Vehiculo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = cargar_imagen("car.png", IMG_DIR, alpha=True)
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

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
              self.update('left')
            if event.key == pygame.K_RIGHT:
              self.update('right')
            if event.key == pygame.K_UP:
              self.update('up')
            if event.key == pygame.K_DOWN:
              self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')


    def topepantalla(self):
        # Controlar que la vehiculo no salga de la pantalla
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Enemigo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("cliente.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.speed = [1, 1]

    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))


class Plaza(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Plazaocupada.png", "imagenes", alpha=False)
        self.rect = self.image.get_rect()



def JuegoParking():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Gestor parking")
    # cargamos los objetos
    fondo = cargar_imagen("parking.png", IMG_DIR, False)

    estacion = Plaza()
    cliente = Enemigo()
    jugador = Vehiculo()
    puntuacion = 0
    clock = pygame.time.Clock()

    #lista que contiene todas las instancias de cada clase
    lista_estacion = pygame.sprite.Group()
    lista_update = pygame.sprite.Group()
    lista_clientes = pygame.sprite.Group()

    #Lista que contiende todos los sprites del juego
    lista_todos_sprites = pygame.sprite.Group()

    # añadir sprites de cada clase al grupo lista_todos_sprites
    lista_todos_sprites.draw(cliente)
    lista_todos_sprites.draw(jugador)


    # caracteristicas textos
    colorTexto = (255, 255, 255)
    textopantalla = "Puntos:"
    tamaño = 20
    tipoFuente = "Consolas"

    #Generar posiciones de las plazas aleatoriamente

    x = 100
    y = 30
    for i in range(4):
        estacion = Plaza() #(x, y)
        estacion.rect.x = x
        x += 150
        estacion.rect.y = y

        lista_estacion.add(estacion)
        lista_todos_sprites.add(estacion)

    x2 = 100
    y2 = 400
    for i in range(4):
        estacion = Plaza()  # (x, y)
        estacion.rect.x = x2
        x2 += 150
        estacion.rect.y = y2

        lista_estacion.add(estacion)
        lista_todos_sprites.add(estacion)


    for i in range(4):
        cliente = Enemigo()
        cliente.rect.x = random.randrange(SCREEN_WIDTH)
        cliente.rect.y = random.randrange(SCREEN_HEIGHT)

        lista_clientes.add(cliente)
        lista_update.add(cliente)
        lista_todos_sprites.add(cliente)


    # el bucle principal del juego
    while True:
        #tiempo refresco
        clock.tick(30)
        jugador.topepantalla()
        cliente.update()
        estacion

        lista_col_estacion = pygame.sprite.spritecollide(jugador, lista_estacion, True)

        for estacion in lista_col_estacion:
            puntuacion += 10

        lista_col_cliente = pygame.sprite.spritecollide(jugador, lista_clientes, True)

        for cliente in lista_col_cliente:
            puntuacion += -2

        contarpuntuacion = mostrartexto(textopantalla + str(puntuacion), tipoFuente, tamaño, colorTexto)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        jugador.handle_event(event)



        #mover el vehiculo con teclado pulsado



        # actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(contarpuntuacion, (0, 0))
        screen.blit(jugador.image, jugador.rect)
        lista_todos_sprites.draw(screen)


        pygame.display.flip()

if __name__ == "__main__":
    JuegoParking()
