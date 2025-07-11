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

**Code:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Simulate steel manufacturing quality metrics
np.random.seed(0)
tensile_strength = np.random.normal(500, 50, 1000)
thickness = np.random.normal(0.5, 0.05, 1000)
surface_finish = np.random.normal(8, 1, 1000)

# Create a DataFrame for the quality metrics
quality_data = pd.DataFrame({
    'Tensile Strength': tensile_strength,
    'Thickness': thickness,
    'Surface Finish': surface_finish
})

# Calculate the process average (X̄) and range (R) for each metric
quality_data['X̄'] = quality_data.mean(axis=0)
quality_data['R'] = quality_data.max(axis=0) - quality_data.min(axis=0)

# Calculate the process standard deviation (S) for each metric
quality_data['S'] = quality_data.std(axis=0)

# Calculate the control limits for each metric using the standard deviation
control_limits = {
    'Tensile Strength': (quality_data['X̄']['Tensile Strength'] - 3 * quality_data['S']['Tensile Strength'], 
                        quality_data['X̄']['Tensile Strength'] + 3 * quality_data['S']['Tensile Strength']),
    'Thickness': (quality_data['X̄']['Thickness'] - 3 * quality_data['S']['Thickness'], 
                  quality_data['X̄']['Thickness'] + 3 * quality_data['S']['Thickness']),
    'Surface Finish': (quality_data['X̄']['Surface Finish'] - 3 * quality_data['S']['Surface Finish'], 
                       quality_data['X̄']['Surface Finish'] + 3 * quality_data['S']['Surface Finish'])
}

# Define a function to detect out-of-control conditions
def detect_out_of_control(quality_data, control_limits):
    out_of_control = []
    for metric in quality_data.columns:
        if quality_data[metric].min() < control_limits[metric][0] or quality_data[metric].max() > control_limits[metric][1]:
            out_of_control.append(metric)
    return out_of_control

# Define a function to trigger alarms and suggest corrective actions
def trigger_alarms(quality_data, out_of_control):
