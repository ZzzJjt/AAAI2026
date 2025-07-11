### Intent:
**Intent Summary:**  
Develop a C++ MPC algorithm to optimize HVAC system performance by balancing temperature, humidity, and energy efficiency under dynamic constraints like weather and occupancy, with simulation outputs demonstrating control effectiveness.  

*(For turbine example: "Implement a Python MPC controller for a turbine system to regulate temperature and power output under varying load and ambient conditions, with simulation and performance metrics.")*

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-T-F:**

🟥 R（Role）

Act as a C++ engineer specializing in control systems for smart energy management in HVAC applications.

🟩 T（Task）

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the operation of an HVAC system. The control strategy should manage temperature, humidity, and energy consumption, while considering external weather fluctuations, occupancy levels, and energy constraints. Additionally, simulate the system dynamics and demonstrate the performance of the MPC under varying conditions.

🟧 F（Format）

Provide a structured C++ program that includes:
	•	HVAC system dynamics modeling
	•	MPC algorithm implementation with constraints
	•	Simulation scenarios for variable demand and environmental conditions
	•	Console output or log results showing performance improvements in energy usage, response time, and comfort maintenance

### Generated Code:
**Intent Summary:**  
Develop a C++ MPC algorithm to optimize HVAC system performance by balancing temperature, humidity, and energy efficiency under dynamic constraints like weather and occupancy, with simulation outputs demonstrating control effectiveness.  

*(For turbine example: "Implement a Python MPC controller for a turbine system to regulate temperature and power output under varying load and ambient conditions, with simulation and performance metrics.")*
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**R-T-F:**

🟥 R（Role）

Act as a C++ engineer specializing in control systems for smart energy management in HVAC applications.

🟩 T（Task）

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the operation of an HVAC system. The control strategy should manage temperature, humidity, and energy consumption, while considering external weather fluctuations, occupancy levels, and energy constraints. Additionally, simulate the system dynamics and demonstrate the performance of the MPC under varying conditions.

🟧 F（Format）

Provide a structured C++ program that includes:
	•	HVAC system dynamics modeling
	•	MPC algorithm implementation with constraints
	•	Simulation scenarios for variable demand and environmental conditions
	•	Console output or log results showing performance improvements in energy usage, response time, and comfort maintenance
(* C++ Program: Model Predictive Control for HVAC System *)
(* Optimizes temperature, humidity, and energy efficiency under dynamic constraints *)
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>

using namespace std;

// HVAC System Parameters
const double T_setpoint = 22.0; // Desired temperature in Celsius
const double RH_setpoint = 50.0; // Desired humidity in %
const double T_ambient = 15.0; // External temperature in Celsius
const double T_max = 25.0; // Maximum heating temperature
const double T_min = 18.0; // Minimum heating temperature
const double RH_max = 60.0; // Maximum humidity
const double RH_min = 40.0; // Minimum humidity
const double T_step = 0.5; // Time step in hours
const double T_horizon = 6.0; // Prediction horizon in hours
const double dt = 0.1; // Time step for simulation in hours
const int N = 100; // Number of simulation steps

// HVAC System Dynamics Model
class HVACSystem {
public:
    double T; // Current temperature
    double RH; // Current humidity
    double Q; // Heating/cooling demand
    double H; // Humidification demand
    double E; // Energy consumption

    HVACSystem() : T(T_setpoint), RH(RH_setpoint), Q(0.0), H(0.0), E(0.0) {}

    // Update temperature and humidity
    void update(double T_ambient, double Q, double H) {
        T = T + Q * dt;
        RH = RH + H * dt;

        // Constraints
        if (T > T_max) T = T_max;
        if (T < T_min) T = T_min;
        if (RH > RH_max) RH = RH_max;
        if (R
