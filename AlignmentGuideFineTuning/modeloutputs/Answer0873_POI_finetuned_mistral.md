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
    X1 : REAL; // First known x-value
    Y1 : REAL; // First known y-value
    X2 : REAL; // Second known x-value
    Y2 : REAL; // Second known y-value
    X : REAL;  // Input value for which to interpolate
END_VAR

VAR_OUTPUT
    Y : REAL;  // Interpolated y-value
END_VAR

VAR
    denominator : REAL;
    numerator : REAL;
    validInput : BOOL;
END_VAR

METHOD Execute : VOID
BEGIN
    // Initialize outputs
    Y := 0.0;
    validInput := TRUE;

    // Check for invalid input
    IF X1 = X2 OR Y1 = Y2 OR X1 = X OR Y1 = Y2 THEN
        validInput := FALSE;
        Y := 0.0;
        RETURN;
    END_IF;

    // Perform linear interpolation
    numerator := (X - X1) * (Y2 - Y1);
    denominator := (X2 - X1);
    Y := Y1 + numerator / denominator;
END_METHOD

// Main execution loop
Execute();
```

### Description

This function block performs linear interpolation between two known points (X1, Y1) and (X2, Y2) based on a given input value X. It ensures numerical stability and handles edge cases to prevent division by zero. The function block is designed for use in real-time PLC environments where accurate scaling and mapping of analog signals is required.

### Features

- Linear interpolation between two points
- Numerical stability with conditional checks
- Reusable function block for PLC applications

### Intent

Provide a reliable and efficient function block for interpolating values in real-time control systems, ensuring safe and accurate results.

### Example Usage

```st
// Initialize inputs
X1 := 0.0; Y1 := 0.0;
X2 := 10.0; Y2 := 100.0;
X :=
