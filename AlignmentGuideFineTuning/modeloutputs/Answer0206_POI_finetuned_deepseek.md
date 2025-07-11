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
#include <cstdlib>
#include <ctime>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

// Define the state vector
typedef VectorXd State;
typedef VectorXd Input;
typedef VectorXd Output;

// Define the system dynamics
class HVACSystem {
public:
    HVACSystem(double dt, double T_max, double T_min, double H_max, double H_min, double E_max, double E_min)
        : dt(dt), T_max(T_max), T_min(T_min), H_max(H_max), H_min(H_min), E_max(E_max), E_min(E_min) {}

    // Compute the next state given the current state and input
    State predict(const State &x, const Input &u) {
        State x_next = x;
        x_next(0) = x(0) + dt * u(0);
        x_next(1) = x(1) + dt * u(1);
        x_next(2) = x(2) + dt * u(2);
        return x_next;
    }

    // Compute the cost function
    double cost(const State &x, const Input &u) {
        double cost = 0.0;
        cost += (x(0) - T_max) * (x(0) - T_max);
        cost += (x(1) - H_max) * (x(1) - H_max);
        cost += (x(2) - E_max) * (x(2) - E_max);
        return cost;
    }

    // Compute the derivative of the cost function
    MatrixXd cost_derivative(const State &x, const Input &u) {
        MatrixXd dcost_dx = MatrixXd::Zero(3, 3);
        dcost_dx(0, 0) = 2 * (x(0) - T_max);
        dcost_dx(0, 1) = 0;
