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

The result can be used to determine if the observed rate is statistically significant or if it's just a random fluctuation. In this case, the probability is 0.1465, which is relatively low, indicating that the observed rate is not significantly different from the expected rate.

⸻

🟧 E (Extension) – Additional Considerations

Consider extending the function block to handle the following:
	•	Additional inputs for the mean (λ) and observed events (K) to allow for more flexibility
	•	An option to return the cumulative Poisson distribution (P(k; λ) + P(k+1; λ) + ... + P(n; λ)) for a given upper limit (n)
	•	An option to return the inverse Poisson distribution (find λ given k and P(k; λ))
	•	An option to return the Poisson distribution for a given confidence level (e.g., 95% confidence interval)
	•	An option to return the Poisson distribution for a given time interval (e.g., 1 hour) and expected rate (e.g., 4 parts/hour)

⸻

🟨 A (Assessment) – The Evaluation Criteria

The function block should be evaluated based on the following criteria:
	•	Accuracy: The calculated probabilities should match the expected values for a range of λ and K values
	•	Safety: The function block should not cause any runtime errors or unexpected behavior
	•	Determinism: The function block should execute in a predictable and deterministic manner
	•	Clarity: The code should be well-commented and easy to understand
	•	Optimization: The function block should be optimized for real-time execution, minimizing the use of recursion and loops
	•	Extensibility: The function block should be designed to accommodate future enhancements and use cases

⸻

🟥 C (Conclusion) – The Final Thoughts

By creating a structured IEC 61131-3 function block for the Poisson distribution, you will provide a valuable tool for industrial event prediction and statistical analysis in PLC environments. This function block will enable engineers to accurately model and predict the likelihood of discrete events, improving system reliability and performance. The block's modular design, clear comments, and optimized execution will ensure its practical use in real-world applications.
