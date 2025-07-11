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
	•	Any potential limitations or assumptions made in the function block design

⸻

🟩 T (Task) – What You Need to Do

1. **Implement the LinearInterpolation function block:**
	•	Create a new function block in your preferred IEC 61131-3 Structured Text development environment.
	•	Define the following five REAL inputs:
		- X1, Y1: First reference point
		- X2, Y2: Second reference point
		- X: The target input value
	•	Define a REAL output named Y, which will hold the interpolated output value.
	•	Implement the interpolation logic using the provided formula, ensuring that division by zero is prevented if X1 = X2.
	•	Include inline comments to explain each computation step and the mathematical rationale behind the formula.
2. **Address precision and rounding concerns:**
	•	Consider the inherent limitations of REAL types on PLCs, which may introduce rounding errors.
	•	Investigate any potential issues related to precision and rounding, and discuss how they might impact the function block's performance in real-time control systems.
	•	Provide suggestions for mitigating these issues, such as using fixed-point arithmetic or implementing a custom rounding algorithm.
3. **Ensure suitability for real-time control systems:**
	•	Consider the function block's execution time and its impact on the overall system's responsiveness.
	•	Ensure that the function block is deterministic, meaning its execution time is predictable and consistent across different inputs.
	•	Investigate any potential limitations or assumptions made in the function block design that could affect its suitability for real-time control systems.
4. **Provide a brief summary:**
	•	Provide a brief summary of the function block's use cases, such as analog signal scaling, lookup tables, or PID feedforward inputs.
	•	Include a brief discussion of the function block's execution time, numerical stability, and portability across different PLC platforms (e.g., CODESYS, TwinCAT, TIA Portal).
	•	Highlight any potential limitations or assumptions made in the function block design that could impact its performance or compatibility with specific platforms.

**Deliverables:**

1. **Function Block:** A fully implemented IEC 61131-3 Structured Text function block with clear input/output declarations, interpolation logic, and inline comments.
2. **Precision and Rounding Considerations
