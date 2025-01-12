import pygame
import os

# Start Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 600

# Create screen and set title
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Two-player Chess")

# Colors
WHITE = (235, 236, 208, 255)
BLACK = (115, 149, 82, 255)

# Chessboard setup
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8
X_OFFSET = (WIDTH - BOARD_SIZE) // 2
Y_OFFSET = (HEIGHT - BOARD_SIZE) // 2

# Load pieces
pieces = {}
for name, (filename, size) in {
    "w_pawn": ("pawn-w.png", SQUARE_SIZE),
    "w_rook": ("rook-w.png", SQUARE_SIZE),
    "w_knight": ("knight-w.png", SQUARE_SIZE),
    "w_bishop": ("bishop-w.png", SQUARE_SIZE),
    "w_queen": ("queen-w.png", SQUARE_SIZE),
    "w_king": ("king-w.png", SQUARE_SIZE),
    "b_pawn": ("pawn-b.png", SQUARE_SIZE),
    "b_rook": ("rook-b.png", SQUARE_SIZE),
    "b_knight": ("knight-b.png", SQUARE_SIZE),
    "b_bishop": ("bishop-b.png", SQUARE_SIZE),
    "b_queen": ("queen-b.png", SQUARE_SIZE),
    "b_king": ("king-b.png", SQUARE_SIZE),
}.items():
    image_path = os.path.join("assets/pieces", filename)  # Ensure the path to images is correct
    image = pygame.image.load(image_path)
    pieces[name] = pygame.transform.scale(image, (size, size))  # Scale the image to fit the square

# Initial positions of pieces on the chessboard
initial_positions = {
    (0, 0): "b_rook", (0, 1): "b_knight", (0, 2): "b_bishop", (0, 3): "b_queen",
    (0, 4): "b_king", (0, 5): "b_bishop", (0, 6): "b_knight", (0, 7): "b_rook",
    (1, 0): "b_pawn", (1, 1): "b_pawn", (1, 2): "b_pawn", (1, 3): "b_pawn",
    (1, 4): "b_pawn", (1, 5): "b_pawn", (1, 6): "b_pawn", (1, 7): "b_pawn",
    (6, 0): "w_pawn", (6, 1): "w_pawn", (6, 2): "w_pawn", (6, 3): "w_pawn",
    (6, 4): "w_pawn", (6, 5): "w_pawn", (6, 6): "w_pawn", (6, 7): "w_pawn",
    (7, 0): "w_rook", (7, 1): "w_knight", (7, 2): "w_bishop", (7, 3): "w_queen",
    (7, 4): "w_king", (7, 5): "w_bishop", (7, 6): "w_knight", (7, 7): "w_rook",
}

# Draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            x = X_OFFSET + col * SQUARE_SIZE
            y = Y_OFFSET + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces on the board
def draw_pieces():
    for (row, col), piece in initial_positions.items():
        x = X_OFFSET + col * SQUARE_SIZE
        y = Y_OFFSET + row * SQUARE_SIZE
        screen.blit(pieces[piece], (x, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))  # Background color
    draw_chessboard()
    draw_pieces()
    pygame.display.flip()

pygame.quit()
