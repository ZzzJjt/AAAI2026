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

⸻

🟦 E (Explanation) – Why You Are Doing This

The Poisson distribution is a fundamental probability distribution used to model the number of events occurring within a fixed time interval or a fixed area, given a known average rate of occurrence. In industrial control systems, the Poisson distribution can be used to model event-driven processes, such as sensor triggers, machine failures, or packet arrivals in communication networks.

The PoissonProbability function block provides a simple and efficient way to calculate the probability of observing a specific number of events (k) given a known average rate of occurrence (λ). By using this function block, engineers can incorporate the Poisson distribution into their control logic to improve system performance, reliability, and safety.

The function block is designed to be self-contained, easy to understand, and efficient in terms of real-time performance. It uses built-in functions for exponential and power calculations, and an iterative loop to compute factorials. The function block also includes input validation to ensure that only valid input values are processed.

One potential limitation of the PoissonProbability function block is the handling of large values of λ. In such cases, the exponential term (e^{-\lambda}) may become very small, leading to potential precision issues. To address this, it is recommended to use a double-precision floating-point data type for the Lambda input and the Probability output. Additionally, the function block can be optimized for real-time performance by minimizing the number of calculations and using efficient data types.

In summary, the PoissonProbability function block is a valuable tool for industrial control engineers who need to model event-driven processes using the Poisson distribution. By providing a simple and efficient way to calculate Poisson probabilities, this function block can help improve system performance, reliability, and safety in a variety of industrial applications.
