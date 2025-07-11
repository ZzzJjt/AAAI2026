### Intent:
The task involves developing a Model Predictive Control (MPC) system in Python to optimize power output while maintaining safe turbine temperatures in response to dynamic load demands, with constraints on ramp rates and operating limits.

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.

### Generated Code:
The task involves developing a Model Predictive Control (MPC) system in Python to optimize power output while maintaining safe turbine temperatures in response to dynamic load demands, with constraints on ramp rates and operating limits.
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 100.0  # Mean of normal distribution
sigma = 10.0  # Standard deviation of normal distribution
x_min = 90.0  # Lower limit of normal distribution
x_max = 110.0  # Upper limit of normal distribution

# Generate 1000 samples from the normal distribution
samples = norm.rvs(mu, sigma, size=1000)

# Calculate the mean and standard deviation of the samples
mean_samples = np.mean(samples)
std_samples = np.std(samples)

# Generate 1000 samples from the normal distribution with the calculated mean and standard deviation
samples_mean_std = norm.rvs(mean_samples, std_samples, size=1000)

# Calculate the mean and standard deviation of the samples with the calculated mean and standard deviation
mean_samples_mean_std = np.mean(samples_mean_std)
std_samples_mean_std = np.std(samples_mean_std)

# Print the results
print("Mean of samples: ", mean_samples)
print("Standard deviation of samples: ", std_samples)
print("Mean of samples with calculated mean and standard deviation: ", mean_samples_mean_std)
print("Standard deviation of samples with calculated mean and standard deviation: ", std_samples_mean_std)

# Plot the histograms of the samples and samples with calculated mean and standard deviation
plt.figure(figsize=(10, 6))

# Histogram of samples
plt.subplot(1, 2, 1)
plt.hist(samples, bins=30, color='blue', alpha=0.5)
plt.title('Histogram of samples')

# Histogram of samples with calculated mean and standard deviation
plt.subplot(1, 2, 2)
plt.hist(samples_mean_std, bins=30, color='red', alpha=0.5)
plt.title('Histogram of samples with calculated mean and standard deviation')

plt.show()

# Calculate the mean and standard deviation of the samples with the calculated mean and
