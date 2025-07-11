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

The function block must ensure safe, predictable results and be suitable for deployment in real-time PLC environments. It should be easy to understand and use, with clear documentation and inline comments.

⸻

🟧 S (Success) – How to Measure It

The function block should meet the following criteria:
	1.	Accuracy: The interpolated output Y should be within 0.1% of the expected value for all valid input combinations.
	2.	Efficiency: The function block should complete its calculation within 1 millisecond for all valid input combinations.
	3.	Stability: The function block should handle input values that are outside the range of the known points without causing errors or undefined behavior.
	4.	Usability: The function block should be easy to understand and use, with clear documentation and inline comments that explain the mathematical formula and any potential issues.

**Function Block Design:**

The function block should have the following inputs and outputs:

Inputs:
•	X1, Y1: First known point (REAL)
•	X2, Y2: Second known point (REAL)
•	X: The value at which interpolation should occur (REAL)

Outputs:
•	Y: The interpolated output value (REAL)

The function block should also include the following features:

•	Conditional check to avoid division by zero
•	Inline comments explaining the mathematical formula and any potential issues
•	Considerations for precision and potential rounding errors
•	Function block efficiency and real-time responsiveness

**Function Block Example:**

```ST
FUNCTION_BLOCK LinearInterpolation
    VAR_INPUT
        X1, Y1: REAL;
        X2, Y2: REAL;
        X: REAL;
    END_VAR

    VAR
        Y: REAL;
    END_VAR

    IF X2 <> X1 THEN
        Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
    ELSE
        Y := Y1; // Or use fallback logic
    END_IF;

END_FUNCTION_BLOCK
```

**Function Block Documentation:**

The LinearInterpolation function block performs linear interpolation between two known data points (X1, Y1) and (X2, Y2) at a given value X. The interpolated output Y is calculated using the formula:

Y = Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1)

This formula ensures that the interpolated output is a continuous and smooth function between the two known points. The
