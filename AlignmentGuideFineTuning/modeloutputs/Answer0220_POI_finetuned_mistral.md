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
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 1: Load and Preprocess Data
# Load historical steel manufacturing data
data = pd.read_csv('steel_manufacturing_data.csv')

# Preprocess the data: remove missing values, normalize variables, split into training and testing sets
data = data.dropna()
X = data[['tensile_strength', 'thickness', 'surface_finish']]
y = data['defect_rate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 2: Train the Model
# Train a linear regression model to predict defect rate based on tensile strength, thickness, and surface finish
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Evaluate the Model
# Evaluate the model's performance on the test set
y_pred = model.predict(X_test)
print(f'R-squared: {r2_score(y_test, y_pred)}')

# Step 4: Implement SPC System
# Initialize control charts for each variable
xbar_chart = ControlChart(data='Xbar_Chart', limits=(0, 100))
r_chart = ControlChart(data='R_Chart', limits=(0, 3))
s_chart = ControlChart(data='S_Chart', limits=(0, 2))

# Update the charts with new data every hour
new_data = pd.DataFrame({
    'tensile_strength': [95, 98, 96, 97],
    'thickness': [2.5, 2.4, 2.5, 2.5],
    'surface_finish': [120, 115, 118, 120],
    'defect_rate': [0.01, 0.005, 0.015,
