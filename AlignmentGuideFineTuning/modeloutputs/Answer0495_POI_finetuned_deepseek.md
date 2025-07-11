### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to multiply two 4x4 matrices efficiently, with clear comments and scalability considerations for PLC-based control systems.  

*(Focus: Implementation of real-time matrix operations for automation tasks, emphasizing modularity and performance constraints.)*

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
Create an IEC 61131-3 Structured Text function block to multiply two 4x4 matrices efficiently, with clear comments and scalability considerations for PLC-based control systems.  

*(Focus: Implementation of real-time matrix operations for automation tasks, emphasizing modularity and performance constraints.)*
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
    MatrixA : ARRAY[1..4, 1..4] OF REAL;
    MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR

VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR

VAR
    i, j, k : INT;
    Sum : REAL;
END_VAR

// Outer loop: Matrix rows
FOR i := 1 TO 4 DO
    // Inner loop: Matrix columns
    FOR j := 1 TO 4 DO
        // Accumulate product for each element
        Sum := 0.0;
        FOR k := 1 TO 4 DO
            Sum := Sum + MatrixA[i, k] * MatrixB[k, j];
        END_FOR;
        
        // Store result in MatrixC
        MatrixC[i, j] := Sum;
    END_FOR;
END_FOR;
END_FUNCTION_BLOCK

// Comments:
// - Outer loop iterates over rows of MatrixA
// - Inner loop iterates over columns of MatrixB
// - For each element, sum the corresponding products from MatrixA and MatrixB
// - Accumulated sum is stored in MatrixC
// - Fixed-size indexing ensures predictable execution time
// - Suitable for coordinate transformations, robotics, or motion planning
// - Not recommended for large matrices due to O(n³) complexity
// - May require memory checks, iteration limits, or segmentation for larger matrices
// - Can be extended to support fixed NxN configurations
// - Easy to understand and maintain by other developers working within IEC 61131-3 environments
(* IEC 61131-3 Structured Text: Matrix Multiply 4x4 *)
(* Purpose: Computes the product of two 4x4 matrices *)
(* Input: MatrixA and MatrixB, both 4x4 arrays of REAL *)
(* Output: MatrixC, a 4x4 array of REAL representing the product *)
(* Complexity: O(n³) due to nested loops *)
(* Limitations: Not suitable for large matrices or real-time systems *)

FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
