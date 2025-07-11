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
FUNCTION_BLOCK FB_KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; // Noisy position measurement
    Q : REAL;                // Process noise covariance
    R : REAL;                // Measurement noise covariance
    DeltaT : REAL;           // Sample time (s)
    Reset : BOOL;            // Reset filter state
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; // Estimated position
    EstimatedVelocity : REAL; // Estimated velocity
    ErrorCovariance : REAL;   // Error covariance
    KalmanGain : REAL;        // Kalman gain
END_VAR

VAR
    x_est_pos : REAL := 0.0;  // Estimated position
    x_est_vel : REAL := 0.0;  // Estimated velocity
    x_est_prev : REAL := 0.0; // Previous estimated position
    p : REAL := 0.0;          // Error covariance
    k : REAL := 0.0;          // Kalman gain
    k_prev : REAL := 0.0;     // Previous Kalman gain
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset filter state on rising edge of Reset
    IF Reset THEN
        x_est_pos := 0.0;
        x_est_vel := 0.0;
        p := 0.0;
        k := 0.0;
        k_prev := 0.0;
        RETURN TRUE;
    END_IF;

    // Prediction step
    x_est_vel := x_est_vel + (MeasuredPosition - x_est_pos) * DeltaT; // Predict velocity
    x_est_pos := x_est_pos + x_est_vel * DeltaT;                      // Predict position
    p := p + Q * DeltaT;                                              // Update error covariance

    // Correction step
    k := p / (p + R);                                                 // Compute Kalman gain
    x_est_pos := x_est_pos
