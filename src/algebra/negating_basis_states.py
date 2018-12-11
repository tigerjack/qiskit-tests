import numpy as np
from math import sqrt

### DEFAULT QUBITS AND GATES
H = np.array([[1, 1], [1, -1]]) / sqrt(2)
I = np.eye(2)
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
X = np.array([[0, 1], [1, 0]])
CX = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
CCX = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]])
Z = np.array([[1, 0], [0, -1]])
CZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])

q0 = np.array([1, 0])
q1 = np.array([0, 1])
plus = np.dot(H, q0)
minus = np.dot(H, q1)

### NON STANDARD BUT USEFUL GATES
IIH = np.kron(I, np.kron(I, H))

# 1st bit controlled, 2nd and 3rd control bits
XCC = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0]])
# 2nd bit controlled, 1st and 3rd control bits
CXC = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0]])


def negating_000():
    zzz = np.kron(q0, np.kron(q0, q0))
    XXX = np.kron(X, np.kron(X, X))
    print("Should be \n[-1, 0, 0, 0, 0, 0, 0, 0]")
    return XXX @ IIH @ CCX @ IIH @ XXX @ zzz


def negating_111():
    ooo = np.kron(q1, np.kron(q1, q1))
    print("Should be \n[0, 0, 0, 0, 0, 0, 0, -1]")
    return IIH @ CCX @ IIH @ ooo


def negating_001():
    zzo = np.kron(q0, np.kron(q0, q1))
    XXI = np.kron(X, np.kron(X, I))
    return XXI @ IIH @ CCX @ IIH @ XXI @ zzo


def negating_100():
    ozz = np.kron(q1, np.kron(q0, q0))
    HXX = np.kron(H, np.kron(X, X))
    return HXX @ XCC @ HXX @ ozz


def negating_010():
    zoz = np.kron(q0, np.kron(q1, q0))
    XHX = np.kron(X, np.kron(H, X))
    return XHX @ CXC @ XHX @ zoz


def negating_011():
    zoo = np.kron(q0, np.kron(q1, q1))
    XIH = np.kron(X, np.kron(I, H))
    return XIH @ CCX @ XIH @ zoo


def negating_110():
    ooz = np.kron(q1, np.kron(q1, q0))
    HIX = np.kron(H, np.kron(I, X))
    return HIX @ XCC @ HIX @ ooz


def negating_101():
    ozo = np.kron(q1, np.kron(q0, q1))
    IXI = np.kron(I, np.kron(X, I))
    IHI = np.kron(I, np.kron(H, I))
    return IXI @ IHI @ CXC @ IHI @ IXI @ ozo
