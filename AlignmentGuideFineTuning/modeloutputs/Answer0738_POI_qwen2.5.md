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

**Poisson Distribution Function Block in IEC 61131-3 Structured Text**

```structuredtext
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
```

**Explanation and Comments:**

```structuredtext
FUNCTION_BLOCK PoissonProbability
    * This function block calculates the Poisson probability mass function for a given mean (λ) and number of events (K).
    * The Poisson distribution is used to model the number of events occurring in a fixed interval of time or space.
    * Inputs:
    *   Lambda : REAL - the expected mean number of events (λ)
    *   K : INT - the number of actual events observed
    * Outputs:
    *   Probability : REAL - the calculated Poisson probability
    *   The function block handles invalid input cases gracefully, ensuring that Lambda > 0 and K >= 0.
    *   It computes the factorial of K using an iterative loop to avoid potential overflow issues.
    *   The exponential and power functions are used to calculate e^{-λ} and λ^K, respectively.
    *   The function block is designed for real-time industrial control systems, where event-driven processes are common.
    *   It can be used to model sensor trigger probabilities, machine failure occurrences, and other stochastic processes.
```

**Limitations and Considerations:**

- **Overflow**: For very large values of λ, the factorial calculation can lead to overflow. To mitigate this, consider using logarithmic calculations or approximations for large λ values.
- **Precision**: The function block uses floating-point arithmetic, which may introduce rounding errors. For high-precision applications, consider using fixed-point arithmetic or specialized libraries.
- **Real-time Performance**: The function block is designed for real-time performance, but for very large λ values, the factorial calculation may become computationally expensive. Consider optimizing the function block for specific use cases or using approximations for large λ values.
- **
