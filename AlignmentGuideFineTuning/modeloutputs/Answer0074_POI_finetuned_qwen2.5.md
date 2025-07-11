### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block (`PoissonProbability`) to compute Poisson probabilities for event prediction in industrial automation (e.g., failure rates), with input validation, edge-case handling, and PLC-optimized numerical stability.

### Prompt:
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

🟥 B (Before) – The Challenge

In industrial automation, there is often a need to optimize processes—such as minimizing energy use or maximizing throughput—under constraints like capacity, cost, or material availability. While linear programming (LP) is a powerful mathematical tool for such optimization, most PLCs lack native support for solving LP problems due to limited memory, no matrix libraries, and strict scan time constraints. This creates a challenge for real-time optimization on embedded control systems.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named SimplexSolver, that:
	•	Solves linear programming problems using the Simplex method
	•	Accepts parameters for:
	•	Objective function coefficients
	•	Constraint matrix
	•	Right-hand-side values
	•	Returns the optimal solution vector and objective function value
	•	Is designed to handle multiple constraints and variables (within bounded array sizes for PLC compatibility)
	•	Includes detailed comments for each algorithm step:
	•	Initialization of the tableau
	•	Pivot selection
	•	Row transformations
	•	Optimality checks
	•	Reports solution status (e.g., optimal, infeasible, iteration limit reached)

Also include a discussion of:
	•	The limitations of running LP solvers on PLCs, such as:
	•	Memory for matrix storage
	•	Real-time iteration constraints
	•	Lack of floating-point precision on some platforms
	•	Recommended use cases such as:
	•	Production scheduling
	•	Resource allocation
	•	Load balancing
	•	Blending and mixing optimization

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Define array-based inputs for the objective function and constraint matrix, with preallocated sizes (e.g., max 5 constraints × 5 variables).
	2.	Use nested loops to implement tableau initialization and pivot operations.
	3.	Include iteration limits and diagnostic outputs to prevent infinite loops or unstable conditions.
	4.	Comment clearly, for example:
 // Step 2: Identify pivot column (most negative coefficient in objective row)
// Step 3: Identify pivot row (minimum positive ratio)
// Step 4: Perform row operations to update tableau
5.	Use practical examples such as:
	•	Optimizing the mix ratio of raw materials within cost and availability limits
	•	Distributing machine workloads across production lines to minimize idle time

This structured and lightweight implementation will make on-PLC optimization feasible for many common scenarios without external solvers or systems.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block (`PoissonProbability`) to compute Poisson probabilities for event prediction in industrial automation (e.g., failure rates), with input validation, edge-case handling, and PLC-optimized numerical stability.
**Linear Programming:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve a linear programming problem using the simplex method. Ensure the function block is designed to handle multiple constraints and objective functions, with detailed comments explaining the algorithm and each computational step. Discuss the limitations of implementing linear programming in a PLC environment, particularly with respect to memory and processing power, and provide examples of how this function block could be applied in industrial optimization scenarios.

🟥 B (Before) – The Challenge

In industrial automation, there is often a need to optimize processes—such as minimizing energy use or maximizing throughput—under constraints like capacity, cost, or material availability. While linear programming (LP) is a powerful mathematical tool for such optimization, most PLCs lack native support for solving LP problems due to limited memory, no matrix libraries, and strict scan time constraints. This creates a challenge for real-time optimization on embedded control systems.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named SimplexSolver, that:
	•	Solves linear programming problems using the Simplex method
	•	Accepts parameters for:
	•	Objective function coefficients
	•	Constraint matrix
	•	Right-hand-side values
	•	Returns the optimal solution vector and objective function value
	•	Is designed to handle multiple constraints and variables (within bounded array sizes for PLC compatibility)
	•	Includes detailed comments for each algorithm step:
	•	Initialization of the tableau
	•	Pivot selection
	•	Row transformations
	•	Optimality checks
	•	Reports solution status (e.g., optimal, infeasible, iteration limit reached)

Also include a discussion of:
	•	The limitations of running LP solvers on PLCs, such as:
	•	Memory for matrix storage
	•	Real-time iteration constraints
	•	Lack of floating-point precision on some platforms
	•	Recommended use cases such as:
	•	Production scheduling
	•	Resource allocation
	•	Load balancing
	•	Blending and mixing optimization

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Define array-based inputs for the objective function and constraint matrix, with preallocated sizes (e.g., max 5 constraints × 5 variables).
	2.	Use nested loops to implement tableau initialization and pivot operations.
	3.	Include iteration limits and diagnostic outputs to prevent infinite loops or unstable conditions.
	4.	Comment clearly, for example:
 // Step 2: Identify pivot column (most negative coefficient in objective row)
// Step 3: Identify pivot row (minimum positive ratio)
// Step 4: Perform row operations to update tableau
5.	Use practical examples such as:
	•	Optimizing the mix ratio of raw materials within cost and availability limits
	•	Distributing machine workloads across production lines to minimize idle time

This structured and lightweight implementation will make on-PLC optimization feasible for many common scenarios without external solvers or systems.  

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, optimization is key to improving efficiency, reducing waste, and maintaining compliance. However, most PLCs lack native support for linear programming, which is essential for solving optimization problems involving multiple constraints and objective functions.

⸻

🟩 A (Action) – The Implementation

Develop a self-contained function block in IEC 61131-3 Structured Text to solve linear programming problems using the Simplex method. Ensure that the function block:
	•	Accepts multiple constraints and objective functions
	•	Uses detailed comments to explain the Simplex algorithm
	•	Includes limitations and considerations for real-time PLC environments
	•	Is designed for industrial optimization tasks like resource allocation and process control

⸻

🟧 R (Result) – The Outcome

The result is a function block that:
	•	Works within the constraints of a PLC environment
	•	Is optimized for scan-time efficiency
	•	Includes detailed comments for each computational step
	•	Is suitable for real-time optimization tasks in industrial automation
	•	Helps engineers solve complex optimization problems directly on the control system

⸻

🟦 E (Example) – The Application

	•	Optimize the blending of raw materials in a chemical reactor, balancing cost, quality, and regulatory constraints
	•	Automate the allocation of tasks across multiple production lines to minimize downtime and maximize throughput
	•	Manage energy consumption in a power plant by optimizing fuel usage under varying demand and environmental conditions
	•	Implement a traffic light control system that dynamically adjusts timing to optimize traffic flow while adhering to safety and efficiency constraints
	•	Develop a pick-and-place robotic system that optimizes the sequence of operations to minimize cycle time and ensure efficient use of resources
	•	Design a sensor network that optimizes data collection and processing to reduce communication load while maintaining system responsiveness
	•	Create a predictive maintenance system that optimizes sensor placement and monitoring intervals to balance accuracy and resource usage
	•	Implement a chemical dosing system that optimizes the timing and amounts of reactants to improve reaction efficiency and reduce waste
	•	Develop a traffic light control system that dynamically adjusts timing to optimize traffic flow while adhering to safety and efficiency constraints
	•	Create a sensor network that optimizes data collection and processing to reduce communication load while maintaining system responsiveness
	•	Design a predictive maintenance system that optimizes
