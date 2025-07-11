### Intent:
The task is to **implement a Python-based fuzzy logic control system for optimizing chemical reactor performance by managing temperature, pressure, and reaction rate under dynamic and uncertain conditions**.  

*(Intent: Develop adaptive fuzzy control for nonlinear reactor dynamics in Python.)*

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
The task is to **implement a Python-based fuzzy logic control system for optimizing chemical reactor performance by managing temperature, pressure, and reaction rate under dynamic and uncertain conditions**.  

*(Intent: Develop adaptive fuzzy control for nonlinear reactor dynamics in Python.)*
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
from scipy.integrate import odeint
from skfuzzy import control
from skfuzzy import control as ctrl
from skfuzzy import membership

# Parameters
T_ref = 90.0  # Target temperature (°C)
P_ref = 10.0  # Target pressure (bar)
R_ref = 0.5  # Target reaction rate (mol/min)

# Dynamics
def dynamics(t, state, P, T, R):
    dTdt = 0.005 * (T - T_ref)  # Temperature decay
    dPdt = 0.005 * (P - P_ref)  # Pressure decay
    dRdt = 0.005 * (R - R_ref)  # Reaction rate decay
    return [dTdt, dPdt, dRdt]

# State space
def state_space(t, state):
    return state

# Input space
def input_space(t, state):
    return [state[0], state[1], state[2]]

# Output space
def output_space(t, state):
    return [state[0], state[1], state[2]]

# Membership functions
def temperature_func(x):
    return membership.trimf(x, [80.0, 90.0, 100.0])

def pressure_func(x):
    return membership.trimf(x, [8.0, 10.0, 12.0])

def reaction_rate_func(x):
    return membership.trimf(x, [0.4, 0.5, 0.6])

# Fuzzy logic rules
def temperature_rules():
    return [
        ctrl.Rule(output_space(0, [80.0, 90.0, 100.0]) & input_space(0, [8.0, 10.0, 12.0]) & state_space(0, [0.0, 0.0, 0.0]), [0.0, 0.0, 0
