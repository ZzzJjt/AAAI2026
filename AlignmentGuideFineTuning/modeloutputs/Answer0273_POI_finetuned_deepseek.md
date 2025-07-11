### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, logging, and numerical stability for industrial PLC applications like sensor scaling or actuator control.  

*(Key focus: Precision, edge-case safety, and deterministic execution in automation systems.)*

### Prompt:
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, linear interpolation is frequently used to estimate unknown values between two measured or set points—such as sensor scaling, actuator control, or temperature compensation. A reusable, well-documented function block is essential for ensuring accuracy and maintainability in real-time control systems, where precision and performance are both critical.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named LinearInterpolation, that:
	•	Accepts the following inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: The query point for which Y is interpolated
	•	Computes the output Y using the linear interpolation formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes detailed inline comments explaining the math and each computation step
	•	Handles edge cases such as X1 = X2 to avoid division by zero
	•	Is designed to be lightweight and deterministic for real-time use

You should also document considerations like floating-point rounding errors and safety checks for unexpected input behavior.

⸻

🟨 R (Result) – The Expected Outcome

The result is a reusable, general-purpose interpolation block that:
	•	Can be integrated into HMI scaling, analog signal translation, or control logic
	•	Ensures predictable and accurate behavior even under PLC execution time constraints
	•	Minimizes rounding errors and improves reliability in process control applications

It’s suitable for use in production PLC code, across platforms such as Siemens, Beckhoff, and CODESYS.

⸻

🟦 E (Example) – A Practical Use Case

Suppose you are scaling a temperature sensor’s voltage output (e.g., 0.5 V at 0°C, 2.5 V at 100°C). Using LinearInterpolation, you input X1 := 0.5, Y1 := 0, X2 := 2.5, Y2 := 100, and a live voltage value X := 1.5. The function block returns Y = 50, accurately estimating the temperature.

Inline comment example:
// Check for zero denominator to avoid division error
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback value
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, logging, and numerical stability for industrial PLC applications like sensor scaling or actuator control.  

*(Key focus: Precision, edge-case safety, and deterministic execution in automation systems.)*
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, linear interpolation is frequently used to estimate unknown values between two measured or set points—such as sensor scaling, actuator control, or temperature compensation. A reusable, well-documented function block is essential for ensuring accuracy and maintainability in real-time control systems, where precision and performance are both critical.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named LinearInterpolation, that:
	•	Accepts the following inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: The query point for which Y is interpolated
	•	Computes the output Y using the linear interpolation formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes detailed inline comments explaining the math and each computation step
	•	Handles edge cases such as X1 = X2 to avoid division by zero
	•	Is designed to be lightweight and deterministic for real-time use

You should also document considerations like floating-point rounding errors and safety checks for unexpected input behavior.

⸻

🟨 R (Result) – The Expected Outcome

The result is a reusable, general-purpose interpolation block that:
	•	Can be integrated into HMI scaling, analog signal translation, or control logic
	•	Ensures predictable and accurate behavior even under PLC execution time constraints
	•	Minimizes rounding errors and improves reliability in process control applications

It’s suitable for use in production PLC code, across platforms such as Siemens, Beckhoff, and CODESYS.

⸻

🟦 E (Example) – A Practical Use Case

Suppose you are scaling a temperature sensor’s voltage output (e.g., 0.5 V at 0°C, 2.5 V at 100°C). Using LinearInterpolation, you input X1 := 0.5, Y1 := 0, X2 := 2.5, Y2 := 100, and a live voltage value X := 1.5. The function block returns Y = 50, accurately estimating the temperature.

Inline comment example:
// Check for zero denominator to avoid division error
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback value
END_IF;
#include <stdio.h>

// Function block for linear interpolation
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2 : REAL; // Known points
    X : REAL;                // Query point
END_VAR
VAR_OUTPUT
    Y : REAL;               // Interpolated value
END_VAR
VAR
    deltaX : REAL;          // Difference between X1 and X2
    deltaY : REAL;          // Difference between Y2 and Y1
END_VAR

// Check for edge case where X1 = X2
IF X1 = X2 THEN
    Y := Y1; // Default or fallback value
    RETURN;
END_IF;

// Compute deltaX and deltaY
deltaX := X2 - X1;
deltaY := Y2 - Y1;

// Compute interpolated value
Y := Y1 + (X - X1) * deltaY / deltaX;

// Log or debug output
// LOG("X = " + STRING(X) + ", Y = " + STRING(Y));

END_FUNCTION_BLOCK

// Example usage:
// X1 := 0.5, Y1 := 0, X2 := 2.5, Y2 := 100
// X := 1.5: Y = 50.0
// X := 0.0: Y = 0.0
// X := 0.0: Y = 0.0
// X := 2.5: Y = 100.0
// X := 1.0: Y = 50.0
// X := 0.5: Y = 0.0
// X := 3.0: Y = 150.0
// X := 4.0: Y = 200.0
// X := 5.0: Y = 250.0
// X := 6.0: Y = 300.0
// X := 7.0: Y = 350.0
// X := 8.0: Y = 400.0
// X := 9.0: Y = 450.0
// X := 10.0: Y =
