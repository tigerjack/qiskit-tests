import numpy as np
from math import sqrt, cos, sin

# basis qubit
zero = np.array([1, 0])
one = np.array([0, 1])
# I
I = np.eye(2)
# Hadamard
H = np.array([[1, 1], [1, -1]]) * 1/sqrt(2)
# plus/minus basis states
plus = np.dot(H, zero)
minus = np.dot(H, one)

# swap qubits q0 and q1
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
# negate qubit
X = np.array([[0, 1], [1, 0]])
# controlled not, first bit is control, second is controlled
CX = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# CCNOT, first two bit are control, thirs is controlled
CCX = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]])
# Y gate
Y = np.array([[0, 0.-1.j], [0.+1.j, 0]], dtype=np.complex_)
# Z and controlled Z gate
Z = np.array([[1, 0], [0, -1]])
CZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])

# sqrt(swap)
SWAP_SQRT = np.array([[1, 0, 0, 0], [0, 0.5+0.5j, 0.5-0.5j, 0], 
                      [0, 0.5-0.5j, 0.5+0.5j, 0], [0, 0, 0, 1]])
# sqrt(not)
X_SQRT = np.array([[1.+1.j, 1.-1.j], [1.-1.j, 1.+1.j]])

# controller_list is a list of number telling use which bit are the controller
# f.e. for a CCX, we have 0, 1 controller and 2 controlled
def controlled_not(controller_list, controlled_bit):
    # the total number of qubits
    n = len(controller_list)+1
    print(n)
    iden = np.eye(2**n)
    row_tmp = 0
    for i, v in enumerate(controller_list):
        row_tmp += 2**(n-v-1)
    tmp = 2**(n-controlled_bit-1)
    print("Exchanging row {0} and {1}".format(row_tmp, row_tmp + tmp))
    iden[[row_tmp, row_tmp+tmp]] = iden[[row_tmp+tmp, row_tmp]]
    return iden

# s gate
def phase_shift(phase):
   return np.array([[1, 0], [0, cos(phase) + sin(phase)*1.j]])
