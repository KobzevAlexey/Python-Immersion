from my_games.chess import *

if __name__ == "__main__":
    successful_placements = 0
    while successful_placements < 4:
        queen = generate_random_placement(8)
        if is_queen_safe(queen):
            print("Успешная расстановка:", queen)
            successful_placements += 1