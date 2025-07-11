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
    // Inputs
    X_Predict : REAL; // Predicted state
    X_Measure : REAL; // Measured state
    K : REAL; // Kalman gain
    R_Predict : REAL; // Predictor covariance
    R_Measure : REAL; // Measurement covariance
    Q : REAL; // Process noise covariance
    P_Predict : REAL; // Predicted covariance
    P_Measure : REAL; // Measured covariance
    D : REAL; // Delta time
END_VAR

VAR_OUTPUT
    X_Estimate : REAL; // Estimated state
    P_Estimate : REAL; // Estimated covariance
    Valid : BOOL; // Input validation flag
END_VAR

VAR
    // Internal variables
    X_Predict_Prev : REAL; // Previous predicted state
    X_Measure_Prev : REAL; // Previous measured state
    K_Prev : REAL; // Previous Kalman gain
    R_Predict_Prev : REAL; // Previous predictor covariance
    R_Measure_Prev : REAL; // Previous measurement covariance
    Q_Prev : REAL; // Previous process noise covariance
    P_Predict_Prev : REAL; // Previous predicted covariance
    P_Measure_Prev : REAL; // Previous measured covariance
    X_Estimate_Prev : REAL; // Previous estimated state
    P_Estimate_Prev : REAL; // Previous estimated covariance
END_VAR

// Reset state on reset
IF Reset = TRUE THEN
    X_Estimate := 0.0;
    P_Estimate := 0.0;
    Valid := TRUE;
    X_Predict_Prev := X_Predict;
    X_Measure_Prev := X_Measure;
    K_Prev := K;
    R_Predict_Prev := R_Predict;
    R_Measure_Prev := R_Measure;
    Q_Prev := Q;
    P_Predict_Prev := P_Predict;
    P_Measure_Prev := P_Measure;
    X_Estimate_Prev := X_Estimate;
    P_Estimate_Prev := P_Estimate;
END_IF;

// Input validation
IF NOT Valid THEN
    X_Estimate := 0.0;
    P_Estimate := 0.
