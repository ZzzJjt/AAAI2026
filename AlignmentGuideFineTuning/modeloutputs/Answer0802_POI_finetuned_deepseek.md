### Intent:
The task is to design and implement a Model Predictive Control (MPC) system in MATLAB to regulate an aircraft's altitude, velocity, and heading by adjusting throttle and elevator inputs while compensating for wind disturbances.  

**Intent Summary:**  
*"Implement MPC for aircraft trajectory control with wind disturbance rejection in MATLAB."*

### Prompt:
**Fuzzy Logic Control for Chemical Reactor Optimization Using Python:**

Develop Python code to implement a fuzzy logic control system for optimizing the operation of a chemical reactor. The control system should manage key reactor variables such as temperature, pressure, and reaction rate, considering the nonlinear and uncertain nature of the reactor’s dynamics. Fuzzy logic should be applied to handle imprecise inputs and adjust control actions in real-time to maintain optimal reactor performance under varying operating conditions.

Implement Python code to simulate the chemical reactor’s dynamics, demonstrating how fuzzy logic control can provide robust and adaptive responses to system uncertainties and process variations.

**T-A-G:**

🟥 T（Task）

Design and implement a Python-based fuzzy logic control system to optimize the operation of a chemical reactor.

🟩 A（Action）

Develop fuzzy logic rules and membership functions to manage key process variables such as temperature, pressure, and reaction rate. Use Python to build the fuzzy inference engine and simulate the chemical reactor’s nonlinear dynamics under varying and uncertain operating conditions. Evaluate the system’s adaptability and performance compared to traditional PID control.

🟦 G（Goal）

Demonstrate that fuzzy logic control can handle imprecise inputs and provide robust, real-time adjustments, leading to more stable and efficient reactor operation under dynamic and uncertain scenarios.

### Generated Code:
The task is to design and implement a Model Predictive Control (MPC) system in MATLAB to regulate an aircraft's altitude, velocity, and heading by adjusting throttle and elevator inputs while compensating for wind disturbances.  

**Intent Summary:**  
*"Implement MPC for aircraft trajectory control with wind disturbance rejection in MATLAB."*
**Fuzzy Logic Control for Chemical Reactor Optimization Using Python:**

Develop Python code to implement a fuzzy logic control system for optimizing the operation of a chemical reactor. The control system should manage key reactor variables such as temperature, pressure, and reaction rate, considering the nonlinear and uncertain nature of the reactor’s dynamics. Fuzzy logic should be applied to handle imprecise inputs and adjust control actions in real-time to maintain optimal reactor performance under varying operating conditions.

Implement Python code to simulate the chemical reactor’s dynamics, demonstrating how fuzzy logic control can provide robust and adaptive responses to system uncertainties and process variations.

**T-A-G:**

🟥 T（Task）

Design and implement a Python-based fuzzy logic control system to optimize the operation of a chemical reactor.

🟩 A（Action）

Develop fuzzy logic rules and membership functions to manage key process variables such as temperature, pressure, and reaction rate. Use Python to build the fuzzy inference engine and simulate the chemical reactor’s nonlinear dynamics under varying and uncertain operating conditions. Evaluate the system’s adaptability and performance compared to traditional PID control.

🟦 G（Goal）

Demonstrate that fuzzy logic control can handle imprecise inputs and provide robust, real-time adjustments, leading to more stable and efficient reactor operation under dynamic and uncertain scenarios.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from scipy.optimize import minimize

# Parameters
m = 100.0  # mass of aircraft (kg)
g = 9.81  # acceleration due to gravity (m/s^2)
L = 10.0  # length of aircraft (m)
rho = 1.225  # air density (kg/m^3)
C_D = 0.01  # drag coefficient (dimensionless)
C_L = 0.001  # lift coefficient (dimensionless)
alpha = 0.01  # angle of attack (rad)
beta = 0.01  # angle of sideslip (rad)

# Dynamics
def dynamics(state, t, u):
    x, y, v, w, e = state
    q = np.arctan2(y, x)  # heading
    p = np.arctan2(v, w)  # pitch angle
    q_dot = np.cos(q) * beta  # heading rate
    p_dot = np.sin(p) * alpha  # pitch rate
    e_dot = -np.sqrt(u[0]**2 + u[1]**2)  # elevator angle rate
    return [x, y, v, w, e, q_dot, p_dot, e_dot]

# Control inputs
def control(state, t, u):
    x, y, v, w, e, q_dot, p_dot, e_dot = state
    u = np.array([u[0], u[1]])  # elevator and aileron inputs
    return u

# Boundary conditions
x0 = 0.0
y0 = 0.0
v0 = 0.0
w0 = 0.0
e0 = 0.0
q0 = 0.0
p0 = 0.0

# Time integration
t_eval = np.linspace(0, 10, 1000)  # time evaluation points
