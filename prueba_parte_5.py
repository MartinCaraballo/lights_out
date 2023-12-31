import numpy as np



matriz = np.array([
    [1,1,0,1,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,0],
    [0,1,1,0,0,1,0,0,0],
    [1,0,0,1,1,0,1,0,0],
    [0,1,0,1,1,1,0,1,0],
    [0,0,1,0,1,1,0,0,1],
    [0,0,0,1,0,0,1,1,0],
    [0,0,0,0,1,0,1,1,1],
    [0,0,0,0,0,1,0,1,1]
])

x = np.array([[0], [0], [0], [0], [1], [0], [0], [0], [1]])

print(np.transpose(np.dot(matriz, x)))
