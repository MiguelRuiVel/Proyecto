import pygame
import sys
import os


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


def contartiempo(cadena, tipoFuente, tamaño, colorTexto):
    tiempo = pygame.time.get_ticks() / 1000
    cadena = cadena + str(tiempo)
    fuente = pygame.font.SysFont(tipoFuente, tamaño)
    texto = fuente.render(cadena, True, colorTexto)
    return texto


def mostrartexto(cadena, tipoFuente, tamaño, colorTexto):
    fuente = pygame.font.SysFont(tipoFuente, tamaño)
    texto = fuente.render(cadena, True, colorTexto)
    return texto
