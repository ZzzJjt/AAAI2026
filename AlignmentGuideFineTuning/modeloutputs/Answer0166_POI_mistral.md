### Intent:
**Intent Summary:**  
Create a self-contained, iterative heapsort function block in IEC 61131-3 Structured Text for PLCs to efficiently sort integer arrays in-place without recursion or advanced language features.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation and autonomous systems, estimating the position and velocity of a moving vehicle is crucial for navigation, control, and safety. However, raw sensor data (e.g., from encoders or GPS) often contains noise and uncertainty, which can lead to unstable or inaccurate control decisions. Without a proper filtering mechanism like a Kalman filter, it becomes difficult to derive smooth and reliable estimates in real time, especially on a PLC that lacks native matrix and recursive math libraries.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for real-time estimation of an autonomous vehicle’s position and velocity. The block should:
	•	Use a discrete-time Kalman filter formulation
	•	Include configurable parameters for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity estimates
	•	Accept position measurements as input and output filtered estimates
	•	Be modular, scan-cycle-safe, and suitable for deployment on industrial PLC hardware

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs for:
	•	MeasuredPosition : REAL
	•	Q : REAL (process noise)
	•	R : REAL (measurement noise)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Include internal states:
	•	Position and velocity estimates
	•	Error covariance matrix components
	•	Kalman gain calculation logic
	3.	Implement the prediction and update steps using scalar math (2-state Kalman filter)
	4.	Return outputs such as:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	Optional: KalmanGain : REAL
	5.	Add initialization logic and inline comments for maintainability

### Generated Code:
**Intent Summary:**  
Create a self-contained, iterative heapsort function block in IEC 61131-3 Structured Text for PLCs to efficiently sort integer arrays in-place without recursion or advanced language features.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation and autonomous systems, estimating the position and velocity of a moving vehicle is crucial for navigation, control, and safety. However, raw sensor data (e.g., from encoders or GPS) often contains noise and uncertainty, which can lead to unstable or inaccurate control decisions. Without a proper filtering mechanism like a Kalman filter, it becomes difficult to derive smooth and reliable estimates in real time, especially on a PLC that lacks native matrix and recursive math libraries.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for real-time estimation of an autonomous vehicle’s position and velocity. The block should:
	•	Use a discrete-time Kalman filter formulation
	•	Include configurable parameters for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity estimates
	•	Accept position measurements as input and output filtered estimates
	•	Be modular, scan-cycle-safe, and suitable for deployment on industrial PLC hardware

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs for:
	•	MeasuredPosition : REAL
	•	Q : REAL (process noise)
	•	R : REAL (measurement noise)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Include internal states:
	•	Position and velocity estimates
	•	Error covariance matrix components
	•	Kalman gain calculation logic
	3.	Implement the prediction and update steps using scalar math (2-state Kalman filter)
	4.	Return outputs such as:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	Optional: KalmanGain : REAL
	5.	Add initialization logic and inline comments for maintainability

**Implementation:**

```
FUNCTION_BLOCK KalmanFilter
  VAR
    // Internal states
    EstimatedPosition : REAL;
    EstimatedVelocity : REAL;
    P : REAL;
    Q : REAL;
    R : REAL;
    DeltaT : REAL;
    Reset : BOOL;

    // Error covariance matrix components
    P_xx : REAL;
    P_xv : REAL;
    P_vv : REAL;

    // Kalman gain calculation
    K : REAL;
    S : REAL;
    Y : REAL;
  END_VAR

  // Initialization
  IF Reset THEN
    EstimatedPosition := 0.0;
    EstimatedVelocity := 0.0;
    P_xx := 10000.0;
    P_xv := 0.0;
    P_vv := 10000.0;
  END_IF

  // Prediction step
  IF NOT Reset THEN
    EstimatedVelocity := EstimatedVelocity + (EstimatedPosition - EstimatedVelocity) * DeltaT;
    P_xx := P_xx + Q * DeltaT;
    P_xv := P_xv + Q * DeltaT;
    P_vv := P_vv + Q * DeltaT;
  END_IF

  // Update step
  Y := MeasuredPosition - EstimatedPosition;
  S := P_xx + R;
  K := P_xv / S;
  EstimatedPosition := EstimatedPosition + K * Y;
  P_xx := (1 - K * K) * P_xx;
  P_xv := K * P_xv;
  P_vv := P_vv;

  // Outputs
  EstimatedPosition := EstimatedPosition;
  EstimatedVelocity := EstimatedVelocity;
  KalmanGain := K;
END_FUNCTION_BLOCK
```

**Notes:**

* This implementation assumes a 2-state Kalman filter, which estimates position and velocity.
* The process noise covariance (Q) and measurement noise covariance
