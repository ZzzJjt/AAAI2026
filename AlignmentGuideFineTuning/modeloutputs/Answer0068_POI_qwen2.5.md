### Intent:
The task is to implement a Simplex algorithm function block in IEC 61131-3 Structured Text for solving linear programming problems with up to 5 variables and constraints in industrial control applications.

### Prompt:
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial systems, processes often involve event-driven behaviors, such as machine failures, sensor triggers, or counting occurrences over time. The Poisson distribution is widely used to model the probability of a given number of events occurring in a fixed time interval. However, most IEC 61131-3 Structured Text environments do not natively support statistical functions, making it difficult to apply this distribution directly in real-time PLC logic. Developers also face challenges handling large factorials and maintaining numerical stability when computing small probabilities.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, that:
	•	Accepts two inputs:
	•	Lambda : REAL — the mean number of expected events (λ)
	•	K : INT — the observed number of events
	•	Outputs one result:
	•	Probability : REAL — the Poisson probability P(k; λ)
	•	Implements the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Includes detailed inline comments explaining:
	•	The mathematical formula
	•	How EXP(-Lambda) and POW(Lambda, K) are used
	•	How to compute K! via a helper function or iterative loop
	•	Incorporates error checks for:
	•	Negative inputs
	•	Overflow from large factorials
	•	Precision loss when λ is large or k is too high
	•	Is optimized for deterministic execution in a PLC scan cycle

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Declare inputs/outputs:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean rate of occurrence
    K : INT;       // Number of occurrences
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR
  2.	Compute K! using a loop:
FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Apply the Poisson formula:
 Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
 	4.	Comment each step, and document limitations:
	•	For large K, factorial grows quickly and may exceed REAL range
	•	Precision may degrade for very small or very large Lambda
	•	Consider clamping K to a max safe value for reliability
	5.	Discuss applications, such as:
	•	Predicting machine failure frequency
	•	Modeling error rates in communication packets
	•	Monitoring how often a sensor is triggered in a defined interval

### Generated Code:
The task is to implement a Simplex algorithm function block in IEC 61131-3 Structured Text for solving linear programming problems with up to 5 variables and constraints in industrial control applications.
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial systems, processes often involve event-driven behaviors, such as machine failures, sensor triggers, or counting occurrences over time. The Poisson distribution is widely used to model the probability of a given number of events occurring in a fixed time interval. However, most IEC 61131-3 Structured Text environments do not natively support statistical functions, making it difficult to apply this distribution directly in real-time PLC logic. Developers also face challenges handling large factorials and maintaining numerical stability when computing small probabilities.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, that:
	•	Accepts two inputs:
	•	Lambda : REAL — the mean number of expected events (λ)
	•	K : INT — the observed number of events
	•	Outputs one result:
	•	Probability : REAL — the Poisson probability P(k; λ)
	•	Implements the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Includes detailed inline comments explaining:
	•	The mathematical formula
	•	How EXP(-Lambda) and POW(Lambda, K) are used
	•	How to compute K! via a helper function or iterative loop
	•	Incorporates error checks for:
	•	Negative inputs
	•	Overflow from large factorials
	•	Precision loss when λ is large or k is too high
	•	Is optimized for deterministic execution in a PLC scan cycle

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Declare inputs/outputs:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean rate of occurrence
    K : INT;       // Number of occurrences
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR
  2.	Compute K! using a loop:
FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Apply the Poisson formula:
 Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
 	4.	Comment each step, and document limitations:
	•	For large K, factorial grows quickly and may exceed REAL range
	•	Precision may degrade for very small or very large Lambda
	•	Consider clamping K to a max safe value for reliability
	5.	Discuss applications, such as:
	•	Predicting machine failure frequency
	•	Modeling error rates in communication packets
	•	Monitoring how often a sensor is triggered in a defined interval

**Simplex Algorithm:**

Design a self-contained function block in IEC 61131-3 Structured Text to implement the Simplex algorithm for solving linear programming problems with up to 5 variables and constraints. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Simplex algorithm and the computational steps involved. Address potential limitations, such as handling degenerate cases and unbounded solutions, and discuss the practical applications of the Simplex algorithm in industrial control systems, particularly in optimizing resource allocation and production planning.

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial control systems, optimizing resource allocation and production planning often involves solving linear programming problems. The Simplex algorithm is a widely used method for solving such problems efficiently. However, most IEC 61131-3 Structured Text environments do not natively support complex mathematical algorithms, making it challenging to implement the Simplex algorithm directly in real-time PLC logic. Developers also face challenges handling degenerate cases and unbounded solutions, which can lead to incorrect or infinite loops in the algorithm.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named SimplexSolver, that:
	•	Accepts inputs:
	•	Constraints : ARRAY[1..5] OF REAL — coefficients of the constraints
	•	Variables : ARRAY[1..5] OF REAL — coefficients of the objective function
	•	Directions : ARRAY[1..5] OF BOOL — inequality directions (≤ or ≥)
	•	RightHandSides : ARRAY[1..5] OF REAL — right-hand side values of the constraints
	•	TargetValue : REAL — the target value of the objective function
	•	Outputs one result:
	•	OptimalSolution : ARRAY[1..5] OF REAL — the optimal values of the variables
	•	Implements the Simplex algorithm to find the optimal solution to the linear programming problem:
	•	Maximize or minimize the objective function subject to the given constraints
	•	Handles degenerate cases and unbounded solutions
	•	Includes detailed inline comments explaining:
	•	The mathematical basis of the Simplex algorithm
	•	How to pivot and update the tableau
	•	How to handle degenerate cases and unbounded solutions
	•	Is optimized for deterministic execution in a
