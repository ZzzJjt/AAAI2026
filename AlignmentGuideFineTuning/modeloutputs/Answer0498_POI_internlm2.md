### Intent:
**Intent Summary:**  
Create a Structured Text function block to compute the Poisson probability distribution for event-driven industrial processes, handling inputs (λ and k) with robust edge-case checks, factorial calculation, and efficient real-time execution.  

*(Focus: Statistical modeling for PLC-based event analysis, emphasizing clarity, precision, and industrial applicability.)*

### Prompt:
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer developing statistical function blocks in IEC 61131-3 Structured Text to support real-time probabilistic event analysis in industrial systems.

⸻

🟩 I (Input) – What You’re Given

You need to implement a function block that calculates the Poisson distribution probability, given:
	•	Lambda : REAL — the expected number of events (mean rate, λ)
	•	K : INT — the number of actual events observed

The output should be:
	•	Probability : REAL — the probability that K events occur given a rate Lambda
	•	Based on the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}

You must also consider:
	•	Overflow and precision loss with large values of λ or k
	•	Executing efficiently within a real-time PLC scan cycle
	•	Proper domain checks (e.g., Lambda > 0, K ≥ 0)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define a function block named PoissonProbability with the following structure:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL;
    K : INT;
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
	2.	Add logic to calculate factorial for K:
 VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Compute the Poisson probability:
 IF (Lambda > 0) AND (K >= 0) THEN
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;
	4.	Add inline comments explaining:
	•	Each step of the Poisson formula
	•	Why factorial is manually computed (no built-in factorial in ST)
	•	How floating-point math affects precision
	•	Consideration of upper limits for K to prevent overflow

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a compact and accurate function block that:
	•	Computes Poisson probabilities reliably for typical values of Lambda and K
	•	Avoids crashing or incorrect output for edge cases (e.g. negative inputs)
	•	Executes quickly enough for inclusion in real-time event monitoring applications
	•	Can be reused in use cases such as:
	•	Predicting machine failure rates
	•	Sensor event tracking over time intervals
	•	Process bottleneck analysis

### Generated Code:
**Intent Summary:**  
Create a Structured Text function block to compute the Poisson probability distribution for event-driven industrial processes, handling inputs (λ and k) with robust edge-case checks, factorial calculation, and efficient real-time execution.  

*(Focus: Statistical modeling for PLC-based event analysis, emphasizing clarity, precision, and industrial applicability.)*
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer developing statistical function blocks in IEC 61131-3 Structured Text to support real-time probabilistic event analysis in industrial systems.

⸻

🟩 I (Input) – What You’re Given

You need to implement a function block that calculates the Poisson distribution probability, given:
	•	Lambda : REAL — the expected number of events (mean rate, λ)
	•	K : INT — the number of actual events observed

The output should be:
	•	Probability : REAL — the probability that K events occur given a rate Lambda
	•	Based on the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}

You must also consider:
	•	Overflow and precision loss with large values of λ or k
	•	Executing efficiently within a real-time PLC scan cycle
	•	Proper domain checks (e.g., Lambda > 0, K ≥ 0)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define a function block named PoissonProbability with the following structure:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL;
    K : INT;
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
	2.	Add logic to calculate factorial for K:
 VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Compute the Poisson probability:
 IF (Lambda > 0) AND (K >= 0) THEN
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;
	4.	Add inline comments explaining:
	•	Each step of the Poisson formula
	•	Why factorial is manually computed (no built-in factorial in ST)
	•	How floating-point math affects precision
	•	Consideration of upper limits for K to prevent overflow

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a compact and accurate function block that:
	•	Computes Poisson probabilities reliably for typical values of Lambda and K
	•	Avoids crashing or incorrect output for edge cases (e.g. negative inputs)
	•	Executes quickly enough for inclusion in real-time event monitoring applications
	•	Can be reused in use cases such as:
	•	Predicting machine failure rates
	•	Sensor event tracking over time intervals
	•	Process bottleneck analysis
	•	Probability of equipment failure in a given time frame
	•	Probability of a specific number of events occurring within a given time frame

⸻

🟨 S (Solution) – How to Implement

1.	Define a function block named PoissonProbability with the following structure:
```ST
FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL;
    K : INT;
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
```
2.	Add logic to calculate factorial for K:
```ST
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
```
3.	Compute the Poisson probability:
```ST
IF (Lambda > 0) AND (K >= 0) THEN
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;
```
4.	Add inline comments explaining:
	•	Each step of the Poisson formula
	•	Why factorial is manually computed (no built-in factorial in ST)
	•	How floating-point math affects precision
	•	Consideration of upper limits for K to prevent overflow

```ST
-- Poisson Probability Function Block
-- This function block calculates the Poisson probability distribution for a given mean (Lambda) and number of events (K).
-- The Poisson distribution is used to model the probability of a given number of events occurring in a fixed interval of time or space.
-- The formula for the Poisson probability mass function is:
-- P(k; λ) = e^(-λ) * (λ^k) / k!
-- where:
-- P(k; λ) is the probability of k events occurring
-- λ is the mean rate of events
-- k is the number of events observed
-- e is the base of the natural logarithm (approximately 2.71828)
-- The function block checks for valid input values (Lambda > 0, K >= 0) to avoid division by zero or negative values.
-- The factorial of K is manually computed to avoid potential precision loss with large values of K.
-- Floating-point math can introduce precision loss, so the EXP and POW functions are used to
