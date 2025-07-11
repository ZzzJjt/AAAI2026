### Intent:
The task is to implement a Simplex algorithm function block in IEC 61131-3 Structured Text for solving linear programming problems with up to 5 variables and constraints in industrial control applications.

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
The task is to implement a Simplex algorithm function block in IEC 61131-3 Structured Text for solving linear programming problems with up to 5 variables and constraints in industrial control applications.
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
	6.	Test the function block with various inputs to ensure correctness and performance.

**Poisson Distribution:**

The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed time interval. It is widely used in various fields, including physics, finance, and engineering, to model the occurrence of rare events. In industrial systems, the Poisson distribution can be applied to event-driven processes, such as machine failures, sensor triggers, or counting occurrences over time.

The Poisson distribution is defined by its mean (λ) and the number of events (k) that have occurred. The probability of k events occurring in a given time interval is given by the formula:

P(k; λ) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}

where e is the base of the natural logarithm (approximately 2.71828), and k! is the factorial of k (the product of all positive integers up to k).

To implement the Poisson distribution in IEC 61131-3 Structured Text, we can create a function block named PoissonProbability that accepts two inputs: Lambda (the mean number of expected events) and K (the observed number of events). The function block will output the Poisson probability P(k; λ).

To compute the factorial of k, we can use a loop to iterate from 1 to k and multiply the current factorial by the next integer. This approach ensures deterministic execution within a PLC scan cycle.

To handle potential limitations, such as large values of λ or k, we can implement error checks and consider clamping k to a safe maximum value. Additionally, we should be aware of precision loss when λ is large or k is too high, and take steps to mitigate it, such as using higher precision data types or scaling the inputs.

The Poisson distribution has numerous practical applications in industrial systems, including:

1. Predicting machine failure frequency: By modeling the rate of machine failures, we can estimate the probability of a failure occurring within a specific time frame. This information can be used to schedule maintenance or allocate resources more effectively.
2. Modeling error rates in communication packets: In networked systems, the Poisson distribution can be used to estimate the probability of packet loss or transmission errors. This can help in designing reliable communication protocols or optimizing network performance.
3. Monitoring sensor triggers: By analyzing the frequency of sensor triggers, we can
