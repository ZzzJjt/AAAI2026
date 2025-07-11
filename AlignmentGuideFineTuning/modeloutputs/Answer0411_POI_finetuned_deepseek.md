### Intent:
The task involves implementing an artificial neural network (ANN)-based controller in Python to regulate temperature in a nonlinear chemical reactor, demonstrating superior performance over traditional PID control through simulation and comparison.  

**Intent summary:**  
*"Develop an ANN-based temperature controller for a chemical reactor to outperform PID control in handling nonlinear dynamics."*

### Prompt:
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**R-I-S-E**

🟥 R（Role）

Act as a process control engineer specializing in AI-driven control systems for chemical reactors.

🟩 I（Input）

You are given a dataset containing historical temperature control data from a chemical reactor with known nonlinear and time-varying behavior. The reactor’s traditional PID control performance under different operating scenarios is also available for comparison.

🟧 S（Steps）
	1.	Develop Python code to build an artificial neural network (ANN) model trained on the historical dataset.
	2.	Implement an ANN-based controller for temperature regulation, leveraging its predictive and adaptive capabilities.
	3.	Simulate the chemical reactor’s temperature control dynamics using both ANN and traditional PID methods.
	4.	Compare and analyze the performance of the ANN controller against the PID controller under various dynamic conditions.

🟦 E（Expectation）

Demonstrate that the ANN-based controller offers improved temperature stability, quicker response to disturbances, and better handling of nonlinearities compared to the traditional PID controller, thereby proving its effectiveness in advanced process control applications.

### Generated Code:
The task involves implementing an artificial neural network (ANN)-based controller in Python to regulate temperature in a nonlinear chemical reactor, demonstrating superior performance over traditional PID control through simulation and comparison.  

**Intent summary:**  
*"Develop an ANN-based temperature controller for a chemical reactor to outperform PID control in handling nonlinear dynamics."*
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**R-I-S-E**

🟥 R（Role）

Act as a process control engineer specializing in AI-driven control systems for chemical reactors.

🟩 I（Input）

You are given a dataset containing historical temperature control data from a chemical reactor with known nonlinear and time-varying behavior. The reactor’s traditional PID control performance under different operating scenarios is also available for comparison.

🟧 S（Steps）
	1.	Develop Python code to build an artificial neural network (ANN) model trained on the historical dataset.
	2.	Implement an ANN-based controller for temperature regulation, leveraging its predictive and adaptive capabilities.
	3.	Simulate the chemical reactor’s temperature control dynamics using both ANN and traditional PID methods.
	4.	Compare and analyze the performance of the ANN controller against the PID controller under various dynamic conditions.

🟦 E（Expectation）

Demonstrate that the ANN-based controller offers improved temperature stability, quicker response to disturbances, and better handling of nonlinearities compared to the traditional PID controller, thereby proving its effectiveness in advanced process control applications.
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
y = X.dot([0.1, 0.2, 0.3]) + np.random.randn(num_samples) * 0.1

# Normalize data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# Train ANN model
model = MLPRegressor(hidden_layer_sizes=(10, 10), activation='relu', solver='adam', alpha=1e-4, batch_size=batch_size, learning_rate_init=learning_rate, max_iter=num_epochs)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Plot training and testing data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], y, c='blue', label='Training Data')
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], y
