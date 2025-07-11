### Intent:
**Intent Summary:**  
Develop a Structured Text function block (`SimplexSolver`) implementing the Simplex algorithm for linear programming on PLCs, handling constraints and objective functions with detailed comments, while addressing PLC-specific limitations like memory, precision, and real-time execution for industrial optimization tasks (e.g., energy or material blending).  

*(Focus: PLC-optimized LP solver with robustness for embedded constraints.)*

### Prompt:
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC developer or control engineer responsible for implementing an optimization algorithm on a programmable logic controller using IEC 61131-3 Structured Text, with the goal of solving linear programming problems directly on industrial hardware.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained function block named SimplexSolver that:
	•	Implements the Simplex algorithm to solve linear programming problems
	•	Accepts as inputs:
	•	An objective function coefficient array: C: ARRAY[1..N] OF REAL
	•	A constraint matrix: A: ARRAY[1..M,1..N] OF REAL
	•	A right-hand side array: B: ARRAY[1..M] OF REAL
	•	Returns:
	•	An optimal solution: X: ARRAY[1..N] OF REAL
	•	The value of the optimized objective function
	•	A Status output (e.g., Optimal, Infeasible, Max Iterations Reached)
	•	Includes detailed comments for each step in the algorithm:
	•	Tableau setup
	•	Pivot column and row selection
	•	Row operations and update rules
	•	Is optimized for PLC constraints, including:
	•	Bounded array sizes (e.g., max 5x5)
	•	Limited floating-point accuracy
	•	Real-time scan-time execution

You should also discuss limitations such as:
	•	Execution time in large or complex LP problems
	•	Numerical precision and convergence
	•	Scalability in embedded systems

⸻

🟧 F (Format) – Expected Output

Your submission should include:
	•	A fully implemented Structured Text code block for the SimplexSolver function block
	•	Well-defined input and output parameters
	•	Inline comments that clearly describe:
	•	Each mathematical transformation in the Simplex method
	•	How edge cases like infeasibility or unboundedness are handled
	•	A short explanatory section outlining:
	•	Use cases, such as energy optimization, scheduling, material blending
	•	Considerations for platform-specific deployment (e.g., on Codesys, TIA Portal, TwinCAT)

### Generated Code:
**Intent Summary:**  
Develop a Structured Text function block (`SimplexSolver`) implementing the Simplex algorithm for linear programming on PLCs, handling constraints and objective functions with detailed comments, while addressing PLC-specific limitations like memory, precision, and real-time execution for industrial optimization tasks (e.g., energy or material blending).  

*(Focus: PLC-optimized LP solver with robustness for embedded constraints.)*
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC developer or control engineer responsible for implementing an optimization algorithm on a programmable logic controller using IEC 61131-3 Structured Text, with the goal of solving linear programming problems directly on industrial hardware.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained function block named SimplexSolver that:
	•	Implements the Simplex algorithm to solve linear programming problems
	•	Accepts as inputs:
	•	An objective function coefficient array: C: ARRAY[1..N] OF REAL
	•	A constraint matrix: A: ARRAY[1..M,1..N] OF REAL
	•	A right-hand side array: B: ARRAY[1..M] OF REAL
	•	Returns:
	•	An optimal solution: X: ARRAY[1..N] OF REAL
	•	The value of the optimized objective function
	•	A Status output (e.g., Optimal, Infeasible, Max Iterations Reached)
	•	Includes detailed comments for each step in the algorithm:
	•	Tableau setup
	•	Pivot column and row selection
	•	Row operations and update rules
	•	Is optimized for PLC constraints, including:
	•	Bounded array sizes (e.g., max 5x5)
	•	Limited floating-point accuracy
	•	Real-time scan-time execution

You should also discuss limitations such as:
	•	Execution time in large or complex LP problems
	•	Numerical precision and convergence
	•	Scalability in embedded systems

⸻

🟧 F (Format) – Expected Output

Your submission should include:
	•	A fully implemented Structured Text code block for the SimplexSolver function block
	•	Well-defined input and output parameters
	•	Inline comments that clearly describe:
	•	Each mathematical transformation in the Simplex method
	•	How edge cases like infeasibility or unboundedness are handled
	•	A short explanatory section outlining:
	•	Use cases, such as energy optimization, scheduling, material blending
	•	Considerations for platform-specific deployment (e.g., on Codesys, TIA Portal, TwinCAT)
	•	Optional: A reference to a real-world industrial application where the solver was used successfully
FUNCTION_BLOCK SimplexSolver
VAR_INPUT
    ObjectiveFunction : ARRAY[1..N] OF REAL; // Objective function coefficients
    ConstraintMatrix : ARRAY[1..M, 1..N] OF REAL; // Constraint matrix
    RightHandSide : ARRAY[1..M] OF REAL; // Right-hand side vector
    MaxIterations : INT := 100; // Maximum number of iterations
    Tolerance : REAL := 1.0E-6; // Convergence tolerance
END_VAR

VAR_OUTPUT
    Solution : ARRAY[1..N] OF REAL; // Optimal solution
    Status : INT; // 0 = Optimal, 1 = Infeasible, 2 = Max Iterations Reached
END_VAR

VAR
    A : ARRAY[1..M, 1..N] OF REAL; // Constraint matrix
    B : ARRAY[1..M] OF REAL; // Right-hand side vector
    C : ARRAY[1..N] OF REAL; // Objective function coefficients
    x : ARRAY[1..N] OF REAL; // Current solution
    x_prev : ARRAY[1..N] OF REAL; // Previous solution
    x_prev_prev : ARRAY[1..N] OF REAL; // Previous previous solution
    x_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous solution
    x_prev_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous previous solution
    x_prev_prev_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous previous previous solution
    x_prev_prev_prev_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous previous previous previous solution
    x_prev_prev_prev_prev_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous previous previous previous previous solution
    x_prev_prev_prev_prev_prev_prev_prev_prev : ARRAY[1..N] OF REAL; // Previous previous previous previous previous previous previous previous solution
    x_prev_prev_prev_prev_prev_prev_prev_prev_prev
