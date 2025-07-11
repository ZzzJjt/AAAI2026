### Intent:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy measurements, with configurable noise parameters, reset capability, and safe PLC execution.  

*(Focus: Real-time state estimation, scalar arithmetic, and PLC-compliant design.)*

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC control engineer developing a Kalman filter in IEC 61131-3 Structured Text for real-time state estimation in an autonomous vehicle control system.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained Kalman filter function block that estimates the position and velocity of an autonomous transport vehicle using noisy position measurements. Your implementation should:
	•	Use a simplified 2-state discrete-time Kalman filter
	•	Accept configuration inputs for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity
	•	Sample time (DeltaT)
	•	Be written entirely with scalar arithmetic (no recursion or matrix libraries)
	•	Include input validation, reset capability, and internal memory for state tracking
	•	Output the estimated position and velocity, as well as optional Kalman gain
	•	Ensure safe execution in PLC scan-cycle environments

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block, including:
	•	Inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL
	•	R : REAL
	•	DeltaT : REAL
	•	Reset : BOOL
	•	Outputs:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	KalmanGain : REAL (optional)
	•	Internal variables:
	•	x_est_pos, x_est_vel, x_est_prev, p, k
	•	Logic structure with:
	•	Prediction step
	•	Correction (update) step
	•	State re-initialization on Reset
	•	Inline comments explaining each calculation and its role in the filter

### Generated Code:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy measurements, with configurable noise parameters, reset capability, and safe PLC execution.  

*(Focus: Real-time state estimation, scalar arithmetic, and PLC-compliant design.)*
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC control engineer developing a Kalman filter in IEC 61131-3 Structured Text for real-time state estimation in an autonomous vehicle control system.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained Kalman filter function block that estimates the position and velocity of an autonomous transport vehicle using noisy position measurements. Your implementation should:
	•	Use a simplified 2-state discrete-time Kalman filter
	•	Accept configuration inputs for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity
	•	Sample time (DeltaT)
	•	Be written entirely with scalar arithmetic (no recursion or matrix libraries)
	•	Include input validation, reset capability, and internal memory for state tracking
	•	Output the estimated position and velocity, as well as optional Kalman gain
	•	Ensure safe execution in PLC scan-cycle environments

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block, including:
	•	Inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL
	•	R : REAL
	•	DeltaT : REAL
	•	Reset : BOOL
	•	Outputs:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	KalmanGain : REAL (optional)
	•	Internal variables:
	•	x_est_pos, x_est_vel, x_est_prev, p, k
	•	Logic structure with:
	•	Prediction step
	•	Correction (update) step
	•	State re-initialization on Reset
	•	Inline comments explaining each calculation and its role in the filter
(* IEC 61131-3 Structured Text: Kalman Filter for Autonomous Vehicle Position Estimation *)
(* Purpose: Estimates vehicle position and velocity using noisy position measurements *)

FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; (* Current position measurement, e.g., m *)
    Q : REAL; (* Process noise covariance, e.g., 0.1 m^2 *)
    R : REAL; (* Measurement noise covariance, e.g., 0.01 m^2 *)
    DeltaT : REAL; (* Sample time, e.g., 100 ms *)
    Reset : BOOL; (* Reset flag, e.g., TRUE to reset state *)
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; (* Estimated position, e.g., m *)
    EstimatedVelocity : REAL; (* Estimated velocity, e.g., m/s *)
    KalmanGain : REAL; (* Kalman gain, e.g., 0.1 to 10 *)
END_VAR

VAR
    x_est_pos : REAL; (* Estimated position *)
    x_est_vel : REAL; (* Estimated velocity *)
    x_est_prev : REAL; (* Previous estimated position *)
    p : REAL; (* Estimated position covariance *)
    k : REAL; (* Kalman gain *)
    deltaT : REAL; (* Sample time *)
    reset : BOOL; (* Reset flag *)
END_VAR

(* Reset state on Reset *)
IF Reset THEN
    x_est_pos := 0.0;
    x_est_vel := 0.0;
    x_est_prev := 0.0;
    p := 1.0;
    k := 0.0;
    deltaT := 0.0;
    reset := FALSE;
    EstimatedPosition := 0.0;
    EstimatedVelocity := 0.0;
    KalmanGain := 0.0;
    RETURN;
END_IF;

(* Predict step *)
x_est_prev := x_est_pos;
p := p + Q * deltaT;

(* Correction step *)
k := p * R / (p + R);
x_est_pos := x_est_prev
