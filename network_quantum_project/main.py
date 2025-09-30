


from network_simulator import QuantumNetworkSimulator

def main():
    # Number of receiver nodes (Bobs)
    num_bobs = 3
    # Depolarizing error rate
    depolarizing_error = 0.05

    # Initialize the quantum network simulator
    simulator = QuantumNetworkSimulator(num_bobs=num_bobs, depolarizing_error=depolarizing_error)

    # Run the simulation
    simulator.run_simulation()

if __name__ == "__main__":
    main()
