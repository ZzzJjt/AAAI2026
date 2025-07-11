### Intent:
The task involves implementing a fuzzy logic controller for a chemical reactor's temperature and pressure regulation, comparing its performance against a PID controller through dynamic simulation.

### Prompt:
**MATLAB Distillation Column Modeling and Control:**

Develop MATLAB code for a mathematical model of a distillation column, capturing its dynamic relationships between feed rates and temperature. Avoid plotting results.
Implement a model predictive control (MPC) scheme using the developed model to optimize the distillation process while considering operational constraints.

**T-A-G:**

🟥 T（Task）

Create a MATLAB-based dynamic model of a distillation column and apply model predictive control (MPC) to optimize its operation.

🟩 A（Action）

Develop a mathematical representation that captures the relationship between feed rates and temperature without plotting the results. Then, implement an MPC algorithm using the model to compute optimal control actions while respecting system constraints.

🟦 G（Goal）

Ensure the distillation column operates efficiently and within defined operational limits by using predictive control to maintain stability and optimize performance, all in a code-only, non-graphical simulation environment.

### Generated Code:
The task involves implementing a fuzzy logic controller for a chemical reactor's temperature and pressure regulation, comparing its performance against a PID controller through dynamic simulation.
**MATLAB Distillation Column Modeling and Control:**

Develop MATLAB code for a mathematical model of a distillation column, capturing its dynamic relationships between feed rates and temperature. Avoid plotting results.
Implement a model predictive control (MPC) scheme using the developed model to optimize the distillation process while considering operational constraints.

**T-A-G:**

🟥 T（Task）

Create a MATLAB-based dynamic model of a distillation column and apply model predictive control (MPC) to optimize its operation.

🟩 A（Action）

Develop a mathematical representation that captures the relationship between feed rates and temperature without plotting the results. Then, implement an MPC algorithm using the model to compute optimal control actions while respecting system constraints.

🟦 G（Goal）

Ensure the distillation column operates efficiently and within defined operational limits by using predictive control to maintain stability and optimize performance, all in a code-only, non-graphical simulation environment.
% Fuzzy Logic Controller for Chemical Reactor
% Implements temperature and pressure control using fuzzy logic
% Simulates reactor dynamics with disturbances

% Constants
reactor_volume = 1000; % Reactor volume (L)
reactor_heat_capacity = 1000000; % Heat capacity (J/K)
reactor_conductivity = 0.1; % Thermal conductivity (W/m·K)
reactor_surface_area = 10; % Surface area (m²)
reactor_initial_temp = 300; % Initial temperature (K)
reactor_initial_pressure = 100000; % Initial pressure (Pa)
reactor_cooling_coefficient = 0.01; % Cooling coefficient (W/K)
reactor_heating_coefficient = 0.1; % Heating coefficient (W/K)
reactor_heat_loss_coefficient = 0.05; % Heat loss coefficient (W/K)
reactor_heat_loss_rate = 500; % Heat loss rate (W)
reactor_max_temp = 350; % Maximum temperature (K)
reactor_min_temp = 250; % Minimum temperature (K)
reactor_max_pressure = 120000; % Maximum pressure (Pa)
reactor_min_pressure = 80000; % Minimum pressure (Pa)
reactor_max_flow = 1000; % Maximum flow rate (L/min)
reactor_min_flow = 500; % Minimum flow rate (L/min)
reactor_max_cooling = 5000; % Maximum cooling rate (W)
reactor_min_cooling = 0; % Minimum cooling rate (W)
reactor_max_heating = 10000; % Maximum heating rate (W)
reactor_min_heating = 0; % Minimum heating rate (W)
reactor_max_pressure_setpoint =
