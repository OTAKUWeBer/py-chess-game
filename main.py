import pygame
import os

# Start Pygame
pygame.init()

# Screen size and FPS
WIDTH, HEIGHT = 600, 600
FPS = 60

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

# Font for labels
font = pygame.font.SysFont("Arial", 18)

piece_image_path = "assets/pieces"

# Load pieces
def load_piece_images(color):
    return {
        "pawn": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-pawn.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "rook": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-rook.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "knight": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-knight.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "bishop": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-bishop.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "queen": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-queen.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "king": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-king.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    }

white_images = load_piece_images("white")
black_images = load_piece_images("black")

# Initial positions
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook'] + ['pawn'] * 8
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)] + [(i, 6) for i in range(8)]

black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook'] + ['pawn'] * 8
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)] + [(i, 1) for i in range(8)]

# Draw the chessboard with labels
def draw_chessboard_with_labels():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            x = X_OFFSET + col * SQUARE_SIZE
            y = Y_OFFSET + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            
            # Lable color
            label_color = BLACK if color == WHITE else WHITE
            
            # Draw labels
            if row == 7:  # Bottom row (letters)
                label = chr(97 + col)  # 'a' to 'h'
                label_surface = font.render(label, True, label_color)
                label_x = x + SQUARE_SIZE // 2 - label_surface.get_width() + 35
                label_y = y + SQUARE_SIZE - label_surface.get_height() -5
                screen.blit(label_surface, (label_x, label_y))

            if col == 0:  # Leftmost column (numbers)
                label = str(8 - row)  # '1' to '8'
                label_surface = font.render(label, True, label_color)
                label_x = x + 5  # Slight padding inside the square
                label_y = y + SQUARE_SIZE // 2 - label_surface.get_height() -10
                screen.blit(label_surface, (label_x, label_y))

# Draw pieces
def draw_pieces():
    for piece, location in zip(white_pieces, white_locations):
        x = X_OFFSET + location[0] * SQUARE_SIZE
        y = Y_OFFSET + location[1] * SQUARE_SIZE
        screen.blit(white_images[piece], (x, y))

    for piece, location in zip(black_pieces, black_locations):
        x = X_OFFSET + location[0] * SQUARE_SIZE
        y = Y_OFFSET + location[1] * SQUARE_SIZE
        screen.blit(black_images[piece], (x, y))

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Check if the ESC key is pressed
                running = False

    screen.fill((200, 200, 200))  # Background color
    draw_chessboard_with_labels()
    draw_pieces()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
