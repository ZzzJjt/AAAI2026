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

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware. Ensure the code is well-commented and follows IEC 61131-3 standards for readability and maintainability.

**Note:** The provided code snippet is a starting point for the Kalman filter implementation. You will need to expand upon this to meet the requirements of the task. **IEC 61131-3 Structured Text Kalman Filter Function Block**

```structuredtext
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL;
    Q : REAL; // Process noise covariance
    R : REAL; // Measurement noise covariance
    DeltaT : REAL; // Sample time
    Reset : BOOL;
END_VAR

VAR
    x_est_pos : REAL; // Estimated position
    x_est_vel : REAL; // Estimated velocity
    x_est_prev : REAL; // Previous position
    p : REAL; // Error covariance
    k : REAL; // Kalman gain
END_VAR

PROCEDURE Initialize
    x_est_pos := 0.0;
    x_est_vel := 0.0;
    x_est_prev := 0.0;
    p := 1000.0; // Initial error covariance
END_PROCEDURE

PROCEDURE Predict
    x_est_pos := x_est_prev + x_est_vel * DeltaT;
    p := p + Q;
END_PROCEDURE

PROCEDURE Correct
    k := p / (p + R);
    x_est_pos := x_est_pos + k * (MeasuredPosition - x_est_pos);
    x_est_vel := (x_est_pos - x_est_prev) / DeltaT;
    p := (1 - k) * p;
END_PROCEDURE

PROCEDURE Execute
    IF Reset THEN
        Initialize();
    ELSE
        Predict();
        Correct();
    END_IF;
END_PROCEDURE

END_FUNCTION_BLOCK
```

This function block implements a discrete-time Kalman filter for estimating the position and velocity of an autonomous vehicle. It takes measured position, process noise covariance (Q), measurement noise covariance (R), sample time (DeltaT), and a reset signal as inputs. The block internally stores the estimated position, velocity, previous position, error covariance, and Kalman gain.

The `Initialize` procedure sets the initial values for the estimated position, velocity, previous position, and error covariance. The `Predict` procedure predicts the new position based on the current velocity and updates the error covariance with the process noise covariance. The `Correct` procedure computes the Kalman gain, updates
