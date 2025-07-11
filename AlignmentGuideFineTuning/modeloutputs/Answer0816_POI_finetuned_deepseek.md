### Intent:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate flight behavior under control inputs (thrust, elevator, rudder) and wind disturbances, calculating forces, accelerations, and angular rates for trajectory tracking.  

*(Focused on code generation for simulating aircraft motion with aerodynamic effects and control inputs.)*

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.

### Generated Code:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate flight behavior under control inputs (thrust, elevator, rudder) and wind disturbances, calculating forces, accelerations, and angular rates for trajectory tracking.  

*(Focused on code generation for simulating aircraft motion with aerodynamic effects and control inputs.)*
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 100.0  # mass of aircraft (kg)
g = 9.81  # acceleration due to gravity (m/s^2)
L = 10.0  # length of aircraft (m)
b = 0.5  # wingspan (m)
rho = 1.225  # air density (kg/m^3)
Cd = 0.025  # drag coefficient
Cl = 0.8  # lift coefficient
alpha = 0.0  # angle of attack (rad)
beta = 0.0  # angle of sideslip (rad)

# State variables
x = np.zeros((2, 100))  # position (m)
v = np.zeros((2, 100))  # velocity (m/s)
omega = np.zeros((2, 100))  # angular velocity (rad/s)

# Control inputs
thrust = np.zeros((2, 100))  # thrust (N)
elevator = np.zeros((2, 100))  # elevator deflection (rad)
rudder = np.zeros((2, 100))  # rudder deflection (rad)

# Time-stepping loop
for t in range(100):
    # Calculate forces and torques
    F_lift = Cl * m * rho * v[0] * np.cos(alpha)
    F_drag = Cd * m * rho * v[0]**2
    F_thrust = np.zeros(2)
    F_lift = F_lift / (b * np.cos(alpha))
    F_thrust[0] = F_lift
    F_thrust[1] = F_lift
    F_torque = F_lift * np.sin(alpha)

    # Calculate acceleration and angular acceleration
    a = F_thrust / m
    omega_x = (F_lift * np.sin(alpha) - F_drag * np.sin(alpha) * np.cos(alpha)) / m
    omega_y = (F_drag *
