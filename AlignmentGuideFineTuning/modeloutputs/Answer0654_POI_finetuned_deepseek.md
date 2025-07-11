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
    // Inputs
    X_Predict : REAL; // Predicted state
    X_Actual : REAL; // Actual state
    U : REAL; // Process noise
    Q : REAL; // Process noise covariance
    R : REAL; // Measurement noise covariance
    K_Reset : BOOL; // Reset flag
    Reset : BOOL; // Reset flag
END_VAR

VAR_OUTPUT
    X_Predict_Filtered : REAL; // Filtered state
    X_Actual_Filtered : REAL; // Filtered state
    X_Predict_Filtered_Covariance : REAL; // Covariance of filtered state
    X_Actual_Filtered_Covariance : REAL; // Covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate : REAL; // Estimate of covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate_Covariance : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate_Covariance : REAL; // Estimate of covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Predict_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance_Covariance_Covariance : REAL; // Estimate of covariance of filtered state
    X_Actual_Filtered_Covariance_Estimate_Covariance_Covariance_Covariance_Cov
