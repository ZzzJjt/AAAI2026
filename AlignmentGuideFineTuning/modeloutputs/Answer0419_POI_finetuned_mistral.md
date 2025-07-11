### Intent:
**Intent Summary:**  
Develop a real-time statistical process control (SPC) system in Python to monitor manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect anomalies via subgroup analysis, and trigger corrective action alerts when limits are violated.  

*(Key focus: SPC implementation for quality monitoring with automated alerts)*

### Prompt:
**Model Predictive Control for Wind Farm Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm to optimize the operation of a wind farm. The control system should consider factors such as wind speed variability, turbine dynamics, and power output efficiency. It should also ensure grid stability while accounting for constraints on turbine operation, energy storage, and power dispatch under fluctuating environmental conditions.

Implement C++ code to simulate the wind farm’s operational dynamics and demonstrate the effectiveness of the MPC in managing real-time power generation and distribution.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ control systems engineer specializing in renewable energy optimization and real-time predictive algorithms.

🟩 I（Input）

You are developing a model predictive control (MPC) system for a wind farm. The system must handle variable wind speeds, nonlinear turbine dynamics, and power output optimization. It should also manage energy storage and ensure grid stability under environmental and operational constraints.

🟧 S（Steps）
	1.	Model the dynamic behavior of wind turbines and storage systems in C++, accounting for wind variability and physical constraints.
	2.	Implement a model predictive control (MPC) algorithm that forecasts wind conditions and optimizes turbine output and power dispatch.
	3.	Integrate logic to manage energy storage and grid delivery while maintaining performance and constraint adherence.
	4.	Simulate operational scenarios (e.g., gusty wind, load surges) to evaluate system responsiveness and efficiency under real-time conditions.

🟦 E（Expectation）

The MPC system should demonstrate improved power generation efficiency, more stable grid output, and enhanced adaptability to environmental disturbances compared to traditional control systems—ensuring robust and intelligent operation of the wind farm.

### Generated Code:
**Intent Summary:**  
Develop a real-time statistical process control (SPC) system in Python to monitor manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect anomalies via subgroup analysis, and trigger corrective action alerts when limits are violated.  

*(Key focus: SPC implementation for quality monitoring with automated alerts)*
**Model Predictive Control for Wind Farm Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm to optimize the operation of a wind farm. The control system should consider factors such as wind speed variability, turbine dynamics, and power output efficiency. It should also ensure grid stability while accounting for constraints on turbine operation, energy storage, and power dispatch under fluctuating environmental conditions.

Implement C++ code to simulate the wind farm’s operational dynamics and demonstrate the effectiveness of the MPC in managing real-time power generation and distribution.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ control systems engineer specializing in renewable energy optimization and real-time predictive algorithms.

🟩 I（Input）

You are developing a model predictive control (MPC) system for a wind farm. The system must handle variable wind speeds, nonlinear turbine dynamics, and power output optimization. It should also manage energy storage and ensure grid stability under environmental and operational constraints.

🟧 S（Steps）
	1.	Model the dynamic behavior of wind turbines and storage systems in C++, accounting for wind variability and physical constraints.
	2.	Implement a model predictive control (MPC) algorithm that forecasts wind conditions and optimizes turbine output and power dispatch.
	3.	Integrate logic to manage energy storage and grid delivery while maintaining performance and constraint adherence.
	4.	Simulate operational scenarios (e.g., gusty wind, load surges) to evaluate system responsiveness and efficiency under real-time conditions.

🟦 E（Expectation）

The MPC system should demonstrate improved power generation efficiency, more stable grid output, and enhanced adaptability to environmental disturbances compared to traditional control systems—ensuring robust and intelligent operation of the wind farm.
# Real-Time Statistical Process Control System in Python

This project implements a real-time statistical process control (SPC) system using Python to monitor and optimize manufacturing quality metrics. The system uses control charts to track tensile strength, thickness, and surface finish measurements, detects anomalies using subgroup analysis, and triggers alerts when process deviations exceed control limits.

## Key Features

* Real-time monitoring of key quality metrics
* Subgroup analysis for early detection of process shifts
* Control chart visualization for trend analysis
* Automated alerts for out-of-control conditions
* Modular, scalable Python implementation

## Getting Started

To get started, follow these steps:

1. **Install Required Libraries**
   Install the required libraries by running:
   ```
   pip install numpy pandas matplotlib
   ```

2. **Create Quality Data**
   Generate a simulated quality dataset with tensile strength, thickness, and surface finish measurements. Save the data in a CSV file for later analysis.

3. **Implement SPC Algorithm**
   Implement the SPC logic in Python, including:
   - Subgroup analysis
   - Control chart calculation
   - Alert generation based on control limits
   - Visualization of control charts

4. **Run Simulation**
   Simulate manufacturing data and process variations, then run the SPC system to detect and respond to quality issues in real time.

## Quality Metrics and Control Charts

The SPC system tracks three key quality metrics:

* **Tensile Strength (TS)**: Measurement of the material’s ability to withstand force.
* **Thickness (TH)**: Measurement of the material’s thickness.
* **Surface Finish (SF)**: Measurement of the material’s smoothness.

For each metric, the system calculates control charts using:

* **X-bar (mean) chart**: Tracks the average value of each subgroup.
* **R chart**: Tracks the range of values within each subgroup.
* **Control limits**: Based on historical process data, the system calculates upper and lower control limits for each chart.

## Subgroup Analysis and Alerting

The system uses subgroup analysis to detect process shifts
