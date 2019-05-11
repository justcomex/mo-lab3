import math
import penalty_method


EPS = 1E-7
X_0 = [0,1]


# первое ограничение
def first_penalty_restriction(x, y):
    if (y - x >= -1):
        return 0
    else:
        return -(y - x + 1)

# второе ограничение
def second_penalty_restriction(x, y):
    return abs(x + y)

def g(x, y):
    #return 100 * (x - y - 1)
    return x - y - 1


# вариации третьего ограничения
def third_penalty_restriction_1(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 1)   # 2n, n = 1

def third_penalty_restriction_2(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 2)   # 2n, n = 2

def third_penalty_restriction_3(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 3)   # 2n, n = 3

def third_penalty_restriction_4(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 4)   # 2n, n = 4

def third_penalty_restriction_5(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 5)   # 2n, n = 5

def third_penalty_restriction_6(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 6)   # 2n, n = 6

def third_penalty_restriction_7(x, y):
    return pow((g(x, y) + abs(g(x, y))) / 2.0, 2 * 7)   # 2n, n = 7


# ограничение для барьерной функции
def first_barrier_restriction(x, y):
    if g(x, y) <= 0:
        #return -1E-5 * math.log(-g(x, y))
        return -math.log(-g(x, y))
    else:
        return math.inf
    
# ограничение для барьерной функции
def second_barrier_restriction(x, y):
    if g(x, y) <= 0:
        return -1 / g(x, y)
    else:
        return math.inf


# функция, для которой необходимо найти минимум    
def f(x, y):
    return  2 * pow(x - y, 2) + 14 * pow(y - 3, 2)


# главная функция
def main():
    
    print("Check penalty method with two different restrictions: ")
    X_min_1 = penalty_method.findMinWithRestriction(f, first_penalty_restriction, X_0, 30, 10, EPS)
    print(X_min_1)
    X_min_2 = penalty_method.findMinWithRestriction(f, second_penalty_restriction, X_0, 5, 5, EPS)
    print(X_min_2)
    print()
    
    print("Penalty change strategy for n = 1..7:")
    X_min_3 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_1, X_0, 10, 10, EPS)
    print(X_min_3)
    X_min_4 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_2, X_0, 10, 10, EPS)
    print(X_min_4)
    X_min_5 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_3, X_0, 10, 10, EPS)
    print(X_min_5)
    X_min_6 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_4, X_0, 10, 10, EPS)
    print(X_min_6)
    X_min_7 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_5, X_0, 10, 10, EPS)
    print(X_min_7)
    X_min_8 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_6, X_0, 10, 10, EPS)
    print(X_min_8)
    X_min_9 = penalty_method.findMinWithRestriction(f, third_penalty_restriction_7, X_0, 10, 10, EPS)
    print(X_min_9)
    print()
    
    print("Check barrier method with two different restrictions: ")
    X_min_barrier_1 = penalty_method.findMinWithRestriction(f, first_barrier_restriction, X_0, 1E-1, 1E-1, EPS)
    print(X_min_barrier_1)
    X_min_barrier_2 = penalty_method.findMinWithRestriction(f, second_barrier_restriction, X_0, 1E-1, 1E-1, EPS)
    print(X_min_barrier_2)

    
if __name__ == "__main__":
    main()