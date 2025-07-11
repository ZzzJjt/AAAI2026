### Intent:
**Intent Summary:**  
Create a Structured Text function block implementing the Simplex method to solve small-scale linear programming problems (e.g., 5x5 constraints) directly on a PLC, enabling real-time optimization tasks like resource allocation or blending ratios while addressing PLC memory and processing limitations.  

*(Key focus: On-device LP solver for industrial optimization with constrained resources.)*

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
Create a Structured Text function block implementing the Simplex method to solve small-scale linear programming problems (e.g., 5x5 constraints) directly on a PLC, enabling real-time optimization tasks like resource allocation or blending ratios while addressing PLC memory and processing limitations.  

*(Key focus: On-device LP solver for industrial optimization with constrained resources.)*
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

**Deliverables:**

1.	A function block called SimplexSolver that implements the Simplex method for solving linear programming problems.
2.	A detailed description of the algorithm and its implementation, including comments explaining each computational step.
3.	A discussion of the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power.
4.	Examples of how the function block could be applied in industrial optimization scenarios.

**Evaluation Criteria:**

1.	The function block correctly implements the Simplex method for solving linear programming problems.
2.	The function block is well-documented and structured for clarity and maintainability.
3.	The function block is optimized for real-time industrial environments, taking into account PLC constraints such as fixed memory, bounded loop execution, and limited floating-point precision.
4.	The function block is demonstrated to be able to handle small LP problems in real time, enabling optimization tasks such as resource allocation, load distribution, and blending/mixing ratios.
5.	The function block provides deterministic outputs, supporting control system decision-making without relying on external solvers or cloud connectivity.

**References:**

1.	"Simplex Method for Linear Programming" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/simplex.pdf
2.	"Linear Programming" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/lp.pdf
3.	"Simplex Method" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/simplex.pdf
4.	"Simplex Method for Linear Programming" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/simplex.pdf
5.	"Simplex Method for Linear Programming" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/simplex.pdf
6.	"Simplex Method for Linear Programming" by Dr. S. S. Rao, https://www.math.iitb.ac.in/~ssrao/lp/simplex.pdf
7.	"Simplex Method for Linear Programming" by Dr. S. S. Rao, https://www.
