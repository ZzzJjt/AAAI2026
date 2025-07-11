### Intent:
Implement a model predictive control (MPC) system in MATLAB to optimize an aircraft's flight trajectory while ensuring fuel efficiency, safety, and robustness against disturbances.

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in MATLAB to optimize the flight trajectory of an aircraft.

🟩 A（Action）

Develop a mathematical model of the aircraft’s dynamics and use it within an MPC framework. Incorporate constraints related to control inputs and aircraft performance, account for external disturbances such as wind, and include objectives for fuel efficiency and flight safety. Simulate realistic flight scenarios to test and validate the controller’s performance.

🟦 G（Goal）

Achieve robust and efficient trajectory tracking that adapts to disturbances, minimizes fuel consumption, and maintains safe, optimal flight paths under dynamic operating conditions.

### Generated Code:
Implement a model predictive control (MPC) system in MATLAB to optimize an aircraft's flight trajectory while ensuring fuel efficiency, safety, and robustness against disturbances.
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**T-A-G:**

🟥 T（Task）

Implement a model predictive control (MPC) system in MATLAB to optimize the flight trajectory of an aircraft.

🟩 A（Action）

Develop a mathematical model of the aircraft’s dynamics and use it within an MPC framework. Incorporate constraints related to control inputs and aircraft performance, account for external disturbances such as wind, and include objectives for fuel efficiency and flight safety. Simulate realistic flight scenarios to test and validate the controller’s performance.

🟦 G（Goal）

Achieve robust and efficient trajectory tracking that adapts to disturbances, minimizes fuel consumption, and maintains safe, optimal flight paths under dynamic operating conditions. Demonstrate the effectiveness of the MPC controller through simulations and analysis.

**MATLAB Code:**

```matlab
% Define aircraft dynamics model
function [x_dot, u] = aircraft_dynamics(x, u, wind)
    % x: state vector [position, velocity, angle of attack, etc.]
    % u: control input vector [thrust, angle of attack, etc.]
    % wind: external disturbance vector [wind speed, direction, etc.]

    % Define aircraft parameters
    m = 1000; % mass (kg)
    Ixx = 100; % moment of inertia about x-axis (kg*m^2)
    Iyy = 100; % moment of inertia about y-axis (kg*m^2)
    Izz = 100; % moment of inertia about z-axis (kg*m^2)
    C_D = 0.02; % drag coefficient
    C_L = 0.5; % lift coefficient
    g = 9.81; % gravitational acceleration (m/s^2)

    % Calculate forces and torques
    F_drag = 0.5 * C_D * rho * A * v^2;
    F_lift = 0.5 * C_L * rho * A * v^2;
    T = m * g + F_drag - F_lift;

    % Calculate state derivatives
    x_dot = [x(2); % position derivative
             u(1) - F_drag / m; % velocity derivative
             u(2); % angle of attack derivative
             u(3) - g; % acceleration derivative];

    % Calculate control input
    u = [T / m; % thrust
         0; % angle of attack
         0]; % roll rate

    % Add external disturbance
    x_dot = x_dot + wind;
end

% Define MPC controller
function [u_opt] = mpc_controller(x, x_ref, Q, R, N, T)
    % x: current state vector
    % x_ref: reference trajectory vector
    % Q: state weighting matrix
    % R: control input weighting matrix
    % N: prediction horizon
    % T: control horizon

    % Initialize MPC variables
    x_pred = x; % predicted state vector
    u_pred = zeros(N, 1); % predicted control input vector

    % Predict state and control inputs
