#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import Funciones
import Plaza
import Vehiculo
from Funciones import cargar_imagen

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
    estaciono = Plaza.Plaza("Plazaocupada.png")
    estaciond = Plaza.Plaza("Plazadisponible.png")
    estacionp = Plaza.Plaza("Plazaprueba.png")
    coche = Vehiculo.Vehiculo()

    # cliente = Obstaculo.Obstaculo()

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
        Vehiculo.Vehiculo.update(coche)
        Vehiculo.Vehiculo.limites(coche)
        estacionp.colision(coche)
        lista_estacion=pygame.sprite.Group()
        # coche.Vehiculo.puntuacion(estacionp)
        # contar = Funciones.mostrartexto(cadena + str(coche.puntos), tipoFuente, tamaño, colorTexto)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        coche.update()

        # actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(contartiempo, (20, 3))
        screen.blit(estaciono.image, estaciono.rect)
        screen.blit(estaciond.image, estaciond.rect)
        screen.blit(estacionp.image, estacionp.rect)
        screen.blit(coche.image, coche.rect)
        # Obstaculo.Obstaculo.posiciones

        pygame.display.flip()


if __name__ == "__main__":
    JuegoParking()
