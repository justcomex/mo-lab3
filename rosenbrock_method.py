import copy
import math
import golden_section_method


# Вычисление нормы
def findNorm(V):
    return math.sqrt(V[0] ** 2 + V[1] ** 2)

# Условие выхода
def exitCondition(function, X1, X0, EPS):
    if math.fabs(function(X1[0], X1[1]) - function(X0[0], X0[1])) < EPS:
        return True
    elif math.fabs(X1[0] - X0[0]) < EPS and math.fabs(X1[1] - X0[1]) < EPS:
        return True
    return False

# Метод Розенброка
def RosenbrockMethod(function, X, S1, S2, EPS):
    FUNC_CALC = 0
    A = [[0, 0], [0, 0]]
    B = [0, 0]
    while True:
        X0 = copy.copy(X)

        L1, func_calc_L1 = golden_section_method.goldenSection(function, -1, X, S1, EPS)
        FUNC_CALC += func_calc_L1
        X[0] = X0[0] + L1 * S1[0]
        X[1] = X0[1] + L1 * S1[1]

        L2, func_calc_L2 = golden_section_method.goldenSection(function, 0, X, S2, EPS)
        FUNC_CALC += func_calc_L2
        X[0] = X[0] + L2 * S2[0]
        X[1] = X[1] + L2 * S2[1]

        A[0][0] = L1 * S1[0] + L2 * S2[0]
        A[0][1] = L1 * S1[1] + L2 * S2[1]

        if math.fabs(L1) >= math.fabs(L2):
            A[1][0] = L2 * S2[0]
            A[1][1] = L2 * S2[1]
        else:
            A[1][0] = L1 * S2[0]
            A[1][1] = L1 * S2[1]

        S1[0] = A[0][0] / findNorm(A[0])
        S1[1] = A[0][1] / findNorm(A[0])

        K = A[1][0] * S1[0] + A[1][1] * S1[1]
        B[0] = A[1][0] - K * S1[0]
        B[1] = A[1][1] - K * S1[1]

        S2[0] = B[0] / findNorm(B)
        S2[1] = B[1] / findNorm(B)

        if exitCondition(function, X, X0, EPS):
            break
    return X, FUNC_CALC
