### Intent:
**Intent Summary:**  
Create a structured IEC 61131-3 function block to compute Poisson probabilities (given λ and *k*) for industrial event prediction, with robust handling of edge cases and numerical stability.  

*(Focus: Statistical computation for discrete event modeling in PLCs, emphasizing clarity, safety, and deterministic execution.)*

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
Create a structured IEC 61131-3 function block to compute Poisson probabilities (given λ and *k*) for industrial event prediction, with robust handling of edge cases and numerical stability.  

*(Focus: Statistical computation for discrete event modeling in PLCs, emphasizing clarity, safety, and deterministic execution.)*
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

This value helps in understanding the likelihood of such an event, which is crucial for real-time monitoring and control decisions in industrial processes.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value (k). Ensure that the implementation is clear, efficient, and includes comments explaining the mathematical basis of the Poisson distribution and the computational steps involved.

⸻

🟩 A (Action) – How to Do It

	•	Define the function block with inputs:
	•	Lambda : REAL – the average number of expected events (λ)
	•	K : INT – the number of observed events
	•	Define the output:
	•	Probability : REAL – the result of the Poisson distribution calculation
	•	Implement the Poisson probability formula:
	•	Probability := e^(-Lambda) * (Lambda^K) / Factorial(K)
	•	Implement a factorial function using a loop to compute K!
	•	Include comments explaining:
	•	The mathematical basis of the Poisson distribution
	•	How the factorial is calculated
	•	How the function block handles edge cases
	•	Optimize the implementation for real-time use:
	•	Avoid recursion
	•	Keep the loop fixed and efficient
	•	Use REAL types to minimize overflow risk
	•	Add comments to explain the steps and the mathematical foundation

⸻

🟨 G (Goal) – What You’re Aiming For

	•	A self-contained function block that:
	•	Computes the Poisson distribution accurately
	•	Is efficient and deterministic
	•	Handles edge cases properly
	•	Is reusable and maintainable
	•	Includes comments explaining the mathematical basis and computational steps
	•	Works well in PLC environments, providing a statistical tool for real-time event-driven applications
	•	Helps in applications such as event prediction, process variability modeling, and sensor-based diagnostics
	•	Ensures that the implementation is both practical and theoretically sound
	•	Is a reliable building block for further statistical analysis in industrial automation
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value.
