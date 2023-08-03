import random


def is_queen_safe(queen):
    for i in range(len(queen)):
        for j in range(i + 1, len(queen)):
            x1, y1 = queen[i]
            x2, y2 = queen[j]

            if x1 == x2 or y1 == y2:
                return False
            if abs(x1 - x2) == abs(y1 - y2):
                return False

    return True


def generate_random_placement(n):
    queen = []
    for i in range(n):
        x = i + 1
        y = random.randint(1, n)
        queen.append((x, y))
    return queen

