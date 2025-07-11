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
import matplotlib.pyplot as plt

# Define the system dynamics
def dynamics(x, u, t, P):
    """
    System dynamics for a chemical reactor.
    x: state vector (T, P)
    u: control input (Q)
    t: time
    P: process parameters
    """
    T, P = x
    Q = u
    
    # Derived variables
    dT_dt = T - P
    dP_dt = 0.5 * P * Q
    
    return np.array([dT_dt, dP_dt])

# Define the disturbance function
def disturbance(x, t, D):
    """
    Disturbance function for the chemical reactor.
    x: state vector (T, P)
    t: time
    D: disturbance vector (D1, D2)
    """
    T, P = x
    D1, D2 = D
    
    # Derived variables
    dT_dt = D1 + 0.1 * D2
    dP_dt = 0.2 * D2
    
    return np.array([dT_dt, dP_dt])

# Define the MPC objective function
def objective(x, u, t, P, D):
    """
    Objective function for the MPC optimization problem.
    x: state vector (T, P)
    u: control input (Q)
    t: time
    P: process parameters
    D: disturbance vector (D1, D2)
    """
    T, P = x
    Q = u
    D1, D2 = D
    
    # Derived variables
    dT_dt = T - P
    dP_dt = 0.5 * P * Q
    dT_D1_dt = D1 + 0.1 * D2
    dP_D2_dt = 0.2 * D2
    
    # Objective function: minimize disturbance
    return np.sum(np.abs(dT_D1_dt) + np.abs(dP_D2_dt))

# Define the MPC optimization problem
def mpc_problem(x0, u0, t
