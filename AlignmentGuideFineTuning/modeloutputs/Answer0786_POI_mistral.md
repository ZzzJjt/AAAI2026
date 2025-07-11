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

**Example:**

```
FUNCTION_BLOCK KalmanFilter
VAR
	x_est_pos, x_est_vel, x_est_prev, p, k : REAL;
	Q, R, DeltaT : REAL;
	Reset : BOOL;
	MeasuredPosition : REAL;
BEGIN
	// Check for reset condition
	IF Reset THEN
		x_est_pos := 0.0;
		x_est_vel := 0.0;
		x_est_prev := 0.0;
		p := 0.0;
	END_IF;

	// Prediction step
	x_est_prev := x_est_pos;
	x_est_pos := x_est_pos + x_est_vel * DeltaT;
	p := p + Q * DeltaT;

	// Correction step
	k := p / (p + R);
	x_est_vel := x_est_vel + k * (MeasuredPosition - x_est_pos);
	x_est_pos := x_est_pos + x_est_vel * DeltaT;
	p := (1 - k) * p;

	// Outputs
	EstimatedPosition := x_est_pos;
	EstimatedVelocity := x_est_vel;
	KalmanGain := k;
END_FUNCTION_BLOCK
```

**Notes:**

* This example is a simplified implementation of a 2-state discrete-time Kalman filter. In practice, you may want to consider more complex filter structures, such as extended or unscented Kalman filters, depending on the specific requirements of your application.
* The provided example assumes that the process noise covariance (Q) and measurement noise covariance (R) are scalars. In some cases, you may need to use diagonal matrices to represent these values if your application requires separate noise terms for position and velocity.
* The example does not include any error checking or handling for invalid input values. In a real-world implementation, you should add appropriate checks to ensure that the input values are within acceptable ranges.
* The example does not include any safety mechanisms to prevent the filter from diverging or becoming un
