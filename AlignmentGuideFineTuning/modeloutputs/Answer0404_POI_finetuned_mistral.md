### Intent:
**Intent Summary:**  
Develop a MATLAB-based Model Predictive Control (MPC) system to optimize aircraft trajectory while enforcing dynamic constraints, fuel efficiency, and adaptive disturbance rejection for flight safety.  

*(Focus: Trajectory optimization via MPC with MATLAB, prioritizing constraints, efficiency, and robustness.)*

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**R-I-S-E:**

🟥 R（Role）

Act as an aerospace control systems engineer specializing in trajectory optimization and predictive control using MATLAB.

🟩 I（Input）

You are tasked with developing a control system for aircraft trajectory optimization. The system must account for dynamic constraints, fuel efficiency, external disturbances (e.g., wind), and ensure compliance with safety and performance requirements. MATLAB will be used for both modeling and implementation.

🟧 S（Steps）
	1.	Model the aircraft’s dynamics in MATLAB, incorporating variables such as position, velocity, control inputs, and external forces.
	2.	Formulate a model predictive control (MPC) scheme that includes constraints on system behavior and objectives related to fuel efficiency and flight safety.
	3.	Implement the MPC algorithm and simulate various flight scenarios with disturbances.
	4.	Evaluate the system’s ability to maintain optimal trajectory under different operational conditions.

🟦 E（Expectation）

The resulting MATLAB system should demonstrate that the MPC algorithm can optimize aircraft trajectory while respecting constraints and reacting adaptively to disturbances—enhancing fuel efficiency and maintaining flight safety.

### Generated Code:
**Intent Summary:**  
Develop a MATLAB-based Model Predictive Control (MPC) system to optimize aircraft trajectory while enforcing dynamic constraints, fuel efficiency, and adaptive disturbance rejection for flight safety.  

*(Focus: Trajectory optimization via MPC with MATLAB, prioritizing constraints, efficiency, and robustness.)*
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**R-I-S-E:**

🟥 R（Role）

Act as an aerospace control systems engineer specializing in trajectory optimization and predictive control using MATLAB.

🟩 I（Input）

You are tasked with developing a control system for aircraft trajectory optimization. The system must account for dynamic constraints, fuel efficiency, external disturbances (e.g., wind), and ensure compliance with safety and performance requirements. MATLAB will be used for both modeling and implementation.

🟧 S（Steps）
	1.	Model the aircraft’s dynamics in MATLAB, incorporating variables such as position, velocity, control inputs, and external forces.
	2.	Formulate a model predictive control (MPC) scheme that includes constraints on system behavior and objectives related to fuel efficiency and flight safety.
	3.	Implement the MPC algorithm and simulate various flight scenarios with disturbances.
	4.	Evaluate the system’s ability to maintain optimal trajectory under different operational conditions.

🟦 E（Expectation）

The resulting MATLAB system should demonstrate that the MPC algorithm can optimize aircraft trajectory while respecting constraints and reacting adaptively to disturbances—enhancing fuel efficiency and maintaining flight safety.
% Aircraft Trajectory Optimization Using MPC
% Simulates aircraft dynamics with MATLAB
% Optimizes trajectory using MPC with fuel efficiency and safety constraints
% Uses MATLAB's ODE solver for aircraft dynamics

% Aircraft State-Space Model
% x = [x; y; vx; vy]
% u = [thrust; pitch_angle]
% dt = 1 (s)

% Constants
g = 9.81; % Acceleration due to gravity (m/s^2)
rho = 1.225; % Air density (kg/m^3)
C_D = 0.02; % Drag coefficient
A = 10.0; % Wing area (m^2)

% Parameters
x0 = [0; 0; 100; 0]; % Initial state: [x; y; vx; vy]
u0 = [1000; 0]; % Initial control: [thrust; pitch_angle]
dt = 1; % Time step (s)
t_final = 10; % Simulation time (s)

% ODE solver
ode_sol = ode45(@(t,x,u) air_dynamics(t,x,u), [0, t_final], x0, u0);
x = ode_sol.y;

% MPC Parameters
N = 10; % Prediction horizon
dt_mpc = 0.1; % MPC sample time (s)

% MPC State and Control Inputs
x_mpc = zeros(N, 4);
u_mpc = zeros(N, 2);

% MPC Initial State
x_mpc(1, :) = x0;

% MPC Control Inputs
u_mpc(1, 1) = u0(1);
u_mpc(1, 2) = u0(2);

% MPC Objective Function
J = zeros(N, 1);
J(1, :) = [0; 0; 0; 0]; % Initial cost

% MPC Constraints
for k =
