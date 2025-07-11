### Intent:
**Intent Summary:**  
Develop a MATLAB-based Model Predictive Control (MPC) system to optimize aircraft trajectory in real time, balancing dynamic constraints, fuel efficiency, disturbance rejection, and safety compliance.  

*(Focus: MPC implementation for trajectory optimization with MATLAB, addressing key aviation constraints.)*

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**B-A-B:**

🟥 B（Before）

Aircraft trajectory planning involves complex dynamics, strict safety requirements, and numerous real-world constraints such as fuel efficiency and environmental disturbances. Traditional control strategies often fall short in simultaneously handling these competing demands in real time.

🟩 A（After）

Develop MATLAB code that implements a model predictive control (MPC) algorithm capable of optimizing an aircraft’s trajectory in real time. The controller should intelligently handle dynamic constraints, enhance fuel efficiency, mitigate external disturbances, and maintain compliance with safety and performance standards.

🟧 B（Bridge）

Use MATLAB to build a dynamic model of aircraft motion, integrate it with an MPC formulation, and encode constraints and performance objectives. Simulate various flight scenarios to demonstrate how the MPC system maintains optimal trajectories even under changing environmental and operational conditions.

### Generated Code:
**Intent Summary:**  
Develop a MATLAB-based Model Predictive Control (MPC) system to optimize aircraft trajectory in real time, balancing dynamic constraints, fuel efficiency, disturbance rejection, and safety compliance.  

*(Focus: MPC implementation for trajectory optimization with MATLAB, addressing key aviation constraints.)*
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**B-A-B:**

🟥 B（Before）

Aircraft trajectory planning involves complex dynamics, strict safety requirements, and numerous real-world constraints such as fuel efficiency and environmental disturbances. Traditional control strategies often fall short in simultaneously handling these competing demands in real time.

🟩 A（After）

Develop MATLAB code that implements a model predictive control (MPC) algorithm capable of optimizing an aircraft’s trajectory in real time. The controller should intelligently handle dynamic constraints, enhance fuel efficiency, mitigate external disturbances, and maintain compliance with safety and performance standards.

🟧 B（Bridge）

Use MATLAB to build a dynamic model of aircraft motion, integrate it with an MPC formulation, and encode constraints and performance objectives. Simulate various flight scenarios to demonstrate how the MPC system maintains optimal trajectories even under changing environmental and operational conditions.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def dynamics(x, u, P, Q, R):
    """
    System dynamics: x' = Ax + Bu + Q*u + R*noise
    """
    x_dot = np.dot(A, x) + np.dot(B, u) + np.dot(Q, u) + R * np.random.randn(x.shape[0], 1)
    return x_dot

# Define the control objective
def objective(x, u, P, Q, R):
    """
    Objective: Minimize the cost function: J = 1/2 * x' * P * x + u' * Q * u
    """
    J = 0.5 * np.dot(x, P * x) + np.dot(u, Q * u)
    return J

# Define the cost function
def cost_function(x, u, P, Q, R):
    """
    Cost function: J = 1/2 * x' * P * x + u' * Q * u + R * noise
    """
    x_dot = dynamics(x, u, P, Q, R)
    J = 0.5 * np.dot(x_dot, P * x_dot) + np.dot(u, Q * u) + R * np.random.randn(x.shape[0], 1)
    return J

# Define the constraints
def constraints(x, u, P, Q, R):
    """
    Constraints: x[0] >= 0, u[0] >= 0, u[0] <= 1, u[1] >= 0, u[1] <= 1
    """
    return [
        x[0] >= 0,
        u[0] >= 0,
        u[0] <= 1,
        u[1] >= 0,
        u[1] <= 1
    ]

# Define the optimization problem
def optimization_problem(x0, u0, P, Q, R):
    """
    Optimization problem: Minimize the cost function
