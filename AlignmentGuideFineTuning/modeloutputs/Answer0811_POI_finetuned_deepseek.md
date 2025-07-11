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
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Parameters
num_samples = 1000
num_features = 10
num_epochs = 100
learning_rate = 0.1
batch_size = 10

# Generate synthetic data
np.random.seed(0)
X = np.random.randn(num_samples, num_features)
y = X[:, 0] + 0.5 * X[:, 1] + 0.2 * X[:, 2] + 0.1 * X[:, 3] + 0.05 * X[:, 4]

# Normalize data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# Train ANN model
model = MLPRegressor(hidden_layer_sizes=(10, 10, 10), activation='relu', solver='adam', alpha=1e-4, batch_size=batch_size, learning_rate_init=learning_rate, max_iter=num_epochs)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Compute and print RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.4f}")

# Plot training and testing data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], y, c='blue', label='Training
