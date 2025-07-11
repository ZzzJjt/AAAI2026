### Intent:
The task involves developing a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, alarms, and corrective actions to reduce variability and defects.  

*Intent summary for code generation:*  
**"Implement Python code for real-time SPC monitoring in steel production using control charts to detect deviations, trigger alarms, and suggest corrective actions for quality optimization."**

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
The task involves developing a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, alarms, and corrective actions to reduce variability and defects.  

*Intent summary for code generation:*  
**"Implement Python code for real-time SPC monitoring in steel production using control charts to detect deviations, trigger alarms, and suggest corrective actions for quality optimization."**
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
tensile_strength = np.random.normal(750, 10, 100)

# Sample data for thickness
thickness = np.random.normal(0.5, 0.01, 100)

# Sample data for surface finish
surface_finish = np.random.normal(2.5, 0.05, 100)

# Sample data for control chart
x_bar = np.mean(tensile_strength)
r = np.array([np.mean(tensile_strength[:50]), np.mean(tensile_strength[50:])])
s = np.sqrt(np.sum((tensile_strength[:50] - r[0]) ** 2) / 4 +
            np.sum((tensile_strength[50:] - r[1]) ** 2) / 4)

# Simulate control chart data
x_bar_chart = np.array([x_bar, r[0], r[1], s])

# Plot control chart
plt.figure(figsize=(10, 6))
plt.plot(x_bar_chart[0], label='x̄')
plt.plot(x_bar_chart[1], label='r1')
plt.plot(x_bar_chart[2], label='r2')
plt.plot(x_bar_chart[3], label='s')
plt.legend()
plt.show()

# Simulate out-of-control condition
x_bar_chart[0] = 700

# Calculate control limits
upper_limit = x_bar_chart[0] + 3 * s
lower_limit = x_bar_chart[0] - 3 * s

# Simulate alarm
if x_bar_chart[0] > upper_limit or x_bar_chart[0] < lower_limit:
    print("Tensile strength out of control!")

# Suggest corrective action
if x_bar_chart[0] < 700:
    print("Increase rolling pressure
