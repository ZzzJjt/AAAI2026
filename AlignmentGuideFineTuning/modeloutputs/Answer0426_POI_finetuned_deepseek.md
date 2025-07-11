### Intent:
**Intent Summary:**  
Develop a fuzzy logic controller in Python to optimize a chemical reactor's temperature, pressure, and reaction rate by dynamically adjusting heater power, pressure valves, and reactant flow, outperforming PID control in disturbance rejection and setpoint tracking.  

*(Focus: Fuzzy control for reactor optimization with performance comparison against PID, using nonlinear dynamics and disturbance handling.)*

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ developer specializing in intelligent building systems and advanced control algorithms.

🟩 I（Input）

You are tasked with developing a model predictive control (MPC) system for an HVAC application. The system must manage indoor temperature, humidity, and energy consumption while considering constraints such as fluctuating external temperatures, varying occupancy levels, and energy efficiency goals. The goal is to maintain occupant comfort and optimize performance under dynamic environmental conditions.

🟧 S（Steps）
	1.	Model the HVAC system dynamics in C++, including thermal response, humidity control, and energy usage behavior.
	2.	Implement an MPC algorithm that forecasts future system states and adjusts control signals in real time.
	3.	Incorporate constraints related to energy limits, external weather, and occupancy profiles.
	4.	Simulate various environmental scenarios to validate system adaptability, responsiveness, and efficiency.

🟦 E（Expectation）

The MPC-based control system should demonstrate improved energy efficiency, faster response to environmental changes, and enhanced occupant comfort compared to traditional control approaches—all while respecting operational constraints in real-time conditions.

### Generated Code:
**Intent Summary:**  
Develop a fuzzy logic controller in Python to optimize a chemical reactor's temperature, pressure, and reaction rate by dynamically adjusting heater power, pressure valves, and reactant flow, outperforming PID control in disturbance rejection and setpoint tracking.  

*(Focus: Fuzzy control for reactor optimization with performance comparison against PID, using nonlinear dynamics and disturbance handling.)*
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ developer specializing in intelligent building systems and advanced control algorithms.

🟩 I（Input）

You are tasked with developing a model predictive control (MPC) system for an HVAC application. The system must manage indoor temperature, humidity, and energy consumption while considering constraints such as fluctuating external temperatures, varying occupancy levels, and energy efficiency goals. The goal is to maintain occupant comfort and optimize performance under dynamic environmental conditions.

🟧 S（Steps）
	1.	Model the HVAC system dynamics in C++, including thermal response, humidity control, and energy usage behavior.
	2.	Implement an MPC algorithm that forecasts future system states and adjusts control signals in real time.
	3.	Incorporate constraints related to energy limits, external weather, and occupancy profiles.
	4.	Simulate various environmental scenarios to validate system adaptability, responsiveness, and efficiency.

🟦 E（Expectation）

The MPC-based control system should demonstrate improved energy efficiency, faster response to environmental changes, and enhanced occupant comfort compared to traditional control approaches—all while respecting operational constraints in real-time conditions.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Define the ODE system
def dydt(y, t, K, T, P, R, Q, T_setpoint, P_setpoint, R_setpoint, Q_setpoint):
    """
    dydt = [dT, dP, dR, dQ]
    """
    T_diff = T - T_setpoint
    P_diff = P - P_setpoint
    R_diff = R - R_setpoint
    Q_diff = Q - Q_setpoint
    
    dT = K * T_diff
    dP = K * P_diff
    dR = K * R_diff
    dQ = K * Q_diff
    
    return dT, dP, dR, dQ

# Define the control parameters
K = 1.0  # Temperature gain
T_setpoint = 25.0  # Target temperature
P_setpoint = 50.0  # Target pressure
R_setpoint = 0.5  # Target reaction rate
Q_setpoint = 0.5  # Target reactant flow

# Define the simulation parameters
T_initial = 20.0  # Initial temperature
P_initial = 40.0  # Initial pressure
R_initial = 0.3  # Initial reaction rate
Q_initial = 0.3  # Initial reactant flow

# Define the simulation time
t_max = 100.0  # Simulation time (s)
dt = 0.1  # Time step (s)
num_steps = int(t_max / dt)

# Initialize the state vector
y = np.zeros((num_steps, 4))
y[0] = [T_initial, P_initial, R_initial, Q_initial]

# Simulate the system
for i in range(num_steps - 1):
    dT, dP, dR, dQ = dydt(y[i], i * dt, K, T_setpoint,
