### Intent:
**Intent Summary:**  
Develop an ANN-based temperature control system for a chemical reactor that outperforms traditional PID control by handling nonlinear dynamics and disturbances, using Python to simulate the reactor, train the neural network, and compare controller performance.  

*(Focus: ANN-driven process control for reactors with disturbance rejection, coded in Python)*

### Prompt:
**Model Predictive Control for Continuous Cellulose Fiber Production Using Python:**

Explain how model predictive control (MPC) can optimize cellulose fiber production from wood, where continuous infeed and outfeed operations are required, while the material undergoes a two-stage batch process. The material is supplied at an average rate of 50 tons per hour, undergoing pre-treatment in a reactor followed by homogenization before entering a 1,000 cubic meter buffer tank. The product is extracted from the tank on demand, not at a constant rate. To minimize downtime in downstream processes, a high fill level in the tank must be maintained, despite the two-hour delay caused by upstream batch processes, making PID control unsuitable.

Develop Python code to simulate the system dynamics, including the dead time and fluctuating demand.

Implement Python code for a model predictive control (MPC) algorithm to optimize material flow, taking into account the time delay, fluctuating demand, and operational constraints.

**C-A-R-E:**

🟥 C（Context）

In continuous cellulose fiber production from wood, material is fed at a steady rate of 50 tons/hour into a two-stage batch process (pre-treatment and homogenization) before being stored in a 1,000 m³ buffer tank. However, due to the batch process and a two-hour upstream delay, while the product outflow from the tank is variable and demand-driven, traditional PID control cannot ensure consistent performance. This can result in low tank levels and potential downstream process interruptions.

🟩 A（Action）

Explain how model predictive control (MPC) can effectively manage this production challenge by accounting for process delays and demand fluctuations. Then, develop Python code to simulate the production system, incorporating upstream batch timing, tank dynamics, and variable outfeed demand. Implement an MPC algorithm that predicts future conditions and adjusts infeed accordingly to maintain desired tank levels.

🟨 R（Result）

The MPC system should keep the buffer tank at an optimal fill level, preventing underfill or overflow, ensuring consistent downstream supply, and minimizing unplanned downtime—something PID control cannot reliably achieve in this scenario.

🟦 E（Example）

For instance, simulate a sudden increase in product demand from the buffer tank. Show how the MPC anticipates the depletion and adjusts infeed proactively—despite the two-hour upstream delay—while PID control either reacts too late or causes oscillations in tank level.

### Generated Code:
**Intent Summary:**  
Develop an ANN-based temperature control system for a chemical reactor that outperforms traditional PID control by handling nonlinear dynamics and disturbances, using Python to simulate the reactor, train the neural network, and compare controller performance.  

*(Focus: ANN-driven process control for reactors with disturbance rejection, coded in Python)*
**Model Predictive Control for Continuous Cellulose Fiber Production Using Python:**

Explain how model predictive control (MPC) can optimize cellulose fiber production from wood, where continuous infeed and outfeed operations are required, while the material undergoes a two-stage batch process. The material is supplied at an average rate of 50 tons per hour, undergoing pre-treatment in a reactor followed by homogenization before entering a 1,000 cubic meter buffer tank. The product is extracted from the tank on demand, not at a constant rate. To minimize downtime in downstream processes, a high fill level in the tank must be maintained, despite the two-hour delay caused by upstream batch processes, making PID control unsuitable.

Develop Python code to simulate the system dynamics, including the dead time and fluctuating demand.

Implement Python code for a model predictive control (MPC) algorithm to optimize material flow, taking into account the time delay, fluctuating demand, and operational constraints.

**C-A-R-E:**

🟥 C（Context）

In continuous cellulose fiber production from wood, material is fed at a steady rate of 50 tons/hour into a two-stage batch process (pre-treatment and homogenization) before being stored in a 1,000 m³ buffer tank. However, due to the batch process and a two-hour upstream delay, while the product outflow from the tank is variable and demand-driven, traditional PID control cannot ensure consistent performance. This can result in low tank levels and potential downstream process interruptions.

🟩 A（Action）

Explain how model predictive control (MPC) can effectively manage this production challenge by accounting for process delays and demand fluctuations. Then, develop Python code to simulate the production system, incorporating upstream batch timing, tank dynamics, and variable outfeed demand. Implement an MPC algorithm that predicts future conditions and adjusts infeed accordingly to maintain desired tank levels.

🟨 R（Result）

The MPC system should keep the buffer tank at an optimal fill level, preventing underfill or overflow, ensuring consistent downstream supply, and minimizing unplanned downtime—something PID control cannot reliably achieve in this scenario.

🟦 E（Example）

For instance, simulate a sudden increase in product demand from the buffer tank. Show how the MPC anticipates the depletion and adjusts infeed proactively—despite the two-hour upstream delay—while PID control either reacts too late or causes oscillations in tank level.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the system dynamics
def dynamics(x, u, T, dt):
    """
    Simulate the chemical reactor dynamics using a 2nd-order system.
    x[0] = temperature, x[1] = pressure, x[2] = flow rate
    u = control input (setpoint)
    T = time (in seconds)
    dt = time step (in seconds)
    """
    x_dot = np.zeros(3)
    x_dot[0] = (u - x[0]) / T * 0.5 * dt
    x_dot[1] = (u - x[1]) / T * 0.5 * dt
    x_dot[2] = (u - x[2]) / T * 0.5 * dt
    return x_dot

# Define the control objective
def objective(x):
    """
    Objective function for the PID controller.
    x[0] = temperature, x[1] = pressure, x[2] = flow rate
    """
    u = x[0]
    return u

# Define the PID controller
def pid_controller(x, u_setpoint, T, dt):
    """
    PID controller for temperature control.
    x[0] = temperature, x[1] = pressure, x[2] = flow rate
    u_setpoint = desired temperature
    T = time (in seconds)
    dt = time step (in seconds)
    """
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01
    e = u_setpoint - x[0]
    e_prev = x[0]
    e_dt = e - e_prev
    e_integral = e_integral + e * dt
    u = Kp * e + Ki * e_integral + Kd * e_dt
    return u

# Define the MPC objective
def mpc_objective(x, u_setpoint, T, dt):
    """
    MPC objective function for temperature control.
    x[0] = temperature, x[1] = pressure,
