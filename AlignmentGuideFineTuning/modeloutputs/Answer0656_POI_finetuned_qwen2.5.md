### Intent:
**Intent Summary:**  
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.

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
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.
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

In industrial automation, estimating the position and velocity of autonomous transport vehicles is critical for navigation and control. However, real-time state estimation using noisy sensor data is difficult without a Kalman filter. Many PLC platforms lack native Kalman filter implementations, and even when available, they often rely on matrix libraries that are not supported in IEC 61131-3 Structured Text.

After: The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. The function block should:
	•	Accept configurable parameters for noise covariance and initial conditions
	•	Perform both the prediction and correction steps of the Kalman filter algorithm
	•	Be scan-cycle-safe and modular, ensuring real-time execution on PLCs
	•	Provide accurate and noise-robust state estimates for motion control applications
	•	Enable industrial developers to implement advanced state estimation without relying on unsupported matrix libraries
	•	Be reusable and maintainable, with clear documentation for integration into motion control systems
	•	Include detailed comments explaining the steps of the Kalman filter and the role of each parameter
	•	Be designed with scan-cycle safety in mind, ensuring deterministic execution and reliable state estimation under varying environmental conditions
	•	Allow for real-time tuning of noise parameters and initial conditions, enabling optimal performance in dynamic environments
	•	Be structured to handle edge cases, such as sensor failures or rapid motion, with robust error handling and fallback mechanisms
	•	Be optimized for scan-cycle performance, with efficient use of PLC resources and memory, to ensure smooth operation in PLC-based motion control systems
	•	Include a discussion of the limitations of the implementation, particularly in terms of scan-cycle timing and numerical stability, and provide suggestions for further optimization or adaptation to specific use cases
	•	Be suitable for integration into a PLC environment, with clear function block inputs and outputs, and a detailed explanation of how to configure and use the function block in practice
	•	Be designed with industrial standards in mind, ensuring compliance with IEC 61131-3 and other relevant PLC programming guidelines
	•	Include a comparison with other state estimation methods, highlighting the advantages of using a Kalman filter in a PLC environment
	•	Be part of a larger system that includes motion control, sensor fusion,
