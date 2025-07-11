### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, precision considerations, and industrial-grade robustness for PLC applications.  

*(Focus: General-purpose interpolation, safety, efficiency, and real-time suitability.)*

### Prompt:
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for creating a reusable function block that performs linear interpolation in real-time industrial control systems using IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You need to develop a function block that:
	•	Accepts five inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: A query input value to interpolate
	•	Returns one output:
	•	Y: The interpolated result
	•	Implements the formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Is safe, efficient, and includes inline comments for maintainability
	•	Addresses precision concerns and real-time performance requirements on PLCs

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
 FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL;
END_VAR
VAR_OUTPUT
    Y : REAL;
END_VAR
	2.	Implement the interpolation logic with error handling:
 IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Fallback to avoid division by zero
END_IF;
	3.	Add inline comments explaining:
	•	The interpolation formula
	•	Division-by-zero checks
	•	Considerations for REAL-type rounding and overflow behavior
	4.	Test the function block using representative use cases (e.g., analog scaling, position control) and validate accuracy under expected PLC scan cycles.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust and efficient interpolation function block that:
	•	Accurately estimates values between two known points
	•	Executes quickly enough for real-time control applications
	•	Is platform-independent, reusable, and easy to maintain
	•	Prevents errors due to division by zero and minimizes rounding impacts

It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, precision considerations, and industrial-grade robustness for PLC applications.  

*(Focus: General-purpose interpolation, safety, efficiency, and real-time suitability.)*
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for creating a reusable function block that performs linear interpolation in real-time industrial control systems using IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You need to develop a function block that:
	•	Accepts five inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: A query input value to interpolate
	•	Returns one output:
	•	Y: The interpolated result
	•	Implements the formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Is safe, efficient, and includes inline comments for maintainability
	•	Addresses precision concerns and real-time performance requirements on PLCs

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
 FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL;
END_VAR
VAR_OUTPUT
    Y : REAL;
END_VAR
	2.	Implement the interpolation logic with error handling:
 IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Fallback to avoid division by zero
END_IF;
	3.	Add inline comments explaining:
	•	The interpolation formula
	•	Division-by-zero checks
	•	Considerations for REAL-type rounding and overflow behavior
	4.	Test the function block using representative use cases (e.g., analog scaling, position control) and validate accuracy under expected PLC scan cycles.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust and efficient interpolation function block that:
	•	Accurately estimates values between two known points
	•	Executes quickly enough for real-time control applications
	•	Is platform-independent, reusable, and easy to maintain
	•	Prevents errors due to division by zero and minimizes rounding impacts

It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling.
FUNCTION_BLOCK FB_LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL;
END_VAR

VAR_OUTPUT
    Y : REAL;
END_VAR

VAR
    denominator : REAL;
    result : REAL;
END_VAR

METHOD Execute : BOOL
BEGIN
    IF X2 <> X1 THEN
        denominator := X2 - X1;
        result := Y1 + ((X - X1) * (Y2 - Y1)) / denominator;
    ELSE
        result := Y1; // Fallback to avoid division by zero
    END_IF;

    Y := result;
    RETURN TRUE;
END_METHOD

// Main execution loop
Execute();

// Reset output for next cycle
Y := 0.0;
RETURN TRUE;
END_FUNCTION_BLOCK

// Documentation:
// - Uses REAL types for precision and compatibility
// - Handles division-by-zero edge case with fallback
// - Designed for real-time use in PLCs
// - Reusable for analog scaling, position control, or recipe scaling

// Example usage:
// X1 := 0.0; Y1 := 0.0; X2 := 10.0; Y2 := 100.0; X := 5.0;
// FB_LinearInterpolation(X1, Y1, X2, Y2, X);
// Y will output 50.0 (linear interpolation)

// Safety considerations:
// - Ensure X1 < X2 for valid interpolation
// - Clamp inputs to safe ranges to prevent overflow or invalid results
// - Use in applications where precision is acceptable and real-time responsiveness is critical

// Future enhancements:
// - Add input validation or error flags
// - Support higher-order polynomial interpolation if needed
// - Optimize for specific PLC platforms (e.g., scan cycle timing, fixed-point arithmetic)

// Industrial application example:
// - Scaling analog sensor values to PLC inputs
// - Adjusting motor position based on distance input
// - Calibrating recipe parameters based on physical measurements
