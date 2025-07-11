### Intent:
Develop a Model Predictive Control (MPC) system for wind farm power optimization that adjusts turbine blade pitch angles to maintain stable grid power output while managing energy storage constraints.

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
Develop a Model Predictive Control (MPC) system for wind farm power optimization that adjusts turbine blade pitch angles to maintain stable grid power output while managing energy storage constraints.
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
n_samples = 1000  # Number of samples

# Generate normal samples
samples = norm.rvs(mu, sigma, n_samples)

# Calculate mean and standard deviation
mean_val = np.mean(samples)
std_dev = np.std(samples)

# Generate histogram
plt.hist(samples, bins=30, density=True)
plt.title('Histogram of Normal Samples')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# Generate normal cumulative distribution function
def normal_cdf(x, mu, sigma):
    return 0.5 * (1 + erf(x / np.sqrt(2) / sigma))

# Generate normal cumulative distribution function plot
x = np.linspace(mu - 5*std_dev, mu + 5*std_dev, 100)
plt.plot(x, normal_cdf(x, mu, sigma), label='Normal CDF')
plt.fill_between(x, normal_cdf(x, mu, sigma), alpha=0.2)
plt.title('Normal Cumulative Distribution Function')
plt.xlabel('Value')
plt.ylabel('CDF')
plt.legend()
plt.show()

# Generate normal cumulative distribution function plot with standard deviation
plt.plot(x, normal_cdf(x, mu, std_dev), label='Normal CDF (std dev = 10)')
plt.fill_between(x, normal_cdf(x, mu, std_dev), alpha=0.2)
plt.title('Normal Cumulative Distribution Function (std dev = 10)')
plt.xlabel('Value')
plt.ylabel('CDF')
plt.legend()
plt.show()

# Generate normal cumulative distribution function plot with standard deviation
plt.plot(x, normal_cdf(x, mu, 5*std_dev), label='Normal CDF (std dev = 50)')
plt.fill_between(x, normal_cdf(x
