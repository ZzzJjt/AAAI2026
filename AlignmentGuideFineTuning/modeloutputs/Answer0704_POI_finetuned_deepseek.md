### Intent:
**Intent Summary:**  
Develop a MATLAB-based model predictive control (MPC) system for aircraft trajectory optimization that enforces dynamic constraints, maximizes fuel efficiency, mitigates disturbances (e.g., wind), and ensures safety/performance compliance.  

*(Focus: MPC implementation for aerospace trajectory control with MATLAB, addressing constraints, efficiency, and robustness.)*

### Prompt:
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**R-T-F:**

🟥 R（Role）

Act as a MATLAB developer focused on aerospace guidance and control systems.

🟩 T（Task）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that optimizes the trajectory of an aircraft. The control system must consider dynamic constraints, enhance fuel efficiency, compensate for external disturbances (e.g., wind), and ensure safety and performance compliance.

🟧 F（Format）

Provide a complete MATLAB script including:
	•	Aircraft dynamic model definition
	•	MPC controller formulation with constraints and objectives
	•	Simulation of trajectory scenarios under disturbance conditions
	•	Output as numerical values or logs (optional: comments explaining each section)

### Generated Code:
**Intent Summary:**  
Develop a MATLAB-based model predictive control (MPC) system for aircraft trajectory optimization that enforces dynamic constraints, maximizes fuel efficiency, mitigates disturbances (e.g., wind), and ensures safety/performance compliance.  

*(Focus: MPC implementation for aerospace trajectory control with MATLAB, addressing constraints, efficiency, and robustness.)*
**Model Predictive Control for Aircraft Trajectory Using MATLAB:**

Develop MATLAB code to implement a model predictive control (MPC) algorithm for optimizing the trajectory of an aircraft. Ensure that the control scheme accounts for dynamic constraints, fuel efficiency, and external disturbances, while maintaining flight safety and performance objectives.

**R-T-F:**

🟥 R（Role）

Act as a MATLAB developer focused on aerospace guidance and control systems.

🟩 T（Task）

Develop MATLAB code to implement a model predictive control (MPC) algorithm that optimizes the trajectory of an aircraft. The control system must consider dynamic constraints, enhance fuel efficiency, compensate for external disturbances (e.g., wind), and ensure safety and performance compliance.

🟧 F（Format）

Provide a complete MATLAB script including:
	•	Aircraft dynamic model definition
	•	MPC controller formulation with constraints and objectives
	•	Simulation of trajectory scenarios under disturbance conditions
	•	Output as numerical values or logs (optional: comments explaining each section)
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

// Constants
const double PI = 3.14159265358979323846;
const double G = 9.81;
const double TOL = 1e-6;
const double MAX_SPEED = 290.0;
const double MAX_ACCEL = 10.0;
const double MAX_ALT = 10000.0;
const double MIN_ALT = 0.0;
const double MAX_THRUST = 10000.0;
const double MIN_THRUST = 0.0;
const double MAX_V_SPEED = 290.0;
const double MIN_V_SPEED = 0.0;
const double MAX_V_ACCEL = 10.0;
const double MIN_V_ACCEL = 0.0;
const double MAX_V_ALT = 10000.0;
const double MIN_V_ALT = 0.0;
const double MAX_V_THRUST = 10000.0;
const double MIN_V_THRUST = 0.0;
const double MAX_V_V_SPEED = 290.0;
const double MIN_V_V_SPEED = 0.0;
const double MAX_V_V_ACCEL = 10.0;
const double MIN_V_V_ACCEL = 0.0;
const double MAX_V_V_ALT = 10000.0;
const double MIN_V_V_ALT = 0.0;
const double MAX_V_V_THRUST = 10000.0;
const double MIN_V_V_THRUST = 0.0;
const double MAX_V_V_V_SPEED = 290.0;
const double MIN_V_V
