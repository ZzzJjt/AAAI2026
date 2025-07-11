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

For example, simulate a steel rolling process where the thickness gradually drifts out of control. The SPC system identifies this trend through control chart signals and triggers an alarm. It then suggests a parameter adjustment in the rolling pressure, helping operators correct the deviation before it affects product quality or results in material scrap. The system continues to monitor the thickness, ensuring it remains within acceptable limits, and maintains a stable production process.

**T-A-B:**

🟥 T（Task）

Develop a Python-based SPC system for steel manufacturing, focusing on monitoring and controlling key quality metrics such as tensile strength, thickness, and surface finish. Implement control charts and alarms to detect process deviations, and provide corrective action suggestions to maintain consistent product quality.

🟩 A（Action）

Implement a Python script that:

1. **Data Collection:** Define a data structure to store real-time quality metrics, such as tensile strength, thickness, and surface finish.
2. **Control Charts:** Implement X̄, R, and S charts to monitor the stability of the manufacturing process. Calculate control limits based on historical data and current process conditions.
3. **Alarm Logic:** Develop logic to trigger alarms when process metrics exceed control limits, indicating potential quality issues.
4. **Corrective Actions:** Provide a set of predefined corrective actions that operators can follow to address out-of-control conditions, such as adjusting process parameters or inspecting equipment.
5. **Simulation:** Simulate a steel manufacturing process, including variations in key quality metrics, and demonstrate how the SPC system can detect and respond to these deviations in real-time.

🟩 B（Behavior）

The Python script should:

- Collect real-time quality data and calculate control limits for X̄, R, and S charts.
- Trigger alarms when process metrics exceed control limits, indicating potential quality issues.
- Provide a set of predefined corrective actions for operators to follow when alarms are triggered.
- Simulate a steel manufacturing process with variations in key quality metrics, demonstrating how the SPC system can detect and respond to these deviations in real-time.

🟩 C（Condition）

The Python script should be able to:

- Continuously monitor and analyze real-time quality data from a steel manufacturing process.
- Detect deviations from process stability using control charts and alarms.
- Provide corrective action suggestions to maintain consistent product quality.
- Simulate a steel manufacturing process with variations in key quality metrics, demonstrating the effectiveness of the SPC system in maintaining process stability and reducing waste.

🟩 R（Result）

The SPC system should help maintain stable production, reduce process variability, and minimize waste by allowing early detection and correction of quality issues. It enables a
