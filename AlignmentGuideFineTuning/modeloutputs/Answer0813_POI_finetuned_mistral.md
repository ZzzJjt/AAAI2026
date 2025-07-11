### Intent:
**Intent Summary:**  
Develop a Python class to model a chemical reactor's temperature and pressure dynamics with disturbance inputs, implementing core equations for simulation without visualization.

### Prompt:
**MATLAB Distillation Column Modeling and Control:**

Develop MATLAB code for a mathematical model of a distillation column, capturing its dynamic relationships between feed rates and temperature. Avoid plotting results.
Implement a model predictive control (MPC) scheme using the developed model to optimize the distillation process while considering operational constraints.

**T-A-G:**

🟥 T（Task）

Create a MATLAB-based dynamic model of a distillation column and apply model predictive control (MPC) to optimize its operation.

🟩 A（Action）

Develop a mathematical representation that captures the relationship between feed rates and temperature without plotting the results. Then, implement an MPC algorithm using the model to compute optimal control actions while respecting system constraints.

🟦 G（Goal）

Ensure the distillation column operates efficiently and within defined operational limits by using predictive control to maintain stability and optimize performance, all in a code-only, non-graphical simulation environment.

### Generated Code:
**Intent Summary:**  
Develop a Python class to model a chemical reactor's temperature and pressure dynamics with disturbance inputs, implementing core equations for simulation without visualization.
**MATLAB Distillation Column Modeling and Control:**

Develop MATLAB code for a mathematical model of a distillation column, capturing its dynamic relationships between feed rates and temperature. Avoid plotting results.
Implement a model predictive control (MPC) scheme using the developed model to optimize the distillation process while considering operational constraints.

**T-A-G:**

🟥 T（Task）

Create a MATLAB-based dynamic model of a distillation column and apply model predictive control (MPC) to optimize its operation.

🟩 A（Action）

Develop a mathematical representation that captures the relationship between feed rates and temperature without plotting the results. Then, implement an MPC algorithm using the model to compute optimal control actions while respecting system constraints.

🟦 G（Goal）

Ensure the distillation column operates efficiently and within defined operational limits by using predictive control to maintain stability and optimize performance, all in a code-only, non-graphical simulation environment.
import numpy as np
import scipy.integrate as spi

class ChemicalReactor:
    def __init__(self):
        self.dt = 1.0  # Time step (s)
        self.T_setpoint = 350.0  # Target temperature (K)
        self.P_setpoint = 10.0  # Target pressure (bar)
        self.T_nominal = 350.0  # Nominal temperature (K)
        self.P_nominal = 10.0  # Nominal pressure (bar)
        self.T_max = 400.0  # Maximum temperature (K)
        self.T_min = 300.0  # Minimum temperature (K)
        self.P_max = 12.0  # Maximum pressure (bar)
        self.P_min = 8.0  # Minimum pressure (bar)
        self.T_disturbance = 0.0  # Temperature disturbance (K)
        self.P_disturbance = 0.0  # Pressure disturbance (bar)
        self.T_error = 0.0  # Temperature error (K)
        self.P_error = 0.0  # Pressure error (bar)
        self.T_prev = self.T_nominal  # Previous temperature (K)
        self.P_prev = self.P_nominal  # Previous pressure (bar)
        self.T_control = 0.0  # Temperature control signal (K)
        self.P_control = 0.0  # Pressure control signal (bar)
        self.T_control_prev = 0.0  # Previous temperature control signal (K)
        self.P_control_prev = 0.0  # Previous pressure control signal (bar)
        self.T_control_integral = 0.0  # Integral of temperature error (K)
        self.P_control_integral = 0.0  # Integral of pressure error (bar)
        self.T_control_derivative = 0.0
