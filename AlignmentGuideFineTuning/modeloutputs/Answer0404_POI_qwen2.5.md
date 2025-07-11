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

The resulting MATLAB system should demonstrate that the MPC algorithm can optimize aircraft trajectory while respecting constraints and reacting adaptively to disturbances—enhancing fuel efficiency and maintaining flight safety. The code should be well-documented and include simulation results to validate the system’s performance.

**MATLAB Code Example:**

```matlab
% Aircraft Dynamics Model
function [x_dot, u] = aircraft_dynamics(x, u, wind)
    % x: state vector [x, y, z, vx, vy, vz]
    % u: control input vector [thrust, angle_of_attack]
    % wind: external disturbance vector [wx, wy, wz]
    
    % Define aircraft parameters
    m = 1000; % mass
    Ixx = 100; % moment of inertia
    Iyy = 100; % moment of inertia
    Izz = 100; % moment of inertia
    Cd = 0.01; % drag coefficient
    Cl = 0.01; % lift coefficient
    g = 9.81; % gravity
    
    % Calculate forces and moments
    Fx = m * u(1) * cos(x(4)) - m * g * sin(x(4)) + wind(1);
    Fy = m * u(1) * sin(x(4)) + wind(2);
    Fz = m * u(1) * cos(x(4)) + m * g * cos(x(4)) + wind(3);
    Mx = Ixx * u(2) + m * x(5) * Fy;
    My = Iyy * u(2) + m * x(6) * Fx;
    Mz = Izz * u(2) + m * x(5) * Fx + m * x(6) * Fy;
    
    % State derivatives
    x_dot = [x(4); x(5); x(6); Fx / m; Fy / m; Fz / m];
    
    % Control input
    u = [Fx / m; Mz / Izz];
end

% MPC Algorithm
function [u_opt] = mpc_algorithm(x, x_ref, Q, R, N, wind)
    % x: current state
    % x_ref: reference trajectory
    % Q: state cost matrix
    % R: control input cost matrix
    % N: prediction horizon
    % wind: external disturbance
    
    % Initialize MPC variables
    x_pred = x;
    u_pred = zeros
