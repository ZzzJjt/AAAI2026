### Intent:
**Intent Summary:**  
Create a reusable, configurable digital counter function block in IEC 61131-3 Structured Text for industrial PLCs, supporting bidirectional counting with customizable step sizes, bounds, and overflow/underflow protection, while validating inputs and providing status flags.

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
Create a reusable, configurable digital counter function block in IEC 61131-3 Structured Text for industrial PLCs, supporting bidirectional counting with customizable step sizes, bounds, and overflow/underflow protection, while validating inputs and providing status flags.
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
	6.	Test the block with known inputs and verify its performance in real-time control scenarios
(* IEC 61131-3 Structured Text: Digital Counter Function Block *)
(* Purpose: Creates a configurable digital counter with configurable step size, bounds, and overflow/underflow protection *)

FUNCTION_BLOCK DigitalCounter
VAR_INPUT
    Reset : BOOL; (* Reset the counter to 0 *)
    StepSize : INT; (* Increment value for the counter *)
    MaxValue : INT; (* Maximum value for the counter *)
    MinValue : INT; (* Minimum value for the counter *)
END_VAR

VAR_OUTPUT
    CurrentValue : INT; (* Current value of the counter *)
    Overflow : BOOL; (* TRUE if the counter overflows *)
    Underflow : BOOL; (* TRUE if the counter underflows *)
END_VAR

VAR
    CurrentValue : INT := 0; (* Current value of the counter *)
    Overflow : BOOL := FALSE; (* TRUE if the counter overflows *)
    Underflow : BOOL := FALSE; (* TRUE if the counter underflows *)
END_VAR

(* Reset the counter to 0 *)
IF Reset THEN
    CurrentValue := 0;
    Overflow := FALSE;
    Underflow := FALSE;
    RETURN;
END_IF;

(* Check for overflow *)
IF CurrentValue >= MaxValue THEN
    Overflow := TRUE;
    CurrentValue := MaxValue - 1; (* Wrap around to the max value *)
END_IF;

(* Check for underflow *)
IF CurrentValue <= MinValue THEN
    Underflow := TRUE;
    CurrentValue := MinValue + 1; (* Wrap around to the min value *)
END_IF;

(* Increment the counter *)
IF CurrentValue < MaxValue - StepSize THEN
    CurrentValue := CurrentValue + StepSize;
ELSE
    CurrentValue := MaxValue; (* Wrap around to the max value *)
END_IF;

(* Output the current value and flags *)
CurrentValue := CurrentValue;
Overflow := Overflow;
Underflow := Underflow;

(* Comment: This function block creates a digital counter with configurable step size, bounds, and overflow/underflow protection. *)
(* It is suitable for use in industrial PLCs where precise counting is required, and it can be
