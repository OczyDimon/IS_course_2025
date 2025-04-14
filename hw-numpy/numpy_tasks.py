import numpy as np


def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)


def cyclic123_array(n): 
    """2. Генерирует numpy массив длины  3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)


def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)


def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    m = np.ones((n, n))
    m[1:-1, 1:-1] = 0
    return m


def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    m = np.zeros((n, n))
    m[::2, ::2] = 1
    m[1::2, 1::2] = 1
    return m


def matrix_with_sum_index(n):
    """6. Создаёт 𝑛 × 𝑛  матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    v = np.arange(n)
    return np.add.outer(v, v)


def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    cosx = np.cos(np.arange(a, b, dx))
    sinx = np.sin(np.arange(a, b, dx))
    return np.array([cosx, sinx])


def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    return np.mean(A), np.sum(A, axis=0), np.sum(A, axis=1)


def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[np.argsort(A[:, j])]


def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:  
    method == 'rectangular' - методом прямоугольника   
    method == 'trapezoidal' - методом трапеций   
    method == 'simpson' - методом Симпсона  
    """
    match method:
        case 'rectangular':
            return np.sum(f(np.arange(a, b, dx))) * dx
        case 'trapezoidal':
            return np.sum((f(np.arange(a, b, dx)) + f(np.arange(a + dx, b + dx/2, dx))) * dx / 2)
        case 'simpson':
            return np.sum((f(np.arange(a, b, dx))
                           + 4*f(np.arange(a + dx/2, b + dx/2, dx)) + f(np.arange(a + dx, b + dx/2, dx))) * dx / 6)

