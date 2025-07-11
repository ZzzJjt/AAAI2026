### Intent:
The task involves implementing a Python-based artificial neural network (ANN) controller to regulate temperature in a chemical reactor, training it on historical data to outperform traditional PID control in handling nonlinear, time-varying dynamics for improved stability and efficiency.  

**Intent Summary:**  
*"Develop an ANN-based temperature control system for a chemical reactor using Python to achieve superior performance over conventional methods under dynamic conditions."*

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
The task involves implementing a Python-based artificial neural network (ANN) controller to regulate temperature in a chemical reactor, training it on historical data to outperform traditional PID control in handling nonlinear, time-varying dynamics for improved stability and efficiency.  

**Intent Summary:**  
*"Develop an ANN-based temperature control system for a chemical reactor using Python to achieve superior performance over conventional methods under dynamic conditions."*
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
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Parameters
num_samples = 1000
num_timesteps = 100
num_features = 10
num_neurons = 10
learning_rate = 0.1
batch_size = 10
num_epochs = 100

# Generate synthetic data
np.random.seed(0)
X = np.random.randn(num_samples, num_timesteps, num_features)
y = X.dot(np.random.rand(num_samples, 1)) + np.random.randn(num_samples, 1)

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Train the ANN
model = MLPRegressor(
    hidden_layer_sizes=(num_neurons,),
    learning_rate_init=learning_rate,
    max_iter=num_epochs,
    batch_size=batch_size,
    activation='relu',
    solver='adam',
    alpha=1e-4,
    random_state=0
)
model.fit(X_train, y_train)

# Predict on validation set
y_pred = model.predict(X_val)

# Compute and print RMSE
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
print(f"RMSE: {rmse:.4f}")

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(num_samples):
    ax.plot(X_val[i, :, 0], X_val[i, :, 1], y_val[i, 0], label=f"Sample {i}")
