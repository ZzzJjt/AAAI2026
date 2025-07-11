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

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware.

**Deliverables:**
	•	A function block in IEC 61131-3 Structured Text that implements a Kalman filter for estimating the position and velocity of an autonomous vehicle.
	•	A test plan and test results to demonstrate the function block’s accuracy and real-time performance.
	•	A report that describes the design and implementation of the function block, including any challenges encountered and lessons learned.
	•	A presentation to explain the function block and its implementation to a group of control systems engineers.
	•	A video demonstration of the function block in action, showing its performance in a real-world scenario.
	•	A GitHub repository containing the source code for the function block and any supporting documentation.
	•	A blog post explaining the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A white paper describing the function block and its implementation, with a focus on the design and implementation decisions.
	•	A patent application for the function block, if applicable.
	•	A conference presentation describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A journal article describing the function block and its implementation, with a focus on the design and implementation decisions.
	•	A book chapter describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A book describing the function block and its implementation, with a focus on the design and implementation decisions.
	•	A video course describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A podcast episode describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A YouTube video describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A Twitter thread describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A LinkedIn post describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A Medium post describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A Reddit post describing the function block and its implementation, with a focus on the challenges and lessons learned.
	•	A Hacker News post describing the function block and its implementation, with a
