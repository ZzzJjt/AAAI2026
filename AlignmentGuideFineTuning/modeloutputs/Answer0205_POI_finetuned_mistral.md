### Intent:
**Intent Summary:**  
Develop an ANN-based temperature control system for a chemical reactor that outperforms traditional PID control by handling nonlinear dynamics and disturbances, using Python to simulate the reactor, train the neural network, and compare controller performance.  

*(Focus: ANN-driven process control for reactors with disturbance rejection, coded in Python)*

### Prompt:
**Model Predictive Control for Continuous Cellulose Fiber Production Using Python:**

Explain how model predictive control (MPC) can optimize cellulose fiber production from wood, where continuous infeed and outfeed operations are required, while the material undergoes a two-stage batch process. The material is supplied at an average rate of 50 tons per hour, undergoing pre-treatment in a reactor followed by homogenization before entering a 1,000 cubic meter buffer tank. The product is extracted from the tank on demand, not at a constant rate. To minimize downtime in downstream processes, a high fill level in the tank must be maintained, despite the two-hour delay caused by upstream batch processes, making PID control unsuitable.

Develop Python code to simulate the system dynamics, including the dead time and fluctuating demand.

Implement Python code for a model predictive control (MPC) algorithm to optimize material flow, taking into account the time delay, fluctuating demand, and operational constraints.

**C-A-R-E:**

🟥 C（Context）

In continuous cellulose fiber production from wood, material is fed at a steady rate of 50 tons/hour into a two-stage batch process (pre-treatment and homogenization) before being stored in a 1,000 m³ buffer tank. However, due to the batch process and a two-hour upstream delay, while the product outflow from the tank is variable and demand-driven, traditional PID control cannot ensure consistent performance. This can result in low tank levels and potential downstream process interruptions.

🟩 A（Action）

Explain how model predictive control (MPC) can effectively manage this production challenge by accounting for process delays and demand fluctuations. Then, develop Python code to simulate the production system, incorporating upstream batch timing, tank dynamics, and variable outfeed demand. Implement an MPC algorithm that predicts future conditions and adjusts infeed accordingly to maintain desired tank levels.

🟨 R（Result）

The MPC system should keep the buffer tank at an optimal fill level, preventing underfill or overflow, ensuring consistent downstream supply, and minimizing unplanned downtime—something PID control cannot reliably achieve in this scenario.

🟦 E（Example）

For instance, simulate a sudden increase in product demand from the buffer tank. Show how the MPC anticipates the depletion and adjusts infeed proactively—despite the two-hour upstream delay—while PID control either reacts too late or causes oscillations in tank level.

### Generated Code:
**Intent Summary:**  
Develop an ANN-based temperature control system for a chemical reactor that outperforms traditional PID control by handling nonlinear dynamics and disturbances, using Python to simulate the reactor, train the neural network, and compare controller performance.  

*(Focus: ANN-driven process control for reactors with disturbance rejection, coded in Python)*
**Model Predictive Control for Continuous Cellulose Fiber Production Using Python:**

Explain how model predictive control (MPC) can optimize cellulose fiber production from wood, where continuous infeed and outfeed operations are required, while the material undergoes a two-stage batch process. The material is supplied at an average rate of 50 tons per hour, undergoing pre-treatment in a reactor followed by homogenization before entering a 1,000 cubic meter buffer tank. The product is extracted from the tank on demand, not at a constant rate. To minimize downtime in downstream processes, a high fill level in the tank must be maintained, despite the two-hour delay caused by upstream batch processes, making PID control unsuitable.

Develop Python code to simulate the system dynamics, including the dead time and fluctuating demand.

Implement Python code for a model predictive control (MPC) algorithm to optimize material flow, taking into account the time delay, fluctuating demand, and operational constraints.

**C-A-R-E:**

🟥 C（Context）

In continuous cellulose fiber production from wood, material is fed at a steady rate of 50 tons/hour into a two-stage batch process (pre-treatment and homogenization) before being stored in a 1,000 m³ buffer tank. However, due to the batch process and a two-hour upstream delay, while the product outflow from the tank is variable and demand-driven, traditional PID control cannot ensure consistent performance. This can result in low tank levels and potential downstream process interruptions.

🟩 A（Action）

Explain how model predictive control (MPC) can effectively manage this production challenge by accounting for process delays and demand fluctuations. Then, develop Python code to simulate the production system, incorporating upstream batch timing, tank dynamics, and variable outfeed demand. Implement an MPC algorithm that predicts future conditions and adjusts infeed accordingly to maintain desired tank levels.

🟨 R（Result）

The MPC system should keep the buffer tank at an optimal fill level, preventing underfill or overflow, ensuring consistent downstream supply, and minimizing unplanned downtime—something PID control cannot reliably achieve in this scenario.

🟦 E（Example）

For instance, simulate a sudden increase in product demand from the buffer tank. Show how the MPC anticipates the depletion and adjusts infeed proactively—despite the two-hour upstream delay—while PID control either reacts too late or causes oscillations in tank level.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# Step 1: Simulate Reactor Dynamics
class Reactor:
    def __init__(self):
        self.T = 300  # Initial temperature (K)
        self.dt = 1   # Time step (hours)
        self.t = 0    # Current time
        self.T_dist = 0  # Disturbance temperature (K)

    def update(self, T_dist):
        self.T += (self.T - 298) * 0.01  # Natural cooling
        self.T += T_dist  # Apply disturbance
        return self.T

# Step 2: Simulate Disturbance
def generate_disturbance(T_setpoint, dt=1, n_steps=100):
    T_dist = np.random.normal(0, 10, n_steps)  # Gaussian disturbance
    T_dist *= np.sin(2 * np.pi * 0.1 * np.arange(n_steps))  # Add periodic component
    return T_dist

# Step 3: Train ANN
class ANNController:
    def __init__(self):
        self.model = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000)
        self.X_train = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])  # Inputs: T_setpoint, T_meas
        self.y_train = np.array([0, 0.1, 0.2, 0.3])  # Output: u
        self.X_test = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
        self.y_test = np.array([0.05, 0.15, 0.25, 0.35])
