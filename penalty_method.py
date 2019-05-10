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

# третье огрнаичение
def third_restriction_1(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 1)   # 2n

def third_restriction_2(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 2)   # 2n

def third_restriction_3(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 3)   # 2n

def third_restriction_4(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 4)   # 2n

def third_restriction_5(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 5)   # 2n

def third_restriction_6(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 6)   # 2n

def third_restriction_7(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 7)   # 2n

# ограничение для барьерной функции
def barrier_restriction(x, y):
    if g(x, y) <= 0:
        return -1 / g(x, y)
        #return -1E-5 * math.log(-g(x, y))
    else:
        return math.inf

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
    X_min_1 = findMinWithRestriction(f, first_restriction, X_0, 10, 10, EPS)
    print(X_min_1)
    X_min_2 = findMinWithRestriction(f, second_restriction, X_0, 10, 10, EPS)
    print(X_min_2)
    print()
    
    ###########################################################################
    X_min_3 = findMinWithRestriction(f, third_restriction_1, X_0, 10, 10, EPS)
    print(X_min_3)
    X_min_4 = findMinWithRestriction(f, third_restriction_2, X_0, 10, 10, EPS)
    print(X_min_4)
    X_min_5 = findMinWithRestriction(f, third_restriction_3, X_0, 10, 10, EPS)
    print(X_min_5)
    X_min_6 = findMinWithRestriction(f, third_restriction_4, X_0, 10, 10, EPS)
    print(X_min_6)
    X_min_7 = findMinWithRestriction(f, third_restriction_5, X_0, 10, 10, EPS)
    print(X_min_7)
    X_min_8 = findMinWithRestriction(f, third_restriction_6, X_0, 10, 10, EPS)
    print(X_min_8)
    X_min_9 = findMinWithRestriction(f, third_restriction_7, X_0, 10, 10, EPS)
    print(X_min_9)
    print()
    ###########################################################################
    
    X_min_barrier = findMinWithRestriction(f, barrier_restriction, X_0, 0.1, 0.1, EPS)
    print(X_min_barrier)
    
if __name__ == "__main__":
    main()