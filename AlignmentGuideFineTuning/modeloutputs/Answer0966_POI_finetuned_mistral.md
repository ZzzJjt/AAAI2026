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
(* IEC 61131-3 Structured Text Function Block for a Kalman Filter *)
(* Estimates position and velocity using noisy sensor data *)
(* Uses discrete-time, 2-state implementation with scalar arithmetic *)
(* Scan-cycle safe, modular, and configurable for PLC use *)

FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL;                  (* Current position measurement, m *)
    Q : REAL;                                (* Process noise covariance, e.g., 0.1 *)
    R : REAL;                                (* Measurement noise covariance, e.g., 1.0 *)
    DeltaT : REAL;                           (* Sample time, e.g., 0.1s *)
    Reset : BOOL;                            (* TRUE to reinitialize state *)
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL;                (* Estimated position, m *)
    EstimatedVelocity : REAL;                (* Estimated velocity, m/s *)
    ErrorCovariance : REAL;                  (* Estimated error covariance *)
    KalmanGain : REAL;                       (* Kalman gain *)
END_VAR

VAR
    PrevPosition : REAL;                     (* Previous position for velocity *)
    State : ARRAY[1..2] OF REAL;            (* State: [1] = position, [2] = velocity *)
    StateCovariance : ARRAY[1..2] OF REAL;   (* Covariance: [1,1] = position, [2,2] = velocity *)
    Prediction : ARRAY[1..2] OF REAL;       (* Predicted state *)
    PredictionCovariance : ARRAY[1..2] OF REAL; (* Predicted covariance *)
    Gain : ARRAY[1..2] OF REAL;             (* Kalman gain *)
    i : INT;                                (* Loop index *)
END_VAR

(* Initialize on Reset *)
IF Reset THEN
    EstimatedPosition := 0.0;
    EstimatedVelocity := 0.0;
    ErrorCov
