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

# Define the nonlinear system dynamics
def system_dynamics(x, u, t):
    x_dot = np.zeros(3)
    x_dot[0] = u[0]
    x_dot[1] = u[1]
    x_dot[2] = u[2]
    return x_dot

# Define the objective function
def objective_function(x, u):
    return -np.sum(u**2)  # Minimize control effort

# Define the constraints
def constraints(x, u):
    # State constraints
    # x[0] (position) must be within [0, 100]
    # x[1] (velocity) must be within [-10, 10]
    # x[2] (acceleration) must be within [-20, 20]
    return np.array([
        x[0] >= 0,
        x[0] <= 100,
        x[1] >= -10,
        x[1] <= 10,
        x[2] >= -20,
        x[2] <= 20
    ])

# Define the initial state
x0 = np.array([0, 0, 0])

# Define the control bounds
u_bounds = np.array([
    (-10, 10),  # u[0] (thrust)
    (-10, 10),  # u[1] (pitch angle)
    (-10, 10)   # u[2] (roll angle)
])

# Define the time horizon
N = 10  # Prediction horizon

# Define the optimization problem
opt_prob = minimize(
    objective_function,
    u0,
    args=(x0,),
    method='SLSQP',
    bounds=u_bounds,
    constraints=constraints
)

# Get the optimal control sequence
u_opt = opt_prob.x

# Simulate the system with the optimal control
x_
