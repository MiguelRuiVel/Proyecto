import sys

import pygame


def Credits():
    pygame.init()
    screen = pygame.display.set_mode((580, 563))
    pygame.display.set_caption("Opciones")

    font_titulo = pygame.font.Font(None, 50)
    font_apartado = pygame.font.Font(None, 32)
    font_nombre = pygame.font.Font(None, 30)
    font_salir = pygame.font.Font(None, 15)
    font_space = pygame.font.Font(None, 40)

    color_titulo = (204, 0, 0)
    color_apartado = (255, 255, 255)
    color_nombre = (215, 215, 215)
    color_fondo = (0, 0, 0)
    screen.fill(color_fondo)

    texto_creditos = font_titulo.render("CRÉDITOS", True, color_titulo)
    texto_desarrollo = font_apartado.render("Desarrollo de la aplicación", True, color_apartado)
    texto_autores = font_nombre.render("Felipe P.S. y Miguel R.V.", True, color_nombre)
    texto_graficos = font_apartado.render("Apartado Gráfico y Efectos de Sonido", True, color_apartado)
    texto_vacio = font_nombre.render("Felipe P.S. y Miguel R.V.", True, color_nombre)
    texto_agradecimientos = font_apartado.render("Agradecimientos", True, color_apartado)
    texto_autores_agradecimientos = font_nombre.render("Javier F.M. y Ferran J.B.", True, color_nombre)
    texto_salir = font_salir.render("Pulsa Esc para salir", True, color_titulo)

    text_center_x = 580 // 2
    text_start_y = 100
    text_spacing = 50

    screen.blit(texto_creditos, (text_center_x - texto_creditos.get_width() // 2, text_start_y))
    screen.blit(texto_desarrollo, (text_center_x - texto_desarrollo.get_width() // 2, text_start_y + text_spacing))
    screen.blit(texto_autores, (text_center_x - texto_autores.get_width() // 2, text_start_y + text_spacing * 2))
    screen.blit(texto_graficos, (text_center_x - texto_graficos.get_width() // 2, text_start_y + text_spacing * 3))
    screen.blit(texto_vacio, (text_center_x - texto_vacio.get_width() // 2, text_start_y + text_spacing * 4))
    screen.blit(texto_agradecimientos,
                (text_center_x - texto_agradecimientos.get_width() // 2, text_start_y + text_spacing * 5))
    screen.blit(texto_autores_agradecimientos,
                (text_center_x - texto_autores_agradecimientos.get_width() // 2, text_start_y + text_spacing * 6))
    screen.blit(texto_salir, (text_center_x - texto_salir.get_width() // 2, text_start_y + text_spacing * 7))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.flip()
