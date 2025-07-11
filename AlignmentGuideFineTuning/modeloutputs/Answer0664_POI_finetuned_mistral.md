### Intent:
**Intent Summary:**  
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate vehicle position and velocity from noisy measurements, with input validation, reset capability, and deterministic execution for industrial motion control applications.  

*(Focus: PLC-compatible state estimation with safety, modularity, and real-time performance.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate vehicle position and velocity from noisy measurements, with input validation, reset capability, and deterministic execution for industrial motion control applications.  

*(Focus: PLC-compatible state estimation with safety, modularity, and real-time performance.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; // Measured position (e.g., in meters)
    Q : REAL;                // Process noise covariance
    R : REAL;                // Measurement noise covariance
    dt : REAL;               // Time step (e.g., 0.1 seconds)
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; // Estimated position
    EstimatedVelocity : REAL; // Estimated velocity
    ValidInput : BOOL;        // TRUE if inputs are valid
END_VAR

VAR
    x_est : ARRAY[1..2] OF REAL; // State vector: [x_est, x_est_dot]
    P : ARRAY[1..2, 1..2] OF REAL; // Error covariance matrix
    F : ARRAY[1..2, 1..2] OF REAL; // State transition matrix
    K : ARRAY[1..2, 1] OF REAL; // Kalman gain
    x_pred : ARRAY[1..2] OF REAL; // Predicted state
    y : REAL;                   // Measurement error
    y_pred : REAL;              // Predicted measurement
    y_est : REAL;               // Estimated measurement
    y_est_error : REAL;         // Measurement error estimate
    y_est_error_pred : REAL;    // Predicted measurement error
    y_est_error_est : REAL;     // Estimated measurement error
    y_est_error_est_pred : REAL;// Predicted estimated measurement error
    i : INT;                    // Iteration counter
    eps : REAL := 1.0e-6;       // Numerical tolerance
END_VAR

// Initialize state
x_est[1] := 0.0; // Initial position estimate
x_est[2] := 0.0; // Initial velocity estimate
P[1,1] := 1.0;    // Initial position error covariance
P[2,2] := 1.0;    // Initial velocity error covariance

//
