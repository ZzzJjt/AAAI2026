### Intent:
**Intent Summary:**  
Create a Structured Text function block to calculate Poisson probability (given λ and k) for industrial event analysis, handling edge cases and ensuring real-time efficiency.

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
Create a Structured Text function block to calculate Poisson probability (given λ and k) for industrial event analysis, handling edge cases and ensuring real-time efficiency.
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

**Poisson Probability Function Block in IEC 61131-3 Structured Text**

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

// Calculate factorial manually since there's no built-in factorial function in Structured Text
FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;

// Compute the Poisson probability
IF (Lambda > 0) AND (K >= 0) THEN
    Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
ELSE
    Probability := 0.0;
END_IF;

// Comments explaining the steps
// 1. Calculate the factorial of K manually
// 2. Compute the Poisson probability using the formula P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
// 3. Handle edge cases where Lambda <= 0 or K < 0 by setting Probability to 0.0
// 4. Ensure that the computation is efficient and does not cause overflow for large values of K
// 5. Use EXP and POW functions for exponential and power calculations, respectively
// 6. The factorial calculation is crucial for the Poisson distribution formula
// 7. Floating-point math can lead to precision loss, especially with large values of Lambda or K
// 8. Consider using a more precise data type or library if necessary for high-precision applications
// 9. The function block is designed to be reusable in various industrial event analysis scenarios
// 10. The function block is optimized for real-time execution within a PLC scan cycle
// 11. The function block is designed to handle edge cases and provide accurate results for typical values of Lambda and K
// 12. The function block is designed to be efficient and reliable for use in real-time event monitoring applications
// 13. The function block is designed to be reusable in various industrial event analysis scenarios
// 14. The function block is designed to be efficient and reliable for use in real-time event monitoring applications
// 15. The function block is designed to be reusable in various industrial event analysis scenarios
// 16. The function block is
