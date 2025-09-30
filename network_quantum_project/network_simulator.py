

from bb84_protocol import bb84_key_exchange
from qec_repetition_code import apply_repetition_code
from depolarizing_channel import apply_depolarizing_noise
from grover_pathfinder import grover_search

class QuantumNetworkSimulator:
    def __init__(self, num_bobs, depolarizing_error=0.05):
        self.num_bobs = num_bobs
        self.depolarizing_error = depolarizing_error

    def run_simulation(self):
        print(" Quantum Network Simulation Started!")
        print(f" Number of Bobs: {self.num_bobs}")
        print(f"⚠ Depolarizing error rate: {self.depolarizing_error}")

        # 1. Run Grover's algorithm to find optimal path (mock demonstration)
        print("\n Running Grover's algorithm for pathfinding...")
        grover_result = grover_search()
        print(f" Grover's algorithm result: {grover_result}")

        # 2. Run BB84 Protocol
        print("\n🔑 Running BB84 QKD Protocol...")
        key, qber = bb84_key_exchange(num_bits=100)
        print(f" BB84 Key Generated: {key[:20]}... (showing first 20 bits)")
        print(f" Estimated QBER: {qber}")

        # 3. Apply Quantum Error Correction
        print("\n🛠 Applying Quantum Error Correction...")
        corrected_key = apply_repetition_code(key)
        print(f" Corrected Key: {corrected_key[:20]}... (showing first 20 bits)")

        print("\n Simulation Completed Successfully!")
