import pygame
import random
import sys

# Inicializar Pygame y el mixer de sonido
pygame.init()
pygame.mixer.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego del Globo")

# Cargar imágenes del globo
globo1 = pygame.image.load("globo1.png").convert_alpha()
globo2 = pygame.image.load("globo2.png").convert_alpha()
globo_img = globo1

# Cargar sonido
pop_sound = pygame.mixer.Sound("pop.mp3")

# Obtener el tamaño del globo
globo_rect = globo_img.get_rect()
globo_radius = globo_rect.width // 2

# Variables del juego
score = 0
font = pygame.font.SysFont(None, 48)
globo_pos = [random.randint(globo_radius, WIDTH-globo_radius), random.randint(globo_radius, HEIGHT-globo_radius)]
show_message = False
message_timer = 0

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))

    # Mover globo a posición aleatoria cada 0.5 segundos
    if pygame.time.get_ticks() % 500 < 20:
        globo_pos = [random.randint(globo_radius, WIDTH-globo_radius), random.randint(globo_radius, HEIGHT-globo_radius)]

    # Dibujar globo
    screen.blit(globo_img, (globo_pos[0] - globo_radius, globo_pos[1] - globo_radius))

    # Mostrar puntaje
    score_text = font.render(f"Puntos: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Mostrar mensaje si corresponde
    if show_message:
        msg = font.render("¡Anotaste un punto!", True, (0, 150, 0))
        screen.blit(msg, (WIDTH//2 - 150, HEIGHT//2))
        if pygame.time.get_ticks() - message_timer > 500:
            show_message = False
            globo_img = globo1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            dist = ((mouse_pos[0] - globo_pos[0])**2 + (mouse_pos[1] - globo_pos[1])**2)**0.5
            if dist < globo_radius:
                globo_img = globo2
                score += 1
                show_message = True
                message_timer = pygame.time.get_ticks()
                pop_sound.play()  # ¡Reproduce el sonido!

    pygame.display.flip()
    clock.tick(60)