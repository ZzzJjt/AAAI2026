### Intent:
**Intent Summary:**  
Create a cubic spline interpolation function block in Structured Text that calculates interpolated y-values from given x-y data points and spline coefficients, with input validation and error handling for industrial control applications.

### Prompt:
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer responsible for implementing statistical computations in IEC 61131-3 Structured Text for use in real-time industrial control systems. Your goal is to create a reliable and efficient function block that models discrete event probabilities using the Poisson distribution.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained function block named PoissonProbability that:
	•	Calculates the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Accepts two inputs:
	•	Lambda : REAL — the expected mean number of events (λ)
	•	K : INT — the number of actual events observed
	•	Outputs:
	•	Probability : REAL — the calculated Poisson probability
	•	Includes logic to:
	•	Compute k! using an iterative loop
	•	Use built-in EXP() and POW() functions for e^{-\lambda} and \lambda^k
	•	Handle invalid input cases gracefully (e.g., Lambda ≤ 0 or K < 0)
	•	Is fully documented with inline comments explaining:
	•	The purpose of each step
	•	The mathematical reasoning
	•	Considerations for overflow, precision, and real-time performance

⸻

🟧 F (Format) – Expected Output

You should provide a complete and readable IEC 61131-3 Structured Text function block like:
FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL;
    K : INT;
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

IF (Lambda > 0.0) AND (K >= 0) THEN
    FOR i := 1 TO K DO
        Factorial := Factorial * i;
    END_FOR;
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;
This function block should be suitable for industrial applications such as:
	•	Modeling sensor trigger probabilities over fixed time intervals
	•	Estimating machine failure occurrences in predictive maintenance
	•	Supporting event-driven control logic in stochastic processes

### Generated Code:
**Intent Summary:**  
Create a cubic spline interpolation function block in Structured Text that calculates interpolated y-values from given x-y data points and spline coefficients, with input validation and error handling for industrial control applications.
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer responsible for implementing statistical computations in IEC 61131-3 Structured Text for use in real-time industrial control systems. Your goal is to create a reliable and efficient function block that models discrete event probabilities using the Poisson distribution.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained function block named PoissonProbability that:
	•	Calculates the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Accepts two inputs:
	•	Lambda : REAL — the expected mean number of events (λ)
	•	K : INT — the number of actual events observed
	•	Outputs:
	•	Probability : REAL — the calculated Poisson probability
	•	Includes logic to:
	•	Compute k! using an iterative loop
	•	Use built-in EXP() and POW() functions for e^{-\lambda} and \lambda^k
	•	Handle invalid input cases gracefully (e.g., Lambda ≤ 0 or K < 0)
	•	Is fully documented with inline comments explaining:
	•	The purpose of each step
	•	The mathematical reasoning
	•	Considerations for overflow, precision, and real-time performance

⸻

🟧 F (Format) – Expected Output

You should provide a complete and readable IEC 61131-3 Structured Text function block like:
FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL;
    K : INT;
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

IF (Lambda > 0.0) AND (K >= 0) THEN
    FOR i := 1 TO K DO
        Factorial := Factorial * i;
    END_FOR;
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;
This function block should be suitable for industrial applications such as:
	•	Modeling sensor trigger probabilities over fixed time intervals
	•	Estimating machine failure occurrences in predictive maintenance
	•	Supporting event-driven control logic in stochastic processes
FUNCTION_BLOCK InterpolateCubicSpline
VAR_INPUT
    x_values : ARRAY[1..10] OF REAL; // x-values
    y_values : ARRAY[1..10] OF REAL; // y-values
    x_target : REAL; // target x-value
END_VAR
VAR_OUTPUT
    y_interpolated : REAL; // interpolated y-value
END_VAR
VAR
    i : INT;
    delta_x : REAL;
    delta_y : REAL;
    a : REAL;
    b : REAL;
    c : REAL;
    d : REAL;
END_VAR

// Check input validity
FOR i := 1 TO 10 DO
    IF x_values[i] < 0.0 OR y_values[i] < 0.0 THEN
        y_interpolated := 0.0;
        RETURN;
    END_IF;
END_FOR;

// Compute coefficients
a := y_values[1];
b := y_values[2] - y_values[1];
c := y_values[3] - y_values[2];
d := y_values[4] - y_values[3];

// Compute interpolated y-value
delta_x := x_target - x_values[1];
y_interpolated := a + (b * delta_x) + (c * delta_x * delta_x) / 2.0 + (d * delta_x * delta_x * delta_x) / 6.0;

// Handle edge cases
IF x_target < x_values[1] THEN
    y_interpolated := y_values[1];
ELSIF x_target > x_values[10] THEN
    y_interpolated := y_values[10];
ELSE
    y_interpolated := y_interpolated;
END_IF;

// Error handling
IF y_interpolated < 0.0 THEN
    y_interpolated := 0.0;
END_IF;

FUNCTION_BLOCK PoissonDistribution
VAR_INPUT
    Lambda : REAL; // Mean number of events (λ)
    K : INT; // Number of observed events
END_VAR
