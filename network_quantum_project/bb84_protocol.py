import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def prepare_bb84_qubit(bit, basis):
    qc = QuantumCircuit(1, 1)
    if bit == 1:
        qc.x(0)
    if basis == 'X':
        qc.h(0)
    return qc

def measure_bb84_qubit(qc, basis):
    if basis == 'X':
        qc.h(0)
    qc.measure(0, 0)
    backend = AerSimulator()
    result = backend.run(qc, shots=1).result()
    counts = result.get_counts()
    measured_bit = int(list(counts.keys())[0])
    return measured_bit

def bb84_key_exchange(num_bits=100, eavesdropper=False, shots=1):
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.choice(['Z', 'X'], size=num_bits)
    bob_bases = np.random.choice(['Z', 'X'], size=num_bits)
    key_bits = []
    error_count = 0

    backend = AerSimulator()

    for i in range(num_bits):
        bit = alice_bits[i]
        basis = alice_bases[i]
        qc = prepare_bb84_qubit(bit, basis)

        if eavesdropper:
            eve_basis = np.random.choice(['Z', 'X'])
            eve_measurement = measure_bb84_qubit(qc.copy(), eve_basis)
            qc = prepare_bb84_qubit(eve_measurement, eve_basis)

        measured_bit = measure_bb84_qubit(qc, bob_bases[i])

        if alice_bases[i] == bob_bases[i]:
            key_bits.append(measured_bit)
            if measured_bit != alice_bits[i]:
                error_count += 1

    key = ''.join(str(bit) for bit in key_bits)
    qber = error_count / len(key_bits) if len(key_bits) > 0 else 0
    return key, qber
