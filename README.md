# Network-Quantum-comprehensive-communication-Secure-with-Simulation
## Overview

This project is a Quantum Network Simulator built with Python and Qiskit that models secure quantum communications and fundamental quantum networking concepts. It integrates BB84 Quantum Key Distribution (QKD), Quantum Error Correction (QEC), Grover’s search algorithm for pathfinding, depolarizing noise modeling, and an eavesdropping simulation (Eve) — all within a modular simulation environment.

The simulator demonstrates how quantum principles can secure communications, handle noise, correct errors, and optimize routing — forming a comprehensive educational and experimental tool for quantum networking research.

## Features

 BB84 Protocol Implementation – Secure quantum key distribution between sender (Alice) and receivers (Bobs).

 3-Qubit Repetition Code – Basic quantum error correction scheme to mitigate noise.

 Grover’s Search Algorithm – Demonstrates quantum speedup for pathfinding in network routing.

Depolarizing Channel Simulation – Models real-world noise and its effects on quantum communications.

 Eavesdropper Simulation (Eve) – Tests BB84’s security by introducing quantum bit errors (QBER) due to interception.

 QBER Analysis Tools – Plots and analyzes QBER against varying depolarizing error rates.

## Project Objectives

Design and implement a simulator for qubit transmission in a quantum network.

Implement secure quantum key distribution with BB84.

Integrate noise modeling via a depolarizing channel.

Apply quantum error correction using the 3-qubit repetition code.

Demonstrate quantum search/pathfinding with Grover’s algorithm.

Visualize and analyze QBER under different conditions, including eavesdropping.

## Project Structure
├── network-simulator.py        # Main simulator class and execution logic
├── bb84-protocol.py            # BB84 QKD implementation (with optional Eve)
├── depolarizing-channel.py     # Noise model simulation
├── test-simulation.py          # Unit tests and QBER analysis tools
├── qber_vs_error_rate.png      # Example QBER graph output
└── README.md                   # Project documentation

## Installation & Usage
1. Clone the Repository
git clone https://github.com/your-username/quantum-network-simulator.git
cd quantum-network-simulator

2. Install Dependencies

Make sure you have Python 3.8+ and Qiskit installed:

pip install qiskit matplotlib numpy

3. Run the Simulator
python network-simulator.py

4. Run QBER Analysis Tests
python test-simulation.py

## Example Outputs
## Simulation Results

BB84 Secure Key: Generated successfully when no eavesdropper is present.

Quantum Error Rate (QBER): ~0.0 without Eve; increases to ~0.22 when Eve is active.

Noise Modeling: QBER fluctuates (~0.20–0.28) under varying depolarizing noise.

Grover’s Algorithm: Correctly identifies marked states for routing.

## QBER vs Depolarizing Error Rate

The graph below shows how QBER changes with noise in the presence of an eavesdropper:

0.0  → 0.24  
0.05 → 0.20  
0.10 → 0.26  
0.15 → 0.28  
0.20 → 0.22  
0.25 → 0.26

## Key Takeaways

Security Validation: The BB84 protocol detects eavesdropping through measurable increases in QBER.

Error Correction: The 3-qubit repetition code mitigates noise effects, enhancing reliability.

Noise Impact: Depolarizing noise impacts transmission quality, highlighting the importance of QEC.

Quantum Advantage: Grover’s algorithm demonstrates potential for efficient network routing.

Sophisticated QEC Codes: Integrate more advanced error correction codes like Shor's code or surface codes for greater fault tolerance.

Entanglement-Based Protocols: Expand the simulator to include entanglement distribution protocols (e.g., E91) to reflect modern quantum networking research.
