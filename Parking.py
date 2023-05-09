#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import Funciones
import Plaza
from Funciones import cargar_imagen
import Vehiculo

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
    coche = Vehiculo.Vehiculo("coche1.png")
    estaciono = Plaza.Plaza("Plazaocupada.png")
    estaciond = Plaza.Plaza("Plazadisponible.png")
    estacionp = Plaza.Plaza("Plazaprueba.png")

    colorTexto = (255, 255, 255)
    cadena = "Tiempo:"
    tamaño = 20
    tipoFuente = "Consolas"

    # el bucle principal del juego
    while True:
        contartiempo = Funciones.contartiempo(cadena, tipoFuente, tamaño, colorTexto)
        Plaza.Plaza.plazadisponible(estaciond)
        Plaza.Plaza.plazadisponible(estaciond)
        Plaza.Plaza.plazaocupada(estaciono)
        Plaza.Plaza.plazaprueba(estacionp)
        Vehiculo.Vehiculo.movimiento_coche(coche)
        Vehiculo.Vehiculo.cliente(coche)
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
