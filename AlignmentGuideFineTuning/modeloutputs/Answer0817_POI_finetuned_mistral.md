### Intent:
**Intent Summary:**  
Implement a Python-based Model Predictive Control (MPC) system for robot navigation that optimizes trajectory tracking while avoiding static/dynamic obstacles and adhering to dynamic constraints.  

*(Focus: MPC-driven path planning, obstacle avoidance, and real-time adaptation in dynamic environments.)*

### Prompt:
**Model Predictive Control for Optimizing Robot Movement Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the movement of a robot. The control system should consider dynamic constraints, path planning, and obstacle avoidance while ensuring smooth, efficient, and adaptive movement in a dynamic environment.

**T-A-G:**

🟥 T（Task）

Design and implement a model predictive control (MPC) system in Python to optimize a robot’s movement in dynamic environments.

🟩 A（Action）

Develop a motion model of the robot and implement an MPC algorithm that handles path planning, obstacle avoidance, and dynamic constraints such as velocity, acceleration, and turning limits. Simulate various environments with moving or static obstacles to evaluate the robot’s performance.

🟦 G（Goal）

Achieve smooth, adaptive, and efficient robot navigation that responds intelligently to environmental changes, ensuring safe motion and optimal path execution in real time.

### Generated Code:
**Intent Summary:**  
Implement a Python-based Model Predictive Control (MPC) system for robot navigation that optimizes trajectory tracking while avoiding static/dynamic obstacles and adhering to dynamic constraints.  

*(Focus: MPC-driven path planning, obstacle avoidance, and real-time adaptation in dynamic environments.)*
**Model Predictive Control for Optimizing Robot Movement Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the movement of a robot. The control system should consider dynamic constraints, path planning, and obstacle avoidance while ensuring smooth, efficient, and adaptive movement in a dynamic environment.

**T-A-G:**

🟥 T（Task）

Design and implement a model predictive control (MPC) system in Python to optimize a robot’s movement in dynamic environments.

🟩 A（Action）

Develop a motion model of the robot and implement an MPC algorithm that handles path planning, obstacle avoidance, and dynamic constraints such as velocity, acceleration, and turning limits. Simulate various environments with moving or static obstacles to evaluate the robot’s performance.

🟦 G（Goal）

Achieve smooth, adaptive, and efficient robot navigation that responds intelligently to environmental changes, ensuring safe motion and optimal path execution in real time.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def system_dynamics(x, u, dt):
    """
    State-space model for a double integrator:
    dx/dt = v
    dv/dt = u
    """
    x_new = np.zeros_like(x)
    x_new[0] = x[1] + dt * u
    x_new[1] = u
    return x_new

# Define the cost function
def cost_function(x, u, dt, y_ref, Q, R):
    """
    Cost function for MPC:
    J = sum( (x - y_ref)^2 + u^2 )
    """
    x_error = x[0] - y_ref
    u_error = u
    cost = np.sum(Q * x_error**2 + R * u_error**2)
    return cost

# Define the constraints
def constraints(x, u, dt):
    """
    Constraints for MPC:
    u_min <= u <= u_max
    """
    u_min = -1.0
    u_max = 1.0
    return np.all(u >= u_min) and np.all(u <= u_max)

# Set simulation parameters
N = 10  # Prediction horizon
dt = 0.1  # Time step
t_span = np.linspace(0, 10, 100)  # Time span for plotting

# Initialize state and reference trajectory
x0 = np.array([0.0, 0.0])  # Initial state: x = 0, v = 0
y_ref = np.sin(t_span)  # Reference trajectory: y_ref = sin(t)

# Initialize optimization variables
x = np.zeros((N, 2))  # Predicted states
u = np.zeros(N)  # Predicted inputs

# Set cost matrix and input matrix
Q = np.eye(2)  # State weight matrix
R = 1.0
