import pygame

from collections import deque
from time import sleep

from classes.Agente import Piggy, Rene
from classes.Laberinto import Laberinto

pygame.init()

ANCHO = 500
ALTO = 400
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption('Pacman versión Univalle')

def welcome():
    fondo = pygame.image.load('images/fondo_bienvenida.png')
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    play_button = pygame.rect.Rect(ANCHO // 2 - 50, ALTO // 2 - 25, 100, 50)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
                pygame.quit()
                return False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(evento.pos):
                    return True

        VENTANA.blit(fondo, (0, 0))
        mouse = pygame.mouse.get_pos()

        button_color = BLANCO
        shadow_offset = 0

        if play_button.collidepoint(mouse):
            button_color = (200, 200, 200)
            shadow_offset = 5

        shadow_rect = pygame.rect.Rect(
            play_button.left + shadow_offset, play_button.top + shadow_offset, play_button.width, play_button.height)
        pygame.draw.rect(VENTANA, (50, 50, 50), shadow_rect, border_radius=10)
        pygame.draw.rect(VENTANA, button_color, play_button, border_radius=10)

        font = pygame.font.Font(None, 40)
        text = font.render("Jugar", True, NEGRO)
        VENTANA.blit(text, (play_button.x + 20, play_button.y + 10))

        pygame.display.flip()

def end_game(text="El juego ha terminado"):
    fondo = pygame.image.load('images/game-over.jpeg')
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    font = pygame.font.Font(None, 40)
    text_surface = font.render(text, True, (255, 255, 255))  # White color

    # Calculate text position
    text_x = (ANCHO - text_surface.get_width()) // 2
    text_y = ALTO - text_surface.get_height() - 10

    # Define background rectangle
    background_rect = pygame.Rect(
        text_x - 10, text_y - 5, text_surface.get_width() + 20, text_surface.get_height() + 10)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False

        VENTANA.blit(fondo, (0, 0))

        # Draw background rectangle
        pygame.draw.rect(VENTANA, (0, 0, 0), background_rect)  # Black background

        # Blit text surface
        VENTANA.blit(text_surface, (text_x, text_y))

        pygame.display.flip()

    
def juego():
    def dibujar_mapa():
        VENTANA.fill(NEGRO)
        laberinto.dibujar(VENTANA)
        pygame.display.flip()

    # Creacion del laberinto 5x5 con todas las pocisiones en 0 que indican el camino libre
    laberinto = Laberinto([[0 for _ in range(5)] for _ in range(5)], ANCHO, ALTO)
    
    mapa_aleatorio, rene_pos, piggy_pos, elmo_pos, galleta_pos = laberinto.generar_mapa()
    dibujar_mapa()

    rene_pos_anterior = None
    piggy_pos_anterior = None

    rene = Rene(rene_pos)
    piggy = Piggy(piggy_pos)
    costo_acumulado_piggy = 0

    rene_path = deque(rene.get_path(laberinto.mapa))
    rene_path.popleft()

    turno = rene
    while True:
        sleep(1)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
               quit()

        if not  rene_path:
            end_game("Rene y Elmo se encontraron")
        elif piggy.find_rene:
            end_game("Piggy y Rene se encontraron")
        elif turno == piggy:
            if not piggy.find_rene:

                piggy_pos_anterior = piggy_pos
                movimiento, costo = piggy.move(rene_pos, laberinto.mapa)
                costo_acumulado_piggy += costo
                piggy_pos = movimiento

                laberinto.mover_agente(
                    piggy_pos, "P", elmo_pos, piggy_pos_anterior, galleta_pos)

            turno = rene
        elif turno == rene and rene_path:
            print("Mueve Rene")
            
            rene_pos_anterior = rene_pos
            rene_pos = rene_path.popleft()

            laberinto.mover_agente(
                rene_pos, "R", elmo_pos, rene_pos_anterior, galleta_pos)

            turno = piggy
            if piggy_pos == rene_pos:
                piggy.find_rene = True 

        print("Costo Acumulado de piggy", costo_acumulado_piggy)
        dibujar_mapa()

if welcome():
    juego()
