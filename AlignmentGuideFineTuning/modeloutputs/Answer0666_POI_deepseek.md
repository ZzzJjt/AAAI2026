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

⸻

🟨 S (Solution) – Solution

```
FUNCTION_BLOCK KalmanFilter
VAR
    x_est_pos : REAL;
    x_est_vel : REAL;
    x_est_prev : REAL;
    p : REAL;
    k : REAL;
END_VAR

VAR_INPUT
    MeasuredPosition : REAL;
    Q : REAL;
    R : REAL;
    DeltaT : REAL;
    Reset : BOOL;
END_VAR

VAR_OUTPUT
    x_est_pos_out : REAL;
    x_est_vel_out : REAL;
    p_out : REAL;
    k_out : REAL;
END_VAR

// Prediction step
x_est_pos_out = x_est_prev + (x_est_vel * DeltaT);
p_out = (1 / (DeltaT * (1 - (Q / (4 * DeltaT))))) * (p + (Q * x_est_prev * x_est_prev));

// Correction step
k_out = (p_out * R) / (p_out * R + (Q + R));
x_est_pos_out = x_est_prev + (k_out * (MeasuredPosition - x_est_prev));
x_est_vel_out = (x_est_pos_out - x_est_prev) / DeltaT;

p_out = (1 / (DeltaT * (1 - (Q / (4 * DeltaT))))) * (p_out + (R + Q) * (x_est_pos_out - x_est_prev * k_out));

// Reset logic
IF Reset = TRUE THEN
    x_est_prev = x_est_pos_out;
    p = p_out;
END_IF;

// Ensure scan-cycle execution
END_FUNCTION_BLOCK
```

This function block provides a modular, scan-safe Kalman filter for estimating the position and velocity of an autonomous vehicle. The block can be easily integrated into industrial PLC systems and configured with noise parameters.
