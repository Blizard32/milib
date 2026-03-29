import numpy as np


def eliminacion_gauss(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)
    for k in range(n-1):
        piv = np.argmax(np.abs(A[k:, k])) + k
        if A[piv, k] == 0:
            raise ValueError("Matriz singular")
        if piv != k:
            A[[k, piv]] = A[[piv, k]]
            b[[k, piv]] = b[[piv, k]]
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
            
    # Sustitucion regresiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x