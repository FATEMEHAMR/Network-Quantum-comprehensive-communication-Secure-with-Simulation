
from network_simulator import QuantumNetworkSimulator
from bb84_protocol import bb84_key_exchange
from qec_repetition_code import apply_repetition_code
from grover_pathfinder import grover_search
from depolarizing_channel import apply_depolarizing_noise
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt


def test_network_simulator():
    print("\n=== Test 1: Different Numbers of Bobs ===")
    for num_bobs in [1, 3, 5]:
        simulator = QuantumNetworkSimulator(num_bobs=num_bobs, depolarizing_error=0.05)
        print(f"Number of Bobs: {simulator.num_bobs}")
        simulator.run_simulation()

def test_depolarizing_error():
    print("\n=== Test 2: Different Depolarizing Error Rates ===")
    for error_rate in [0.0, 0.05, 0.2]:
        qc = QuantumCircuit(1)
        qc.x(0)  # Prepare |1>
        qc.measure_all()  # اضافه کردن مرحله‌ی اندازه‌گیری
        noisy_bit = apply_depolarizing_noise(qc, error_rate)
        print(f"Error rate {error_rate}: Measured bit = {noisy_bit}")

def test_bb84_key_lengths():
    print("\n=== Test 3: Different BB84 Key Lengths ===")
    for num_bits in [10, 50, 200]:
        key, qber = bb84_key_exchange(num_bits=num_bits)
        print(f"Key length {num_bits}: Key (first 20 bits) = {key[:20]}, QBER = {qber}")
def test_bb84_with_eve():
    print("\n=== Test 6: BB84 with Eavesdropper (Eve) ===")
    key, qber = bb84_key_exchange(num_bits=100, eavesdropper=True)
    print(f"Key (first 20 bits): {key[:20]}, QBER with Eve: {qber}")

def test_grover_search():
    print("\n=== Test 4: Grover Search ===")
    result = grover_search()
    print(f"Grover's search result: {result}")

def test_qec_module():
    print("\n=== Test 5: Quantum Error Correction ===")
    test_keys = ["000000", "111111", "101010"]
    for key in test_keys:
        corrected = apply_repetition_code(key)
        print(f"Original key: {key} --> Corrected key: {corrected}")
def test_qber_vs_error_rate():
    print("\n=== Test 7: QBER vs Depolarizing Error Rate ===")
    error_rates = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25]
    qber_values = []

    for rate in error_rates:
        total_qber = 0
        num_trials = 5  # چندین بار اجرا برای میانگین‌گیری
        for _ in range(num_trials):
            key, qber = bb84_key_exchange(num_bits=100, eavesdropper=True)
            total_qber += qber
        avg_qber = total_qber / num_trials
        qber_values.append(avg_qber)
        print(f"Error rate {rate}: Average QBER = {avg_qber:.2f}")

    plt.plot(error_rates, qber_values, marker='o')
    plt.xlabel('Depolarizing Error Rate')
    plt.ylabel('Average QBER')
    plt.title('QBER vs Depolarizing Error Rate (with Eve)')
    plt.grid(True)
    plt.savefig('qber_vs_error_rate.png')
    plt.show()
if __name__ == "__main__":
    test_network_simulator()
    test_depolarizing_error()
    test_bb84_key_lengths()
    test_bb84_with_eve()
    test_grover_search()
    test_qec_module()
    test_qber_vs_error_rate()
    print("\n All tests completed successfully!")
