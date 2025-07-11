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
	•	Example usage in a PLC program

⸻

🟨 S (Solution) – Provide the Solution

```ST
// Kalman Filter Function Block
// Input:
//   MeasuredPosition : REAL
//   Q : REAL
//   R : REAL
//   DeltaT : REAL
//   Reset : BOOL
// Output:
//   EstimatedPosition : REAL
//   EstimatedVelocity : REAL
//   KalmanGain : REAL (optional)
// Internal variables:
//   x_est_pos, x_est_vel, x_est_prev, p, k

// Prediction step
if Reset then
  x_est_pos := 0.0
  x_est_vel := 0.0
  p := 0.0
else
  x_est_pos := x_est_pos + x_est_vel * DeltaT
  x_est_vel := x_est_vel
  p := p + Q * DeltaT
end if;

// Correction (update) step
k := p / (p + R);
EstimatedPosition := x_est_pos + k * (MeasuredPosition - x_est_pos);
EstimatedVelocity := x_est_vel + k * (MeasuredPosition - x_est_pos) / DeltaT;
p := (1 - k) * p;

// Output
if Reset then
  KalmanGain := 0.0
else
  KalmanGain := k
end if;
```

⸻

🟩 T (Test) – Verify the Solution

Test the function block with the following inputs:
	•	MeasuredPosition = 0.0
	•	Q = 0.1
	•	R = 0.01
	•	DeltaT = 0.1
	•	Reset = FALSE
Expected output:
	•	EstimatedPosition = 0.0
	•	EstimatedVelocity = 0.0
	•	KalmanGain = 0.0

Test the function block with the following inputs:
	•	MeasuredPosition = 1.0
	•	Q = 0.1
	•	R = 0.01
	•	DeltaT = 0.1
	•	Reset = FALSE
Expected output:
	•	EstimatedPosition = 1.0
	•	EstimatedVelocity = 0.0
	•	KalmanGain =
