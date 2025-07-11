### Intent:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

### Generated Code:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; // Measured position from sensors
    Q : REAL := 0.01;        // Process noise covariance
    R : REAL := 0.1;         // Measurement noise covariance
    dt : REAL := 0.1;        // Time step (e.g., 100 ms)
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; // Estimated position
    EstimatedVelocity : REAL; // Estimated velocity
    Error : REAL;             // Prediction error
    ValidInput : BOOL := TRUE; // Input validation flag
END_VAR

VAR
    x_est : ARRAY[1..2] OF REAL; // State vector: [x_est, x_est_dot]
    P : ARRAY[1..2, 1..2] OF REAL; // Error covariance matrix
    K : ARRAY[1..2, 1..2] OF REAL; // Gain matrix
    x_pred : ARRAY[1..2] OF REAL; // Predicted state
    y : REAL;                    // Measurement
    y_pred : REAL;               // Predicted measurement
    y_est : REAL;                // Innovation
    y_est_dot : REAL;            // Innovation rate
    y_est_dot_pred : REAL;       // Predicted innovation rate
    y_est_dot_est : REAL;        // Estimated innovation rate
    y_est_dot_est_pred : REAL;   // Predicted estimated innovation rate
    y_est_dot_est_est : REAL;    // Estimated innovation rate at next time step
    y_est_dot_est_est_pred : REAL;// Predicted estimated innovation rate at next time step
    y_est_dot_est_est_est : REAL;// Estimated innovation rate at next next time step
    y_est_dot_est_est_est_pred : REAL;// Predicted estimated innovation rate at next next time step
    y_est_dot_est_est_est_est : REAL
