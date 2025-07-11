### Intent:
The task is to implement an artificial neural network (ANN)-based controller in Python to regulate temperature in a chemical reactor with nonlinear dynamics, comparing its performance against traditional PID control through simulation.

### Prompt:
**Model Predictive Control for Turbine Optimization in a Thermal Power Plant Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the operation of a turbine in a thermal power plant. The MPC should account for operational constraints, energy efficiency, and thermal dynamics, while ensuring robust performance under varying load conditions and external disturbances.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in Python to optimize the operation of a turbine in a thermal power plant.

🟩 A（Action）

Develop a thermal and dynamic model of the turbine, then implement an MPC algorithm that manages control actions while accounting for operational constraints, energy efficiency requirements, and external disturbances. Simulate various load conditions to evaluate the controller’s robustness and performance.

🟦 G（Goal）

Achieve stable, efficient, and adaptive turbine control under dynamic operating conditions, improving energy usage and system reliability beyond what traditional control methods can offer.

### Generated Code:
The task is to implement an artificial neural network (ANN)-based controller in Python to regulate temperature in a chemical reactor with nonlinear dynamics, comparing its performance against traditional PID control through simulation.
**Model Predictive Control for Turbine Optimization in a Thermal Power Plant Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the operation of a turbine in a thermal power plant. The MPC should account for operational constraints, energy efficiency, and thermal dynamics, while ensuring robust performance under varying load conditions and external disturbances.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in Python to optimize the operation of a turbine in a thermal power plant.

🟩 A（Action）

Develop a thermal and dynamic model of the turbine, then implement an MPC algorithm that manages control actions while accounting for operational constraints, energy efficiency requirements, and external disturbances. Simulate various load conditions to evaluate the controller’s robustness and performance.

🟦 G（Goal）

Achieve stable, efficient, and adaptive turbine control under dynamic operating conditions, improving energy usage and system reliability beyond what traditional control methods can offer.
import numpy as np
from scipy.optimize import minimize

# Step 1: Define the ANN structure
ann_structure = [2, 10, 1]  # Input: 2 (temperature, pressure); Hidden: 10; Output: 1 (control signal)

# Step 2: Initialize weights and biases
np.random.seed(42)
weights_input_hidden = np.random.rand(ann_structure[1], ann_structure[0])
weights_hidden_output = np.random.rand(ann_structure[2], ann_structure[1])
biases_hidden = np.random.rand(ann_structure[1])
biases_output = np.random.rand(ann_structure[2])

# Step 3: Define the activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step 4: Implement forward propagation
def forward_propagation(inputs, weights_input_hidden, weights_hidden_output, biases_hidden, biases_output):
    hidden_layer = sigmoid(np.dot(inputs, weights_input_hidden) + biases_hidden)
    output_layer = sigmoid(np.dot(hidden_layer, weights_hidden_output) + biases_output)
    return output_layer

# Step 5: Define the cost function and gradient
def cost_function(weights_input_hidden, weights_hidden_output, biases_hidden, biases_output, inputs, targets):
    predictions = forward_propagation(inputs, weights_input_hidden, weights_hidden_output, biases_hidden, biases_output)
    cost = np.mean((predictions - targets) ** 2)
    d_weights_input_hidden = np.dot(inputs, predictions - targets)
    d_weights_hidden_output = np.dot(hidden_layer, predictions - targets)
    d_biases_hidden = np.sum(predictions - targets, axis=0)
    d_biases_output = np.sum(predictions - targets, axis=0)
    return cost, {'weights_input_hidden': d_
