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
	•	Reliability analysis of critical systems

**Submission Format:**

Submit a zip file containing:
	•	A screenshot of the function block in the PLC programming environment
	•	A screenshot of the function block in action, with sample inputs and outputs
	•	A brief explanation of the function block’s purpose and use cases
	•	A brief explanation of the mathematical basis of the Poisson distribution and how it is used in industrial systems
	•	A brief explanation of the computational steps involved in the function block and how they are optimized for real-time performance
	•	A brief explanation of the edge cases and limitations of the function block and how they are handled
	•	A brief explanation of the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes

**Evaluation Criteria:**

Your submission will be evaluated based on the following criteria:
	•	Accuracy of the function block in computing Poisson probabilities
	•	Robustness of the function block in handling edge cases and avoiding crashes
	•	Efficiency of the function block in executing within a real-time PLC scan cycle
	•	Clarity of the function block’s structure and comments
	•	Practical relevance of the function block to event-driven industrial systems
	•	Overall quality of the submission, including the explanation of the function block’s purpose, use cases, and mathematical basis

**Submission Deadline:**

The submission deadline is 11:59 PM on 12/31/2022. Submissions received after this deadline will not be considered.

**Submission Process:**

To submit your solution, please follow these steps:
	1.	Create a zip file containing the required materials
	2.	Upload the zip file to the submission portal
	3.	Complete the submission form with your contact information and a brief description of your solution
	4.	Submit the form and wait for a confirmation email

**Submission Portal:**

The submission portal will be available on the website.

**Submission Review:**

Your submission will be reviewed by a panel of experts in the field of industrial automation and control systems. The review process will take approximately 2 weeks, and you will be notified of the results via email.

**Submission Rewards:**

The top 3 submissions will receive the following rewards:
	•	1st place: $1,000
	•	2nd place: $
