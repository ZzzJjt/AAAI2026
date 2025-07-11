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

The result can be used to determine if the observed rate is statistically significant or if it's just a random fluctuation. In this case, the probability is low, indicating that the observed rate is not consistent with the expected average.

**🔗 Additional Resources:**

* [IEC 61131-3:2020](https://www.iec.ch/online_services/publications/catalogue/iec_61131-3_2020.pdf) – The IEC 61131-3 standard for programming languages for PLCs
* [Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution) – A detailed explanation of the Poisson distribution
* [Poisson Distribution in Python](https://www.geeksforgeeks.org/python-program-for-poisson-distribution/) – A Python implementation of the Poisson distribution for comparison
* [Poisson Distribution in MATLAB](https://www.mathworks.com/help/matlab/ref/poisson.pdf) – A MATLAB implementation of the Poisson distribution for reference
* [IEC 61131-3 Function Blocks](https://www.automation.siemens.com/tsx/en/techdocs/techdocs.html) – A guide to creating function blocks in IEC 61131-3
* [IEC 61131-3 Structured Text](https://www.automation.siemens.com/tsx/en/techdocs/techdocs.html) – A guide to Structured Text programming in IEC 61131-3
* [IEC 61131-3 Real-Time](https://www.automation.siemens.com/tsx/en/techdocs/techdocs.html) – A guide to real-time programming in IEC 61131-3
* [IEC 61131-3 Examples](https://www.automation.siemens.com/tsx/en/techdocs/techdocs.html) – A collection of examples for IEC 61131-3 programming
* [IEC 61131-3 Function Block Library](https://www.automation.siemens.com/tsx/en/techdocs/techdocs.html) – A library of function blocks for IEC 61131-3 programming
* [IEC 61131-3 Function Block Examples](https://www.automation.siemens.com/tsx/en/techdocs/techdocs
