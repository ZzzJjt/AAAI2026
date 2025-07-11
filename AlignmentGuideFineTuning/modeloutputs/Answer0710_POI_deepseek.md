### Intent:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)

### Generated Code:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)

**Python Code:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate steel manufacturing quality metrics
steel_data = np.random.normal(loc=7000, scale=100, size=1000)  # tensile strength (kN)
steel_thickness = np.random.normal(loc=0.8, scale=0.01, size=1000)  # thickness (mm)
steel_surface = np.random.normal(loc=2.5, scale=0.1, size=1000)  # surface finish (μm)

# Implement real-time SPC tools
X_bar = np.mean(steel_data)
R = np.sum(np.square(steel_data - X_bar)) / len(steel_data)
S = np.sqrt(np.sum(np.square(np.diff(steel_data))) / (len(steel_data)-1))

# Detect out-of-control signals and rule violations
control_limits = [X_bar - 3*S, X_bar + 3*S]
out_of_control = np.where(np.isnan(steel_data) | steel_data < control_limits[0] | steel_data > control_limits[1])

# Alarm system with corrective action suggestions
if len(out_of_control[0]) > 0:
    print("Out-of-control conditions detected:")
    for i in out_of_control[0]:
        print(f"Tensile strength: {i}")
    print("Suggestion: Investigate the manufacturing process and adjust the process parameters to bring the quality metrics back within control limits.")

# Plot the control charts
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(steel_data, label='Actual')
plt.plot([X_bar] * len(steel_data), label='X̄', linestyle="--")
plt.fill_between([X_bar - 3*S, X_bar + 3*S], color="lightgray", alpha=0.2)
