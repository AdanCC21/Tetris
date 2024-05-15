import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Mi Primer Juego en Pygame')

# Cargar una imagen
imagen = pygame.image.load('assets/De hecho 4.jpg')

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar la imagen en la pantalla
    screen.blit(imagen, (0, 0))

    # Actualizar la pantalla
    pygame.display.flip()
