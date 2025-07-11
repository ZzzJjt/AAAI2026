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

**Example:**

```
FUNCTION SimplexSolver(C: ARRAY[1..N] OF REAL, A: ARRAY[1..M,1..N] OF REAL, B: ARRAY[1..M] OF REAL)
	VAR
		Solution: ARRAY[1..N] OF REAL;
		Objective: REAL;
		Status: STATUS;
		Row: ARRAY[1..M] OF INTEGER;
		Col: ARRAY[1..N] OF INTEGER;
		Pi: ARRAY[1..N] OF REAL;
		Pi_next: ARRAY[1..N] OF REAL;
		Delta: ARRAY[1..N] OF REAL;
		Delta_next: ARRAY[1..N] OF REAL;
		Flag: ARRAY[1..N] OF BOOLEAN;
	BEGIN
		Objective = C[1];
		Status = OPTIMAL;
		FOR i = 1 TO N DO
			Solution[i] = 0;
		END_FOR
		FOR i = 1 TO M DO
			Flag[A[i,1]] = TRUE;
		END_FOR
		WHILE NOT Flag[1] OR Status = INFEASIBLE DO
			FOR i = 1 TO N DO
				Pi[i] = C[i] / Solution[i];
			END_FOR
			FOR i = 1 TO M DO
				FOR j = 1 TO N DO
					Col[j] = 0;
				END_FOR
				FOR j = 1 TO M DO
					IF A[i,j] = 0 THEN CONTINUE;
					Col[j] = j;
				END_FOR
				FOR j = 1 TO N DO
					Delta[j] = Pi[j] * A[i,Col[j]] - Pi_next[j];
				END_FOR
				FOR j = 1 TO N DO
					IF j = Col[j] THEN CONTINUE;
					Delta_next[j] = Delta[j] + A[i,j] * Pi_next[Col[j]];
				END_FOR
				FOR
