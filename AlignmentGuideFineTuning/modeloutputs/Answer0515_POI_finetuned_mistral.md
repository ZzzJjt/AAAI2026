### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block (`MatrixMultiply4x4`) to multiply two 4x4 matrices in Structured Text, with clear comments, O(n³) complexity analysis, and scalability considerations for PLC constraints.  

*(Focus: Modular implementation for real-time control tasks like robotics/motion planning.)*

### Prompt:
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control engineer responsible for implementing mathematical computation blocks in IEC 61131-3 Structured Text, with a focus on supporting real-time matrix operations for control and automation tasks.

⸻

🟩 I (Input) – What You’re Given

You need to build a function block named MatrixMultiply4x4 that:
	•	Accepts two 4×4 matrices of type ARRAY[1..4, 1..4] OF REAL as inputs: MatrixA and MatrixB
	•	Returns a resulting 4×4 matrix, MatrixC, representing the matrix product
	•	Follows IEC 61131-3 Structured Text syntax and best practices
	•	Includes detailed inline comments explaining each stage of the algorithm
	•	Handles loop-based computation efficiently within PLC memory and scan-time constraints
	•	Should also discuss computational complexity and limitations of scaling to larger matrices

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface with input/output variables:
 FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA, MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR
2.	Implement the matrix multiplication logic using three nested FOR loops:
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;
	3.	Add inline comments to explain:
	•	Row/column traversal logic
	•	Accumulation of products for each matrix element
	•	The use of fixed array indexing to ensure execution time predictability
	4.	Document performance considerations:
	•	Computational complexity is O(n³), which may not scale well on PLCs
	•	Larger matrix support may require memory checks, iteration limits, or segmentation
	•	Best suited for use cases like transformation matrices or motion control with fixed-size data

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, reusable, and well-commented function block that:
	•	Accurately computes the product of two 4×4 matrices
	•	Runs efficiently within PLC scan time limits
	•	Is suitable for coordinate transformations, robotics, or motion planning
	•	Can be extended to other matrix operations or adapted to support fixed NxN configurations
	•	Is easy to understand and maintain by other developers working within IEC 61131-3 environments

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block (`MatrixMultiply4x4`) to multiply two 4x4 matrices in Structured Text, with clear comments, O(n³) complexity analysis, and scalability considerations for PLC constraints.  

*(Focus: Modular implementation for real-time control tasks like robotics/motion planning.)*
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control engineer responsible for implementing mathematical computation blocks in IEC 61131-3 Structured Text, with a focus on supporting real-time matrix operations for control and automation tasks.

⸻

🟩 I (Input) – What You’re Given

You need to build a function block named MatrixMultiply4x4 that:
	•	Accepts two 4×4 matrices of type ARRAY[1..4, 1..4] OF REAL as inputs: MatrixA and MatrixB
	•	Returns a resulting 4×4 matrix, MatrixC, representing the matrix product
	•	Follows IEC 61131-3 Structured Text syntax and best practices
	•	Includes detailed inline comments explaining each stage of the algorithm
	•	Handles loop-based computation efficiently within PLC memory and scan-time constraints
	•	Should also discuss computational complexity and limitations of scaling to larger matrices

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface with input/output variables:
 FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA, MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR
2.	Implement the matrix multiplication logic using three nested FOR loops:
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;
	3.	Add inline comments to explain:
	•	Row/column traversal logic
	•	Accumulation of products for each matrix element
	•	The use of fixed array indexing to ensure execution time predictability
	4.	Document performance considerations:
	•	Computational complexity is O(n³), which may not scale well on PLCs
	•	Larger matrix support may require memory checks, iteration limits, or segmentation
	•	Best suited for use cases like transformation matrices or motion control with fixed-size data

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, reusable, and well-commented function block that:
	•	Accurately computes the product of two 4×4 matrices
	•	Runs efficiently within PLC scan time limits
	•	Is suitable for coordinate transformations, robotics, or motion planning
	•	Can be extended to other matrix operations or adapted to support fixed NxN configurations
	•	Is easy to understand and maintain by other developers working within IEC 61131-3 environments
FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA : ARRAY[1..4, 1..4] OF REAL; // Input matrix A
    MatrixB : ARRAY[1..4, 1..4] OF REAL; // Input matrix B
END_VAR

VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL; // Output matrix C, result of A * B
END_VAR

VAR
    i, j, k : INT; // Loop indices
END_VAR

// Initialize MatrixC to zero
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0.0;
    END_FOR;
END_FOR;

// Perform matrix multiplication
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0.0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;

// Return the result matrix C
RETURN;
END_FUNCTION_BLOCK

(*
Summary:
Implements a function block to multiply two 4x4 matrices using IEC 61131-3 Structured Text.

Detailed Description:
This function block performs matrix multiplication between two 4x4 matrices, A and B, and returns the resulting 4x4 matrix, C. The implementation uses three nested FOR loops to iterate through the matrices, with one loop for the outermost row index, one for the middle column index, and one for the inner element index. The algorithm follows the standard matrix multiplication formula:

C[i,j] = Σ[k=1 to 4] A[i,k] * B[k,j]

Each element of the output matrix C is calculated by summing the products of corresponding elements from A and B. The function block is designed to be modular, reusable, and efficient within PLC scan-time constraints. It includes
