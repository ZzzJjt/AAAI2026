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
FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Expected number of events
    K : INT;        // Number of observed events
END_VAR

VAR_OUTPUT
    Probability : REAL; // Computed Poisson probability
END_VAR

METHOD Execute : BOOL
BEGIN
    // Initialize output
    Probability := 0.0;

    // Check for valid inputs
    IF Lambda < 0.0 OR K < 0 THEN
        // Invalid input, return 0
        Probability := 0.0;
        RETURN TRUE;
    END_IF;

    // Compute Poisson probability using formula: P(k; λ) = (e^(-λ) * λ^k) / k!
    Probability := EXP(-Lambda) * POW(Lambda, K) / FACTORIAL(K);

    // Return success
    RETURN TRUE;
END_METHOD

// Helper function for factorial calculation
FUNCTION FACTORIAL : INT
VAR_INPUT
    N : INT; // Input number
END_VAR
VAR
    i : INT;
    Result : INT;
BEGIN
    Result := 1;

    FOR i := 2 TO N DO
        Result := Result * i;
    END_FOR;

    RETURN Result;
END_FUNCTION

// Main program entry point
Execute();
```

This implementation provides a reusable function block that computes the Poisson probability distribution for a given expected number of events (Lambda) and observed number of events (K). It includes a detailed method (Execute) for execution, input validation, and a helper function (FACTORIAL) for calculating factorials. The function block is designed for deterministic execution on PLCs and can be integrated into applications such as event prediction, failure rate estimation, or batch process monitoring.

---

### 📘 IEC 61131-3 Structured Text Reference

#### 📌 Basic Types

- **BOOL**: Boolean values (TRUE, FALSE)
- **INT**: Signed integer values
- **REAL**: Floating-point values
- **STRING**: Fixed-
