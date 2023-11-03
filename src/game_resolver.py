import numpy as np


def resolve(game_matrix):
    """
    Función para resolver el juego lights out!.
    :param game_matrix: Matriz con el estado inicial del juego.
    :return: Solución indicando las luces que se deben cambiar de estado para ganar.
    """
    # Si las luces empiezan todas apagadas.
    if check_game_status(game_matrix) is True:
        return 'Las luces ya están todas apagadas.'
    game_matrix_shape = np.shape(game_matrix)
    # Si la matrix no es cuadrada.
    if game_matrix_shape[0] != game_matrix_shape[1]:
        return 'La matriz no es cuadrada.'

    # Lista con todas las ecuaciones posibles.
    equations: [([int], int)] = [() for i in range(game_matrix_shape[0] ** 2)]
    # Bucle para recorrer la matriz y generar las ecuaciones.
    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[0])):
            neighbors = get_neighbor_indexes(len(game_matrix), len(game_matrix[0]), i, j)
            equation: [int] = [0 for i in range(game_matrix_shape[0] ** 2)]
            equation_index: int = get_vector_index(len(game_matrix), i, j)
            equation[equation_index] = 1
            for row, column in neighbors:
                element_index = get_vector_index(game_matrix_shape[0], row, column)
                equation[element_index] = 1

            light_value = game_matrix[i][j]
            equations[equation_index] = (equation, light_value)

    # Lista de ecuaciones
    equation_list = []
    # Lista de valores de luces
    lights_values = []
    for i in range(len(equations)):
        eq, val = equations[i]
        equation_list.append(eq)
        lights_values.append([val])

    matrix_a = np.array(equation_list)
    matrix_b = np.array(lights_values)
    matrix_to_resolve = np.concatenate((matrix_a, matrix_b), axis=1)

    return solve_by_gauss_method(matrix_to_resolve)


def get_neighbor_indexes(rows: int, columns: int, row_element_index: int, column_element_index: int):
    """
    Función para obtener todos los indices de los elementos vecinos a una coordenada especificada.
    :param rows: cantidad de filas de la matriz
    :param columns: cantidad de columnas de la matriz
    :param row_element_index: indice en la fila del elemento a evaluar
    :param column_element_index: indice en la columna del elemento a evaluar
    :return: Matriz con los indices de los elementos vecinos.
    """
    if (0 > row_element_index > rows - 1) and (0 > column_element_index > columns - 1):
        return None

    if row_element_index == 0 or row_element_index == rows - 1:
        if column_element_index == 0 or column_element_index == columns - 1:
            num_neighbors = 2
        else:
            num_neighbors = 3
    else:
        if column_element_index == 0 or column_element_index == columns - 1:
            num_neighbors = 3
        else:
            num_neighbors = 4

    neighbor_positions: [[int]] = [[0, 0] for i in range(num_neighbors)]
    position_index: int = 0
    # primero se fija a la izquierda, luego derecha, luego arriba y por ultimo abajo.
    valid_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for direction in valid_directions:
        i, j = direction
        if 0 <= row_element_index + i < rows and 0 <= column_element_index + j < columns:
            neighbor_positions[position_index][0] = row_element_index + i
            neighbor_positions[position_index][1] = column_element_index + j
            position_index += 1

    return neighbor_positions


def solve_by_gauss_method(matrix):
    """
    Función para resolver el sistema de ecuaciones a través de una modificación del algoritmo de escalerización
    Gaussiana
    :param matrix: Matrix preparada para resolver.
    :return: Matriz con la solución del sistema
    """
    n = np.shape(matrix)[0]
    for i in range(n - 1):
        for k in range(i + 1, n):
            # Realizar la eliminación hacia adelante sin pivoteo
            if matrix[i, i] != 0:
                # suma binaria
                matrix[k, :] = (matrix[k, :] + matrix[i, :]) % 2

    x = np.zeros(n, dtype=int)

    for i in range(n - 1, -1, -1):
        suma = 0
        for j in range(i + 1, n - 1):
            # suma binaria
            suma = (suma + matrix[i, j] * x[j]) % 2
        b = matrix[i, n - 1]
        # resta y suma binaria
        x[i] = (b - suma) % 2

    x = np.transpose([x])
    return x


def check_game_status(matrix) -> bool:
    """
    Chequea si todas las luces estan apagadas o no.
    :param matrix: Matriz a chequear
    :return: True si estan todas apagadas, False de caso contrario.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                return False
    return True


def get_vector_index(matrix_shape: int, row_element_index: int, column_element_index: int) -> int:
    """
    Función para obtener el indice de la matriz representada como vector de una dimensión.
    :param matrix_shape: Tamaño de la matriz.
    :param row_element_index: Indice del elemento en la fila.
    :param column_element_index: Indice del elemento en la columna.
    :return: El indice del elemento de la matriz en una representación como vector.
    """
    return matrix_shape * row_element_index + column_element_index
