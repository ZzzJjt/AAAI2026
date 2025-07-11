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
FUNCTION_BLOCK LinearInterpolation
VAR_INPUT
    X1, Y1, X2, Y2, X : REAL; // Inputs
END_VAR

VAR_OUTPUT
    Y : REAL; // Output
END_VAR

VAR
    XDiff : REAL; // X - X1
    YDiff : REAL; // Y2 - Y1
END_VAR

// Prevent division by zero
IF X2 = X1 THEN
    Y := Y1; // Default fallback
ELSE
    XDiff := X - X1;
    YDiff := Y2 - Y1;

    IF XDiff <> 0.0 THEN
        Y := Y1 + XDiff * YDiff / (X2 - X1);
    ELSE
        Y := Y1; // Default fallback
    END_IF;

END_IF;

// Documentation
//
// Linear interpolation is computed using the formula:
// Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
//
// This function block is designed for general use in industrial control systems,
// where real-time responsiveness is critical. It includes safeguards to prevent
// division by zero and ensures deterministic execution.
//
// The interpolation is suitable for use in analog signal scaling, lookup tables,
// PID feedforward inputs, and other applications where a smooth transition is
// required between two known values.
END_FUNCTION_BLOCK
(* IEC 61131-3 Structured Text: Linear Interpolation Function Block *)
(* Purpose: Computes linear interpolation between two points *)
(* Inputs: X1, Y1, X2, Y2, X: REAL values representing two reference points and a target *)
(* Output: Y: REAL value representing the interpolated output *)
(* Notes: 
    - Prevents division by zero if X1 = X2
    - Uses inline comments to explain each computation step
    - Suitable for use in real-time control systems
    - R-T-F:
        - R: PLC programmer or automation systems developer
        - T: Develop a self-contained function block using IEC 61131-3 Structured Text
        - F: Include inline comments, division protection, and real-time suitability
*)

FUNCTION_
