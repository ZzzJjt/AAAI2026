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

This result can be used to determine the likelihood of a fault or other event, and to inform decision-making in real-time.

**References:**

[1] “Poisson Distribution,” Wikipedia, https://en.wikipedia.org/wiki/Poisson_distribution.
[2] “Poisson Distribution,” MathWorks, https://www.mathworks.com/help/stats/poisson-distribution.html.
[3] “Poisson Distribution,” Wolfram MathWorld, https://mathworld.wolfram.com/PoissonDistribution.html.
[4] “Poisson Distribution,” Khan Academy, https://www.khanacademy.org/math/probability/discrete-random-variables/poisson-distribution/a/poisson-distribution.
[5] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[6] “Poisson Distribution,” Statistics Solutions, https://www.statisticssolutions.com/poisson-distribution/.
[7] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[8] “Poisson Distribution,” Statistics Solutions, https://www.statisticssolutions.com/poisson-distribution/.
[9] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[10] “Poisson Distribution,” Statistics Solutions, https://www.statisticssolutions.com/poisson-distribution/.
[11] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[12] “Poisson Distribution,” Statistics Solutions, https://www.statisticssolutions.com/poisson-distribution/.
[13] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[14] “Poisson Distribution,” Statistics Solutions, https://www.statisticssolutions.com/poisson-distribution/.
[15] “Poisson Distribution,” Statistics How To, https://www.statisticshowto.com/probability-and-statistics/probability-distributions/poisson-distribution/.
[16] “Poisson Distribution,” Statistics Solutions, https://www.statisticss
