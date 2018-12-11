from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.tools.visualization import circuit_drawer
import sys

def usage():
    print("""Parameters:
            o/a for OR or AND function
            0/1 the value of 1st qubit
            0/1 the value of 2nd qubit""")

def cs_and(q0, q1):
    # qr[2] = 0 to compute qr[0] AND qr[1] on qr[2]
    # qr[0] and qr[1] can be chosen arbitrarily

    # qc.x(qr[0])
    if(q0): # q0 = 1
        qc.x(qr[0])
    if(q1):
        qc.x(qr[1])
    print("AND, result on q2")


def cs_or(q0, q1):
    # qr[2] = 1 to compute qr[0] OR qr[1] on qr[1]
    # qr[0] and qr[1] can be chosen arbitrarily
    qc.x(qr[2])
    if(q0): # q0 = 1
        qc.x(qr[0])
    if(q1):
        qc.x(qr[1])
    print("OR, result on q1")


if (len(sys.argv) < 4):
    usage()
    exit()

#Create a Quantum Register with 2 qubits.
qr = QuantumRegister(3)
# Create a Classical Register with 2 bits.
cr = ClassicalRegister(3)
# Create a Quantum Circuit
qc = QuantumCircuit(qr, cr)

c = sys.argv[1]
if c == 'a':
    cs_and(sys.argv[2] == '1', sys.argv[3] == '1')
    append = "_and"
elif c == 'o':
    cs_or(sys.argv[2] == '1', sys.argv[3] == '1')
    append = "_or"
else:
    sys.exit("Error choice")

qc.cswap(qr[0], qr[1], qr[2])

qc.measure(qr, cr)
circuit_drawer(qc, filename="imgs/swap" + append + ".png")

backend = Aer.get_backend('qasm_simulator')

job = execute(qc, backend=backend)
result = job.result()
print(result.get_counts(qc))
