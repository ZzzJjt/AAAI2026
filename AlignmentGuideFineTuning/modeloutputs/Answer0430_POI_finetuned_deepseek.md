### Intent:
The task involves developing a Model Predictive Control (MPC) system in MATLAB to optimize an aircraft's 2D longitudinal trajectory by adjusting thrust and elevator inputs while maintaining altitude and handling wind disturbances, with numerical performance outputs.

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.

### Generated Code:
The task involves developing a Model Predictive Control (MPC) system in MATLAB to optimize an aircraft's 2D longitudinal trajectory by adjusting thrust and elevator inputs while maintaining altitude and handling wind disturbances, with numerical performance outputs.
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def dynamics(x, u, P, Q, R):
    """
    System dynamics: 2D longitudinal aircraft trajectory
    x: [x, y, vx, vy] - state vector
    u: [thrust, elevator] - control inputs
    P: [10, 10] - process noise covariance
    Q: [10, 10] - measurement noise covariance
    R: [1, 1] - measurement noise covariance
    """
    x_dot = u[0] + 0.1 * x[2] * (1 - x[0] / 100)
    y_dot = u[1] + 0.1 * x[3] * (1 - x[1] / 100)
    return np.array([x_dot, y_dot, u[0], u[1]])

# Define the MPC objective function
def objective(x, u, P, Q, R):
    """
    Objective function: minimize tracking error
    x: [x, y, vx, vy] - state estimate
    u: [thrust, elevator] - control input
    P: [10, 10] - process noise covariance
    Q: [10, 10] - measurement noise covariance
    R: [1, 1] - measurement noise covariance
    """
    x_error = x - np.array([100, 100, 0, 0])
    return np.sum(x_error**2)

# Define the MPC problem
def mpc_problem(x, u, P, Q, R):
    """
    MPC problem: minimize tracking error
    x: [x, y, vx, vy] - state estimate
    u: [thrust, elevator] - control input
    P: [10, 10] - process noise covariance
    Q: [10, 10] - measurement noise covariance
    R: [1, 1] - measurement noise covariance
    """
    # Define the state and control constraints
    x_lower = np.array([-
