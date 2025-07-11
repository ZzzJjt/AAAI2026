### Intent:
**Intent Summary:**  
Develop a C++ implementation of a Model Predictive Control (MPC) algorithm to optimize HVAC system performance by dynamically balancing temperature, humidity, and energy efficiency under varying environmental conditions, outperforming traditional PID control.  

*(Focus: MPC-based HVAC optimization with constraints, dynamic forecasting, and energy-comfort trade-offs.)*

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**C-A-R-E:**

🟥 C（Context）

Heating, Ventilation, and Air Conditioning (HVAC) systems are essential for maintaining occupant comfort in buildings, but traditional control methods often fail to optimize energy consumption while maintaining comfort. These methods do not account for dynamic environmental changes, such as fluctuating external temperatures or varying occupancy levels, leading to inefficient energy use and delayed system responses.

🟩 A（Action）

Develop C++ code to implement a model predictive control (MPC) algorithm that optimizes HVAC performance. The algorithm should manage temperature, humidity, and energy consumption by forecasting future conditions and adjusting control inputs accordingly, while considering dynamic constraints like external temperature, occupancy, and energy efficiency requirements.

🟨 R（Result）

The MPC-based HVAC control system should significantly reduce energy consumption while maintaining comfort levels. It should demonstrate the ability to respond quickly to environmental changes, minimize delays in achieving desired temperature and humidity levels, and ensure optimal energy efficiency under varying operational conditions.

🟦 E（Example）

For example, if the system detects an increase in occupancy and an external temperature rise, the MPC controller would proactively adjust HVAC settings to maintain comfort while minimizing energy usage, compared to a traditional control method that would react only after these changes are detected.

### Generated Code:
**Intent Summary:**  
Develop a C++ implementation of a Model Predictive Control (MPC) algorithm to optimize HVAC system performance by dynamically balancing temperature, humidity, and energy efficiency under varying environmental conditions, outperforming traditional PID control.  

*(Focus: MPC-based HVAC optimization with constraints, dynamic forecasting, and energy-comfort trade-offs.)*
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**C-A-R-E:**

🟥 C（Context）

Heating, Ventilation, and Air Conditioning (HVAC) systems are essential for maintaining occupant comfort in buildings, but traditional control methods often fail to optimize energy consumption while maintaining comfort. These methods do not account for dynamic environmental changes, such as fluctuating external temperatures or varying occupancy levels, leading to inefficient energy use and delayed system responses.

🟩 A（Action）

Develop C++ code to implement a model predictive control (MPC) algorithm that optimizes HVAC performance. The algorithm should manage temperature, humidity, and energy consumption by forecasting future conditions and adjusting control inputs accordingly, while considering dynamic constraints like external temperature, occupancy, and energy efficiency requirements.

🟨 R（Result）

The MPC-based HVAC control system should significantly reduce energy consumption while maintaining comfort levels. It should demonstrate the ability to respond quickly to environmental changes, minimize delays in achieving desired temperature and humidity levels, and ensure optimal energy efficiency under varying operational conditions.

🟦 E（Example）

For example, if the system detects an increase in occupancy and an external temperature rise, the MPC controller would proactively adjust HVAC settings to maintain comfort while minimizing energy usage, compared to a traditional control method that would react only after these changes are detected.
#include <iostream>
#include <vector>
#include <cmath>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

// System parameters
const double dt = 1.0; // Time step (minutes)
const double T_ref = 20.0; // Reference temperature (°C)
const double RH_ref = 50.0; // Reference humidity (%)
const double Q_max = 1000.0; // Maximum heating/cooling power (W)
const double Q_min = 0.0; // Minimum heating/cooling power (W)
const double H_max = 1000.0; // Maximum humidification rate (L/min)
const double H_min = 0.0; // Minimum humidification rate (L/min)
const double T_max = 30.0; // Maximum outdoor temperature (°C)
const double T_min = 0.0; // Minimum outdoor temperature (°C)
const double RH_max = 100.0; // Maximum outdoor humidity (%)
const double RH_min = 0.0; // Minimum outdoor humidity (%)
const double T_sensitivity = 0.1; // Temperature sensitivity (°C/W)
const double RH_sensitivity = 0.01; // Humidity sensitivity (%)/L/min

// State variables
double T = 20.0; // Current temperature (°C)
double RH = 50.0; // Current humidity (%)
double Q = 0.0; // Current heating/cooling power (W)
double H = 0.0; // Current humidification rate (L/min)
double T_out = 20.0; // Current outdoor temperature (°C)
double RH_out = 50.0; // Current outdoor humidity (%)
double T_forecast = 0.0; // Predicted temperature (°C)
double RH_forecast = 0.0; // Predicted humidity (%)

// Prediction model
VectorX
