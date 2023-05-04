#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import pygame

# -------------------
# Constante
# -------------------
SCREEN_WITDH = 580
SCREEN_HEIGHT = 474
IMG_DIR = "imagenes"
# -------------------
# Clases y Funciones utilizadas
# -------------------
def cargar_imagen(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        imagen = pygame.image.load(ruta)
    except:
        print("Error al cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        imagen = imagen.convert_alpha()
    else:
        imagen = imagen.convert()
    return imagen


def main():
 pygame.init()
 #Posiciones
 coche_pos_x = 10
 coche_pos_y = 220
 plaza_ocu_x = 365
 plaza_ocu_y = 290
 plaza_dis_x = 365
 plaza_dis_y = 290
 # Creación de la ventana inicial del juego
 screen = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
 pygame.display.set_caption("Gestor de un parking")
 # Cargar el imagenes
 parking = cargar_imagen("parking.png", IMG_DIR, alpha=False)
 coche = cargar_imagen("coche.png", IMG_DIR, alpha=True)
 plazaocupada = cargar_imagen("Plazadisponible.png", IMG_DIR, alpha=False)
 plazadisponible = cargar_imagen("Plazaocupada.png", IMG_DIR, alpha=False)

 # Mostrar cambios en pantalla
 pygame.display.flip()
 # Bucle principal del juego
 while True:
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

     # mostrar disponibilidad plazas


     # Cerrar el juego
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == "__main__":
 main()
