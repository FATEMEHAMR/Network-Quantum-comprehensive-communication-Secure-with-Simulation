

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def grover_search():
    """
    Demonstration of Grover’s algorithm to find a marked state.
    """
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])        # Apply Hadamard to both qubits
    qc.cz(0, 1)         # Oracle (dummy)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])

    backend = AerSimulator()
    result = backend.run(qc, shots=1).result()
    counts = result.get_counts()
    marked_state = list(counts.keys())[0]
    return marked_state
