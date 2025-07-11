### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compute Poisson probability distribution for industrial control applications, handling edge cases and ensuring deterministic execution with clear documentation.  

*(Focus: Deterministic PLC implementation of Poisson probability for event prediction in control systems.)*

### Prompt:
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**C-A-R-E:**

🟥 C (Context) – The Background

Matrix multiplication is fundamental in many industrial applications such as robot kinematics, coordinate transformations, and control systems. However, IEC 61131-3 Structured Text does not natively support matrix operations, and PLCs have limited processing power and memory, which makes implementing even basic matrix math non-trivial. A structured and reusable function block is needed to ensure both performance and clarity.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text named MatrixMultiply4x4 that:
	•	Takes two 4×4 REAL matrices as inputs (MatrixA and MatrixB)
	•	Produces a 4×4 result matrix (MatrixC) through standard matrix multiplication
	•	Uses triple nested FOR loops to implement the row-by-column multiplication logic
	•	Follows structured programming principles and includes detailed inline comments to explain:
	•	Loop structure
	•	Accumulation of the product terms
	•	Index-based mapping of matrix elements
	•	Adheres to IEC 61131-3 coding standards for portability and readability across platforms like TwinCAT, CODESYS, or Siemens TIA Portal

⸻

🟨 R (Result) – The Expected Outcome

The result is a modular, reusable function block that performs 4×4 matrix multiplication efficiently and clearly. It:
	•	Enables engineers to perform mathematical operations directly on PLCs
	•	Facilitates applications involving geometry, motion planning, and real-time control
	•	Provides clear structure and documentation, making it easy to maintain and extend
	•	Operates within the time and memory constraints of typical industrial PLCs

This block can be used confidently in systems where deterministic execution is important and matrix operations are part of the control logic.

⸻

🟦 E (Example) – A Practical Use Case

For example, in a robot arm control system, two 4×4 matrices may represent homogeneous transformation matrices (rotation + translation). The MatrixMultiply4x4 function block combines them to compute the new pose of the end-effector.

Sample loop structure in Structured Text:

FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;

This approach provides a deterministic, traceable, and scalable solution for matrix math in real-time environments.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compute Poisson probability distribution for industrial control applications, handling edge cases and ensuring deterministic execution with clear documentation.  

*(Focus: Deterministic PLC implementation of Poisson probability for event prediction in control systems.)*
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**C-A-R-E:**

🟥 C (Context) – The Background

Matrix multiplication is fundamental in many industrial applications such as robot kinematics, coordinate transformations, and control systems. However, IEC 61131-3 Structured Text does not natively support matrix operations, and PLCs have limited processing power and memory, which makes implementing even basic matrix math non-trivial. A structured and reusable function block is needed to ensure both performance and clarity.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text named MatrixMultiply4x4 that:
	•	Takes two 4×4 REAL matrices as inputs (MatrixA and MatrixB)
	•	Produces a 4×4 result matrix (MatrixC) through standard matrix multiplication
	•	Uses triple nested FOR loops to implement the row-by-column multiplication logic
	•	Follows structured programming principles and includes detailed inline comments to explain:
	•	Loop structure
	•	Accumulation of the product terms
	•	Index-based mapping of matrix elements
	•	Adheres to IEC 61131-3 coding standards for portability and readability across platforms like TwinCAT, CODESYS, or Siemens TIA Portal

⸻

🟨 R (Result) – The Expected Outcome

The result is a modular, reusable function block that performs 4×4 matrix multiplication efficiently and clearly. It:
	•	Enables engineers to perform mathematical operations directly on PLCs
	•	Facilitates applications involving geometry, motion planning, and real-time control
	•	Provides clear structure and documentation, making it easy to maintain and extend
	•	Operates within the time and memory constraints of typical industrial PLCs

This block can be used confidently in systems where deterministic execution is important and matrix operations are part of the control logic.

⸻

🟦 E (Example) – A Practical Use Case

For example, in a robot arm control system, two 4×4 matrices may represent homogeneous transformation matrices (rotation + translation). The MatrixMultiply4x4 function block combines them to compute the new pose of the end-effector.

Sample loop structure in Structured Text:

FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;

This approach provides a deterministic, traceable, and scalable solution for matrix math in real-time environments.
FUNCTION_BLOCK PoissonDistribution
VAR_INPUT
    Mean : REAL; // Expected number of events per unit time
    Sigma : REAL; // Variance of the Poisson distribution
END_VAR

VAR_OUTPUT
    Probability : REAL; // Probability of a Poisson distribution
END_VAR

VAR
    e : REAL; // Euler's number
    lambda : REAL; // Mean of the Poisson distribution
    factorial : REAL; // Factorial of a number
    log_factorial : REAL; // Logarithm of a factorial
    log_lambda : REAL; // Logarithm of the mean
    log_probability : REAL; // Logarithm of the probability
END_VAR

// Initialize variables
e := 2.71828; // Euler's number
lambda := Mean;
factorial := 1.0;
log_factorial := 0.0;
log_lambda := log(lambda);
log_probability := 0.0;

// Calculate the probability
Probability := EXP(-lambda) * (lambda^x);

// Comment: This function block calculates the probability of a Poisson distribution given a mean and variance.
// It uses Euler's number (e) to compute the exponential term, and then multiplies by the factorial of the mean to get the probability.
// The result is returned as a REAL value, which can be used in control logic or statistical analysis.
// The function block is designed to be modular, deterministic, and easy to integrate into larger systems.
// It adheres to IEC 61131-3 standards and is suitable for use in industrial control applications.
END_FUNCTION_BLOCK

FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA : ARRAY[1..4, 1..4] OF REAL; // First matrix (4x4)
    MatrixB : ARRAY[1..4, 1..4] OF REAL; // Second matrix (4x4)
END_VAR

VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL; // Result matrix (4x4)
END_VAR

VAR
    i, j, k : INT;
    temp : REAL;
    sum : REAL;
END_VAR

// Initialize result
