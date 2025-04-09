import pygame
import random

# Inicializando o Pygame
pygame.init()

# Tamanho da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pac-Man')

# Cores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Pac-Man (feito de um círculo)
pacman_radius = 20
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
pacman_speed = 5

# Função para desenhar o Pac-Man
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), pacman_radius)

# Função principal do jogo
def game_loop():
    global pacman_x, pacman_y

    # Controlando o loop do jogo
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)  # Limpa a tela a cada quadro

        # Checando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do Pac-Man
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT]:
            pacman_x += pacman_speed
        if keys[pygame.K_UP]:
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN]:
            pacman_y += pacman_speed

        # Desenha o Pac-Man
        draw_pacman(pacman_x, pacman_y)

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de quadros (FPS)
        clock.tick(30)

    pygame.quit()

# Inicia o jogo
game_loop()
