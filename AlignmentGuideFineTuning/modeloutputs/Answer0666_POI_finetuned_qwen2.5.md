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

**B-A-B-E:**

Before: The Challenge

In autonomous transport systems, estimating position and velocity from noisy sensor data is critical for navigation and control. However, implementing a Kalman filter in IEC 61131-3 Structured Text—without matrix libraries—on a PLC presents significant challenges. The scan-cycle-safe execution, real-time performance, and configurable parameters make it difficult to maintain both accuracy and scan-cycle compliance.

After: The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for estimating position and velocity. The block should:
	•	Accept configurable noise parameters (Q and R) and initial conditions
	•	Perform both prediction and correction steps within a scan-cycle-safe framework
	•	Be modular and reusable for real-time state estimation in industrial control systems
	•	Ensure scan-cycle-safe execution, with all computations fitting within the PLC’s scan time
	•	Include detailed comments explaining the steps and parameter roles for clarity and maintainability
	•	Enable real-time adjustment of noise models and initial conditions for robust performance under varying environmental conditions
	•	Be designed with industrial PLC constraints in mind, ensuring scan-cycle compatibility and deterministic execution
	•	Provide a clear, scan-cycle-safe implementation of the Kalman filter algorithm, with a focus on real-time applicability in motion control and navigation systems
	•	Include a discussion of the limitations of scan-cycle-safe execution in Kalman filtering and potential trade-offs between accuracy and scan-cycle compliance
	•	Be suitable for use in applications where real-time state estimation is required, such as autonomous transport, robotics, or industrial automation
	•	Be designed with scan-cycle-safe execution in mind, ensuring that all computations and state updates occur within the constraints of the PLC’s scan cycle
	•	Include detailed comments explaining the steps and parameter roles for clarity and maintainability
	•	Enable real-time adjustment of noise models and initial conditions for robust performance under varying environmental conditions
	•	Be designed with industrial PLC constraints in mind, ensuring scan-cycle compatibility and deterministic execution
	•	Provide a clear, scan-cycle-safe implementation of the Kalman filter algorithm, with a focus on real-time applicability in motion control and navigation systems
	•	Include a discussion of the limitations of scan-cycle-safe execution in Kalman filtering and potential trade-offs between accuracy and scan-cycle compliance
	•	Be suitable for use in applications
