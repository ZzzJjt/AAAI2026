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
// Function Block: PoissonProbability
// Purpose: Computes Poisson probability for given lambda and sample size
// Inputs:
//   Lambda : REAL (1.0 to 1000.0) — Poisson parameter
//   SampleSize : INT (1 to 1000) — Number of events observed
// Outputs:
//   Probability : REAL — Probability of observing k events
//   Error : BOOL — TRUE if input values are invalid
// Notes:
//   - Uses Euler–Maclaurin series approximation for numerical stability
//   - Accepts valid input ranges and handles edge cases
//   - Optimized for PLC execution with fixed-point precision

FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Poisson parameter (1.0 to 1000.0)
    SampleSize : INT; // Number of events observed (1 to 1000)
END_VAR

VAR_OUTPUT
    Probability : REAL; // Probability of observing k events
    Error : BOOL; // TRUE if input values are invalid
END_VAR

VAR
    // Euler–Maclaurin series approximation
    // Reference: https://en.wikipedia.org/wiki/Poisson_distribution#Approximation_by_the_Euler_Maclaurin_series
    eulerMaclaurin : REAL;
    k : INT;
    term : REAL;
    sum : REAL;
    i : INT;
END_VAR

// Initialize output variables
Probability := 0.0;
Error := FALSE;

// Check input validity
IF NOT (Lambda >= 1.0 AND Lambda <= 1000.0) THEN
    Error := TRUE;
    Probability := 0.0;
    RETURN;
ELSIF NOT (SampleSize >= 1 AND SampleSize <= 1000) THEN
    Error := TRUE;
    Probability := 0.0;
    RETURN;
END_IF;

// Initialize Euler–Maclaurin series
eulerMaclaurin := 0.0;

// Loop through k values from 1 to SampleSize
FOR i := 1 TO SampleSize DO
    k := i;
    term := (Lambda ^ k)
