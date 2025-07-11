### Intent:
**Intent Summary:**  
Develop MATLAB-based Model Predictive Control (MPC) code to dynamically optimize aircraft trajectory while handling constraints (dynamics, fuel efficiency, safety) and disturbances (e.g., wind gusts) for real-time performance.

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**C-A-R-E:**

🟥 C（Context）

Aircraft trajectory optimization must consider multiple factors simultaneously—dynamic constraints, fuel consumption, environmental disturbances, and safety requirements. Traditional control methods often lack the predictive capability to handle such complexity effectively.

🟩 A（Action）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that dynamically optimizes an aircraft’s trajectory. Incorporate system dynamics, fuel efficiency goals, external disturbances, and safety/performance constraints into the MPC formulation.

🟨 R（Result）

The MPC-based control system should enable precise and efficient trajectory tracking, improving overall flight performance while ensuring safe operation under varying environmental and operational conditions.

🟦 E（Example）

For example, simulate a scenario where the aircraft experiences sudden wind gusts. Show how the MPC system adjusts the trajectory in real time, maintaining safety and efficiency, in contrast to a traditional open-loop or rule-based system that might overreact or fail to adapt.

### Generated Code:
**Intent Summary:**  
Develop MATLAB-based Model Predictive Control (MPC) code to dynamically optimize aircraft trajectory while handling constraints (dynamics, fuel efficiency, safety) and disturbances (e.g., wind gusts) for real-time performance.
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**C-A-R-E:**

🟥 C（Context）

Aircraft trajectory optimization must consider multiple factors simultaneously—dynamic constraints, fuel consumption, environmental disturbances, and safety requirements. Traditional control methods often lack the predictive capability to handle such complexity effectively.

🟩 A（Action）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that dynamically optimizes an aircraft’s trajectory. Incorporate system dynamics, fuel efficiency goals, external disturbances, and safety/performance constraints into the MPC formulation.

🟨 R（Result）

The MPC-based control system should enable precise and efficient trajectory tracking, improving overall flight performance while ensuring safe operation under varying environmental and operational conditions.

🟦 E（Example）

For example, simulate a scenario where the aircraft experiences sudden wind gusts. Show how the MPC system adjusts the trajectory in real time, maintaining safety and efficiency, in contrast to a traditional open-loop or rule-based system that might overreact or fail to adapt.
% Aircraft Trajectory Optimization Using MPC
% Simulates wind gust disturbance and optimizes trajectory
% Inputs: x0, v0, h0, t_f, dt, wind_speed, wind_direction
% Outputs: x_opt, v_opt, h_opt, u_opt

function [x_opt, v_opt, h_opt, u_opt] = mpc_aircraft_trajectory(x0, v0, h0, t_f, dt, wind_speed, wind_direction)
    % Parameters
    g = 9.81; % Acceleration due to gravity (m/s^2)
    m = 10000; % Aircraft mass (kg)
    c_d = 0.02; % Drag coefficient
    rho = 1.225; % Air density (kg/m^3)
    A = 100; % Reference wing area (m^2)
    S = 1000; % Reference wing span (m)
    V_ref = 200; % Reference airspeed (m/s)
    kp = 10; % Proportional gain for altitude tracking
    ki = 0.5; % Integral gain for altitude tracking
    kd = 0.1; % Derivative gain for altitude tracking
    dt = 0.1; % MPC prediction horizon (s)
    N = 10; % Prediction horizon length
    % State variables
    x = [x0; v0; h0]; % Position, velocity, altitude (m, m/s, m)
    x_ref = [0; V_ref; 0]; % Reference position, velocity, altitude (m, m/s, m)
    u = [0; 0; 0]; % Control inputs (thrust, pitch angle, rudder)
    % Disturbance model
    wind_speed = wind_speed * cos(wind_direction); % Simulate wind gust
    wind_speed = max(wind_speed, 0);
    wind_speed = min(wind_speed, 20);
    wind_speed = wind_speed
