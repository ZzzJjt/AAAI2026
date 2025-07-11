### Intent:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate position, velocity, and attitude responses to thrust and control surface inputs, incorporating aerodynamic forces and wind disturbances for flight control applications.  

*(Focus: Aircraft simulation for control system design, with states, inputs, and aerodynamics explicitly modeled.)*

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**T-A-G:**

🟥 T（Task）

Create a Python-based statistical process control (SPC) system to monitor and improve quality in steel manufacturing.

🟩 A（Action）

Simulate key quality metrics such as tensile strength, thickness, and surface finish in real time. Implement SPC tools including X̄ and R charts to detect process deviations, trigger alarms for out-of-control conditions, and recommend corrective actions to minimize defects and maintain consistency.

🟦 G（Goal）

Ensure high product quality, reduce waste, and maintain process stability by enabling early detection and response to quality variations through a data-driven, real-time control system.

### Generated Code:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate position, velocity, and attitude responses to thrust and control surface inputs, incorporating aerodynamic forces and wind disturbances for flight control applications.  

*(Focus: Aircraft simulation for control system design, with states, inputs, and aerodynamics explicitly modeled.)*
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**T-A-G:**

🟥 T（Task）

Create a Python-based statistical process control (SPC) system to monitor and improve quality in steel manufacturing.

🟩 A（Action）

Simulate key quality metrics such as tensile strength, thickness, and surface finish in real time. Implement SPC tools including X̄ and R charts to detect process deviations, trigger alarms for out-of-control conditions, and recommend corrective actions to minimize defects and maintain consistency.

🟦 G（Goal）

Ensure high product quality, reduce waste, and maintain process stability by enabling early detection and response to quality variations through a data-driven, real-time control system.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 100.0  # Mean value
sigma = 10.0  # Standard deviation
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)  # Sample points

# Generate normal distribution
dist = norm(mu, sigma)

# Generate 1000 samples
samples = dist.rvs(size=1000)

# Calculate mean and standard deviation
mean_samples = np.mean(samples)
std_samples = np.std(samples)

# Generate 10000 samples
samples_10000 = dist.rvs(size=10000)
mean_samples_10000 = np.mean(samples_10000)
std_samples_10000 = np.std(samples_10000)

# Calculate mean and standard deviation for 10000 samples
mean_samples_10000 = np.mean(samples_10000)
std_samples_10000 = np.std(samples_10000)

# Print results
print("Mean of 1000 samples:", mean_samples)
print("Standard deviation of 1000 samples:", std_samples)
print("Mean of 10000 samples:", mean_samples_10000)
print("Standard deviation of 10000 samples:", std_samples_10000)

# Plot histogram of 1000 samples
plt.hist(samples, bins=30, density=True)
plt.title("Histogram of 1000 Samples")
plt.show()

# Plot histogram of 10000 samples
plt.hist(samples_10000, bins=30, density=True)
plt.title("Histogram of 10000 Samples")
plt.show()

# Plot density plots of 1000 samples
plt.plot(x, dist.pdf(x, mu, sigma), label="
