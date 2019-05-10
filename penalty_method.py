import math
import rosenbrock_method


# поиск минимума с ограничением
def findMinWithRestriction(f, restriction, x_0, r_0, C_0, eps):
    for i in range(100):
        res = rosenbrock_method.RosenbrockMethod(lambda x, y: f(x, y) + r_0 * restriction(x, y), x_0, [1, 0], [0, 1], eps)
        if r_0 * restriction(res[0], res[1]) < eps:
            return res, i + 1
        r_0 *= C_0
    return res, 100
        