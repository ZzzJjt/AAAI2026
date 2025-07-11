### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for linear interpolation between two points, with safeguards against division by zero, clear documentation, and considerations for real-time industrial control precision and performance.  

*(Key focus: General-purpose interpolation, robustness, and real-time suitability.)*

### Prompt:
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation systems developer tasked with creating a general-purpose linear interpolation function block using IEC 61131-3 Structured Text for use in real-time industrial control applications.

⸻

🟩 T (Task) – What You Need to Do

Develop a function block named LinearInterpolation that:
	•	Accepts five REAL inputs:
	•	X1, Y1: First reference point
	•	X2, Y2: Second reference point
	•	X: The target input value
	•	Computes Y, the interpolated output value, using the formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes logic to prevent division by zero if X1 = X2
	•	Provides inline comments to explain each computation step, including mathematical rationale
	•	Addresses precision and rounding concerns inherent to REAL types on PLCs
	•	Is suitable for integration into real-time control systems, ensuring deterministic execution

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A fully implemented IEC 61131-3 Structured Text function block with clear input/output declarations
	•	The interpolation logic wrapped in safe conditionals:

 IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback behavior
END_IF;
	•	Well-documented code with comments explaining how interpolation is computed and why safeguards are in place
	•	A brief summary of:
	•	Use cases (e.g., analog signal scaling, lookup tables, PID feedforward inputs)
	•	Considerations for execution time, numerical stability, and portability across platforms like CODESYS, TwinCAT, and TIA Portal

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for linear interpolation between two points, with safeguards against division by zero, clear documentation, and considerations for real-time industrial control precision and performance.  

*(Key focus: General-purpose interpolation, robustness, and real-time suitability.)*
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation systems developer tasked with creating a general-purpose linear interpolation function block using IEC 61131-3 Structured Text for use in real-time industrial control applications.

⸻

🟩 T (Task) – What You Need to Do

Develop a function block named LinearInterpolation that:
	•	Accepts five REAL inputs:
	•	X1, Y1: First reference point
	•	X2, Y2: Second reference point
	•	X: The target input value
	•	Computes Y, the interpolated output value, using the formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes logic to prevent division by zero if X1 = X2
	•	Provides inline comments to explain each computation step, including mathematical rationale
	•	Addresses precision and rounding concerns inherent to REAL types on PLCs
	•	Is suitable for integration into real-time control systems, ensuring deterministic execution

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A fully implemented IEC 61131-3 Structured Text function block with clear input/output declarations
	•	The interpolation logic wrapped in safe conditionals:

 IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback behavior
END_IF;
	•	Well-documented code with comments explaining how interpolation is computed and why safeguards are in place
	•	A brief summary of:
	•	Use cases (e.g., analog signal scaling, lookup tables, PID feedforward inputs)
	•	Considerations for execution time, numerical stability, and portability across platforms like CODESYS, TwinCAT, and TIA Portal
	•	Any additional insights or best practices for implementing linear interpolation in industrial control systems

⸻

**Note:** The function block should be designed with the understanding that it will be used in a real-time environment, where deterministic execution and minimal latency are crucial. The code should be optimized for performance and robustness, with a focus on minimizing the risk of numerical instability or overflow errors. The function block should be versatile enough to be used in various applications, such as scaling analog signals, interpolating values from lookup tables, or providing feedforward inputs to PID controllers. The code should also be well-documented, with comments explaining the mathematical rationale behind the interpolation process and the safeguards implemented to prevent division by zero. Finally, the function block should be tested thoroughly to ensure that it meets the requirements for precision, performance, and real-time suitability.
**Linear Interpolation Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1 : REAL; // First reference point X-coordinate
    Y1 : REAL; // First reference point Y-coordinate
    X2 : REAL; // Second reference point X-coordinate
    Y2 : REAL; // Second reference point Y-coordinate
    X : REAL; // Target input value
END_VAR

VAR_OUTPUT
    Y : REAL; // Interpolated output value
END_VAR

VAR
    deltaX : REAL; // Difference between X2 and X1
    deltaY : REAL; // Difference between Y2 and Y1
    slope : REAL; // Slope of the line between the two points
END_VAR

// Compute the slope of the line between the two points
slope := (Y2 - Y1) / (X2 - X1);

// Check for division by zero
IF X2 = X1 THEN
    Y := Y1; // Default or fallback behavior
ELSE
    // Compute the interpolated output value
    Y := Y1 + (X - X1) * slope;
END_IF;

// Ensure Y is within the range of Y1 and Y2
IF Y < Y1 THEN
    Y := Y1;
ELSEIF Y > Y2 THEN
    Y := Y2;
END_IF;
END_FUNCTION_BLOCK
```

**Function Block Description:**

The `LinearInterpolation` function block is designed to compute the linear interpolation between two points `(X1, Y1)` and `(X2, Y2)` for a given
