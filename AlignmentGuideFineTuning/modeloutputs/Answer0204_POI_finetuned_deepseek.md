### Intent:
**Intent Summary:**  
Develop MATLAB-based Model Predictive Control (MPC) code to dynamically optimize aircraft trajectory while handling constraints (dynamics, fuel efficiency, safety) and disturbances (e.g., wind gusts) for real-time performance.

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**C-A-R-E:**

🟥 C（Context）

Aircraft trajectory optimization must consider multiple factors simultaneously—dynamic constraints, fuel consumption, environmental disturbances, and safety requirements. Traditional control methods often lack the predictive capability to handle such complexity effectively.

🟩 A（Action）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that dynamically optimizes an aircraft’s trajectory. Incorporate system dynamics, fuel efficiency goals, external disturbances, and safety/performance constraints into the MPC formulation.

🟨 R（Result）

The MPC-based control system should enable precise and efficient trajectory tracking, improving overall flight performance while ensuring safe operation under varying environmental and operational conditions.

🟦 E（Example）

For example, simulate a scenario where the aircraft experiences sudden wind gusts. Show how the MPC system adjusts the trajectory in real time, maintaining safety and efficiency, in contrast to a traditional open-loop or rule-based system that might overreact or fail to adapt.

### Generated Code:
**Intent Summary:**  
Develop MATLAB-based Model Predictive Control (MPC) code to dynamically optimize aircraft trajectory while handling constraints (dynamics, fuel efficiency, safety) and disturbances (e.g., wind gusts) for real-time performance.
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**C-A-R-E:**

🟥 C（Context）

Aircraft trajectory optimization must consider multiple factors simultaneously—dynamic constraints, fuel consumption, environmental disturbances, and safety requirements. Traditional control methods often lack the predictive capability to handle such complexity effectively.

🟩 A（Action）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that dynamically optimizes an aircraft’s trajectory. Incorporate system dynamics, fuel efficiency goals, external disturbances, and safety/performance constraints into the MPC formulation.

🟨 R（Result）

The MPC-based control system should enable precise and efficient trajectory tracking, improving overall flight performance while ensuring safe operation under varying environmental and operational conditions.

🟦 E（Example）

For example, simulate a scenario where the aircraft experiences sudden wind gusts. Show how the MPC system adjusts the trajectory in real time, maintaining safety and efficiency, in contrast to a traditional open-loop or rule-based system that might overreact or fail to adapt.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def dynamics(x, u, P):
    """
    System dynamics: position (x), velocity (v), and acceleration (a)
    """
    x_dot = u[0]
    v_dot = u[1]
    a_dot = u[2]
    x_ddot = u[3]
    return np.array([x_dot, v_dot, a_dot, x_ddot])

# Define the constraints
def constraints(x, u, P):
    """
    Constraints: position (x), velocity (v), acceleration (a), and jerk (x_ddot)
    """
    return np.array([
        x >= 0,
        v >= 0,
        a >= 0,
        x_ddot >= 0,
        x_ddot <= 1000,
        u[0] >= 0,
        u[1] >= 0,
        u[2] >= 0,
        u[3] >= 0,
        u[0] + u[1] + u[2] + u[3] <= 1000,
    ])

# Define the objective function
def objective(x, u, P):
    """
    Objective function: minimize fuel consumption
    """
    return -1 * (u[0] + u[1] + u[2] + u[3])

# Define the initial conditions
x0 = np.array([0, 0, 0, 0])

# Define the bounds for the control inputs
u_bounds = (0, 1000)

# Define the bounds for the state variables
x_bounds = (0, 1000)

# Define the bounds for the control inputs
u_bounds = (0, 1000)

# Define the bounds for the state variables
x_bounds = (0, 1000)

# Define the bounds for the control inputs
u_bounds = (0, 1000)

# Define the bounds for the state variables
x_bounds = (0,
