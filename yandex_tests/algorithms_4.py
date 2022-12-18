"""
Задача комивояжeра. Библиотека python-tsp
https://www.youtube.com/watch?v=08AotAknAqc
"""
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = np.array([[0, 8, 4, 10],
                           [8, 0, 7, 5],
                           [4, 7, 0, 3],
                           [10, 5, 3, 0]])

path, distance = solve_tsp_dynamic_programming(distance_matrix)

print(path, distance)
