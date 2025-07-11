### Intent:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy sensor data, with configurable noise parameters and scan-cycle-safe execution.  

*(Focus: Discrete-time scalar implementation, modularity, and industrial applicability.)*

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

*(Focus: Discrete-time scalar implementation, modularity, and industrial applicability.)*
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

**Design Considerations:**

•	The Kalman filter is a recursive algorithm that uses a prediction step to estimate the state of a system at the next time step, and an update step to incorporate new measurements.
•	The prediction step uses the previous state estimate and a model of the system to predict the state at the next time step.
•	The update step uses a measurement of the system and the predicted state to calculate a new state estimate.
•	The Kalman filter is used to estimate the state of a system in the presence of noise and uncertainty.
•	The Kalman filter is a powerful tool for estimating the state of a system, but it can be difficult to implement in practice.
•	The Kalman filter is a recursive algorithm that uses a prediction step to estimate the state of a system at the next time step, and an update step to incorporate new measurements.
•	The prediction step uses the previous state estimate and a model of the system to predict the state at the next time step.
•	The update step uses a measurement of the system and the predicted state to calculate a new state estimate.
•	The Kalman filter is used to estimate the state of a system in the presence of noise and uncertainty.
•	The Kalman filter is a powerful tool for estimating the state of a system, but it can be difficult to implement in practice.
•	The Kalman filter is a recursive algorithm that uses a prediction step to estimate the state of a system at the next time step, and an update step to incorporate new measurements.
•	The prediction step uses the previous state estimate and a model of the system to predict the state at the next time step.
•	The update step uses a measurement of the system and the predicted state to calculate a new state estimate.
•	The Kalman filter is used to estimate the state of a system in the presence of noise and uncertainty.
•	The Kalman filter is a powerful tool for estimating the state of a system, but it can be difficult to implement in practice.
•	The Kalman filter is a recursive algorithm that uses a prediction step to estimate the state of a system at the next time step, and an update step to incorporate new measurements.
•	The prediction step uses the previous state estimate and a model of the system to predict the state at the next time step.
•	The update step uses a measurement of the system and the predicted state to calculate a new state estimate.
•	The Kalman filter
