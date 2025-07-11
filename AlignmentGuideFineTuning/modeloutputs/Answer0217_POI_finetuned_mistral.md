### Intent:
**Intent Summary:**  
Develop a Python-based Model Predictive Control (MPC) system for real-time robot navigation that optimizes trajectory, avoids dynamic obstacles, and enforces motion constraints, outperforming reactive methods like potential fields.  

**Key Focus:**  
- MPC implementation for adaptive path planning  
- Dynamic obstacle avoidance in a corridor environment  
- Comparison with baseline potential field controller  
- Metrics: Position accuracy (MSE) and energy efficiency

### Prompt:
**Model Predictive Control for Optimizing Robot Movement Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the movement of a robot. The control system should consider dynamic constraints, path planning, and obstacle avoidance while ensuring smooth, efficient, and adaptive movement in a dynamic environment.

**C-A-R-E:**

🟥 C（Context）

Robots operating in dynamic environments often face challenges such as moving obstacles, tight path constraints, and the need for smooth and efficient motion. Traditional control methods may not adapt quickly enough to ensure safe and optimal navigation, especially when real-time decisions are required.

🟩 A（Action）

Develop Python code to implement a model predictive control (MPC) algorithm for robot motion optimization. The controller should handle path planning, obstacle avoidance, and dynamic constraints, while continuously predicting and adjusting the robot’s movement to maintain smooth and efficient operation.

🟨 R（Result）

The resulting MPC-controlled robot should demonstrate adaptive, real-time trajectory optimization, maintaining smooth motion and effectively avoiding collisions. Compared to static or reactive control methods, the MPC approach should provide more intelligent and reliable navigation in complex environments.

🟦 E（Example）

For example, simulate a robot navigating through a corridor with moving obstacles. Show how the MPC predicts future positions, reroutes accordingly, and maintains a smooth trajectory—avoiding jerky movements and ensuring timely arrival at the goal.

### Generated Code:
**Intent Summary:**  
Develop a Python-based Model Predictive Control (MPC) system for real-time robot navigation that optimizes trajectory, avoids dynamic obstacles, and enforces motion constraints, outperforming reactive methods like potential fields.  

**Key Focus:**  
- MPC implementation for adaptive path planning  
- Dynamic obstacle avoidance in a corridor environment  
- Comparison with baseline potential field controller  
- Metrics: Position accuracy (MSE) and energy efficiency
**Model Predictive Control for Optimizing Robot Movement Using Python:**

Develop Python code to implement a model predictive control (MPC) algorithm for optimizing the movement of a robot. The control system should consider dynamic constraints, path planning, and obstacle avoidance while ensuring smooth, efficient, and adaptive movement in a dynamic environment.

**C-A-R-E:**

🟥 C（Context）

Robots operating in dynamic environments often face challenges such as moving obstacles, tight path constraints, and the need for smooth and efficient motion. Traditional control methods may not adapt quickly enough to ensure safe and optimal navigation, especially when real-time decisions are required.

🟩 A（Action）

Develop Python code to implement a model predictive control (MPC) algorithm for robot motion optimization. The controller should handle path planning, obstacle avoidance, and dynamic constraints, while continuously predicting and adjusting the robot’s movement to maintain smooth and efficient operation.

🟨 R（Result）

The resulting MPC-controlled robot should demonstrate adaptive, real-time trajectory optimization, maintaining smooth motion and effectively avoiding collisions. Compared to static or reactive control methods, the MPC approach should provide more intelligent and reliable navigation in complex environments.

🟦 E（Example）

For example, simulate a robot navigating through a corridor with moving obstacles. Show how the MPC predicts future positions, reroutes accordingly, and maintains a smooth trajectory—avoiding jerky movements and ensuring timely arrival at the goal.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def system_dynamics(x, u, dt):
    """
    State-space model for a 2-link robot arm with joint angles x = [theta_1, theta_2]
    Input: u = [torque_1, torque_2]
    """
    theta_1, theta_2 = x
    u_1, u_2 = u
    # Dynamics for joint 1
    dtheta_1_dt = u_1 / (0.1 + 0.01 * np.sin(theta_1))  # Torque-dependent dynamics
    # Dynamics for joint 2 (coupled to joint 1)
    dtheta_2_dt = (u_2 * np.cos(theta_1) - 0.05 * theta_2) / (0.1 + 0.01 * np.sin(theta_1))
    return np.array([dtheta_1_dt, dtheta_2_dt])

# Define the cost function
def cost_function(x, u, y, dt):
    """
    Cost function for MPC: sum of squared errors between predicted and desired positions
    """
    theta_1, theta_2 = x
    x_pred = np.array([theta_1, theta_2])
    x_desired = np.array([np.pi / 2, np.pi / 2])  # Desired joint angles
    cost = np.sum((x_pred - x_desired) ** 2)
    return cost

# Define the constraints
def constraints(x, u, y, dt):
    """
    Constraints: torque limits and joint angle bounds
    """
    theta_1, theta_2 = x
    u_1, u_2 = u
    # Torque limits
    u_1_min, u_1_max = -10, 10
    u_2_min, u_2_max = -10, 10
    # Joint angle bounds
    the
