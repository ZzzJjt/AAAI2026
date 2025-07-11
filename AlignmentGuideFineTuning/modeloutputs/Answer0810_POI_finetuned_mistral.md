### Intent:
Develop a Model Predictive Control (MPC) system for wind farm power optimization that adjusts turbine blade pitch angles to maintain stable grid power output while managing energy storage constraints.

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**T-A-G:**

🟥 T（Task）

Create a Python-based statistical process control (SPC) system to monitor and improve quality in steel manufacturing.

🟩 A（Action）

Simulate key quality metrics such as tensile strength, thickness, and surface finish in real time. Implement SPC tools including X̄ and R charts to detect process deviations, trigger alarms for out-of-control conditions, and recommend corrective actions to minimize defects and maintain consistency.

🟦 G（Goal）

Ensure high product quality, reduce waste, and maintain process stability by enabling early detection and response to quality variations through a data-driven, real-time control system.

### Generated Code:
Develop a Model Predictive Control (MPC) system for wind farm power optimization that adjusts turbine blade pitch angles to maintain stable grid power output while managing energy storage constraints.
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**T-A-G:**

🟥 T（Task）

Create a Python-based statistical process control (SPC) system to monitor and improve quality in steel manufacturing.

🟩 A（Action）

Simulate key quality metrics such as tensile strength, thickness, and surface finish in real time. Implement SPC tools including X̄ and R charts to detect process deviations, trigger alarms for out-of-control conditions, and recommend corrective actions to minimize defects and maintain consistency.

🟦 G（Goal）

Ensure high product quality, reduce waste, and maintain process stability by enabling early detection and response to quality variations through a data-driven, real-time control system.
import numpy as np
import casadi as ca
import matplotlib.pyplot as plt

# Define the system dynamics
def f(x, u, t):
    """
    State-space model for wind turbine dynamics
    """
    # State variables: [theta, omega, blade_pitch, battery_state_of_charge]
    theta, omega, pitch, soh = x
    # Control variables: [pitch_setpoint, battery_charge_rate]
    pitch_setpoint, charge_rate = u
    # Parameters
    k_theta = 1.0  # Torque constant
    k_omega = 0.5  # Moment of inertia
    k_battery = 0.1  # Battery capacity
    dt = 1.0  # Time step
    # Dynamics
    dtheta_dt = omega
    domega_dt = (k_theta * pitch_setpoint - k_omega * omega) / k_battery
    dpitch_dt = (pitch_setpoint - pitch) / dt
    dsoh_dt = charge_rate
    return [dtheta_dt, domega_dt, dpitch_dt, dsoh_dt]

# Define the cost function
def h(x, u):
    """
    Cost function for power output and battery constraints
    """
    theta, omega, pitch, soh = x
    pitch_setpoint, charge_rate = u
    # Cost terms
    power_output = omega * k_theta * pitch_setpoint
    battery_constraint = soh >= 0.5  # Battery constraint
    # Cost function
    cost = -power_output  # Maximize power output
    return [cost, battery_constraint]

# Define the optimization problem
def mpc_problem(x, u_prev, t, N=10):
    """
    MPC problem definition
    """
    # Initialize states and controls
    x_pred = np.array([x[0], x[1], x[2], x[3]])  # Predicted states
    u = np.zeros((N, 2))  # Predicted controls
