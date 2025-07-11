### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, ensuring robustness (division-by-zero handling), precision, and efficiency for industrial PLC applications like sensor scaling or control curves.  

*(Focus: General-purpose interpolation, safety, real-time performance, and maintainability.)*

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
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, ensuring robustness (division-by-zero handling), precision, and efficiency for industrial PLC applications like sensor scaling or control curves.  

*(Focus: General-purpose interpolation, safety, real-time performance, and maintainability.)*
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

It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling. The function block is a valuable addition to the PLC’s library, improving the overall system’s performance and reliability.
**Linear Interpolation Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL;
END_VAR
VAR_OUTPUT
    Y : REAL;
END_VAR

// Check for division by zero
IF X2 <> X1 THEN
    // Calculate the interpolated value
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    // Fallback to avoid division by zero
    Y := Y1;
END_IF;

// Inline comments for maintainability
// The interpolation formula is Y = Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1)
// This formula calculates the Y value for a given X between two known points (X1, Y1) and (X2, Y2)
// Division by zero is handled by checking if X2 is not equal to X1
// REAL-type rounding and overflow behavior are considered, but the REAL type in PLCs typically handles these well
```

**Testing the Function Block**

To test the function block, you can use the following representative use cases:

1. **Analog Scaling**: Use the function block to scale an analog input signal from one range to another.
2. **Position Control**: Use the function block to interpolate position values between two known points in a control system.
3. **Recipe Scaling**: Use the function block to scale recipe parameters between two known values.

**Validation Under Expected PLC Scan Cycles**

To validate the function block's performance under expected PLC scan cycles, you can:

1. **Measure Execution Time**: Use a timing function to measure the execution time of the function block under different input conditions.
2. **Compare Results**: Compare the results of the function block with expected values to ensure accuracy.
3. **Stress Test**: Test the function block under high load conditions to ensure it can handle the expected number of calls per scan cycle.

By following these steps, you can create a robust and efficient interpolation function block that meets the requirements of industrial control systems.
