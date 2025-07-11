### Intent:
**Intent Summary:**  
Develop MATLAB-based model predictive control (MPC) for aircraft trajectory optimization, incorporating dynamic constraints, fuel efficiency, and disturbance rejection to ensure safe and efficient flight performance.  

*(Focus: MPC implementation for aircraft dynamics with real-time adaptation to disturbances and operational constraints.)*

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
Develop MATLAB-based model predictive control (MPC) for aircraft trajectory optimization, incorporating dynamic constraints, fuel efficiency, and disturbance rejection to ensure safe and efficient flight performance.  

*(Focus: MPC implementation for aircraft dynamics with real-time adaptation to disturbances and operational constraints.)*
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
def dynamics(x, u, P, Q, R):
    """
    System dynamics: aircraft state evolution
    x: [x, y, v, e, p]
    u: [a, e]
    P: [x, y, v, e, p]
    Q: [x, y, v, e, p]
    R: [x, y, v, e, p]
    """
    x_dot = u[0]
    y_dot = u[1]
    v_dot = 0
    e_dot = 0
    p_dot = 0
    x_ddot = 0
    y_ddot = 0
    v_ddot = 0
    e_ddot = 0
    p_ddot = 0

    # State constraints
    x_dot = np.clip(x_dot, -100, 100)
    y_dot = np.clip(y_dot, -100, 100)
    v_dot = np.clip(v_dot, -100, 100)
    e_dot = np.clip(e_dot, -100, 100)
    p_dot = np.clip(p_dot, -100, 100)

    return np.array([x_dot, y_dot, v_dot, e_dot, p_dot])

# Define the control objective
def objective(x, u, P, Q, R):
    """
    Objective function: minimize fuel consumption
    x: [x, y, v, e, p]
    u: [a, e]
    P: [x, y, v, e, p]
    Q: [x, y, v, e, p]
    R: [x, y, v, e, p]
    """
    # State evolution
    x_dot = u[0]
    y_dot = u[1]
    v_dot = 0
    e_dot = 0
    p_
