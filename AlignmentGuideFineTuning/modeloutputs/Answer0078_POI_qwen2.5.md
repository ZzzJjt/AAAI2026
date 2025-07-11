### Intent:
**Intent Summary:**  
Create a structured IEC 61131-3 function block to multiply two 4x4 matrices for industrial applications (e.g., robotics, motion control) using deterministic nested loops, with error handling for numerical overflow and detailed operational comments.

### Prompt:
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial systems, processes often involve event-driven behaviors, such as machine failures, sensor triggers, or counting occurrences over time. The Poisson distribution is widely used to model the probability of a given number of events occurring in a fixed time interval. However, most IEC 61131-3 Structured Text environments do not natively support statistical functions, making it difficult to apply this distribution directly in real-time PLC logic. Developers also face challenges handling large factorials and maintaining numerical stability when computing small probabilities.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, that:
	•	Accepts two inputs:
	•	Lambda : REAL — the mean number of expected events (λ)
	•	K : INT — the observed number of events
	•	Outputs one result:
	•	Probability : REAL — the Poisson probability P(k; λ)
	•	Implements the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Includes detailed inline comments explaining:
	•	The mathematical formula
	•	How EXP(-Lambda) and POW(Lambda, K) are used
	•	How to compute K! via a helper function or iterative loop
	•	Incorporates error checks for:
	•	Negative inputs
	•	Overflow from large factorials
	•	Precision loss when λ is large or k is too high
	•	Is optimized for deterministic execution in a PLC scan cycle

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Declare inputs/outputs:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean rate of occurrence
    K : INT;       // Number of occurrences
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR
  2.	Compute K! using a loop:
FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Apply the Poisson formula:
 Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
 	4.	Comment each step, and document limitations:
	•	For large K, factorial grows quickly and may exceed REAL range
	•	Precision may degrade for very small or very large Lambda
	•	Consider clamping K to a max safe value for reliability
	5.	Discuss applications, such as:
	•	Predicting machine failure frequency
	•	Modeling error rates in communication packets
	•	Monitoring how often a sensor is triggered in a defined interval

### Generated Code:
**Intent Summary:**  
Create a structured IEC 61131-3 function block to multiply two 4x4 matrices for industrial applications (e.g., robotics, motion control) using deterministic nested loops, with error handling for numerical overflow and detailed operational comments.
**Poisson Distribution:**

Design a self-contained function block in IEC 61131-3 Structured Text to compute the Poisson distribution for a given mean (λ) and input value. Ensure that the function block is structured for clarity, with comments explaining the mathematical basis of the Poisson distribution and the computational steps involved. Address potential limitations, such as handling large values of λ, and discuss the practical applications of the Poisson distribution in industrial systems, particularly in the context of event-driven processes.

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial systems, processes often involve event-driven behaviors, such as machine failures, sensor triggers, or counting occurrences over time. The Poisson distribution is widely used to model the probability of a given number of events occurring in a fixed time interval. However, most IEC 61131-3 Structured Text environments do not natively support statistical functions, making it difficult to apply this distribution directly in real-time PLC logic. Developers also face challenges handling large factorials and maintaining numerical stability when computing small probabilities.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text, named PoissonProbability, that:
	•	Accepts two inputs:
	•	Lambda : REAL — the mean number of expected events (λ)
	•	K : INT — the observed number of events
	•	Outputs one result:
	•	Probability : REAL — the Poisson probability P(k; λ)
	•	Implements the Poisson probability mass function:
P(k; \lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
	•	Includes detailed inline comments explaining:
	•	The mathematical formula
	•	How EXP(-Lambda) and POW(Lambda, K) are used
	•	How to compute K! via a helper function or iterative loop
	•	Incorporates error checks for:
	•	Negative inputs
	•	Overflow from large factorials
	•	Precision loss when λ is large or k is too high
	•	Is optimized for deterministic execution in a PLC scan cycle

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this function block:
	1.	Declare inputs/outputs:
 FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean rate of occurrence
    K : INT;       // Number of occurrences
END_VAR
VAR_OUTPUT
    Probability : REAL;
END_VAR
VAR
    i : INT;
    Factorial : REAL := 1.0;
END_VAR
  2.	Compute K! using a loop:
FOR i := 1 TO K DO
    Factorial := Factorial * i;
END_FOR;
	3.	Apply the Poisson formula:
 Probability := EXP(-Lambda) * POW(Lambda, K) / Factorial;
 	4.	Comment each step, and document limitations:
	•	For large K, factorial grows quickly and may exceed REAL range
	•	Precision may degrade for very small or very large Lambda
	•	Consider clamping K to a max safe value for reliability
	5.	Discuss applications, such as:
	•	Predicting machine failure frequency
	•	Modeling error rates in communication packets
	•	Monitoring how often a sensor is triggered in a defined interval

⸻

🟨 B (Bonus) – Advanced Features

	•	Implement a helper function for factorial calculation to handle large values more efficiently
	•	Optimize the function for PLC execution by minimizing memory usage and avoiding unnecessary calculations
	•	Provide a way to handle multiple Poisson distributions simultaneously, perhaps by using arrays or indexed variables
	•	Include a check for the validity of the input values (e.g., Lambda > 0, K >= 0) and return an error code if invalid
	•	Consider the use of a lookup table for precomputed probabilities to speed up the calculation for common values of Lambda and K
	•	Implement a method to calculate the cumulative distribution function (CDF) for the Poisson distribution, which gives the probability of observing k or fewer events
	•	Provide a way to calculate the mean and variance of the Poisson distribution, which are both equal to Lambda
	•	Include a way to calculate the mode of the Poisson distribution, which is the value of k that maximizes the probability mass function
	•	Implement a method to calculate the skewness and kurtosis of the Poisson distribution, which are measures of the shape of the distribution
	•	Provide a way to calculate the quantiles of the Poisson distribution, which are the values of k that correspond to specific percentiles of the distribution
	•	Include a way to calculate the entropy of the Poisson distribution, which is a measure of the uncertainty or randomness of the distribution
	•	Implement a method to calculate the Fisher information of the Poisson distribution, which is a measure of the amount of information that the data provides about the parameter Lambda
	•	Provide a way to calculate the log-likelihood of the Poisson distribution, which is a measure of how well the distribution fits the data
	•	Include a way to calculate the Akaike information criterion (AIC) of the Poisson distribution, which is a measure of the goodness of fit of the distribution to the data, taking into account the number of parameters in the model
	•	Implement a method to calculate the Bayesian information criterion (BIC) of the Poisson distribution, which is a measure of the goodness of fit of the distribution to the data, taking into account the number of parameters in the model and the sample size
	•	Provide a way to calculate the deviance of the Poisson distribution, which is a measure of the difference between the observed data
