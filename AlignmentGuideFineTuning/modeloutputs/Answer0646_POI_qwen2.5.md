### Intent:
**Intent Summary:**  
Create a Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy measurements, with configurable noise parameters and real-time PLC execution.

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
Create a Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy measurements, with configurable noise parameters and real-time PLC execution.
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

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware. Ensure the code is well-commented and follows IEC 61131-3 standards for clarity and maintainability.

**Code:**
```plaintext
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL;
    Q, R : REAL; // Noise covariances
    DeltaT : REAL; // Sample time
    Reset : BOOL;
END_VAR

VAR
    x_est_pos, x_est_prev : REAL; // Estimated position and previous position
    x_est_vel : REAL; // Estimated velocity
    p : REAL; // Error covariance
    k : REAL; // Kalman gain
END_VAR

// Prediction step
PROCEDURE Predict
VAR
    x_pred_pos : REAL; // Predicted position
    x_pred_vel : REAL; // Predicted velocity
END_VAR

x_pred_pos := x_est_pos + x_est_vel * DeltaT;
x_pred_vel := x_est_vel;

p := p + Q;
END_PROCEDURE

// Correction step
PROCEDURE Correct
VAR
    y : REAL; // Innovation
    S : REAL; // Innovation covariance
END_VAR

y := MeasuredPosition - x_pred_pos;
S := p + R;
k := p / S;
x_est_pos := x_pred_pos + k * y;
x_est_vel := x_est_vel + k * (MeasuredPosition - x_est_pos - x_est_vel * DeltaT);
p := (1 - k) * p;
END_PROCEDURE

// Reset logic
PROCEDURE ResetStates
VAR
    x_est_pos, x_est_vel : REAL; // Reset estimated position and velocity
    p : REAL; // Reset error covariance
END_VAR

x_est_pos := 0.0;
x_est_vel := 0.0;
p := 0.0;
END_PROCEDURE

// Main execution
PROCEDURE Execute
VAR
    x_est_pos, x_est_vel : REAL; // Estimated position and velocity
    p : REAL; // Error covariance
    k : REAL; // Kalman gain
END_VAR

IF Reset THEN
    ResetStates;
ELSE
    Predict;
    Correct;
END_IF;

// Output estimated position and velocity
OutputPosition := x_est_pos;
OutputVelocity := x_est_vel;
END_PROCEDURE
END_FUNCTION_BLOCK
```

**Explanation:**
This function block implements a discrete-time Kalman filter for estimating the position and velocity of an autonomous vehicle. It includes configurable noise covariances (Q and R
