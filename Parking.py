#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import funciones
import plaza
from funciones import cargar_imagen
import vehiculo

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 580
SCREEN_HEIGHT = 474
IMG_DIR = "imagenes"


def JuegoParking():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Gestor parking")
    # cargamos los objetos
    fondo = cargar_imagen("parking.png", IMG_DIR, alpha=False)
    coche = vehiculo.Vehiculo("coche1.png")
    estaciono = plaza.Plaza("Plazaocupada.png")
    estaciond = plaza.Plaza("Plazadisponible.png")
    estacionp = plaza.Plaza("Plazaprueba.png")

    colorTexto = (255, 255, 255)
    cadena = "Tiempo:"
    tamaño = 20
    tipoFuente = "Consolas"

    # el bucle principal del juego
    while True:
        contartiempo = funciones.contartiempo(cadena, tipoFuente, tamaño, colorTexto)
        plaza.Plaza.plazadisponible(estaciond)
        plaza.Plaza.plazadisponible(estaciond)
        plaza.Plaza.plazaocupada(estaciono)
        plaza.Plaza.plazaprueba(estacionp)
        vehiculo.Vehiculo.movimiento_coche(coche)
        vehiculo.Vehiculo.cliente(coche)
        estacionp.colision(coche)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(contartiempo, (20, 3))
        screen.blit(estaciono.imagen, estaciono.rect)
        screen.blit(estaciond.imagen, estaciond.rect)
        screen.blit(estacionp.imagen, estacionp.rect)
        screen.blit(coche.imagen, coche.rect)


        pygame.display.flip()

if __name__ == "__main__":
    JuegoParking()
