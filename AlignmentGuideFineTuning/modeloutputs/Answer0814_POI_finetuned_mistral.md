### Intent:
The task is to implement a steel quality monitoring system in Python that simulates manufacturing process data with controlled drift to test statistical process control methods.

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in MATLAB to optimize the flight trajectory of an aircraft.

🟩 A（Action）

Develop a mathematical model of the aircraft’s dynamics and use it within an MPC framework. Incorporate constraints related to control inputs and aircraft performance, account for external disturbances such as wind, and include objectives for fuel efficiency and flight safety. Simulate realistic flight scenarios to test and validate the controller’s performance.

🟦 G（Goal）

Achieve robust and efficient trajectory tracking that adapts to disturbances, minimizes fuel consumption, and maintains safe, optimal flight paths under dynamic operating conditions.

### Generated Code:
The task is to implement a steel quality monitoring system in Python that simulates manufacturing process data with controlled drift to test statistical process control methods.
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in MATLAB to optimize the flight trajectory of an aircraft.

🟩 A（Action）

Develop a mathematical model of the aircraft’s dynamics and use it within an MPC framework. Incorporate constraints related to control inputs and aircraft performance, account for external disturbances such as wind, and include objectives for fuel efficiency and flight safety. Simulate realistic flight scenarios to test and validate the controller’s performance.

🟦 G（Goal）

Achieve robust and efficient trajectory tracking that adapts to disturbances, minimizes fuel consumption, and maintains safe, optimal flight paths under dynamic operating conditions.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate simulated manufacturing data with controlled drift
def generate_data(n_samples=1000):
    # Simulate sensor readings with noise
    x = np.random.normal(size=n_samples)
    y = np.random.normal(size=n_samples)
    z = np.random.normal(size=n_samples)

    # Add drift to y-axis (temperature)
    y += 0.005 * np.arange(n_samples)

    # Add drift to z-axis (thickness)
    z += 0.002 * np.arange(n_samples)

    # Create a DataFrame for analysis
    df = pd.DataFrame({'x': x, 'y': y, 'z': z})
    return df

# Simulate manufacturing process with drift
df = generate_data()

# Plot the data to visualize drift
plt.figure(figsize=(10, 6))
plt.plot(df['x'], label='x-axis')
plt.plot(df['y'], label='y-axis')
plt.plot(df['z'], label='z-axis')
plt.legend()
plt.show()

# Calculate moving averages for each axis
def moving_average(data, window_size=100):
    return data.rolling(window_size, min_periods=1).mean()

# Apply moving averages to the data
df['x_moving_avg'] = moving_average(df['x'], window_size=100)
df['y_moving_avg'] = moving_average(df['y'], window_size=100)
df['z_moving_avg'] = moving_average(df['z'], window_size=100)

# Plot moving averages to compare with original data
plt.figure(figsize=(10, 6))
plt.plot(df['x'], label='x-axis')
plt.plot(df['x_moving_
