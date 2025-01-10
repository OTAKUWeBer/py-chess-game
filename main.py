import pygame

# Start Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 600

# Create screen and set title
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Two-player Chess")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Chessboard setup
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8
X_OFFSET = (WIDTH - BOARD_SIZE) // 2
Y_OFFSET = (HEIGHT - BOARD_SIZE) // 2

# Draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            x = X_OFFSET + col * SQUARE_SIZE
            y = Y_OFFSET + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))  # Background color
    draw_chessboard()
    pygame.display.flip()

pygame.quit()
