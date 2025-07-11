### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to multiply two 4x4 matrices using structured text, with detailed comments and analysis of computational limitations for industrial control applications like robotics or motion systems.  

*(Focus: Implementation + scalability constraints for PLCs)*

### Prompt:
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer tasked with implementing mathematical operations on industrial controllers using IEC 61131-3 Structured Text. Your goal is to enable efficient matrix computation for use in control logic, robotics, or motion coordination systems.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block named MatrixMultiply4x4 that:
	•	Performs multiplication of two 4×4 matrices
	•	Accepts two inputs:
	•	MatrixA: ARRAY[1..4, 1..4] OF REAL
	•	MatrixB: ARRAY[1..4, 1..4] OF REAL
	•	Returns:
	•	MatrixC: ARRAY[1..4, 1..4] OF REAL, the resulting matrix product
	•	Implements standard matrix multiplication logic using triple nested FOR loops
	•	Includes detailed inline comments explaining each step of the multiplication process, including:
	•	Iteration over rows and columns
	•	Inner loop to compute dot products
	•	Resetting the output element before summing products
	•	Follows IEC 61131-3 structured text conventions for clarity, reusability, and compatibility
	•	Discusses limitations:
	•	Computational complexity: O(n³), not scalable for large matrices on PLCs
	•	Real-time constraints: impact of loop depth on scan cycle time
	•	Memory usage: array-based implementation must be fixed and pre-sized

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A fully implemented IEC 61131-3 function block:

 FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA, MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR
    i, j, k : INT;
END_VAR

FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;
	•	Commented explanation for each block of code
	•	A short note on real-world applications, such as using the block to perform coordinate frame transformations or chaining 3D transformation matrices in robotic arms

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to multiply two 4x4 matrices using structured text, with detailed comments and analysis of computational limitations for industrial control applications like robotics or motion systems.  

*(Focus: Implementation + scalability constraints for PLCs)*
**Matrix Multiplication:**

Develop a self-contained function block in IEC 61131-3 to perform multiplication of two 4x4 matrices. Ensure that the implementation adheres to the standards of structured text programming and includes detailed comments explaining each part of the process. Discuss the computational complexity and potential limitations when scaling this approach to larger matrices.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer tasked with implementing mathematical operations on industrial controllers using IEC 61131-3 Structured Text. Your goal is to enable efficient matrix computation for use in control logic, robotics, or motion coordination systems.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block named MatrixMultiply4x4 that:
	•	Performs multiplication of two 4×4 matrices
	•	Accepts two inputs:
	•	MatrixA: ARRAY[1..4, 1..4] OF REAL
	•	MatrixB: ARRAY[1..4, 1..4] OF REAL
	•	Returns:
	•	MatrixC: ARRAY[1..4, 1..4] OF REAL, the resulting matrix product
	•	Implements standard matrix multiplication logic using triple nested FOR loops
	•	Includes detailed inline comments explaining each step of the multiplication process, including:
	•	Iteration over rows and columns
	•	Inner loop to compute dot products
	•	Resetting the output element before summing products
	•	Follows IEC 61131-3 structured text conventions for clarity, reusability, and compatibility
	•	Discusses limitations:
	•	Computational complexity: O(n³), not scalable for large matrices on PLCs
	•	Real-time constraints: impact of loop depth on scan cycle time
	•	Memory usage: array-based implementation must be fixed and pre-sized

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A fully implemented IEC 61131-3 function block:

 FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA, MatrixB : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL;
END_VAR
VAR
    i, j, k : INT;
END_VAR

FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k] * MatrixB[k,j];
        END_FOR;
    END_FOR;
END_FOR;
	•	Commented explanation for each block of code
	•	A short note on real-world applications, such as using the block to perform coordinate frame transformations or chaining 3D transformation matrices in robotic arms
	•	A brief discussion of alternatives (e.g., using matrix libraries, matrix decompositions, or using external hardware for larger computations)
(* IEC 61131-3 Structured Text Function Block for Matrix Multiplication *)
(* Performs standard 4x4 matrix multiplication using triple nested FOR loops *)
(* Designed for use in industrial control applications such as robotics or motion systems *)
(* Follows IEC 61131-3 standards for clarity, reusability, and real-time compatibility *)
(* Includes detailed inline comments for each step of the multiplication process *)
(* Note: Not optimized for large matrices due to PLC limitations *)

FUNCTION_BLOCK MatrixMultiply4x4
VAR_INPUT
    MatrixA : ARRAY[1..4, 1..4] OF REAL; (* Input matrix A, 4x4 double-precision array *)
    MatrixB : ARRAY[1..4, 1..4] OF REAL; (* Input matrix B, 4x4 double-precision array *)
END_VAR
VAR_OUTPUT
    MatrixC : ARRAY[1..4, 1..4] OF REAL; (* Output matrix C, 4x4 double-precision array *)
END_VAR
VAR
    i, j, k : INT; (* Loop variables for row and column indices *)
END_VAR

(* Reset output matrix to zero *)
FOR i := 1 TO 4 DO
    FOR j := 1 TO 4 DO
        MatrixC[i,j] := 0.0; (* Initialize matrix C to zero *)
    END_FOR;
END_FOR;

(* Perform matrix multiplication using triple nested FOR loops *)
(* Outer loop iterates over rows of MatrixA *)
FOR i := 1 TO 4 DO
    (* Inner loop iterates over columns of MatrixA, computing dot products *)
    FOR j := 1 TO 4 DO
        (* Inner-most loop iterates over rows of MatrixB, summing products *)
        MatrixC[i,j] := 0.0;
        FOR k := 1 TO 4 DO
            MatrixC[i,j] := MatrixC[i,j] + MatrixA[i,k]
