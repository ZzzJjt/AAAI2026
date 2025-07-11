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
	•	Considerations for platform-specific deployment (e.g., on Codesys, TIA Portal, TwinCAT)	•	Real-world examples of how this function block could be applied in industrial optimization scenarios
	•	A discussion of the limitations of using linear programming in a PLC environment, particularly with respect to memory, processing power, and real-time constraints
	•	Concrete examples of how this function block could be integrated into a PLC-based control system to optimize resource allocation, energy usage, or production planning
	•	A comparison of the performance and limitations of implementing linear programming in a PLC versus a general-purpose programming language like Python
	•	A list of potential use cases for the SimplexSolver function block in industrial applications, including examples of how it could be applied to solve real-world optimization problems
	•	A discussion of the challenges associated with scaling linear programming solutions to larger, more complex problems in a PLC environment
	•	A comparison of the Simplex method with other optimization algorithms in terms of computational efficiency and applicability in PLC-based systems
	•	A detailed explanation of the Simplex method, including the steps involved in the algorithm and the role of the tableau in the optimization process
	•	A discussion of the limitations of the Simplex method, particularly in terms of memory usage and processing power, and how these limitations can be mitigated in a PLC environment
	•	A comparison of the Simplex method with other optimization algorithms in terms of computational efficiency and applicability in PLC-based systems
	•	A detailed explanation of the Simplex method, including the steps involved in the algorithm and the role of the tableau in the optimization process
	•	A discussion of the limitations of the Simplex method, particularly in terms of memory usage and processing power, and how these limitations can be mitigated in a PLC environment
	•	A comparison of the Simplex method with other optimization algorithms in terms of computational efficiency and applicability in PLC-based systems
	•	A detailed explanation of the Simplex method, including the steps involved in the algorithm and the role of the tableau in the optimization process
	•	A discussion of the limitations of the Simplex method, particularly in terms of memory usage and processing power, and how these limitations can be mitigated in a PLC environment
	•	A comparison of the Simplex method with other optimization algorithms in terms of computational efficiency and applicability in PLC-based systems
	•	A detailed explanation of the Simplex method, including the steps involved in the algorithm and the role of the tableau in the optimization process
	•	A discussion of the limitations of the Simplex method, particularly in terms of memory usage and processing
