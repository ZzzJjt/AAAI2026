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

**Implementation:**

```
FUNCTION_BLOCK KalmanFilter
	VAR
		// Internal variables
		EstimatedPosition : REAL;
		EstimatedVelocity : REAL;
		PreviousPosition : REAL;
		ErrorCovariance : ARRAY[0..1] OF REAL;
		KalmanGain : ARRAY[0..1] OF REAL;

		// Inputs
		MeasuredPosition : REAL;
		Q : REAL;
		R : REAL;
		DeltaT : REAL;
		Reset : BOOL;

		// Outputs
		EstimatedPosition_OUT : REAL;
		EstimatedVelocity_OUT : REAL;

		// Constants
		P_0 : ARRAY[0..1] OF REAL := [1.0, 0.0; 0.0, 1.0];
		Q_0 : ARRAY[0..1] OF REAL := [0.0, 0.0; 0.0, Q];
		R_0 : ARRAY[0..1] OF REAL := [R, 0.0; 0.0, R];

		// Prediction
		IF Reset THEN
			EstimatedPosition := 0.0;
			EstimatedVelocity := 0.0;
			PreviousPosition := 0.0;
			ErrorCovariance := P_0;
		ELSE
			// Predict position and velocity
			EstimatedPosition := EstimatedPosition + EstimatedVelocity * DeltaT;
			EstimatedVelocity := EstimatedVelocity + (Q / DeltaT) * (PreviousPosition - EstimatedPosition);

			// Update error covariance
			ErrorCovariance[0, 0] := ErrorCovariance[0, 0] - 2 * (Q / DeltaT) * ErrorCovariance[0, 1] + Q_0[0, 0];
			ErrorCovariance[0, 1] := ErrorCov
