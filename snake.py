snake_size = int(input())
nmoves = int(input())
moves = list(input() for _ in range(nmoves))

def shift(position, direction):
    if direction == "D": return position[0] + 1, position[1]
    elif direction == "G": return position[0] - 1, position[1]
    elif direction == "H": return position[0], position[1] - 1
    elif direction == "B": return position[0], position[1] + 1

snake = list((x, 0) for x in range(snake_size))
for move in moves:
    snake = snake[1:]
    snake.append(shift(snake[-1], move))
print(*snake[0])
