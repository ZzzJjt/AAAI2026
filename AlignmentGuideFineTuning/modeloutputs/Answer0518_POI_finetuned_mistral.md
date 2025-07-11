### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to compute Poisson probabilities (P(k; λ)) for event-driven industrial applications, handling edge cases (invalid inputs, overflow) while ensuring real-time efficiency and clarity through comments.  

*(Key focus: Statistical calculation, robustness, and industrial relevance.)*

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
Create a reusable IEC 61131-3 Structured Text function block to compute Poisson probabilities (P(k; λ)) for event-driven industrial applications, handling edge cases (invalid inputs, overflow) while ensuring real-time efficiency and clarity through comments.  

*(Key focus: Statistical calculation, robustness, and industrial relevance.)*
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
FUNCTION_BLOCK FB_PoissonProbability
VAR_INPUT
    Lambda : REAL; // Expected number of events (mean rate, λ)
    K : INT; // Number of actual events observed
END_VAR

VAR_OUTPUT
    Probability : REAL; // Probability that K events occur given a rate Lambda
END_VAR

VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR

METHOD Execute;
BEGIN
    // Check for valid input
    IF (Lambda > 0) AND (K >= 0) THEN
        // Compute factorial manually
        FOR i := 1 TO K DO
            Factorial := Factorial * i;
        END_FOR;

        // Calculate Poisson probability
        Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
    ELSE
        Probability := 0.0; // Default value for invalid inputs
    END_IF;
END_METHOD

// Main execution loop
Execute();
```

### Function Block Overview

This function block computes the Poisson probability for a given mean rate (`Lambda`) and observed number of events (`K`). It is designed for use in IEC 61131-3 Structured Text environments, where floating-point math and built-in factorial functions may not be available. The function block includes input validation, manual factorial calculation, and output of the Poisson probability.

### Key Features

1. **Input Validation**: Ensures that `Lambda` is positive and `K` is non-negative to avoid undefined or invalid results.
2. **Manual Factorial Calculation**: Computes the factorial of `K` manually using a loop, as no built-in factorial function is available in Structured Text.
3. **Poisson Probability Formula**: Applies the Poisson probability mass function:
   ```
   Probability = e^(-Lambda) * (Lambda^K) / K!
   ```
4. **Output Clamping**: Sets `Probability` to 0.0 if any input is invalid, ensuring safe operation in real-time control
