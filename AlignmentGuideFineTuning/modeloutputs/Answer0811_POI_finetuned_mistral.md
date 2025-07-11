### Intent:
**Intent Summary:**  
Implement an ANN-based temperature control system for a chemical reactor in Python to achieve superior regulation over traditional methods by leveraging predictive and adaptive capabilities for nonlinear, dynamic conditions.

### Prompt:
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**T-A-G**

🟥 T（Task）

Design and implement a Python-based artificial neural network (ANN) controller to regulate the temperature of a chemical reactor with nonlinear and time-varying dynamics.

🟩 A（Action）

Train the ANN using historical temperature and process data to enable predictive and adaptive control. Simulate the reactor’s temperature response and compare the ANN-based control performance with that of a traditional PID controller, focusing on stability and responsiveness.

🟦 G（Goal）

Demonstrate that the ANN-based control system achieves superior temperature regulation under dynamic conditions, ensuring higher process efficiency, reduced oscillations, and improved adaptability over conventional methods.

### Generated Code:
**Intent Summary:**  
Implement an ANN-based temperature control system for a chemical reactor in Python to achieve superior regulation over traditional methods by leveraging predictive and adaptive capabilities for nonlinear, dynamic conditions.
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**T-A-G**

🟥 T（Task）

Design and implement a Python-based artificial neural network (ANN) controller to regulate the temperature of a chemical reactor with nonlinear and time-varying dynamics.

🟩 A（Action）

Train the ANN using historical temperature and process data to enable predictive and adaptive control. Simulate the reactor’s temperature response and compare the ANN-based control performance with that of a traditional PID controller, focusing on stability and responsiveness.

🟦 G（Goal）

Demonstrate that the ANN-based control system achieves superior temperature regulation under dynamic conditions, ensuring higher process efficiency, reduced oscillations, and improved adaptability over conventional methods.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# Step 1: Generate Simulated Data
np.random.seed(42)

# Simulate 1000 data points of temperature and pressure
temperature = np.random.normal(50, 5, 1000)
pressure = np.random.normal(100, 10, 1000)

# Add noise to simulate measurement errors
temperature += np.random.normal(0, 2, 1000)
pressure += np.random.normal(0, 5, 1000)

# Step 2: Preprocess Data
# Normalize temperature and pressure to [0, 1]
temperature_norm = (temperature - np.min(temperature)) / (np.max(temperature) - np.min(temperature))
pressure_norm = (pressure - np.min(pressure)) / (np.max(pressure) - np.min(pressure))

# Step 3: Split Data
train_size = int(0.8 * len(temperature))
train_data = np.column_stack([temperature_norm[:train_size], pressure_norm[:train_size]])
test_data = np.column_stack([temperature_norm[train_size:], pressure_norm[train_size:]])

# Step 4: Train ANN Model
ann_model = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000, activation='relu', solver='adam', alpha=0.001)
ann_model.fit(train_data, np.zeros(train_size))  # Train to predict temperature from pressure

# Step 5: Evaluate Model
predicted_temperature = ann_model.predict(test_data)

# Plot actual vs predicted temperature
plt.scatter(test_data[:, 1], test_data[:, 0], color='blue', label='Actual')
plt.scatter(test_data[:, 1], predicted
