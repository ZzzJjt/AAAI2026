### Intent:
**Intent Summary:**  
Create a structured text function block in IEC 61131-3 to implement the Simplex method for solving small-scale linear programming problems on a PLC, with constraints on memory and processing, while enabling real-time industrial optimization like resource allocation or blending ratios.

### Prompt:
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer tasked with implementing an on-device linear programming solver using the Simplex method, optimized for real-time industrial environments through IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You are required to build a function block called SimplexSolver that:
	•	Solves linear programming problems using the Simplex algorithm
	•	Accepts:
	•	An array for the objective function coefficients (e.g., C: ARRAY[1..N] OF REAL)
	•	A constraint matrix (e.g., A: ARRAY[1..M,1..N] OF REAL)
	•	A right-hand side array (B: ARRAY[1..M] OF REAL)
	•	Produces:
	•	An optimal solution vector (X: ARRAY[1..N] OF REAL)
	•	The optimal objective function value
	•	A status flag (e.g., solution found, infeasible, max iterations reached)
	•	Operates under PLC constraints, including fixed memory, bounded loop execution, and limited floating-point precision

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface with arrays sized for typical industrial applications (e.g., max 5 variables, 5 constraints).
	2.	Implement the core Simplex method:
	•	Initialize the Simplex tableau
	•	Identify the pivot column and row
	•	Perform row operations to update the tableau
	•	Repeat until optimality or iteration limit is reached
	3.	Add inline comments to explain:
	•	Mathematical steps (e.g., pivot logic, ratio tests)
	•	Performance considerations (e.g., avoid recursion, use FOR loops)
	•	Error-handling (e.g., division by zero, unbounded solutions)
	4.	Integrate safety and performance limits, including:
	•	Max iteration count
	•	Output flag for infeasibility
	•	Optional watchdog trigger or time-slicing logic

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a modular, reusable function block that allows a PLC to perform basic linear optimization autonomously. The block:
	•	Handles small LP problems in real time
	•	Is documented and structured for clarity and maintainability
	•	Enables optimization tasks such as:
	•	Resource allocation
	•	Load distribution
	•	Blending/mixing ratios
	•	Provides deterministic outputs, supporting control system decision-making without relying on external solvers or cloud connectivity

### Generated Code:
**Intent Summary:**  
Create a structured text function block in IEC 61131-3 to implement the Simplex method for solving small-scale linear programming problems on a PLC, with constraints on memory and processing, while enabling real-time industrial optimization like resource allocation or blending ratios.
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer tasked with implementing an on-device linear programming solver using the Simplex method, optimized for real-time industrial environments through IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You are required to build a function block called SimplexSolver that:
	•	Solves linear programming problems using the Simplex algorithm
	•	Accepts:
	•	An array for the objective function coefficients (e.g., C: ARRAY[1..N] OF REAL)
	•	A constraint matrix (e.g., A: ARRAY[1..M,1..N] OF REAL)
	•	A right-hand side array (B: ARRAY[1..M] OF REAL)
	•	Produces:
	•	An optimal solution vector (X: ARRAY[1..N] OF REAL)
	•	The optimal objective function value
	•	A status flag (e.g., solution found, infeasible, max iterations reached)
	•	Operates under PLC constraints, including fixed memory, bounded loop execution, and limited floating-point precision

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface with arrays sized for typical industrial applications (e.g., max 5 variables, 5 constraints).
	2.	Implement the core Simplex method:
	•	Initialize the Simplex tableau
	•	Identify the pivot column and row
	•	Perform row operations to update the tableau
	•	Repeat until optimality or iteration limit is reached
	3.	Add inline comments to explain:
	•	Mathematical steps (e.g., pivot logic, ratio tests)
	•	Performance considerations (e.g., avoid recursion, use FOR loops)
	•	Error-handling (e.g., division by zero, unbounded solutions)
	4.	Integrate safety and performance limits, including:
	•	Max iteration count
	•	Output flag for infeasibility
	•	Optional watchdog trigger or time-slicing logic

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a modular, reusable function block that allows a PLC to perform basic linear optimization autonomously. The block:
	•	Handles small LP problems in real time
	•	Is documented and structured for clarity and maintainability
	•	Enables optimization tasks such as:
	•	Resource allocation
	•	Load distribution
	•	Blending/mixing ratios
	•	Provides deterministic outputs, supporting control system decision-making without relying on external solvers or cloud connectivity
FUNCTION_BLOCK SimplexSolver
VAR_INPUT
    C : ARRAY[1..N] OF REAL; // Objective function coefficients
    A : ARRAY[1..M, 1..N] OF REAL; // Constraint matrix
    B : ARRAY[1..M] OF REAL; // Right-hand side
END_VAR

VAR_OUTPUT
    X : ARRAY[1..N] OF REAL; // Optimal solution
    ObjectiveValue : REAL; // Objective function value
    Solved : BOOL; // TRUE if solution found
    Infeasible : BOOL; // TRUE if solution is infeasible
    MaxIterationsReached : BOOL; // TRUE if max iterations reached
END_VAR

VAR
    i : INT;
    j : INT;
    k : INT;
    pivotRow : INT;
    pivotCol : INT;
    pivotValue : REAL;
    temp : REAL;
    tempX : ARRAY[1..N] OF REAL;
    tempB : ARRAY[1..M] OF REAL;
    tempA : ARRAY[1..M, 1..N] OF REAL;
END_VAR

// Initialize Simplex Tableau
FOR i := 1 TO N DO
    X[i] := 0.0;
END_FOR;
ObjectiveValue := 0.0;
Solved := FALSE;
Infeasible := FALSE;
MaxIterationsReached := FALSE;

// Step 1: Initialize Simplex Tableau
FOR i := 1 TO N DO
    tempX[i] := C[i];
END_FOR;
ObjectiveValue := SUM(tempX);

FOR i := 1 TO N DO
    X[i] := 0.0;
END_FOR;

FOR i := 1 TO M DO
    tempB[i] := B[i];
END_FOR;

FOR i := 1 TO M DO
    FOR j := 1 TO N DO
        tempA[i, j] := A[i, j];
    END_FOR;
END_FOR;

// Step 2: Identify Pivot Row
FOR i := 1 TO N DO
    IF ABS(tempX[i]) > 1.0E-6 THEN
        pivotRow := i;
        EX
