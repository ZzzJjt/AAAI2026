### Intent:
**Intent Summary:**  
Create a Structured Text function block implementing the Simplex algorithm for linear programming in PLCs to enable on-device optimization of industrial processes (e.g., resource allocation, batch blending) with constraints on memory, execution time, and numerical precision.

### Prompt:
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a self-contained function block in IEC 61131-3 Structured Text that can solve a linear programming problem using the Simplex method, suitable for deployment in industrial PLC environments.

⸻

🟩 A (Action) – How to Do It
	1.	Create a function block named SimplexSolver with the following inputs:
	•	C: Objective function coefficients (ARRAY[1..N] OF REAL)
	•	A: Constraint matrix (ARRAY[1..M, 1..N] OF REAL)
	•	B: Right-hand side values (ARRAY[1..M] OF REAL)
	2.	Implement the Simplex algorithm, including:
	•	Initialization of the simplex tableau
	•	Pivot column and row selection logic
	•	Row operations and tableau updates
	•	Termination criteria for optimality or maximum iterations
	3.	Output the results:
	•	Optimal solution vector X: ARRAY[1..N] OF REAL
	•	Optimized objective value
	•	Status flag (e.g., success, infeasible, timeout)
	4.	Add clear inline comments for each algorithm step to explain:
	•	Mathematical logic
	•	Handling of infeasible solutions and potential rounding issues
	•	Performance and memory considerations for real-time PLC execution
	5.	Discuss limitations and design choices, such as:
	•	Fixed matrix sizes for memory safety
	•	Execution time constraints on PLCs
	•	Floating-point accuracy concerns

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, efficient, and well-documented function block that enables PLCs to perform on-device optimization using linear programming. This allows for:
	•	Autonomous decision-making in production systems
	•	Optimization of resource allocation, batch blending, or energy usage
	•	Integration of optimization logic directly into real-time control loops without relying on external systems

### Generated Code:
**Intent Summary:**  
Create a Structured Text function block implementing the Simplex algorithm for linear programming in PLCs to enable on-device optimization of industrial processes (e.g., resource allocation, batch blending) with constraints on memory, execution time, and numerical precision.
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a self-contained function block in IEC 61131-3 Structured Text that can solve a linear programming problem using the Simplex method, suitable for deployment in industrial PLC environments.

⸻

🟩 A (Action) – How to Do It
	1.	Create a function block named SimplexSolver with the following inputs:
	•	C: Objective function coefficients (ARRAY[1..N] OF REAL)
	•	A: Constraint matrix (ARRAY[1..M, 1..N] OF REAL)
	•	B: Right-hand side values (ARRAY[1..M] OF REAL)
	2.	Implement the Simplex algorithm, including:
	•	Initialization of the simplex tableau
	•	Pivot column and row selection logic
	•	Row operations and tableau updates
	•	Termination criteria for optimality or maximum iterations
	3.	Output the results:
	•	Optimal solution vector X: ARRAY[1..N] OF REAL
	•	Optimized objective value
	•	Status flag (e.g., success, infeasible, timeout)
	4.	Add clear inline comments for each algorithm step to explain:
	•	Mathematical logic
	•	Handling of infeasible solutions and potential rounding issues
	•	Performance and memory considerations for real-time PLC execution
	5.	Discuss limitations and design choices, such as:
	•	Fixed matrix sizes for memory safety
	•	Execution time constraints on PLCs
	•	Floating-point accuracy concerns

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, efficient, and well-documented function block that enables PLCs to perform on-device optimization using linear programming. This allows for:
	•	Autonomous decision-making in production systems
	•	Optimization of resource allocation, batch blending, or energy usage
	•	Integration of optimization logic directly into real-time control loops without relying on external systems

This function block should be modular, reusable, and adaptable to a wide range of industrial optimization scenarios within PLC constraints.
FUNCTION_BLOCK FB_LinearProgramming
VAR_INPUT
    C : ARRAY[1..N] OF REAL; // Objective function coefficients
    A : ARRAY[1..M, 1..N] OF REAL; // Constraint matrix
    B : ARRAY[1..M] OF REAL; // Right-hand side values
END_VAR

VAR_OUTPUT
    X : ARRAY[1..N] OF REAL; // Optimal solution vector
    F : REAL; // Optimized objective value
    Status : BOOL; // TRUE if solution found, FALSE if infeasible or timeout
END_VAR

VAR
    // Simplex tableau
    Tableau : ARRAY[1..M, 1..N + 1] OF REAL;

    // Pivot information
    PivotRow : INT;
    PivotCol : INT;
    MaxIterations : INT := 100; // Maximum number of iterations
    Timeout : TON;
    TimeoutTime : T#100ms;

    // Temporary variables
    Temp : REAL;
    MaxRatio : REAL;
    Ratio : REAL;
    TempRow : INT;
    TempCol : INT;
    TempX : REAL;
    TempF : REAL;

    // Error handling
    Error : BOOL;
    ErrorMessage : STRING(255);
END_VAR

// Initialize outputs
Status := FALSE;
F := 0.0;
Error := FALSE;
ErrorMessage := '';

// Initialize Simplex tableau
// Rows correspond to constraints, columns correspond to variables
// First row is objective function, remaining rows are constraints
// First column is constant term, remaining columns are coefficients

// Initialize with all zeros
FOR i := 1 TO M DO
    FOR j := 1 TO N + 1 DO
        Tableau[i, j] := 0.0;
    END_FOR;
END_FOR;

// Set objective function in first row
FOR i := 1 TO N DO
    Temp :=
