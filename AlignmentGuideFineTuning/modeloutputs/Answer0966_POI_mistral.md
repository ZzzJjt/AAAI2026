### Intent:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy sensor data, with configurable noise parameters and scan-cycle-safe execution.  

*(Focus: Discrete 2-state filter, scalar arithmetic, modularity for motion control integration.)*

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**T-A-G:**

🟥 T (Task)

Design a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy sensor input.

⸻

🟩 A (Action)
	•	Implement a discrete-time, 2-state Kalman filter using only scalar arithmetic, avoiding matrix operations or recursion
	•	Accept configurable inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL – process noise covariance
	•	R : REAL – measurement noise covariance
	•	DeltaT : REAL – sample time
	•	Reset : BOOL – to reinitialize state
	•	Internally manage variables for:
	•	Estimated position and velocity
	•	Previous position (for velocity update)
	•	Error covariance and Kalman gain
	•	Perform prediction and update steps each scan cycle
	•	Add clear comments for each stage of the algorithm to support maintainability and clarity

⸻

🟦 G (Goal)

Deliver a modular, scan-cycle-safe function block that produces reliable estimates of position and velocity despite measurement noise. The block should be easy to configure, integrate into motion control logic, and adaptable for various autonomous or mobile platform applications.

### Generated Code:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy sensor data, with configurable noise parameters and scan-cycle-safe execution.  

*(Focus: Discrete 2-state filter, scalar arithmetic, modularity for motion control integration.)*
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**T-A-G:**

🟥 T (Task)

Design a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy sensor input.

⸻

🟩 A (Action)
	•	Implement a discrete-time, 2-state Kalman filter using only scalar arithmetic, avoiding matrix operations or recursion
	•	Accept configurable inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL – process noise covariance
	•	R : REAL – measurement noise covariance
	•	DeltaT : REAL – sample time
	•	Reset : BOOL – to reinitialize state
	•	Internally manage variables for:
	•	Estimated position and velocity
	•	Previous position (for velocity update)
	•	Error covariance and Kalman gain
	•	Perform prediction and update steps each scan cycle
	•	Add clear comments for each stage of the algorithm to support maintainability and clarity

⸻

🟦 G (Goal)

Deliver a modular, scan-cycle-safe function block that produces reliable estimates of position and velocity despite measurement noise. The block should be easy to configure, integrate into motion control logic, and adaptable for various autonomous or mobile platform applications.

**Notes:**

1.	The function block should be designed to be called at each scan cycle, with the input parameters updated accordingly.
2.	The filter should be initialized with sensible default values for Q, R, and initial state if the Reset input is true.
3.	The filter should be able to handle the case where the Reset input is false, continuing to update the state estimates based on the previous measurements.
4.	The filter should be designed to minimize the computational overhead, making it suitable for real-time control applications.
5.	The filter should be designed to be easily integrated into a larger motion control system, with clear input and output variables and minimal dependencies on external resources.
6.	The filter should be thoroughly tested to ensure its accuracy and robustness under various noise conditions and initial conditions.
7.	The filter should be designed to be easily configurable, allowing users to adjust the noise parameters and initial conditions as needed for their specific application.
8.	The filter should be designed to be easily maintainable, with clear comments and modular structure to support future modifications or improvements.
9.	The filter should be designed to be easily adaptable for various autonomous or mobile platform applications, with minimal modifications required to accommodate different sensor types or platform dynamics.
10.	The filter should be designed to be easily scalable, allowing for extension to multi-dimensional state spaces or more complex dynamics if needed in the future.
11.	The filter should be designed to be easily verified, with clear documentation and test cases to support validation and verification efforts.
12.	The filter should be designed to be easily validated, with clear performance metrics and comparison to ground truth data where possible to demonstrate its effectiveness.
13.	The filter should be designed to be easily integrated with other motion control components, such as PID controllers or path planning algorithms, to create a complete autonomous control system.
14.	The filter should be designed to be easily calibrated, with clear instructions and guidance on how to adjust the noise parameters and initial conditions based on experimental data or user feedback.
15.	The filter should be designed to be easily debugged, with clear error handling and diagnostic capabilities to support troubleshooting and problem resolution.
16.	The filter should be designed to be easily documented, with clear and concise documentation that explains its purpose, functionality, and usage
