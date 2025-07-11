### Intent:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate position, velocity, and attitude responses to thrust and control surface inputs, incorporating aerodynamic forces and wind disturbances for flight control applications.  

*(Focus: Aircraft simulation for control system design, with states, inputs, and aerodynamics explicitly modeled.)*

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
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate position, velocity, and attitude responses to thrust and control surface inputs, incorporating aerodynamic forces and wind disturbances for flight control applications.  

*(Focus: Aircraft simulation for control system design, with states, inputs, and aerodynamics explicitly modeled.)*
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
import scipy.integrate as spi
from matplotlib import pyplot as plt

# 6-DOF Aircraft Dynamics Model
class Aircraft:
    def __init__(self):
        # States
        self.x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  # [x, y, z, vx, vy, vz]
        self.v = np.array([0.0, 0.0, 0.0])                 # [roll, pitch, yaw]
        self.u = np.array([0.0, 0.0])                      # [thrust, control surface]
        self.dt = 0.1                                      # Time step
        self.mass = 10000.0                                # Aircraft mass (kg)
        self.Ixx = 1000000.0                               # Moment of inertia (kg m^2)
        self.Iyy = 1000000.0
        self.Izz = 1000000.0
        self.Cd = 0.2                                      # Drag coefficient
        self.Cm = 0.1                                      # Moment coefficient
        self.rho = 1.225                                  # Air density (kg/m^3)
        self.A = 10.0                                      # Wing area (m^2)
        self.g = 9.81                                      # Gravity (m/s^2)
        self.wind = np.array([0.0, 0.0, 0.0])             # Wind disturbance

    def update(self, thrust, control_surface):
        # Thrust and control surface inputs
        self.u[0] = thrust
        self.u[1] = control_surface

        # State update
        x_dot = np.zeros(6)
        v_dot = np.zeros(3)
        v_dot[:2] = self.u[0] / self.mass
