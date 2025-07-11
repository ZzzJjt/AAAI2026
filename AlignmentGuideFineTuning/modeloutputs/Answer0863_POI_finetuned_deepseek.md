### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for linear interpolation between two points, with error handling and real-time suitability for industrial PLC applications like sensor scaling or setpoint adjustments.  

*(Key focus: Reusability, safety, and efficiency in control systems.)*

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
Create a reusable IEC 61131-3 Structured Text function block for linear interpolation between two points, with error handling and real-time suitability for industrial PLC applications like sensor scaling or setpoint adjustments.  

*(Key focus: Reusability, safety, and efficiency in control systems.)*
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
    X : REAL;               // Point to interpolate
END_VAR

VAR_OUTPUT
    Y : REAL;              // Interpolated value
END_VAR

VAR
    XDiff : REAL;           // X - X1
    YDiff : REAL;           // Y2 - Y1
    InterpolatedY : REAL;   // Intermediate result
END_VAR

// Check for division by zero
IF X2 <> X1 THEN
    XDiff := X - X1;
    YDiff := Y2 - Y1;

    // Calculate interpolated value
    InterpolatedY := Y1 + (XDiff * YDiff) / (X2 - X1);
ELSE
    Y := Y1; // Or use fallback logic
END_IF;

// Output interpolated value
Y := InterpolatedY;
END_FUNCTION_BLOCK

// Example usage:
// X1 := 0.0; Y1 := 1.0; X2 := 1.0; Y2 := 2.0;
// X := 0.5; // Interpolate between 0.0 and 1.0
// Y := FB_LinearInterpolation(X1, Y1, X2, Y2, X);
// // Y := 1.5 (interpolated value)
// // Note: This assumes X1 <= X <= X2
// //       and Y1 <= Y2 to avoid overflow
// //       and maintain real-time scan cycle safety
// //       (e.g., 1000 ms scan time)
// //       Also, rounding may occur due to floating-point precision
// //       (e.g., 1.5000000000000001 → 1.5)
// //       Use fixed-point or rounding logic if required
// //       (e.g., ROUND(Y, 2) := 1.50)
// //       Or use fixed-point interpolation if scan time is shorter
// //       (e.g., 10 ms)
// //       (e.g., FB_FixedPointInterpol
