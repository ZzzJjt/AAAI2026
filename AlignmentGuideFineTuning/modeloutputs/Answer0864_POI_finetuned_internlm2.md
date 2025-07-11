### Intent:
**Intent Summary:**  
Create a Structured Text function block implementing the Simplex method for linear programming in PLCs, with inputs for constraints/objective functions, outputs for solutions, and documentation on industrial applicability and limitations.  

*(Focus: On-device optimization for real-time control tasks like resource allocation or batch blending.)*

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
Create a Structured Text function block implementing the Simplex method for linear programming in PLCs, with inputs for constraints/objective functions, outputs for solutions, and documentation on industrial applicability and limitations.  

*(Focus: On-device optimization for real-time control tasks like resource allocation or batch blending.)*
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

**🔴 R (Red) – What You Should Not Do**

Avoid:
	•	Overcomplicating the function block with unnecessary features
	•	Assuming the PLC has sufficient memory or processing power to handle large-scale linear programming problems
	•	Implementing the simplex method without clear comments or explanations of each step

**🟢 Y (Yellow) – What You Can Do Instead**

Instead, focus on:
	•	Providing a clear, self-contained function block that can be easily integrated into a PLC program
	•	Explaining the simplex algorithm in detail, with comments for each step
	•	Highlighting the limitations of implementing linear programming in a PLC environment, including memory and processing constraints
	•	Offering examples of industrial applications where this function block could be used to optimize production processes

**🟢 Y (Yellow) – What You Can Do Instead**

Instead, focus on:
	•	Providing a clear, self-contained function block that can be easily integrated into a PLC program
	•	Explaining the simplex algorithm in detail, with comments for each step
	•	Highlighting the limitations of implementing linear programming in a PLC environment, including memory and processing constraints
	•	Offering examples of industrial applications where this function block could be used to optimize production processes
**🟩 A (Action) – How to Do It**

Create a self-contained function block in IEC 61131-3 Structured Text named SimplexSolver that can solve a linear programming problem using the Simplex method. The function block should have the following inputs:

•	C: Objective function coefficients (ARRAY[1..N] OF REAL)
•	A: Constraint matrix (ARRAY[1..M, 1..N] OF REAL)
•	B: Right-hand side values (ARRAY[1..M] OF REAL)

Implement the Simplex algorithm, including initialization of the simplex tableau, pivot column and row selection logic, row operations and tableau updates, and termination criteria for optimality or maximum iterations. Output the results, including the optimal solution vector X (ARRAY[1..N] OF REAL), the optimized objective value, and a status flag (e.g., success, infeasible, timeout).

Add clear inline comments for each algorithm step to explain the mathematical logic, handling of infeasible solutions and potential rounding issues, and
