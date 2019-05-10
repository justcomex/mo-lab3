import math

import rosenbrock_method


EPS = 1E-7
X_0 = [-1, 0]
r_0 = 1


# первое ограничение
def first_restriction(x, y):
    if (y - x >= -1):
        return 0
    else:
        return -(y - x - 1)

# второе ограничение
def second_restriction(x, y):
    return abs(x + y)

def g(x, y):
    return 100*(x - y + 1)

# третье ограничение
def third_restriction(x, y):
    if g(x, y) <= 0:
        return -1 / g(x, y)
        #return -1E-5 * math.log(-g(x, y))
    else:
        return math.inf

# создать ограничение
def makeRestriction(n, g):
    return pow((g + abs(g)) / 2.0, 2 * n)

# функция, для которой необходимо найти минимум    
def f(x, y):
    return  2 * pow(x - y, 2) + 14 * pow(y - 3, 2)

# поиск минимума с ограничением
def findMinWithRestriction(f, restriction, x_0, r_0, C_0, eps):
    for i in range(100):
        res = rosenbrock_method.RosenbrockMethod(lambda x, y: f(x, y) + r_0 * restriction(x, y), X_0, [1, 0], [0, 1], eps)
        if r_0 * restriction(res[0], res[1]) < eps:
            return res, i + 1
        r_0 *= C_0
    return res, 100
        

def main():
    X_min = findMinWithRestriction(f, first_restriction, X_0, 10, 10, EPS)
    print(X_min)

    
if __name__ == "__main__":
    main()