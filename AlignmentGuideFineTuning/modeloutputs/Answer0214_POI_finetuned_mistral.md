### Intent:
**Intent Summary:**  
Develop MATLAB-based model predictive control (MPC) for aircraft trajectory optimization, incorporating dynamic constraints, fuel efficiency, and disturbance rejection to ensure safe and efficient flight performance.  

*(Focus: MPC implementation for aircraft dynamics with real-time adaptation to disturbances and operational constraints.)*

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
Develop MATLAB-based model predictive control (MPC) for aircraft trajectory optimization, incorporating dynamic constraints, fuel efficiency, and disturbance rejection to ensure safe and efficient flight performance.  

*(Focus: MPC implementation for aircraft dynamics with real-time adaptation to disturbances and operational constraints.)*
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
% Simulates wind disturbance and optimizes trajectory
% Inputs: x0, u0, dt, N, wind_disturbance
% Outputs: x, u, MPC_cost, MPC_time

function [x, u, MPC_cost, MPC_time] = mpc_aircraft(x0, u0, dt, N, wind_disturbance)
    % Parameters
    tspan = [0 10]; % Simulation time (s)
    N = N; % Prediction horizon
    dt = dt; % Time step (s)
    x0 = x0; % Initial state
    u0 = u0; % Initial control
    wind_disturbance = wind_disturbance; % Wind disturbance (m/s)

    % Model
    sys = airplane_model();
    sys.InputName = 'u';
    sys.OutputName = 'x';

    % MPC
    mpc = mpc_designer(sys, N, dt);
    mpc.Objective = @(x, u) sum(u.^2); % Minimize control effort
    mpc.Constraints = @(x, u) u <= 10; % Max control limit

    % Simulate wind disturbance
    x = x0;
    u = u0;
    MPC_cost = [];
    MPC_time = [];
    for t = 0:dt:10
        % Predict wind disturbance
        wind_disturbance_pred = wind_disturbance(t);

        % Compute MPC solution
        [x_pred, u_pred, MPC_cost_pred] = mpc(x, u, wind_disturbance_pred);

        % Update state and control
        x = x_pred(end, :);
        u = u_pred(end, :);
        MPC_cost = [MPC_cost, MPC_cost_pred];
        MPC_time = [MPC_time, t];
    end
end

% Aircraft model
function sys = airplane_model()
    sys = ss(
