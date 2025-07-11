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

This structured and lightweight implementation will make on-PLC optimization feasible for many common scenarios without external solvers or systems. The function block will be a valuable tool for industrial engineers looking to optimize their processes in real-time. **PoissonProbability Function Block in IEC 61131-3 Structured Text**

```structuredtext
// PoissonProbability Function Block
// Computes Poisson probabilities for event prediction
// Input: lambda (mean rate of events), x (number of events)
// Output: probability of x events occurring

VAR
    lambda : REAL; // Mean rate of events
    x : INT; // Number of events
    probability : REAL; // Probability of x events occurring
END_VAR

// Validate inputs
IF lambda < 0 OR x < 0 THEN
    probability := 0; // Invalid input
ELSE
    // Calculate factorial of x
    VAR
        factorial : REAL := 1;
        i : INT := 1;
    END_VAR
    WHILE i <= x DO
        factorial := factorial * i;
        i := i + 1;
    END_WHILE

    // Calculate Poisson probability
    probability := (EXP(-lambda) * (lambda ^ x)) / factorial;
END_IF
```

**Linear Programming Function Block in IEC 61131-3 Structured Text**

```structuredtext
// SimplexSolver Function Block
// Solves linear programming problems using the Simplex method
// Input: objectiveFunction (coefficients), constraintMatrix (constraints), rhs (right-hand-side values)
// Output: optimalSolution (solution vector), objectiveValue (objective function value)

VAR
    objectiveFunction : ARRAY[0..4] OF REAL; // Objective function coefficients
    constraintMatrix : ARRAY[0..4, 0..4] OF REAL; // Constraint matrix
    rhs : ARRAY[0..4] OF REAL; // Right-hand-side values
    optimalSolution : ARRAY[0..4] OF REAL; // Optimal solution vector
    objectiveValue : REAL; // Objective function value
    tableau : ARRAY[0..5, 0..5] OF REAL; // Tableau for Simplex method
    iterationLimit : INT := 100; // Maximum number of iterations
    solutionStatus : INT; // Solution status (0: optimal, 1: infeasible, 2: iteration limit reached)
END_VAR

// Initialize tableau
FOR i := 0 TO 4 DO
    FOR j := 0 TO 4 DO
        tableau[i, j
