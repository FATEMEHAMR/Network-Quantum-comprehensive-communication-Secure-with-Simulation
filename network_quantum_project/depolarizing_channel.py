from qiskit import QuantumCircuit
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import AerSimulator

def apply_depolarizing_noise(qc, error_rate):
    """
    Apply depolarizing noise to a quantum circuit.
    """
    noise_model = NoiseModel()

    # تک کیوبیتی
    single_qubit_error = depolarizing_error(error_rate, 1)
    noise_model.add_all_qubit_quantum_error(single_qubit_error, ['id', 'u1', 'u2', 'u3'])

    # دو کیوبیتی (مثلاً CNOT)
    two_qubit_error = depolarizing_error(error_rate, 2)
    noise_model.add_all_qubit_quantum_error(two_qubit_error, ['cx'])

    backend = AerSimulator()
    result = backend.run(qc, noise_model=noise_model, shots=1).result()
    counts = result.get_counts()
    measured_bit = int(list(counts.keys())[0][0])
    return measured_bit
