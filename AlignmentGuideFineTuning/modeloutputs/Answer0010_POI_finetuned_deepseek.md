### Intent:
**Intent Summary:**  
Develop a model predictive control (MPC) system in C++ to optimize HVAC operations by dynamically adjusting heating, cooling, and humidity control based on real-time indoor conditions, weather forecasts, and occupancy patterns, while minimizing energy usage.  

*(Focus: MPC algorithm for HVAC control, energy efficiency, and comfort optimization.)*

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.

### Generated Code:
**Intent Summary:**  
Develop a model predictive control (MPC) system in C++ to optimize HVAC operations by dynamically adjusting heating, cooling, and humidity control based on real-time indoor conditions, weather forecasts, and occupancy patterns, while minimizing energy usage.  

*(Focus: MPC algorithm for HVAC control, energy efficiency, and comfort optimization.)*
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 100.0  # Mean temperature (°C)
sigma = 5.0  # Standard deviation
T_min = 50.0  # Minimum temperature (°C)
T_max = 120.0  # Maximum temperature (°C)
T_step = 1.0  # Temperature step (°C)

# Generate random temperature samples
np.random.seed(42)
T = np.random.normal(mu, sigma, 1000)

# Calculate temperature deviations
T_dev = T - mu

# Generate normal distribution for temperature deviations
dist = norm(mu, sigma)

# Generate histogram of temperature deviations
plt.hist(T_dev, bins=50, density=True)
plt.title('Temperature Deviation Histogram')
plt.show()

# Calculate mean and standard deviation of temperature deviations
mean_T_dev = np.mean(T_dev)
std_T_dev = np.std(T_dev)

# Generate normal distribution for temperature deviations
dist_T_dev = norm(mean_T_dev, std_T_dev)

# Generate histogram of temperature deviations
plt.hist(T_dev, bins=50, density=True)
plt.title('Temperature Deviation Histogram')
plt.show()

# Calculate mean and standard deviation of temperature deviations
mean_T_dev = np.mean(T_dev)
std_T_dev = np.std(T_dev)

# Generate normal distribution for temperature deviations
dist_T_dev = norm(mean_T_dev, std_T_dev)

# Generate histogram of temperature deviations
plt.hist(T_dev, bins=50, density=True)
plt.title('Temperature Deviation Histogram')
plt.show()

# Calculate mean and standard deviation of temperature deviations
mean_T_dev = np.mean(T_dev)
std_T_dev = np.std(T_dev)

# Generate normal distribution for temperature deviations
dist_T_dev = norm(mean_T_dev, std_T_
