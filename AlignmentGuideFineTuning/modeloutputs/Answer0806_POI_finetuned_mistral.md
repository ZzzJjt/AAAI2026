### Intent:
The task is to implement a Model Predictive Control (MPC) algorithm in C++ to optimize an HVAC system's energy efficiency while maintaining temperature and humidity comfort levels under dynamic environmental conditions.

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.

### Generated Code:
The task is to implement a Model Predictive Control (MPC) algorithm in C++ to optimize an HVAC system's energy efficiency while maintaining temperature and humidity comfort levels under dynamic environmental conditions.
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.
#include <iostream>
#include <vector>
#include <cmath>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

// System parameters
const double dt = 1.0; // Time step (hours)
const double T_ref = 20.0; // Reference temperature (°C)
const double RH_ref = 50.0; // Reference humidity (%)
const double Q_max = 1000.0; // Maximum heating/cooling capacity (W)
const double Q_hum_max = 500.0; // Maximum humidification capacity (W)
const double Q_hum_min = 0.0; // Minimum humidification capacity (W)
const double T_min = 10.0; // Minimum temperature (°C)
const double T_max = 30.0; // Maximum temperature (°C)
const double RH_min = 30.0; // Minimum humidity (%)
const double RH_max = 70.0; // Maximum humidity (%)
const double T_outside = 15.0; // Outside temperature (°C)
const double RH_outside = 40.0; // Outside humidity (%)
const double alpha = 0.9; // Prediction horizon
const double beta = 0.1; // Control weight
const double gamma = 0.8; // Constraint weight

// State variables
double T; // Temperature (°C)
double RH; // Humidity (%)
double Q_heat; // Heating/cooling power (W)
double Q_hum; // Humidification power (W)

// Constraints
double T_min_con = T_min;
double T_max_con = T_max;
double RH_min_con = RH_min;
double RH_max_con = RH_max;
double Q_heat_con = Q_max;
double Q_hum_con = Q_hum_min;

// Prediction model
MatrixXd A(4, 4); // State transition
