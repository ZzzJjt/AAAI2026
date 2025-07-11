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

**Code structure:**

1. Import necessary libraries (e.g., numpy, pandas, matplotlib, and scipy)
2. Define functions for data collection, control chart calculations, and alarm management
3. Implement a main loop to continuously monitor the steel manufacturing process
4. Simulate the steel manufacturing process with varying quality metrics
5. Visualize the control charts and alarms in real-time
6. Suggest corrective actions based on alarm conditions
7. Evaluate the performance of the SPC system in terms of process stability, defect reduction, and waste minimization.

**Code snippets:**

1. Data collection function:

```python
def collect_data(process):
    tensile_strength = process.tensile_strength()
    thickness = process.thickness()
    surface_finish = process.surface_finish()
    return tensile_strength, thickness, surface_finish
```

2. Control chart calculation functions:

```python
def calculate_xbar_chart(data):
    xbar = np.mean(data, axis=0)
    upper_control_limit = np.percentile(data, 99.73)
    lower_control_limit = np.percentile(data, 0.27)
    return xbar, upper_control_limit, lower_control_limit

def calculate_r_chart(data):
    r = np.apply_along_axis(np.std, 0, data)
    upper_control_limit = np.percentile(r, 99.73)
    lower_control_limit = np.percentile(r, 0.27)
    return r, upper_control_limit, lower_control_limit
```

3. Alarm management function:

```python
def check_alarms(xbar, r, upper_control_limit, lower_control_limit):
    tensile_strength_alarm = xbar[0] > upper_control_limit[0] or xbar[0] < lower_control_limit[0]
    thickness_alarm = xbar[1] > upper_control_limit[1] or xbar[1
