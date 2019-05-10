import math


# Метод золотого сечения для одномерного поиска
def goldenSection(function, l0, X, S, EPS):
    interval = searchSection(function, l0, X, S)
    if interval[1] >= interval[0]:
        b = interval[1]
        a = interval[0]
    else:
        a = interval[1]
        b = interval[0]
    lenOfSection = b - a
    l1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
    l2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
    f1 = function(X[0] + l1 * S[0], X[1] + l1 * S[1])
    f2 = function(X[0] + l2 * S[0], X[1] + l2 * S[1])
    while lenOfSection > EPS:
        if f1 > f2:
            a = l1
            l1 = l2
            l2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
            f1 = f2
            f2 = function(X[0] + l2 * S[0], X[1] + l2 * S[1])
        else:
            b = l2
            l2 = l1
            l1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
            f2 = f1
            f1 = function(X[0] + l1 * S[0], X[1] + l1 * S[1])
        lenOfSection = b - a
    return (b + a) / 2

# Поиск отрезка, содержащий минимум 
def searchSection(function, l0, X, S):
    delta = 0.001
    l1 = 0
    h = 0
    f0 = function(X[0] + l0 * S[0], X[1] + l0 * S[1])
    if f0 > function(X[0] + (l0 + delta) * S[0], X[1] + (l0 + delta) * S[1]):
        l1 = l0 + delta
        h = delta
    elif f0 > function(X[0] + (l0 - delta) * S[0], X[1] + (l0 - delta) * S[1]):
        l1 = l0 - delta
        h = - delta
    else:
        return l0 - delta, l0 + delta
    h = 2 * h
    f1 = function(X[0] + l1 * S[0], X[1] + l1 * S[1])
    l2 = l1 + h
    f2 = function(X[0] + l2 * S[0], X[1] + l2 * S[1])
    while f1 > f2:
        l0 = l1
        f0 = f1
        l1 = l2
        f1 = f2
        h = 2 * h
        l2 = l1 + h
        f2 = function(X[0] + l2 * S[0], X[1] + l2 * S[1])
    return l0 - h / 2, l2