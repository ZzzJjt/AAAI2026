### Intent:
**Intent Summary:**  
Develop a C++-based Model Predictive Control (MPC) system to optimize HVAC performance by dynamically adjusting temperature, humidity, and energy use while responding to environmental changes (e.g., occupancy, outdoor conditions) to balance comfort and efficiency.  

*(Focus: MPC algorithm for HVAC control, dynamic constraints, energy optimization, C++ implementation.)*

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
Develop a C++-based Model Predictive Control (MPC) system to optimize HVAC performance by dynamically adjusting temperature, humidity, and energy use while responding to environmental changes (e.g., occupancy, outdoor conditions) to balance comfort and efficiency.  

*(Focus: MPC algorithm for HVAC control, dynamic constraints, energy optimization, C++ implementation.)*
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
const double T_outside = 15.0; // Current outdoor temperature (°C)
const double RH_outside = 40.0; // Current outdoor humidity (%)
const double T_inside = 22.0; // Current indoor temperature (°C)
const double RH_inside = 45.0; // Current indoor humidity (%)
const double T_setpoint = 20.0; // Desired indoor temperature (°C)
const double RH_setpoint = 45.0; // Desired indoor humidity (%)
const double T_step = 0.5; // Step size for temperature control (°C)
const double RH_step = 0.05; // Step size for humidity control (%)
const double T_horizon = 60.0; // Prediction horizon (s)
const double RH_horizon = 60.0; // Prediction horizon (s
