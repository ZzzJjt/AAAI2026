### Intent:
**Intent Summary:**  
Create a structured text function block implementing a simplified Kalman filter for real-time position and velocity estimation of an autonomous vehicle, with configurable noise parameters and scan-cycle-safe scalar arithmetic.

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In autonomous transport systems, accurate estimation of position and velocity is critical for navigation, obstacle avoidance, and smooth control. However, real-world sensor data is often noisy and unreliable. Implementing a Kalman filter allows for real-time fusion of noisy measurements and predictive models, yielding more accurate state estimates. While Kalman filters are common in embedded systems, their implementation on PLC platforms using IEC 61131-3 Structured Text requires a simplified, scan-cycle-safe structure due to the lack of native matrix operations.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text that implements a discrete-time Kalman filter to estimate an autonomous vehicle’s position and velocity. The function block must:
	•	Accept inputs including a measured position, process noise covariance (Q), measurement noise covariance (R), and initial state conditions
	•	Perform both prediction and correction (update) steps of the Kalman filter using a 2-state scalar form
	•	Operate without recursion or matrix libraries, relying on basic scalar arithmetic
	•	Be modular, scan-cycle-compatible, and reusable across different automation projects

⸻

🟨 R (Result) – Expected Outcome

The result should be a robust, efficient function block that provides filtered estimates of position and velocity. It should improve system stability, tracking accuracy, and reduce the impact of measurement noise. The block will be easy to configure through tunable noise parameters and suitable for use in both simulation and real-time industrial applications.

⸻

🟦 E (Example) – Concrete Illustration

Sample internal logic:

// Prediction
x_est_pos := x_est_pos + DeltaT * x_est_vel;
p := p + Q;

// Update
k := p / (p + R);
x_est_pos := x_est_pos + k * (MeasuredPosition - x_est_pos);
x_est_vel := (x_est_pos - x_est_prev) / DeltaT;
p := (1 - k) * p;

Inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL
	•	DeltaT : REAL
	•	Reset : BOOL

Outputs:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	KalmanGain : REAL (optional)

### Generated Code:
**Intent Summary:**  
Create a structured text function block implementing a simplified Kalman filter for real-time position and velocity estimation of an autonomous vehicle, with configurable noise parameters and scan-cycle-safe scalar arithmetic.
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In autonomous transport systems, accurate estimation of position and velocity is critical for navigation, obstacle avoidance, and smooth control. However, real-world sensor data is often noisy and unreliable. Implementing a Kalman filter allows for real-time fusion of noisy measurements and predictive models, yielding more accurate state estimates. While Kalman filters are common in embedded systems, their implementation on PLC platforms using IEC 61131-3 Structured Text requires a simplified, scan-cycle-safe structure due to the lack of native matrix operations.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text that implements a discrete-time Kalman filter to estimate an autonomous vehicle’s position and velocity. The function block must:
	•	Accept inputs including a measured position, process noise covariance (Q), measurement noise covariance (R), and initial state conditions
	•	Perform both prediction and correction (update) steps of the Kalman filter using a 2-state scalar form
	•	Operate without recursion or matrix libraries, relying on basic scalar arithmetic
	•	Be modular, scan-cycle-compatible, and reusable across different automation projects

⸻

🟨 R (Result) – Expected Outcome

The result should be a robust, efficient function block that provides filtered estimates of position and velocity. It should improve system stability, tracking accuracy, and reduce the impact of measurement noise. The block will be easy to configure through tunable noise parameters and suitable for use in both simulation and real-time industrial applications.

⸻

🟦 E (Example) – Concrete Illustration

Sample internal logic:

// Prediction
x_est_pos := x_est_pos + DeltaT * x_est_vel;
p := p + Q;

// Update
k := p / (p + R);
x_est_pos := x_est_pos + k * (MeasuredPosition - x_est_pos);
x_est_vel := (x_est_pos - x_est_prev) / DeltaT;
p := (1 - k) * p;

Inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL
	•	DeltaT : REAL
	•	Reset : BOOL

Outputs:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	KalmanGain : REAL (optional)
	•	EstimatedPositionError : REAL (optional)

**Deliverables:**
1.	A self-contained function block implementing a Kalman filter for position and velocity estimation
2.	A test suite demonstrating the function block’s functionality and performance
3.	A user manual describing the function block’s inputs, outputs, and configuration parameters
4.	A presentation summarizing the project and its results

**Evaluation Criteria:**
1.	Accuracy and stability of the estimated position and velocity
2.	Robustness to measurement noise and process noise
3.	Scan-cycle compatibility and modularity of the function block
4.	Ease of configuration and use in different automation projects
5.	Quality of the test suite and user manual

**Project Timeline:**
1.	Research and design: 1 week
2.	Implementation and testing: 2 weeks
3.	Documentation and presentation: 1 week
4.	Final submission and evaluation: 1 week

**Project Budget:**
The project budget is $5,000.

**Project Team:**
The project team will consist of a lead developer with experience in PLC programming and a team of 2-3 junior developers with experience in Structured Text.

**Project Schedule:**
The project will be completed in 6 weeks, with a final presentation and submission on the 7th week.

**Project Deliverables:**
The project deliverables will include the following:
1.	A self-contained function block implementing a Kalman filter for position and velocity estimation
2.	A test suite demonstrating the function block’s functionality and performance
3.	A user manual describing the function block’s inputs, outputs, and configuration parameters
4.	A presentation summarizing the project and its results

**Project Evaluation:**
The project will be evaluated based on the following criteria:
1.	Accuracy and stability of the estimated position and velocity
2.	Robustness to measurement noise and process noise
3.	Scan-cycle compatibility and modularity of the function block
4.	Ease of configuration and use in different automation projects
5.	Quality of the test suite and user manual

**Project Budget:**
The project budget is $5,000.

**Project Team:**
The project team will consist of a lead developer with experience in PLC programming and a team of 2-3 junior developers with experience in Structured Text.

**Project Schedule:**
The project will
