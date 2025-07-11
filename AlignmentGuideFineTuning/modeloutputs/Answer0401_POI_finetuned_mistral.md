### Intent:
The task involves implementing an MPC controller in Python to optimize a two-stage batch chemical process with time delays, ensuring stable tank levels while responding to fluctuating demand forecasts.

### Prompt:
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**R-I-S-E**

🟥 R（Role）

Act as a process control engineer specializing in AI-driven control systems for chemical reactors.

🟩 I（Input）

You are given a dataset containing historical temperature control data from a chemical reactor with known nonlinear and time-varying behavior. The reactor’s traditional PID control performance under different operating scenarios is also available for comparison.

🟧 S（Steps）
	1.	Develop Python code to build an artificial neural network (ANN) model trained on the historical dataset.
	2.	Implement an ANN-based controller for temperature regulation, leveraging its predictive and adaptive capabilities.
	3.	Simulate the chemical reactor’s temperature control dynamics using both ANN and traditional PID methods.
	4.	Compare and analyze the performance of the ANN controller against the PID controller under various dynamic conditions.

🟦 E（Expectation）

Demonstrate that the ANN-based controller offers improved temperature stability, quicker response to disturbances, and better handling of nonlinearities compared to the traditional PID controller, thereby proving its effectiveness in advanced process control applications.

### Generated Code:
The task involves implementing an MPC controller in Python to optimize a two-stage batch chemical process with time delays, ensuring stable tank levels while responding to fluctuating demand forecasts.
**Artificial Neural Network Control for Temperature Regulation in a Chemical Reactor Using Python:**

**Origin**

Develop Python code to implement an artificial neural network (ANN) for advanced process control of the temperature in a chemical reactor. The control system should leverage the predictive and adaptive capabilities of ANNs to manage the reactor’s temperature, considering the nonlinear and time-varying nature of the reactor’s dynamics. Train the ANN using historical process data to optimize temperature control, ensuring stability and efficiency under varying operational conditions.

Implement Python code to simulate the chemical reactor’s temperature control dynamics and demonstrate how ANN-based control can outperform traditional methods in handling complex, nonlinear systems.

**R-I-S-E**

🟥 R（Role）

Act as a process control engineer specializing in AI-driven control systems for chemical reactors.

🟩 I（Input）

You are given a dataset containing historical temperature control data from a chemical reactor with known nonlinear and time-varying behavior. The reactor’s traditional PID control performance under different operating scenarios is also available for comparison.

🟧 S（Steps）
	1.	Develop Python code to build an artificial neural network (ANN) model trained on the historical dataset.
	2.	Implement an ANN-based controller for temperature regulation, leveraging its predictive and adaptive capabilities.
	3.	Simulate the chemical reactor’s temperature control dynamics using both ANN and traditional PID methods.
	4.	Compare and analyze the performance of the ANN controller against the PID controller under various dynamic conditions.

🟦 E（Expectation）

Demonstrate that the ANN-based controller offers improved temperature stability, quicker response to disturbances, and better handling of nonlinearities compared to the traditional PID controller, thereby proving its effectiveness in advanced process control applications.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 📋 Problem Definition
# 
# 🔹 Objective
# 
# Develop an MPC controller in Python to optimize the two-stage batch process of a chemical production system.
# The controller must maintain stable tank levels while responding to fluctuating demand forecasts.
# 
# 🔸 Constraints
# 
#  •	The system operates in a discrete-time environment with a 1-hour sampling interval.
#  •	The process consists of two tanks: Tank 1 (T1) and Tank 2 (T2).
#  •	Tank 1 is filled from an external source at a constant rate of 100 L/h.
#  •	Tank 2 is filled from Tank 1 at a rate proportional to the level difference between the two tanks.
#  •	The demand forecast is a step function with three demand levels: 0, 50, and 100 L/h.
#  •	The control input is the valve opening to Tank 2, which must be between 0 and 100%.
#  •	The system has a 2-hour time delay due to transport delays.
# 
# 🔹 Task Breakdown
# 
# 1.	Define the system dynamics and constraints.
# 
# 2.	Implement the MPC algorithm with a prediction horizon of 3 steps and a control horizon of 1 step.
# 
# 3.	Optimize the control policy using a quadratic cost function and linear constraints.
# 
# 4.	Simulate the closed-loop system under fluctuating demand and compare to a baseline.
# 
# 5.	Analyze the results in terms of stability, tracking performance, and robustness to disturbances.

# 🧪 Chemical Batch Process Simulation
class ChemicalBatchProcess:
    def __init__(self):
        # Parameters
        self.dt = 1  # Hourly sampling interval
        self.T1_init = 1000  # Initial volume in
