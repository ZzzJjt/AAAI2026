### Intent:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect deviations, trigger alarms, and simulate corrective actions to reduce variability and defects.  

*(Focus: Real-time monitoring, anomaly detection, and process optimization via SPC tools in Python.)*

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
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect deviations, trigger alarms, and simulate corrective actions to reduce variability and defects.  

*(Focus: Real-time monitoring, anomaly detection, and process optimization via SPC tools in Python.)*
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

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process. The system should be scalable and adaptable to different manufacturing processes and quality metrics.

**Code Snippet:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate steel manufacturing process
def simulate_steel_production(num_samples):
    tensile_strength = np.random.normal(loc=500, scale=10, size=num_samples)
    thickness = np.random.normal(loc=10, scale=0.1, size=num_samples)
    surface_finish = np.random.normal(loc=0.5, scale=0.05, size=num_samples)
    return tensile_strength, thickness, surface_finish

# Implement SPC tools
def calculate_control_limits(data, alpha=0.05):
    mean = np.mean(data)
    std_dev = np.std(data)
    upper_limit = mean + 3 * std_dev
    lower_limit = mean - 3 * std_dev
    return mean, upper_limit, lower_limit

def plot_control_chart(data, mean, upper_limit, lower_limit):
    plt.figure(figsize=(10, 5))
    plt.plot(data, label='Data')
    plt.axhline(y=mean, color='r', linestyle='--', label='Mean')
    plt.axhline(y=upper_limit, color='g', linestyle='--', label='Upper Limit')
    plt.axhline(y=lower_limit, color='g', linestyle='--', label='Lower Limit')
    plt.legend()
    plt.show()

# Detect out-of-control conditions
def detect_out_of_control(data, mean, upper_limit, lower_limit):
    out_of_control = []
    for i in range(len(data)):
        if data[i] > upper_limit or data[i] < lower_limit:
            out_of_control.append(i)
    return out_of_control

# Simulate and monitor steel production
num_samples = 100
tensile_strength, thickness, surface_finish = simulate_steel_production(num_samples)

# Calculate control limits
mean_tensile, upper_limit_tensile, lower_limit_tensile = calculate_control_limits(tensile_strength)
mean_thickness, upper_limit_thickness, lower_limit_thickness = calculate_control_limits(thickness)
mean_surface, upper_limit_surface, lower_limit_surface = calculate_control_limits(surface_finish)

# Plot control charts
plot_control_chart(tensile_strength, mean_tensile, upper_limit_tensile, lower_limit_tensile)
plot_control_chart(thickness, mean_thickness, upper_limit_thickness, lower
