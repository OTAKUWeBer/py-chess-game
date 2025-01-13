import pygame
import os
import chess

# Start Pygame
pygame.init()

# Set the size of the screen and the frame rate
WIDTH, HEIGHT = 600, 600
FPS = 60

# Create the screen and set the title
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Two-player Chess")

# Colors for board and pieces
WHITE = (235, 236, 208)
BLACK = (115, 149, 82)
HIGHLIGHT = (255, 0, 0)  # Color to show valid moves
DOT_COLOR = (0, 255, 0)  # Color for move destination dots
LAST_MOVE_COLOR = (245,246,129,255)  # Yellow for last move background

# Chessboard setup
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8
X_OFFSET = (WIDTH - BOARD_SIZE) // 2  # Centering the board
Y_OFFSET = (HEIGHT - BOARD_SIZE) // 2  # Centering the board

# Font for labels on the board (like 'a', 'b', 'c', etc.)
font = pygame.font.SysFont("Arial", 18)

# Path to the folder where the piece images are stored
piece_image_path = "assets/pieces"

# Load piece images (like pawn, rook, etc.)
def load_piece_images(color):
    return {
        "pawn": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-pawn.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "rook": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-rook.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "knight": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-knight.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "bishop": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-bishop.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "queen": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-queen.png")), (SQUARE_SIZE, SQUARE_SIZE)),
        "king": pygame.transform.scale(pygame.image.load(os.path.join(piece_image_path, f"{color}-king.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    }

# Load both white and black piece images
white_images = load_piece_images("white")
black_images = load_piece_images("black")

# Initialize the chessboard with python-chess
board = chess.Board()

# Function to draw the chessboard and labels (like 'a', 'b', etc. for columns)
def draw_chessboard_with_labels(last_move=None):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK  # Alternate square colors
            x = X_OFFSET + col * SQUARE_SIZE
            y = Y_OFFSET + row * SQUARE_SIZE

            # If it's part of the last move, draw the background with a yellow color
            if last_move:
                from_square, to_square = last_move
                if chess.square(col, 7 - row) == from_square or chess.square(col, 7 - row) == to_square:
                    color = LAST_MOVE_COLOR  # Set the background color to yellow

            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            
            # Draw column letters at the bottom and row numbers on the left
            label_color = BLACK if color == WHITE else WHITE
            
            if row == 7:  # Letters 'a' to 'h'
                label = chr(97 + col)  # Convert number to letter (0 -> 'a', 1 -> 'b', ...)
                label_surface = font.render(label, True, label_color)
                label_x = x + SQUARE_SIZE // 2 - label_surface.get_width() + 35
                label_y = y + SQUARE_SIZE - label_surface.get_height() - 5
                screen.blit(label_surface, (label_x, label_y))

            if col == 0:  # Numbers '1' to '8'
                label = str(8 - row)  # Rows are numbered from 8 to 1
                label_surface = font.render(label, True, label_color)
                label_x = x + 5
                label_y = y + SQUARE_SIZE // 2 - label_surface.get_height() - 10
                screen.blit(label_surface, (label_x, label_y))

# Function to draw all the pieces on the board
def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            color = "white" if piece.color == chess.WHITE else "black"
            piece_type = piece.piece_type
            piece_name = {chess.PAWN: "pawn", chess.ROOK: "rook", chess.KNIGHT: "knight", chess.BISHOP: "bishop", chess.QUEEN: "queen", chess.KING: "king"}[piece_type]
            x = X_OFFSET + (square % 8) * SQUARE_SIZE
            y = Y_OFFSET + (7 - (square // 8)) * SQUARE_SIZE
            screen.blit(white_images[piece_name] if color == "white" else black_images[piece_name], (x, y))

# Function to highlight valid moves
def draw_valid_moves(valid_moves):
    for move in valid_moves:
        col, row = move % 8, 7 - (move // 8)  # Convert square to grid position
        x = X_OFFSET + col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = Y_OFFSET + row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(screen, DOT_COLOR, (x, y), 10)

# Function to handle mouse clicks
def handle_click(pos):
    global selected_square, valid_moves, last_move

    col, row = (pos[0] - X_OFFSET) // SQUARE_SIZE, (pos[1] - Y_OFFSET) // SQUARE_SIZE
    square = chess.square(col, 7 - row)  # Convert click position to board square

    if selected_square is None:
        piece = board.piece_at(square)
        if piece and piece.color == board.turn:  # If the piece belongs to the current player
            selected_square = square
            valid_moves = [move.to_square for move in board.legal_moves if move.from_square == selected_square]  # Get all valid moves for the piece
    else:
        # If a piece is selected and a valid move is clicked
        if square in valid_moves:
            move = chess.Move(selected_square, square)
            if move in board.legal_moves:
                board.push(move)  # Make the move
                last_move = (selected_square, square)  # Save the last move
            selected_square = None  # Deselect the piece
            valid_moves = []  # Clear valid moves
        else:
            selected_square = None  # Deselect if clicked somewhere invalid
            valid_moves = []  # Clear valid moves if no valid click

    return valid_moves

# Function to draw check or checkmate indicator
def draw_checkmate_indicator():
    if board.is_check():
        # Draw a red border around the king if it's in check
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.KING and piece.color == board.turn:
                col, row = square % 8, 7 - (square // 8)
                x = X_OFFSET + col * SQUARE_SIZE
                y = Y_OFFSET + row * SQUARE_SIZE
                pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE_SIZE, SQUARE_SIZE), 5)  # Red border

    if board.is_checkmate():
        # If it's checkmate, highlight the king's square in red
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.KING and piece.color == board.turn:
                col, row = square % 8, 7 - (square // 8)
                x = X_OFFSET + col * SQUARE_SIZE
                y = Y_OFFSET + row * SQUARE_SIZE
                pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE_SIZE, SQUARE_SIZE), 5)  # Red border for checkmate

# Function to display the win message when the game ends
def draw_win_message():
    if board.is_checkmate():
        winner = "White" if board.turn == chess.BLACK else "Black"
        message = f"{winner} wins!"
    elif board.is_stalemate():
        message = "Stalemate! It's a draw."
    else:
        return  # No message if the game is still ongoing

    # Create the message surface
    message_surface = font.render(message, True, (0, 0, 0))  # Black text
    message_width = message_surface.get_width()
    message_height = message_surface.get_height()

    # Positioning the message box and text
    box_x = WIDTH // 2 - message_width // 2 - 10
    box_y = HEIGHT // 2 - message_height // 2 - 10
    box_width = message_width + 20
    box_height = message_height + 20

    # Draw a white rectangle as the background for the message
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))

    # Draw the message text on top of the rectangle
    message_x = WIDTH // 2 - message_width // 2
    message_y = HEIGHT // 2 - message_height // 2
    screen.blit(message_surface, (message_x, message_y))

# Main game loop
clock = pygame.time.Clock()
running = True
selected_square = None  # Initialize the variable here
valid_moves = []
last_move = None  # Variable to store the last move

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Check if the ESC key is pressed
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left-click
                valid_moves = handle_click(event.pos)

    screen.fill((200, 200, 200))  # Set background color
    draw_chessboard_with_labels(last_move)  # Pass the last move to draw it
    draw_pieces()
    draw_valid_moves(valid_moves)  # Show valid move dots
    draw_checkmate_indicator()  # Show check or checkmate
    draw_win_message()
    pygame.display.flip()  # Update the screen
    clock.tick(FPS)

pygame.quit()  # Close Pygame when the game ends
