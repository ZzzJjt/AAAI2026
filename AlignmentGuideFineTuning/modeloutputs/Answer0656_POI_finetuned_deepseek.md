### Intent:
**Intent Summary:**  
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation of an autonomous vehicle’s position and velocity on a PLC.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a discrete-time Kalman filter that:
	•	Estimates position and velocity based on noisy position measurements
	•	Accepts configurable parameters including:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Sample time (DeltaT)
	•	Initial position and velocity
	•	Must be written in Structured Text without matrix libraries
	•	Should be modular and suitable for scan-cycle-based PLC execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL (noise covariances)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Internally store:
	•	Estimated position (x_est_pos) and velocity (x_est_vel)
	•	Previous position (x_est_prev)
	•	Error covariance (p)
	•	Kalman gain (k)
	3.	Implement the prediction step:
	•	Predict new position based on current velocity
	•	Update error covariance with Q
	4.	Implement the correction step:
	•	Compute Kalman gain
	•	Update position with measurement
	•	Estimate velocity based on position change
	•	Update error covariance with R
	5.	Add reset logic and initialize all states on Reset = TRUE
	6.	Ensure the block executes within one scan cycle with safe real-time behavior

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware.

### Generated Code:
**Intent Summary:**  
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation of an autonomous vehicle’s position and velocity on a PLC.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a discrete-time Kalman filter that:
	•	Estimates position and velocity based on noisy position measurements
	•	Accepts configurable parameters including:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Sample time (DeltaT)
	•	Initial position and velocity
	•	Must be written in Structured Text without matrix libraries
	•	Should be modular and suitable for scan-cycle-based PLC execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL (noise covariances)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Internally store:
	•	Estimated position (x_est_pos) and velocity (x_est_vel)
	•	Previous position (x_est_prev)
	•	Error covariance (p)
	•	Kalman gain (k)
	3.	Implement the prediction step:
	•	Predict new position based on current velocity
	•	Update error covariance with Q
	4.	Implement the correction step:
	•	Compute Kalman gain
	•	Update position with measurement
	•	Estimate velocity based on position change
	•	Update error covariance with R
	5.	Add reset logic and initialize all states on Reset = TRUE
	6.	Ensure the block executes within one scan cycle with safe real-time behavior

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware.
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; // Current position measurement
    Q : REAL; // Process noise covariance
    R : REAL; // Measurement noise covariance
    DeltaT : REAL; // Sample time
    Reset : BOOL; // Reset flag
END_VAR

VAR_OUTPUT
    x_est_pos : REAL; // Estimated position
    x_est_vel : REAL; // Estimated velocity
    p : REAL; // Error covariance
    k : REAL; // Kalman gain
END_VAR

VAR
    x_est_prev : REAL; // Previous estimated position
    p_prev : REAL; // Previous error covariance
    k_prev : REAL; // Previous Kalman gain
    x_est_prev_prev : REAL; // Previous previous estimated position
    p_prev_prev : REAL; // Previous previous error covariance
    k_prev_prev : REAL; // Previous previous Kalman gain
END_VAR

// Prediction step
x_est_pos := x_est_prev + k_prev * (MeasuredPosition - x_est_prev);
p_prev := p_prev + Q * DeltaT;

// Correction step
k := (p_prev * R) / (p_prev + R);
x_est_vel := (MeasuredPosition - x_est_pos) / DeltaT;
x_est_pos := x_est_pos + k * (MeasuredPosition - x_est_pos);
p := (p_prev - k * p_prev) / (1 - k);

// Reset logic
IF Reset THEN
    x_est_prev := 0.0;
    p_prev := 0.0;
    k_prev := 0.0;
    x_est_prev_prev := 0.0;
    p_prev_prev := 0.0;
    k_prev_prev := 0.0;
ELSE
    x_est_prev := x_est_pos;
    p_prev := p;
    k_prev := k;
    x_est_prev_prev := x_est_prev;
    p_prev_prev := p_prev;
    k_prev_prev := k_prev;
END
