### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to compute Poisson probabilities (P(k; λ)) for industrial event prediction, with input validation, numerical stability safeguards, and diagnostic logging for PLC environments.  

*(Key focus: Statistical calculation, edge-case handling, and real-time applicability in automation systems.)*

### Prompt:
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation and process monitoring, it’s often important to predict the likelihood of discrete events occurring over a period of time—such as sensor triggers, part arrivals, or faults. The Poisson distribution is widely used in such event-driven systems to estimate the probability of a certain number of events happening within a fixed interval. However, most IEC 61131-3 Structured Text environments do not provide built-in statistical functions, making it necessary to implement this computation manually and carefully handle numerical stability and factorials.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, which:
	•	Inputs:
	•	Lambda : REAL – the average number of expected events (λ)
	•	K : INT – the number of observed events
	•	Output:
	•	Probability : REAL – the result of the Poisson distribution calculation:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Steps to implement:
	1.	Calculate the exponential component using EXP(-Lambda)
	2.	Raise Lambda to the power of K using POW(Lambda, K)
	3.	Compute K! using a loop
	4.	Combine all terms to get the result
	•	Comment your code to explain:
	•	The mathematical basis of the Poisson formula
	•	Why and how the factorial is computed manually
	•	How the block handles edge cases such as K < 0 or Lambda ≤ 0
	•	Optimize for real-time use:
	•	Avoid recursion
	•	Keep loop depth fixed
	•	Use REAL types to minimize overflow

⸻

🟨 R (Result) – The Expected Outcome

The result is a modular and reusable function block that:
	•	Accurately computes the Poisson probability
	•	Is safe for use in PLC environments, with deterministic execution
	•	Handles edge cases and overflows gracefully
	•	Can be applied in:
	•	Event prediction (e.g., machine faults)
	•	Production variability modeling
	•	Queue arrival simulations
	•	Provides an essential statistical tool for real-time diagnostic or prediction logic

⸻

🟦 E (Example) – A Practical Use Case

Imagine a sensor that detects metal parts passing on a conveyor belt. If the expected average rate is 4 parts/min (λ = 4), and 2 parts are observed in one minute (K = 2), this block calculates the probability of that event:

// INPUT: Lambda := 4.0; K := 2
// OUTPUT: Probability ≈ 0.1465

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to compute Poisson probabilities (P(k; λ)) for industrial event prediction, with input validation, numerical stability safeguards, and diagnostic logging for PLC environments.  

*(Key focus: Statistical calculation, edge-case handling, and real-time applicability in automation systems.)*
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation and process monitoring, it’s often important to predict the likelihood of discrete events occurring over a period of time—such as sensor triggers, part arrivals, or faults. The Poisson distribution is widely used in such event-driven systems to estimate the probability of a certain number of events happening within a fixed interval. However, most IEC 61131-3 Structured Text environments do not provide built-in statistical functions, making it necessary to implement this computation manually and carefully handle numerical stability and factorials.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, which:
	•	Inputs:
	•	Lambda : REAL – the average number of expected events (λ)
	•	K : INT – the number of observed events
	•	Output:
	•	Probability : REAL – the result of the Poisson distribution calculation:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Steps to implement:
	1.	Calculate the exponential component using EXP(-Lambda)
	2.	Raise Lambda to the power of K using POW(Lambda, K)
	3.	Compute K! using a loop
	4.	Combine all terms to get the result
	•	Comment your code to explain:
	•	The mathematical basis of the Poisson formula
	•	Why and how the factorial is computed manually
	•	How the block handles edge cases such as K < 0 or Lambda ≤ 0
	•	Optimize for real-time use:
	•	Avoid recursion
	•	Keep loop depth fixed
	•	Use REAL types to minimize overflow

⸻

🟨 R (Result) – The Expected Outcome

The result is a modular and reusable function block that:
	•	Accurately computes the Poisson probability
	•	Is safe for use in PLC environments, with deterministic execution
	•	Handles edge cases and overflows gracefully
	•	Can be applied in:
	•	Event prediction (e.g., machine faults)
	•	Production variability modeling
	•	Queue arrival simulations
	•	Provides an essential statistical tool for real-time diagnostic or prediction logic

⸻

🟦 E (Example) – A Practical Use Case

Imagine a sensor that detects metal parts passing on a conveyor belt. If the expected average rate is 4 parts/min (λ = 4), and 2 parts are observed in one minute (K = 2), this block calculates the probability of that event:

// INPUT: Lambda := 4.0; K := 2
// OUTPUT: Probability ≈ 0.1465

This value helps in understanding the likelihood of such an event, which is crucial for real-time monitoring and control decisions in industrial systems.

⸻

In summary, the PoissonProbability function block is a practical and reusable tool for industrial automation systems, enabling real-time event-driven probabilistic analysis using IEC 61131-3 Structured Text. It’s designed to be both mathematically sound and efficient for PLC execution, with comments explaining the steps and considerations for real-world use.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value (k). Ensure that the implementation is clear, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved.

⸻

🟩 A (Action) – How to Do It

	•	Define the function block with inputs:
	•	Lambda : REAL – the average number of expected events (λ)
	•	K : INT – the number of observed events
	•	Define the output:
	•	Probability : REAL – the result of the Poisson distribution calculation:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Implement the steps:
	•	Compute the exponential component using the built-in EXP function
	•	Compute \lambda^k using the built-in POWER function
	•	Compute the factorial of k using a loop
	•	Combine all terms to get the Poisson probability
	•	Add comments to explain:
	•	The mathematical basis of the Poisson formula
	•	How the factorial is calculated
	•	How the function block handles edge cases
	•	Optimize for real-time use:
	•	Avoid recursion
	•	Keep the loop structure simple and efficient
	•	Use REAL types to minimize overflow risk
	•	Include detailed comments on the computational steps and the mathematical formula

⸻

🟨 G (Goal) – What You’re Aiming For

The goal is to create a reliable and reusable function block that:
	•	Computes the Poisson distribution accurately
	•	Is optimized for real-time execution in PLC environments
	•	Handles edge cases and potential numerical issues
	•	Is well-documented with comments explaining the mathematical
