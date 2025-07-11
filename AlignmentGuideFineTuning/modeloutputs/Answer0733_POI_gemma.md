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
	•	Potential improvements or extensions to the function block (e.g., support for higher-order interpolation, dynamic range scaling)

**Deliverables:**

Your deliverable should include:
	•	A fully implemented IEC 61131-3 Structured Text function block with clear input/output declarations
	•	The interpolation logic wrapped in safe conditionals
	•	Well-documented code with comments explaining how interpolation is computed and why safeguards are in place
	•	A brief summary of:
	•	Use cases
	•	Considerations for execution time, numerical stability, and portability across platforms
	•	Potential improvements or extensions to the function block

**Evaluation Criteria:**

Your deliverable will be evaluated based on the following criteria:
	•	Correctness: The function block should compute linear interpolation between two points using the specified formula and safeguard against division by zero
	•	Precision: The function block should address precision and rounding concerns inherent to REAL types on PLCs
	•	Real-time suitability: The function block should be suitable for integration into real-time control systems, ensuring deterministic execution
	•	Documentation: The function block should be well-documented with comments explaining how interpolation is computed and why safeguards are in place
	•	Use cases: The function block should be suitable for a range of use cases, such as analog signal scaling, lookup tables, and PID feedforward inputs
	•	Considerations: The function block should address considerations for execution time, numerical stability, and portability across platforms
	•	Improvements: The function block should be extensible and open to potential improvements or extensions

**Resources:**

The following resources may be helpful in completing this task:
	•	IEC 61131-3 standard for programming industrial control systems
	•	Online documentation for the IEC 61131-3 Structured Text language
	•	Tutorials and examples for implementing linear interpolation in IEC 61131-3 Structured Text
	•	Information on precision and rounding concerns for REAL types on PLCs
	•	Documentation for real-time control systems and their requirements for deterministic execution
	•	Information on use cases for linear interpolation in industrial control systems
	•	Information on considerations for execution time, numerical stability, and portability across platforms

**Deliverables:**

Your deliverable should include:
	•	A fully implemented IEC 61131-3 Structured
