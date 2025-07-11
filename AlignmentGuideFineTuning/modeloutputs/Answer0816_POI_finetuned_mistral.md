### Intent:
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate flight behavior under control inputs (thrust, elevator, rudder) and wind disturbances, calculating forces, accelerations, and angular rates for trajectory tracking.  

*(Focused on code generation for simulating aircraft motion with aerodynamic effects and control inputs.)*

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
**Intent Summary:**  
Develop a 6-DOF aircraft dynamics model in MATLAB to simulate flight behavior under control inputs (thrust, elevator, rudder) and wind disturbances, calculating forces, accelerations, and angular rates for trajectory tracking.  

*(Focused on code generation for simulating aircraft motion with aerodynamic effects and control inputs.)*
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
% Aircraft Dynamics Model in MATLAB
% Simulates 6-DOF motion under control inputs and wind disturbances
% Inputs:
%   - Thrust (thrust)
%   - Elevator angle (elevator)
%   - Rudder angle (rudder)
%   - Wind speed (wind_speed)
%   - Time step (dt)
% Outputs:
%   - Aircraft position (x, y, z)
%   - Velocity (vx, vy, vz)
%   - Acceleration (ax, ay, az)
%   - Angular velocity (omega_x, omega_y, omega_z)
%   - Angular acceleration (alpha_x, alpha_y, alpha_z)
%   - Control inputs (thrust, elevator, rudder)
%   - Wind disturbance (wind_force)
% Simulation Parameters
aircraft_mass = 10000; % kg
wing_area = 50; % m^2
drag_coeff = 0.02; % dimensionless
lift_coeff = 0.05; % dimensionless
thrust_coeff = 0.05; % dimensionless
rho = 1.225; % kg/m^3
g = 9.81; % m/s^2
dt = 0.1; % s
t_sim = 10; % s

% State-space matrices for linearized aircraft dynamics
A = [0 0 0 1 0 0;
     0 0 0 0 1 0;
     0 0 0 0 0 1;
     -g/aircraft_mass 0 0 0;
     0 -g/aircraft_mass 0 0;
     0 0 -g/aircraft_mass 0 0];
B = [0;
     0;
     0;
     thrust_coeff/aircraft_mass;
     thrust_coeff/aircraft_mass;
     0;
     0;
     0;
     0;
     0;
     lift_coeff/aircraft_mass;
