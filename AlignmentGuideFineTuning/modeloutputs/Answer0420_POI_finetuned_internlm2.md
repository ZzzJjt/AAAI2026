### Intent:
The task involves developing a Model Predictive Control (MPC) system in Python to optimize power output while maintaining safe turbine temperatures in response to dynamic load demands, with constraints on ramp rates and operating limits.

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.

### Generated Code:
The task involves developing a Model Predictive Control (MPC) system in Python to optimize power output while maintaining safe turbine temperatures in response to dynamic load demands, with constraints on ramp rates and operating limits.
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process. The code should be modular, well-documented, and easy to integrate with existing manufacturing systems.

🟥 A（Action）

Develop a Python code snippet that simulates the steel manufacturing process, including real-time data generation for tensile strength, thickness, and surface finish. Implement SPC tools such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions. Design a logic system to trigger alarms and suggest corrective actions based on the detected deviations. Evaluate the system's performance by demonstrating how it can reduce process variation and improve consistency in the steel manufacturing process.

**C:**

Develop a Python code snippet that simulates the steel manufacturing process, including real-time data generation for tensile strength, thickness, and surface finish. Implement SPC tools such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions. Design a logic system to trigger alarms and suggest corrective actions based on the detected deviations. Evaluate the system's performance by demonstrating how it can reduce process variation and improve consistency in the steel manufacturing process.

**Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate steel manufacturing process
def simulate_process():
    t = np.linspace(0, 10, 1000)  # Time vector
    thickness = 0.1 * np.sin(2 * np.pi * t) + 0.05 * np.random.randn(1000)  # Thickness variation
    tensile_strength = 500 + 50 * np.random.randn(1000)  # Tensile strength variation
    surface_finish = 0.5 * np.sin(4 * np.pi * t) + 0.1 * np.random.randn(1000)  # Surface finish variation

    return thickness, tensile_strength, surface_finish

# Generate data
thickness, tensile_strength, surface_finish = simulate_process()

# Plot data
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(thickness, label='Thickness')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(tensile_strength, label='Tensile Strength')
plt.legend()
plt.show()

# Implement SPC tools
def calculate_control_limits(data, alpha=0.05):
    n = len(data)
    s = np
