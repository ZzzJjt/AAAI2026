### Intent:
**Intent Summary:**  
Create a structured text function block in IEC 61131-3 that implements the Simplex method to solve small-scale linear programming problems on a PLC, handling constraints and objective functions while addressing real-time industrial limitations like memory and processing power.  

*(Focus: On-device LP solver for resource allocation/optimization in PLC environments.)*

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
Create a structured text function block in IEC 61131-3 that implements the Simplex method to solve small-scale linear programming problems on a PLC, handling constraints and objective functions while addressing real-time industrial limitations like memory and processing power.  

*(Focus: On-device LP solver for resource allocation/optimization in PLC environments.)*
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

⸻

🟨 A (Assumptions) – What You Can Assume

You can assume that the input arrays are valid and that the problem is feasible. You can also assume that the PLC has sufficient memory and processing power to run the function block.

⸻

🟩 C (Constraints) – What You Must Consider

You must consider the following constraints when implementing the function block:
	•	Real-time constraints: The function block must operate within the PLC's cycle time.
	•	Memory constraints: The function block must use minimal memory, as PLCs have limited memory resources.
	•	Processing power constraints: The function block must be computationally efficient, as PLCs have limited processing power.
	•	Floating-point precision: The function block must handle floating-point precision limitations of PLCs.

⸻

🟩 T (Tips) – Helpful Hints

Here are some tips to help you complete the task:
	•	Use FOR loops instead of recursion to avoid stack overflow.
	•	Use integer division and multiplication to handle floating-point precision limitations.
	•	Use inline comments to explain the algorithm and each computational step.
	•	Consider using a watchdog timer or time-slicing logic to prevent the function block from monopolizing the PLC's processing time.
	•	Test the function block with different problem sizes and constraints to ensure it operates within the PLC's constraints.

⸻

🟩 R (Resources) – Additional Resources

Here are some resources that may help you complete the task:
	•	IEC 61131-3 Standard: https://www.iec.ch/online_services/standards/standard/IEC_61131-3.pdf
	•	Linear Programming: https://en.wikipedia.org/wiki/Linear_programming
	•	Simplex Algorithm: https://en.wikipedia.org/wiki/Simplex_algorithm
	•	PLC Programming: https://www.plcprogramming.net/
	•	PLC Memory and Processing Power: https://www.plcprogramming.net/plc-memory-and-processing-power.html

⸻

🟩 A (Acknowledgements) – Credits

*This prompt was adapted from the [R-I-S-E prompt format](https://www.freecodecamp.org/news/rise-prompt-format/) created by [@bgoonz](https://www.f
