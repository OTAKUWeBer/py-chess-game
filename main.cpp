#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <iostream>
#include <map>
#include <string>

// Screen size
const int WIDTH = 600;
const int HEIGHT = 600;

// Colors
const SDL_Color WHITE = {235, 236, 208, 255};
const SDL_Color BLACK = {115, 149, 82, 255};

// Chessboard setup
const int BOARD_SIZE = 600;
const int SQUARE_SIZE = BOARD_SIZE / 8;
const int X_OFFSET = (WIDTH - BOARD_SIZE) / 2;
const int Y_OFFSET = (HEIGHT - BOARD_SIZE) / 2;

// Function to create an SDL_Rect
SDL_Rect createRect(int x, int y, int w, int h) {
    SDL_Rect rect;
    rect.x = x;
    rect.y = y;
    rect.w = w;
    rect.h = h;
    return rect;
}

int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        std::cerr << "SDL_Init Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    if (!(IMG_Init(IMG_INIT_PNG) & IMG_INIT_PNG)) {
        std::cerr << "IMG_Init Error: " << IMG_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("Two-player Chess", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        std::cerr << "SDL_CreateWindow Error: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        std::cerr << "SDL_CreateRenderer Error: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Load chess pieces
    std::map<std::string, SDL_Texture*> pieces;
    std::map<std::string, std::string> pieceFiles = {
        {"w_pawn", "assets/pieces/white-pawn.png"},
        {"w_rook", "assets/pieces/white-rook.png"},
        {"w_knight", "assets/pieces/white-knight.png"},
        {"w_bishop", "assets/pieces/white-bishop.png"},
        {"w_queen", "assets/pieces/white-queen.png"},
        {"w_king", "assets/pieces/white-king.png"},
        {"b_pawn", "assets/pieces/black-pawn.png"},
        {"b_rook", "assets/pieces/black-rook.png"},
        {"b_knight", "assets/pieces/black-knight.png"},
        {"b_bishop", "assets/pieces/black-bishop.png"},
        {"b_queen", "assets/pieces/black-queen.png"},
        {"b_king", "assets/pieces/black-king.png"}
    };

    for (const auto& [name, path] : pieceFiles) {
        SDL_Surface* surface = IMG_Load(path.c_str());
        if (!surface) {
            std::cerr << "IMG_Load Error: " << IMG_GetError() << std::endl;
            continue;
        }
        SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, surface);
        SDL_FreeSurface(surface);
        if (!texture) {
            std::cerr << "SDL_CreateTextureFromSurface Error: " << SDL_GetError() << std::endl;
            continue;
        }
        pieces[name] = texture;
    }

    // Initial positions of pieces on the chessboard
    std::map<std::pair<int, int>, std::string> initialPositions = {
        {{0, 0}, "b_rook"}, {{0, 1}, "b_knight"}, {{0, 2}, "b_bishop"}, {{0, 3}, "b_queen"},
        {{0, 4}, "b_king"}, {{0, 5}, "b_bishop"}, {{0, 6}, "b_knight"}, {{0, 7}, "b_rook"},
        {{1, 0}, "b_pawn"}, {{1, 1}, "b_pawn"}, {{1, 2}, "b_pawn"}, {{1, 3}, "b_pawn"},
        {{1, 4}, "b_pawn"}, {{1, 5}, "b_pawn"}, {{1, 6}, "b_pawn"}, {{1, 7}, "b_pawn"},
        {{6, 0}, "w_pawn"}, {{6, 1}, "w_pawn"}, {{6, 2}, "w_pawn"}, {{6, 3}, "w_pawn"},
        {{6, 4}, "w_pawn"}, {{6, 5}, "w_pawn"}, {{6, 6}, "w_pawn"}, {{6, 7}, "w_pawn"},
        {{7, 0}, "w_rook"}, {{7, 1}, "w_knight"}, {{7, 2}, "w_bishop"}, {{7, 3}, "w_queen"},
        {{7, 4}, "w_king"}, {{7, 5}, "w_bishop"}, {{7, 6}, "w_knight"}, {{7, 7}, "w_rook"}
    };

    // Main game loop
    bool running = true;
    SDL_Event event;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            } else if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym == SDLK_ESCAPE) {
                    running = false;
                }
            }
        }

        // Clear screen
        SDL_SetRenderDrawColor(renderer, 200, 200, 200, 255);
        SDL_RenderClear(renderer);

        // Draw chessboard
        for (int row = 0; row < 8; ++row) {
            for (int col = 0; col < 8; ++col) {
                SDL_Color color = (row + col) % 2 == 0 ? WHITE : BLACK;
                SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, color.a);
                SDL_Rect rect = createRect(X_OFFSET + col * SQUARE_SIZE, Y_OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
                SDL_RenderFillRect(renderer, &rect);
            }
        }

        // Draw pieces
        for (const auto& [pos, piece] : initialPositions) {
            int row = pos.first;
            int col = pos.second;
            if (pieces.find(piece) != pieces.end()) {
                SDL_Rect dstRect = createRect(X_OFFSET + col * SQUARE_SIZE, Y_OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
                SDL_RenderCopy(renderer, pieces[piece], nullptr, &dstRect);
            }
        }

        SDL_RenderPresent(renderer);
    }

    // Clean up
    for (auto& [name, texture] : pieces) {
        SDL_DestroyTexture(texture);
    }
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    IMG_Quit();
    SDL_Quit();

    return 0;
}
