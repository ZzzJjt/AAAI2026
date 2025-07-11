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
	5.	Add initialization logic and inline comments for maintainability and readability
	6.	Test and validate the function block using simulated or real-world data

**Digital Counter:**

🟥 B (Before) – The Problem or Challenge

In industrial automation, it is often necessary to count events or occurrences of a certain condition. For example, a PLC might need to count the number of times a sensor is triggered, the number of times a motor has rotated, or the number of times a process has completed. However, implementing a simple counter in IEC 61131-3 Structured Text can be challenging, especially when considering edge cases such as overflow and underflow, and ensuring that the counter is scan-cycle-safe and modular.

⸻

🟩 A (After) – The Desired Outcome

Create a reusable, configurable digital counter function block in IEC 61131-3 Structured Text that supports bidirectional counting with customizable step sizes, bounds, and overflow/underflow protection, while validating inputs and providing status flags. The function block should:
	•	Accept a single input (count) and return a single output (count)
	•	Support both positive and negative step sizes
	•	Allow for setting upper and lower bounds
	•	Provide status flags for overflow, underflow, and invalid input
	•	Be scan-cycle-safe and modular
	•	Be suitable for deployment on industrial PLC hardware

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs for:
	•	Count : INT
	•	StepSize : INT
	•	UpperBound : INT
	•	LowerBound : INT
	•	Reset : BOOL
	2.	Include internal states for:
	•	Current count
	•	Overflow/underflow flags
	3.	Implement the counting logic using scalar math
	4.	Add validation logic to check for invalid inputs and set status flags accordingly
	5.	Add initialization logic and inline comments for maintainability and readability
	6.	Test and validate the function block using simulated or real-world data

**Kalman Filter:**

🟥 B (Before) – The Problem or Challenge

In industrial automation and autonomous systems, estimating the position and velocity of a moving vehicle is crucial for navigation, control, and safety. However, raw sensor data (e.g., from encoders or GPS) often contains noise and uncertainty, which can lead to unstable or inaccurate
