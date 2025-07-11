### Intent:
The task is to implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time position and velocity estimation in industrial control systems, with process noise handling and reset capability.

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
The task is to implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time position and velocity estimation in industrial control systems, with process noise handling and reset capability.
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
    MeasuredPosition : REAL; // Measured position from sensor
    ProcessNoise : REAL := 0.01; // Process noise variance
    Q : REAL := 1.0; // Process noise covariance matrix
    R : REAL := 0.01; // Measurement noise variance
    Measurement : REAL := 0.0; // Measured position from sensor
    Reset : BOOL; // Reset flag to initialize or reinitialize the filter
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; // Estimated position
    EstimatedVelocity : REAL; // Estimated velocity
    Error : REAL; // Estimation error
    Valid : BOOL; // Flag indicating if the filter is valid
END_VAR

VAR
    x_est : ARRAY[1..2] OF REAL; // State vector: [x_est1, x_est2]
    P : ARRAY[1..2, 1..2] OF REAL; // Error covariance matrix
    F : ARRAY[1..2, 1..2] OF REAL; // State transition matrix
    K : ARRAY[1..2, 1..2] OF REAL; // Kalman gain
    x_pred : ARRAY[1..2] OF REAL; // Predicted state
    y : REAL; // Measurement residual
    y_pred : REAL; // Predicted measurement
    i : INT;
    j : INT;
    dt : REAL := 0.1; // Time step
    x_est_prev : ARRAY[1..2] OF REAL; // Previous state
    P_prev : ARRAY[1..2, 1..2] OF REAL; // Previous error covariance matrix
    initialized : BOOL := FALSE; // Flag to track if the filter is initialized
END_VAR

METHOD Initialize : BOOL
BEGIN
    // Initialize state vector and error covariance matrix
    FOR i := 1 TO 2 DO
        x_est[i] := 0.0;
        FOR j := 1 TO 2 DO
            P[i, j
