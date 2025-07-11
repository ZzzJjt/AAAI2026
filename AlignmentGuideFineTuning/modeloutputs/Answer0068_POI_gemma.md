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
	6.	Test the function block with a variety of inputs, including:
	•	Negative Lambda
	•	Large Lambda
	•	Large K
	•	Small K
	•	Small Probability
	•	Large Probability
	7.	Ensure the function block is deterministic and can be used in real-time PLC logic.

**Poisson Distribution:**

The Poisson distribution is a probability distribution that describes the number of events occurring in a fixed interval of time or space, given the average rate of occurrence. It is often used to model the number of occurrences of rare events, such as machine failures, sensor triggers, or counting occurrences over time.

The Poisson distribution is characterized by a single parameter, λ, which represents the average rate of occurrence. The probability of observing k events in a given interval is given by the formula:

P(k; λ) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}

where e is the base of the natural logarithm, k is the number of events, and k! is the factorial of k.

The Poisson distribution is widely used in industrial systems to model the probability of a given number of events occurring in a fixed time interval. For example, in a manufacturing process, the Poisson distribution can be used to model the probability of a machine failure occurring in a given time period. By understanding the average rate of occurrence of machine failures, a manufacturer can estimate the probability of a failure occurring and take appropriate action to minimize downtime and maintain production efficiency.

In the context of event-driven processes, the Poisson distribution can be used to model the probability of a sensor trigger occurring in a given time interval. By understanding the average rate of occurrence of sensor triggers, a system can be designed to respond appropriately to the event, such as triggering an alarm or initiating a corrective action.

The Poisson distribution is also useful in monitoring the number of occurrences of a given event over time. For example, in a communication system, the Poisson distribution can be used to model the probability of a communication packet being corrupted or lost. By understanding the average rate of occurrence of corrupted or lost packets, a system can be designed to minimize the impact of these events on the overall communication process.

In summary, the Poisson distribution is a powerful tool for modeling the probability of a given number of events occurring in a fixed time interval. It is widely used in industrial systems to model the probability of machine failures, sensor triggers, and other rare events, and can
