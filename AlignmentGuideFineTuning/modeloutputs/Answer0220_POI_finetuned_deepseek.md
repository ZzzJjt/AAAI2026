### Intent:
The task involves developing a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, anomaly detection rules, and corrective action suggestions to maintain production stability and reduce defects.

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**C-A-R-E:**

🟥 C（Context）

Steel manufacturing processes are sensitive to variability in key quality metrics such as tensile strength, thickness, and surface finish. Without real-time monitoring and analysis, these variations can lead to product defects, increased waste, and inconsistent quality, making it difficult to meet industry standards and customer expectations.

🟩 A（Action）

Develop Python code to implement a statistical process control (SPC) system that continuously monitors these quality metrics. Use control charts (e.g., X̄, R, and S charts) and other SPC techniques to detect deviations from process stability. Incorporate alarms for out-of-control conditions and provide logic to suggest corrective actions that guide operators in reducing defects and maintaining process consistency.

🟨 R（Result）

The SPC system should help maintain stable production, reduce process variability, and minimize waste by allowing early detection and correction of quality issues. It enables a proactive rather than reactive quality control strategy, ensuring that production stays within specification limits.

🟦 E（Example）

For example, simulate a steel rolling process where the thickness gradually drifts out of control. The SPC system identifies this trend through control chart signals and triggers an alarm. It then suggests a parameter adjustment in the rolling pressure, helping operators correct the deviation before it affects product quality or results in material scrap.

### Generated Code:
The task involves developing a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, anomaly detection rules, and corrective action suggestions to maintain production stability and reduce defects.
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**C-A-R-E:**

🟥 C（Context）

Steel manufacturing processes are sensitive to variability in key quality metrics such as tensile strength, thickness, and surface finish. Without real-time monitoring and analysis, these variations can lead to product defects, increased waste, and inconsistent quality, making it difficult to meet industry standards and customer expectations.

🟩 A（Action）

Develop Python code to implement a statistical process control (SPC) system that continuously monitors these quality metrics. Use control charts (e.g., X̄, R, and S charts) and other SPC techniques to detect deviations from process stability. Incorporate alarms for out-of-control conditions and provide logic to suggest corrective actions that guide operators in reducing defects and maintaining process consistency.

🟨 R（Result）

The SPC system should help maintain stable production, reduce process variability, and minimize waste by allowing early detection and correction of quality issues. It enables a proactive rather than reactive quality control strategy, ensuring that production stays within specification limits.

🟦 E（Example）

For example, simulate a steel rolling process where the thickness gradually drifts out of control. The SPC system identifies this trend through control chart signals and triggers an alarm. It then suggests a parameter adjustment in the rolling pressure, helping operators correct the deviation before it affects product quality or results in material scrap.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Sample data for tensile strength
tensile_strength = np.random.normal(750, 10, 1000)

# Sample data for thickness
thickness = np.random.normal(2.5, 0.05, 1000)

# Sample data for surface finish
surface_finish = np.random.normal(2.0, 0.1, 1000)

# Define control limits
upper_limit_tensile = 780
lower_limit_tensile = 720
upper_limit_thickness = 2.7
lower_limit_thickness = 2.3
upper_limit_surface_finish = 2.2
lower_limit_surface_finish = 1.8

# Define control chart parameters
n_samples = 1000
n_control_points = 10
n_cycles = 10

# Initialize control chart variables
X_bar = np.zeros((n_samples, n_control_points, n_cycles))
R_bar = np.zeros((n_samples, n_control_points, n_cycles))
S_bar = np.zeros((n_samples, n_control_points, n_cycles))

# Generate control chart data
for i in range(n_samples):
    X_bar[i] = np.mean(tensile_strength[i:i+n_control_points])
    R_bar[i] = np.sum((X_bar[i] - np.mean(tensile_strength[i:i+n_control_points]))**2) / n_control_points
    S_bar[i] = np.sqrt(R_bar[i])

# Generate control chart plots
fig, axs = plt.subplots(3, 1, figsize=(8, 6))

axs[0].plot(X_bar[:, 0, 0], label='X̄')
axs[0].set_title('Tensile Strength X̄')
axs[0].legend()

axs
