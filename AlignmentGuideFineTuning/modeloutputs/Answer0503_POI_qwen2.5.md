### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, ensuring safety (e.g., division-by-zero handling), precision, and efficiency for industrial PLC applications.  

*(Focus: General-purpose interpolation, robustness, and real-time performance in control systems.)*

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
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, ensuring safety (e.g., division-by-zero handling), precision, and efficiency for industrial PLC applications.  

*(Focus: General-purpose interpolation, robustness, and real-time performance in control systems.)*
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

It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling. The function block is a valuable addition to the automation engineer's toolkit, promoting code reuse and reducing development time.
**Linear Interpolation Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL;
END_VAR
VAR_OUTPUT
    Y : REAL;
END_VAR

// Interpolation formula: Y = Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1)
// This formula calculates the interpolated value Y for a given X between two known points (X1, Y1) and (X2, Y2).

// Check for division by zero to prevent runtime errors
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Fallback to avoid division by zero
END_IF;

// Considerations for REAL-type rounding and overflow behavior:
// - The REAL type in PLCs typically has a limited precision, which can lead to rounding errors.
// - To minimize these errors, ensure that the inputs are within the representable range of the REAL type.
// - For critical applications, consider using fixed-point arithmetic or higher-precision data types if available.

// Test the function block using representative use cases:
// - Analog scaling: Use the function block to convert sensor readings to a desired scale.
// - Position control: Apply the function block to interpolate positions between two points in a control system.
// - Recipe scaling: Use the function block to scale recipe parameters based on input conditions.

// The function block is designed to be reusable and easy to maintain, promoting code reuse and reducing development time.
// It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling.
// The function block is a valuable addition to the automation engineer's toolkit, promoting code reuse and reducing development time.
END_FUNCTION_BLOCK
```

This function block provides a robust and efficient solution for linear interpolation in real-time industrial control systems. It includes error handling to prevent division by zero and addresses precision concerns by using the REAL type. The function block is designed to be reusable and easy to maintain, promoting code reuse and reducing development time. It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling. The function block is a valuable
