### Intent:
**Intent Summary:**  
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using configurable noise parameters, ensuring real-time execution on a PLC.  

*(Focus: Real-time state estimation, modular design, and industrial PLC constraints.)*

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
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using configurable noise parameters, ensuring real-time execution on a PLC.  

*(Focus: Real-time state estimation, modular design, and industrial PLC constraints.)*
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
    EstimatedPosition : REAL; // Estimated position
    EstimatedVelocity : REAL; // Estimated velocity
    ErrorCovariance : REAL; // Error covariance
    KalmanGain : REAL; // Kalman gain
END_VAR

VAR
    x_est_pos : REAL; // Estimated position
    x_est_prev : REAL; // Previous estimated position
    x_est_vel : REAL; // Estimated velocity
    p : REAL; // Error covariance
    k : REAL; // Kalman gain
END_VAR

// Reset state on Reset = TRUE
IF Reset THEN
    x_est_pos := 0.0;
    x_est_prev := 0.0;
    x_est_vel := 0.0;
    p := 0.0;
    k := 0.0;
    EstimatedPosition := 0.0;
    EstimatedVelocity := 0.0;
    ErrorCovariance := 0.0;
    KalmanGain := 0.0;
    RETURN;
END_IF;

// Prediction step
x_est_pos := x_est_prev + x_est_vel * DeltaT;

// Update error covariance with process noise
p := p + Q * DeltaT;

// Compute Kalman gain
k := p / (p + R);

// Correct position
x_est_pos := x_est_pos + k * (MeasuredPosition - x_est_prev);

// Estimate velocity
x_est_vel := (x_est_pos - x_est_prev) / DeltaT;

// Update error covariance with measurement noise
p := (1 - k) * p;

// Store results
EstimatedPosition := x_est_pos;
EstimatedVelocity := x_est_vel;
ErrorCovariance := p;
KalmanGain := k;
END_FUNCTION_BLOCK

// Example usage:
// MeasuredPosition := 10.0;
