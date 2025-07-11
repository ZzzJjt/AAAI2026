### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compute the sine of an angle (in radians) using either a native `SIN()` function or a Taylor series approximation (7th-order), with documentation on precision, limitations, and real-time PLC optimization.  

*(Focus: Modular sine calculation for industrial motion/signal applications where native support may be lacking.)*

### Prompt:
**Sine Function**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the sine of a given angle in radians. Ensure that the function block is modular and reusable, with appropriate comments detailing the mathematical operations involved. Include a discussion on the precision of the sine function within the context of PLC programming and its potential limitations in real-time applications.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC control engineer or automation programmer developing core trigonometric utilities in IEC 61131-3 Structured Text to support real-time industrial applications such as motion control, signal generation, and waveform analysis.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block named SineFunction that:
	•	Computes the sine of a given angle expressed in radians
	•	Uses the built-in SIN() function if available
	•	Alternatively, approximates sine using a Taylor series expansion up to the 7th power term for environments without native support
	•	Accepts one input:
	•	AngleRad : REAL — the angle in radians
	•	Returns one output:
	•	SineValue : REAL — the computed sine value
	•	Is fully documented with inline comments explaining:
	•	The mathematical basis for the sine function
	•	Why radians (not degrees) are used
	•	The range, convergence characteristics, and error limitations of the Taylor series approximation
	•	Is optimized for real-time execution on PLCs, using no recursion and fixed iteration logic

⸻

🟧 F (Format) – Expected Output

You should produce a readable, efficient, and reusable IEC 61131-3 Structured Text function block like:

FUNCTION_BLOCK SineFunction
VAR_INPUT
    AngleRad : REAL;
END_VAR
VAR_OUTPUT
    SineValue : REAL;
END_VAR
VAR
    x, x2, x3, x5, x7 : REAL;
END_VAR

// Use Taylor Series approximation if SIN() is unavailable
x := AngleRad;
x2 := x * x;
x3 := x2 * x;
x5 := x3 * x2;
x7 := x5 * x2;
SineValue := x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0);

// Note: For large inputs, consider normalizing to -PI..PI

This function block is suitable for real-time control tasks where trigonometric functions are required but platform support is limited. It’s a reliable and maintainable tool for implementing smooth motion curves, phase-based timing, or signal shaping directly within PLC logic.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compute the sine of an angle (in radians) using either a native `SIN()` function or a Taylor series approximation (7th-order), with documentation on precision, limitations, and real-time PLC optimization.  

*(Focus: Modular sine calculation for industrial motion/signal applications where native support may be lacking.)*
**Sine Function**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the sine of a given angle in radians. Ensure that the function block is modular and reusable, with appropriate comments detailing the mathematical operations involved. Include a discussion on the precision of the sine function within the context of PLC programming and its potential limitations in real-time applications.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC control engineer or automation programmer developing core trigonometric utilities in IEC 61131-3 Structured Text to support real-time industrial applications such as motion control, signal generation, and waveform analysis.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block named SineFunction that:
	•	Computes the sine of a given angle expressed in radians
	•	Uses the built-in SIN() function if available
	•	Alternatively, approximates sine using a Taylor series expansion up to the 7th power term for environments without native support
	•	Accepts one input:
	•	AngleRad : REAL — the angle in radians
	•	Returns one output:
	•	SineValue : REAL — the computed sine value
	•	Is fully documented with inline comments explaining:
	•	The mathematical basis for the sine function
	•	Why radians (not degrees) are used
	•	The range, convergence characteristics, and error limitations of the Taylor series approximation
	•	Is optimized for real-time execution on PLCs, using no recursion and fixed iteration logic

⸻

🟧 F (Format) – Expected Output

You should produce a readable, efficient, and reusable IEC 61131-3 Structured Text function block like:

FUNCTION_BLOCK SineFunction
VAR_INPUT
    AngleRad : REAL;
END_VAR
VAR_OUTPUT
    SineValue : REAL;
END_VAR
VAR
    x, x2, x3, x5, x7 : REAL;
END_VAR

// Use Taylor Series approximation if SIN() is unavailable
x := AngleRad;
x2 := x * x;
x3 := x2 * x;
x5 := x3 * x2;
x7 := x5 * x2;
SineValue := x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0);

// Note: For large inputs, consider normalizing to -PI..PI

This function block is suitable for real-time control tasks where trigonometric functions are required but platform support is limited. It’s a reliable and maintainable tool for implementing smooth motion curves, phase-based timing, or signal shaping directly within PLC logic.
(* IEC 61131-3 Structured Text: SineFunction Function Block *)
(* Purpose: Computes the sine of a given angle in radians *)

FUNCTION_BLOCK SineFunction
VAR_INPUT
    AngleRad : REAL; (* Input angle in radians *)
END_VAR
VAR_OUTPUT
    SineValue : REAL; (* Computed sine value *)
END_VAR
VAR
    x, x2, x3, x5, x7 : REAL; (* Intermediate variables for Taylor series *)
    i : INT; (* Loop counter for Taylor series *)
END_VAR

(* Main Execution Logic *)
x := AngleRad;
x2 := x * x;
x3 := x2 * x;
x5 := x3 * x2;
x7 := x5 * x2;
SineValue := x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0);

(* Taylor Series Approximation for Sine *)
(* Uses 7th-order approximation for accuracy and efficiency *)
(* Note: For large inputs, normalize to -PI..PI to avoid overflow *)

(* Example Usage: *)
(* SineFunction.AngleRad := 1.5708; (* PI radians *)
(* Execute function block *)
(* SineValue := SineFunction.SineValue; *)
(* Use SineValue for motion control or signal generation *)

(* Documentation: *)
(* - Uses Taylor series approximation for sine *)
(* - Accurate up to 7th-order *)
(* - Optimized for real-time execution *)
(* - Not suitable for high-precision scientific applications *)
(* - Input angle must be in radians *)
(* - Not guaranteed to converge for extreme values *)
(* - Use with caution in PLC scan cycles *)

(* Example: *)
(* SineFunction.AngleRad := 0.0; (* 0 radians *)
(* SineValue := SineFunction.SineValue; *)
(* Result: SineValue = 0.0 *)

(* Example: *)
(* SineFunction.AngleRad := 3.
