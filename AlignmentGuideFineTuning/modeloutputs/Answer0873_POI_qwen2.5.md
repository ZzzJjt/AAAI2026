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

The function block must ensure safe, predictable results and be suitable for deployment in real-time PLC environments. **Linear Interpolation Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK LinearInterpolation
    VAR_INPUT
        X1 : REAL; // First known point X-coordinate
        Y1 : REAL; // First known point Y-coordinate
        X2 : REAL; // Second known point X-coordinate
        Y2 : REAL; // Second known point Y-coordinate
        X : REAL;  // Value at which interpolation should occur
    END_VAR

    VAR_OUTPUT
        Y : REAL;  // Interpolated output Y-coordinate
    END_VAR

    VAR
        slope : REAL; // Slope of the line
        Y_interpolated : REAL; // Interpolated Y value
    END_VAR

    // Check for division by zero
    IF X2 <> X1 THEN
        slope := (Y2 - Y1) / (X2 - X1);
        Y_interpolated := Y1 + slope * (X - X1);
    ELSE
        // Handle vertical line case or use fallback logic
        Y_interpolated := Y1;
    END_IF;

    Y := Y_interpolated;
END_FUNCTION_BLOCK
```

**Explanation:**

1. **Inputs:**
   - `X1`, `Y1`: Coordinates of the first known point.
   - `X2`, `Y2`: Coordinates of the second known point.
   - `X`: The value at which interpolation should occur.

2. **Output:**
   - `Y`: The interpolated output Y-coordinate.

3. **Variables:**
   - `slope`: The slope of the line connecting the two points.
   - `Y_interpolated`: The interpolated Y value.

4. **Calculation:**
   - The function calculates the slope of the line using the formula:
     \[
     \text{slope} = \frac{Y2 - Y1}{X2 - X1}
     \]
   - It then computes the interpolated Y value using the formula:
     \[
     Y_{\text{interpolated}} = Y1 + \text{slope} \times (X - X1)
     \]
   - A conditional check ensures that division by zero is handled gracefully.

5. **Comments:**
   - Inline comments explain each step of the calculation, making the code self-documenting.

6. **Precision and Real-Time Considerations:**
   - The function is designed
