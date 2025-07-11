### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to compute the sine of an angle (in radians) efficiently, either using built-in `SIN()` or a Taylor series approximation, with documentation on precision and real-time constraints for industrial PLC applications.  

*(For the matrix task: "Implement a 4x4 matrix multiplication function block in Structured Text for industrial control systems.")*

### Prompt:
**Sine Function**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the sine of a given angle in radians. Ensure that the function block is modular and reusable, with appropriate comments detailing the mathematical operations involved. Include a discussion on the precision of the sine function within the context of PLC programming and its potential limitations in real-time applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for developing reusable mathematical utilities in IEC 61131-3 Structured Text. Your objective is to implement a real-time-capable trigonometric function block to compute the sine of a given angle, supporting motion control or waveform modeling tasks in industrial systems.

⸻

🟩 I (Input) – What You’re Given

You need to build a function block that:
	•	Accepts an input:
	•	AngleRad : REAL — the input angle in radians
	•	Returns an output:
	•	SineValue : REAL — the calculated sine of the angle
	•	Should work even in systems that do not support built-in SIN()
	•	Must execute efficiently within a PLC scan cycle and handle rounding/precision issues appropriately

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block structure:
 FUNCTION_BLOCK SineFunction
VAR_INPUT
    AngleRad : REAL;
END_VAR
VAR_OUTPUT
    SineValue : REAL;
END_VAR
	2.	Implement the core logic using one of two approaches:
	•	If the platform supports it:
 SineValue := SIN(AngleRad);
 •	If not, use a Taylor series approximation:
 VAR
    x, x2, x3, x5, x7 : REAL;
END_VAR
x := AngleRad;
x2 := x * x;
x3 := x2 * x;
x5 := x3 * x2;
x7 := x5 * x2;
SineValue := x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0);
3.	Add inline comments:
	•	State the formula used and assumptions (e.g., radians, approximation terms)
	•	Note that the series works best near 0 and may require input normalization
	•	Warn of performance/accuracy trade-offs in long-running loops or real-time control
	4.	Optional: Normalize large angles to the range [-π, π] to improve accuracy

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular and reusable function block that:
	•	Computes the sine of a given angle accurately
	•	Can be deployed in real-time applications like:
	•	Oscillatory actuator control
	•	Simulated waveforms
	•	Robot trajectory smoothing
	•	Runs predictably within scan time constraints
	•	Includes clear documentation, making it easy for others to understand, modify, and extend

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to compute the sine of an angle (in radians) efficiently, either using built-in `SIN()` or a Taylor series approximation, with documentation on precision and real-time constraints for industrial PLC applications.  

*(For the matrix task: "Implement a 4x4 matrix multiplication function block in Structured Text for industrial control systems.")*
**Sine Function**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the sine of a given angle in radians. Ensure that the function block is modular and reusable, with appropriate comments detailing the mathematical operations involved. Include a discussion on the precision of the sine function within the context of PLC programming and its potential limitations in real-time applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for developing reusable mathematical utilities in IEC 61131-3 Structured Text. Your objective is to implement a real-time-capable trigonometric function block to compute the sine of a given angle, supporting motion control or waveform modeling tasks in industrial systems.

⸻

🟩 I (Input) – What You’re Given

You need to build a function block that:
	•	Accepts an input:
	•	AngleRad : REAL — the input angle in radians
	•	Returns an output:
	•	SineValue : REAL — the calculated sine of the angle
	•	Should work even in systems that do not support built-in SIN()
	•	Must execute efficiently within a PLC scan cycle and handle rounding/precision issues appropriately

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block structure:
 FUNCTION_BLOCK SineFunction
VAR_INPUT
    AngleRad : REAL;
END_VAR
VAR_OUTPUT
    SineValue : REAL;
END_VAR
	2.	Implement the core logic using one of two approaches:
	•	If the platform supports it:
 SineValue := SIN(AngleRad);
 •	If not, use a Taylor series approximation:
 VAR
    x, x2, x3, x5, x7 : REAL;
END_VAR
x := AngleRad;
x2 := x * x;
x3 := x2 * x;
x5 := x3 * x2;
x7 := x5 * x2;
SineValue := x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0);
3.	Add inline comments:
	•	State the formula used and assumptions (e.g., radians, approximation terms)
	•	Note that the series works best near 0 and may require input normalization
	•	Warn of performance/accuracy trade-offs in long-running loops or real-time control
	4.	Optional: Normalize large angles to the range [-π, π] to improve accuracy

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular and reusable function block that:
	•	Computes the sine of a given angle accurately
	•	Can be deployed in real-time applications like:
	•	Oscillatory actuator control
	•	Simulated waveforms
	•	Robot trajectory smoothing
	•	Runs predictably within scan time constraints
	•	Includes clear documentation, making it easy for others to understand, modify, and extend

**Matrix Multiplication**

Implement a 4x4 matrix multiplication function block in IEC 61131-3 Structured Text for industrial control systems. The function block should accept two 4x4 matrices as inputs and return the product of the two matrices as an output. The function block should be modular and reusable, with appropriate comments detailing the mathematical operations involved.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for developing reusable mathematical utilities in IEC 61131-3 Structured Text. Your objective is to implement a real-time-capable matrix multiplication function block to support advanced control algorithms in industrial systems.

⸻

🟩 I (Input) – What You’re Given

You need to build a function block that:
	•	Accepts two inputs:
	•	MatrixA : ARRAY[1..4, 1..4] OF REAL — the first matrix
	•	MatrixB : ARRAY[1..4, 1..4] OF REAL — the second matrix
	•	Returns an output:
	•	MatrixC : ARRAY[1..4, 1..4] OF REAL — the product of the two matrices
	•	Must execute efficiently within a PLC scan cycle and handle rounding/precision issues appropriately

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block structure:
 FUNCTION_BLOCK MatrixMult
VAR_INPUT
    MatrixA : ARRAY[1..4, 1..4] OF REAL;
    MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR
	2.	Implement the core logic using a nested loop:
 VAR
    i, j, k : INTEGER;
END_VAR
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i, j] := 0.0;
        FOR k := 1 TO 4 DO
            MatrixC[i, j] := MatrixC[i, j] + MatrixA[i, k] * MatrixB[k, j];
        END_FOR
    END_FOR
END_FOR
3.
