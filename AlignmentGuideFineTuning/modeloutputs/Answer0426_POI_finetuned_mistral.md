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
# Chemical Reactor Fuzzy Control in Python

This code implements a fuzzy logic controller in Python to optimize the operation of a chemical reactor. The controller adjusts the reactor's temperature, pressure, and reaction rate by dynamically adjusting heater power, pressure valve settings, and reactant flow rates. The fuzzy logic system uses linguistic terms to represent the process variables and control actions, and employs a rule-based approach to make decisions.

## Fuzzy Logic Controller Design

The fuzzy logic controller is designed with the following components:

1. **Fuzzification**: Maps the process variables (temperature, pressure, and reaction rate) to fuzzy sets using linguistic terms such as "cold," "hot," "low," "medium," and "high."

2. **Fuzzy Inference System (FIS)**: Uses a rule-based approach to make decisions based on the fuzzified process variables. The rules are defined using IF-THEN logic, where conditions (e.g., "temperature is high") are matched with actions (e.g., "increase heater power").

3. **Defuzzification**: Converts the fuzzy output (control actions) into a crisp value that can be used to adjust the reactor's control parameters.

## System Overview

The chemical reactor operates under nonlinear and time-varying conditions, making it difficult to control using traditional methods such as PID. The fuzzy logic controller provides a more adaptive and robust solution by handling uncertainty and disturbances. The system architecture is shown below:

![System Architecture](https://i.imgur.com/6jJ6jJl.png)

## Implementation

### Step 1: Define Fuzzy Sets

Define membership functions for temperature, pressure, and reaction rate using Python's `triu` function:

```python
import numpy as np

# Membership functions
def triu(x, a=1.0, b=5.0):
    return np.piecewise(x, [x < a, x >= a], [0, (x - a) / (b - a)])

# Fuzzy sets for temperature
temperature_cold =
