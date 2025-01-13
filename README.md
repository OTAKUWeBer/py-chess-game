# Two-player Chess Game

This is a simple two-player chess game built with Python using the `pygame` and `python-chess` libraries. It features a graphical chessboard, valid move highlighting, and basic game rules including check, checkmate, and stalemate detection.

## Features

- **Graphical Chessboard**: Interactive chessboard rendered using `pygame`.
- **Valid Move Highlighting**: Highlights all valid moves for the selected piece.
- **Check and Checkmate Indicators**: Displays visual indicators for check and checkmate scenarios.
- **Win or Draw Messages**: Displays the winner or a draw message when the game ends.
- **Fully Playable**: Supports all standard chess rules for two players.

## Prerequisites

To run this project, you need:

- Python 3.7 or higher
- `pygame` library
- `python-chess` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OTAKUWeBer/chess.git
   cd chess
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt   
   ```

3. Make sure to have the chess piece images in the `assets/pieces` directory:
   - `white-pawn.png`, `white-rook.png`, `white-knight.png`, `white-bishop.png`, `white-queen.png`, `white-king.png`
   - `black-pawn.png`, `black-rook.png`, `black-knight.png`, `black-bishop.png`, `black-queen.png`, `black-king.png`

## Usage

1. Run the game:
   ```bash
   python main.py
   ```

2. Play chess! Use the mouse to select and move pieces.

3. Press `Esc` to quit the game.

## How to Play

1. The game starts with the white player's turn.
2. Click on a piece to view its valid moves (highlighted with green dots).
3. Click on a valid destination square to move the selected piece.
4. The game detects check, checkmate, and stalemate scenarios.

## Game Controls

- **Left Mouse Click**: Select a piece and make moves.
- **Esc**: Quit the game.


## Contributing

Contributions are welcome! Feel free to submit a pull request or create an issue if you find any bugs or have feature suggestions.

