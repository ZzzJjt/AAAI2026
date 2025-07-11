### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling and numerical stability checks, suitable for industrial PLC applications like sensor scaling and dynamic setpoint adjustments.

### Prompt:
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained function block in IEC 61131-3 Structured Text that performs linear interpolation between two known data points.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block named LinearInterpolation with the following REAL inputs:
	•	X1, Y1: First known point
	•	X2, Y2: Second known point
	•	X: The value at which interpolation should occur
	2.	Compute the interpolated output Y using the formula:
Y := Y1 + \frac{(X - X1) \times (Y2 - Y1)}{(X2 - X1)}
Add a conditional check to avoid division by zero:
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Or use fallback logic
END_IF;
3.	Include inline comments that explain each part of the calculation.
	4.	Address floating-point rounding and real-time scan cycle constraints, ensuring the block runs efficiently in control applications.

⸻

🟦 G (Goal) – What You Want to Achieve

Provide a reusable, lightweight, and accurate function block for linear interpolation that supports applications like:
	•	Sensor signal scaling
	•	Analog-to-digital conversion mapping
	•	Dynamic setpoint adjustments

The function block must ensure safe, predictable results and be suitable for deployment in real-time PLC environments.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling and numerical stability checks, suitable for industrial PLC applications like sensor scaling and dynamic setpoint adjustments.
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained function block in IEC 61131-3 Structured Text that performs linear interpolation between two known data points.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block named LinearInterpolation with the following REAL inputs:
	•	X1, Y1: First known point
	•	X2, Y2: Second known point
	•	X: The value at which interpolation should occur
	2.	Compute the interpolated output Y using the formula:
Y := Y1 + \frac{(X - X1) \times (Y2 - Y1)}{(X2 - X1)}
Add a conditional check to avoid division by zero:
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Or use fallback logic
END_IF;
3.	Include inline comments that explain each part of the calculation.
	4.	Address floating-point rounding and real-time scan cycle constraints, ensuring the block runs efficiently in control applications.

⸻

🟦 G (Goal) – What You Want to Achieve

Provide a reusable, lightweight, and accurate function block for linear interpolation that supports applications like:
	•	Sensor signal scaling
	•	Analog-to-digital conversion mapping
	•	Dynamic setpoint adjustments

The function block must ensure safe, predictable results and be suitable for deployment in real-time PLC environments.
FUNCTION_BLOCK FB_LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2 : REAL; // Known points
    X : REAL;               // Interpolation point
END_VAR

VAR_OUTPUT
    Y : REAL;              // Interpolated value
END_VAR

VAR
    XDiff : REAL;           // X2 - X1
    YDiff : REAL;           // Y2 - Y1
    InterpolatedY : REAL;   // Intermediate result
END_VAR

// Check for valid inputs
IF X1 = X2 THEN
    Y := Y1; // No interpolation
    RETURN;
END_IF;

IF Y1 = Y2 THEN
    Y := Y1; // No interpolation
    RETURN;
END_IF;

// Compute XDiff and YDiff
XDiff := X2 - X1;
YDiff := Y2 - Y1;

// Check for division by zero
IF XDiff = 0.0 THEN
    Y := Y1; // Prevent division by zero
    RETURN;
END_IF;

// Perform interpolation
InterpolatedY := Y1 + ((X - X1) * YDiff) / XDiff;

// Round to 2 decimal places
Y := ROUND(InterpolatedY, 2);

END_FUNCTION_BLOCK
// Example usage:
// X1 := 0.0; Y1 := 1.0; X2 := 1.0; Y2 := 2.0; X := 0.5;
// Y := FB_LinearInterpolation(X1, Y1, X2, Y2, X); // Output: 1.5
// This function block can be used in PLC applications like:
// - Sensor scaling
// - Analog-to-digital conversion mapping
// - Dynamic setpoint adjustments
// It ensures safe, predictable results and is suitable for real-time scan cycles.
(* IEC 61131-3 Structured Text: FB_LinearInterpolation *)
(* Purpose: Computes linear interpolation between two known points *)
(* Inputs: X1, Y1, X2, Y2: Known points, X: Interpolation point *)
(* Output: Y: Interpolated value *)

FUNCTION_BLOCK FB_
