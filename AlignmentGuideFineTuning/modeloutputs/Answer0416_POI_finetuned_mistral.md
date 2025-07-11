### Intent:
**Intent Summary:**  
Develop a C++-based Model Predictive Control (MPC) system for HVAC optimization that dynamically adjusts temperature, humidity, and energy use while accommodating external disturbances and occupancy constraints to balance comfort and efficiency.  

*(Focus: MPC implementation for HVAC with real-time constraints, coded in C++.)*

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ developer specializing in intelligent building systems and advanced control algorithms.

🟩 I（Input）

You are tasked with developing a model predictive control (MPC) system for an HVAC application. The system must manage indoor temperature, humidity, and energy consumption while considering constraints such as fluctuating external temperatures, varying occupancy levels, and energy efficiency goals. The goal is to maintain occupant comfort and optimize performance under dynamic environmental conditions.

🟧 S（Steps）
	1.	Model the HVAC system dynamics in C++, including thermal response, humidity control, and energy usage behavior.
	2.	Implement an MPC algorithm that forecasts future system states and adjusts control signals in real time.
	3.	Incorporate constraints related to energy limits, external weather, and occupancy profiles.
	4.	Simulate various environmental scenarios to validate system adaptability, responsiveness, and efficiency.

🟦 E（Expectation）

The MPC-based control system should demonstrate improved energy efficiency, faster response to environmental changes, and enhanced occupant comfort compared to traditional control approaches—all while respecting operational constraints in real-time conditions.

### Generated Code:
**Intent Summary:**  
Develop a C++-based Model Predictive Control (MPC) system for HVAC optimization that dynamically adjusts temperature, humidity, and energy use while accommodating external disturbances and occupancy constraints to balance comfort and efficiency.  

*(Focus: MPC implementation for HVAC with real-time constraints, coded in C++.)*
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-I-S-E:**

🟥 R（Role）

Act as a C++ developer specializing in intelligent building systems and advanced control algorithms.

🟩 I（Input）

You are tasked with developing a model predictive control (MPC) system for an HVAC application. The system must manage indoor temperature, humidity, and energy consumption while considering constraints such as fluctuating external temperatures, varying occupancy levels, and energy efficiency goals. The goal is to maintain occupant comfort and optimize performance under dynamic environmental conditions.

🟧 S（Steps）
	1.	Model the HVAC system dynamics in C++, including thermal response, humidity control, and energy usage behavior.
	2.	Implement an MPC algorithm that forecasts future system states and adjusts control signals in real time.
	3.	Incorporate constraints related to energy limits, external weather, and occupancy profiles.
	4.	Simulate various environmental scenarios to validate system adaptability, responsiveness, and efficiency.

🟦 E（Expectation）

The MPC-based control system should demonstrate improved energy efficiency, faster response to environmental changes, and enhanced occupant comfort compared to traditional control approaches—all while respecting operational constraints in real-time conditions.
#include <iostream>
#include <vector>
#include <cmath>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

// System parameters
const double dt = 1.0; // Time step (s)
const double T_ref = 20.0; // Reference temperature (°C)
const double RH_ref = 50.0; // Reference humidity (%)
const double Q_max = 1000.0; // Maximum heating/cooling power (W)
const double Q_min = 0.0; // Minimum heating/cooling power (W)
const double H_max = 500.0; // Maximum humidification rate (L/s)
const double H_min = 0.0; // Minimum humidification rate (L/s)
const double T_max = 30.0; // Maximum outdoor temperature (°C)
const double T_min = 0.0; // Minimum outdoor temperature (°C)
const double RH_max = 100.0; // Maximum outdoor humidity (%)
const double RH_min = 0.0; // Minimum outdoor humidity (%)
const double T_sensitivity = 0.1; // Temperature sensitivity (°C/W)
const double RH_sensitivity = 0.01; // Humidity sensitivity (%)/L/s

// State variables
double T = 20.0; // Current temperature (°C)
double RH = 50.0; // Current humidity (%)
double Q = 0.0; // Current heating/cooling power (W)
double H = 0.0; // Current humidification rate (L/s)
double T_out = 20.0; // Current outdoor temperature (°C)
double RH_out = 50.0; // Current outdoor humidity (%)

// External disturbances
double T_out_prev = 20.0; // Previous outdoor temperature (°C)
double RH_out_prev = 50.0; // Previous outdoor humidity
