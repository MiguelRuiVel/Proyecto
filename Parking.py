#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import pygame

# -------------------
# Constante
# -------------------
SCREEN_WITDH = 580
SCREEN_HEIGHT = 474
# -------------------
# Clases y Funciones utilizadas
# -------------------

# -------------------
# Funcion principal del juego
# -------------------

def main():
 pygame.init()
 # Creación de la ventana inicial del jeugo
 screen = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
 pygame.display.set_caption("Gestor de un parking")
 # Cargar el imagenes
 parking = pygame.image.load("parking.png").convert()
 coche = pygame.image.load("coche.png").convert_alpha()
 coche_pos_x = 10
 coche_pos_y = 220
 plazaocupada = pygame.image.load("Plazaocupada.png").convert()
 plaza_ocu_x = 365
 plaza_ocu_y = 290
 plazadisponible = pygame.image.load("Plazadisponible.png").convert()
 plaza_dis_x = 365
 plaza_dis_y = 290

 # Posición de aparición de las imagenes
 screen.blit(parking, (0, 0))
 screen.blit(coche, (coche_pos_x, coche_pos_y))
 screen.blit(plazaocupada, (plaza_ocu_x, plaza_ocu_y))
 screen.blit(plazadisponible, (plaza_dis_x, plaza_dis_y))

 # Mostrar cambios en pantalla
 pygame.display.flip()
 # Bucle principal del juego
 while True:
    # mostrar disponibilidad plazas

    # mover coche
    coche_pos_x = coche_pos_x + 0.1
    screen.blit(parking, (0, 0))
    screen.blit(coche, (coche_pos_x, coche_pos_y))
    pygame.display.flip()
    if coche_pos_x <= 330:
        screen.blit(plazadisponible, (plaza_dis_x, plaza_dis_y))
        pygame.display.flip()

    elif coche_pos_x >= 330:
        coche = pygame.image.load("coche2.png").convert_alpha()
        coche_pos_x = 330
        coche_pos_y = coche_pos_y + 0.1
        if coche_pos_y >= 320:
           screen.blit(plazaocupada, (plaza_ocu_x, plaza_ocu_y))
           coche = pygame.image.load("coche2.png").convert_alpha()
           coche_pos_x = 330
           coche_pos_y = 320
           screen.blit(coche, (coche_pos_x, coche_pos_y))
           pygame.display.flip()


    # Cerrar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == "__main__":
 main()
