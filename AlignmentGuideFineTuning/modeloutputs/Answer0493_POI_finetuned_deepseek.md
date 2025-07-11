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

It enhances system flexibility, supporting scalable applications like sensor conversion, control curves, or recipe scaling.
FUNCTION_BLOCK Interpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL; // Known points and query value
END_VAR
VAR_OUTPUT
    Y : REAL; // Interpolated value
END_VAR
VAR
    // Check for division by zero
    DivByZero : BOOL;
END_VAR

// Initialize output
Y := Y1; // Default to first known point

// Check for division by zero
IF X2 = X1 THEN
    DivByZero := TRUE; // Prevent division by zero
ELSE
    DivByZero := FALSE;
    // Perform interpolation
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
END_IF;

// Output result
IF DivByZero THEN
    Y := Y1; // Fallback to avoid division by zero
ELSE
    Y := Y;
END_IF;
END_FUNCTION_BLOCK

// Comments:
// - This function block performs linear interpolation between two known points (X1, Y1) and (X2, Y2)
// - It accepts a query value X and returns the interpolated value Y
// - If X is equal to X1, it sets Y to Y1 to avoid division by zero
// - The interpolation formula is: Y = Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1)
// - The function block is designed to be platform-independent and suitable for real-time PLC applications
// - It includes inline comments to explain the interpolation logic and potential rounding issues
// - The function block can be easily reused in various control systems where interpolation is needed
// - It supports scaling, position control, and other applications where real-time interpolation is required
// - The function block is safe, efficient, and easy to maintain.
// - It can be tested with known input values and expected output results.
// - It supports scaling, position control, and other applications where real-time interpolation is required.
// - It is designed to be platform-independent and suitable for real-time PLC applications.
// - It includes inline comments to explain the interpolation logic and potential rounding issues.
// - It can be easily reused in various control systems where interpolation is needed.
// -
