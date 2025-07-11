### Intent:
**Intent Summary:**  
Develop a Python-based artificial neural network (ANN) controller to optimize temperature regulation in a nonlinear chemical reactor, demonstrating superior performance over traditional PID control through adaptive prediction and disturbance handling.  

*(Focus: ANN-based control, nonlinear dynamics, Python implementation, comparison with PID)*

### Prompt:
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**C-A-R-E**

🟥 C（Context）

In chemical process industries, temperature control of reactors is critical. However, due to the nonlinear and time-varying nature of reactor dynamics, traditional PID controllers often fall short in maintaining optimal performance.

🟩 A（Action）

Develop Python code to implement an artificial neural network (ANN)-based advanced process control system. Train the ANN using historical process data to predict and adjust temperature more effectively than conventional methods. Also, simulate the reactor’s temperature dynamics to validate control performance.

🟨 R（Result）

The ANN controller should demonstrate superior adaptability and predictive accuracy, resulting in more stable temperature control, improved energy efficiency, and reduced oscillations compared to traditional PID-based approaches.

🟦 E（Example）

For instance, simulate a scenario where the reactor experiences a sudden change in feed temperature. Show how the ANN anticipates and adjusts the control signal smoothly, while the PID controller lags or causes instability.

### Generated Code:
**Intent Summary:**  
Develop a Python-based artificial neural network (ANN) controller to optimize temperature regulation in a nonlinear chemical reactor, demonstrating superior performance over traditional PID control through adaptive prediction and disturbance handling.  

*(Focus: ANN-based control, nonlinear dynamics, Python implementation, comparison with PID)*
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**C-A-R-E**

🟥 C（Context）

In chemical process industries, temperature control of reactors is critical. However, due to the nonlinear and time-varying nature of reactor dynamics, traditional PID controllers often fall short in maintaining optimal performance.

🟩 A（Action）

Develop Python code to implement an artificial neural network (ANN)-based advanced process control system. Train the ANN using historical process data to predict and adjust temperature more effectively than conventional methods. Also, simulate the reactor’s temperature dynamics to validate control performance.

🟨 R（Result）

The ANN controller should demonstrate superior adaptability and predictive accuracy, resulting in more stable temperature control, improved energy efficiency, and reduced oscillations compared to traditional PID-based approaches.

🟦 E（Example）

For instance, simulate a scenario where the reactor experiences a sudden change in feed temperature. Show how the ANN anticipates and adjusts the control signal smoothly, while the PID controller lags or causes instability.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# Step 1: Generate Simulated Data
np.random.seed(42)

# Nonlinear process dynamics (simulated chemical reactor)
def process_dynamics(x, u, t):
    # Nonlinear process: y = x^2 + u + 0.5*t
    return x**2 + u + 0.5*t

# Simulate 1000 data points with noise
x = np.random.uniform(0, 10, 1000)
u = np.random.uniform(0, 1, 1000)
t = np.linspace(0, 10, 1000)
y = process_dynamics(x, u, t) + 0.1*np.random.normal(0, 1, 1000)

# Step 2: Prepare Training and Testing Data
X = np.array([x, u]).T
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train ANN Model
ann_model = MLPRegressor(hidden_layer_sizes=(10, 5), activation='relu', solver='lbfgs', alpha=0.001,
                         max_iter=1000, verbose=0)
ann_model.fit(X_train, y_train)

# Step 4: Evaluate ANN Model
print("ANN Training Score: ", ann_model.score(X_train, y_train))
print("ANN Testing Score: ", ann_model.score(X_test, y_test))

# Step 5: Predict Output and Compare with PID
def pid_controller(setpoint, process_output, kp=1.0, ki=0.1, kd
