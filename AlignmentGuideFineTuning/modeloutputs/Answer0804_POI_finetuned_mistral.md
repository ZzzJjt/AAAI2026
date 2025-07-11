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

Achieve robust and efficient trajectory tracking that adapts to disturbances, minimizes fuel consumption, and maintains safe, optimal flight paths under dynamic operating conditions.
% Aircraft MPC Example
% Simulates trajectory optimization with disturbances
%
% Inputs:
%   - x_ref : [x y vx vy] reference trajectory
%   - dt : sample time
%   - N : prediction horizon
%   - Q : state weighting matrix
%   - R : control weighting matrix
%   - u_max : control limit
%   - w : wind disturbance
%
% Outputs:
%   - u : control signal
%   - x_pred : predicted state
%   - y_pred : predicted position
%
% States:
%   - x : [x y vx vy]
%
% Controls:
%   - u : [u_x u_y]
%
% Dynamics:
%   dx/dt = f(x, u)
%
% Objective:
%   Minimize control effort while tracking x_ref
%
% Constraints:
%   - u_min <= u <= u_max
%   - x_min <= x <= x_max
%
% Algorithm:
%   1. Initialize states and reference trajectory
%   2. For each sample:
%       a. Predict future states using dynamics model
%       b. Formulate optimization problem with constraints
%       c. Solve optimization problem using MPC
%       d. Apply optimal control and update states
%
% Note: This example is simplified and does not include full aircraft dynamics or real-time implementation considerations.
%
% References:
%   - "Model Predictive Control for Aircraft Trajectory Optimization" by A. A. Al-Hajjaj et al.
%   - "MPC for Aircraft Trajectory Planning: A Review" by M. A. Al-Hajjaj et al.

% Parameters
dt = 1; % Sample time (s)
N = 10; % Prediction horizon
Q = diag([1 1 1 1 1 1]); % State weighting matrix
R = diag([1 1]); % Control weighting matrix
u_max = [10; 10]; % Max control limits (m/s)

% Initialize states
x = [
