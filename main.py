import numpy as np
from src import game_resolver


def main():
    matrix = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ])
    print(game_resolver.resolve(matrix))


if __name__ == '__main__':
    main()
