### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to calculate the Poisson probability for discrete events in real-time industrial control systems, with input validation, error handling, and numerical stability checks.

### Prompt:
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained IEC 61131-3 Structured Text function block that calculates the mean and standard deviation of an input array consisting of 100 integer values.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block named MeanStdDevCalculator with the following structure:
	•	Input:
	•	InputArray : ARRAY[1..100] OF INT
	•	Outputs:
	•	Mean : REAL
	•	StdDev : REAL
	2.	Implement the calculation logic:
	•	Mean:
	•	Sum all input values using a REAL accumulator
	•	Divide the total sum by 100.0 to get the average
	•	Standard Deviation:
	•	Loop through the array again, subtracting the mean from each element
	•	Square the difference, accumulate the squared values
	•	Divide the total by 99.0 (sample standard deviation), then apply SQRT
	3.	Add inline comments to explain:
	•	Each step of the calculation
	•	Why REAL is used instead of INT
	•	Why the divisor is 99 (N−1)
	•	How this approach ensures deterministic timing for PLC scan cycles
	4.	Address edge cases and system constraints:
	•	Prevent integer overflow by converting to REAL early
	•	Avoid floating-point precision loss
	•	Ensure the function block executes within real-time control limits

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a modular, efficient, and reusable function block that enables a PLC to compute statistical metrics in real time. This allows industrial systems to:
	•	Monitor data quality and consistency
	•	Detect process variability
	•	Trigger alarms or adjustments based on standard deviation thresholds

The function block should be easy to integrate into existing control programs and maintain performance and accuracy across scan cycles.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to calculate the Poisson probability for discrete events in real-time industrial control systems, with input validation, error handling, and numerical stability checks.
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained IEC 61131-3 Structured Text function block that calculates the mean and standard deviation of an input array consisting of 100 integer values.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block named MeanStdDevCalculator with the following structure:
	•	Input:
	•	InputArray : ARRAY[1..100] OF INT
	•	Outputs:
	•	Mean : REAL
	•	StdDev : REAL
	2.	Implement the calculation logic:
	•	Mean:
	•	Sum all input values using a REAL accumulator
	•	Divide the total sum by 100.0 to get the average
	•	Standard Deviation:
	•	Loop through the array again, subtracting the mean from each element
	•	Square the difference, accumulate the squared values
	•	Divide the total by 99.0 (sample standard deviation), then apply SQRT
	3.	Add inline comments to explain:
	•	Each step of the calculation
	•	Why REAL is used instead of INT
	•	Why the divisor is 99 (N−1)
	•	How this approach ensures deterministic timing for PLC scan cycles
	4.	Address edge cases and system constraints:
	•	Prevent integer overflow by converting to REAL early
	•	Avoid floating-point precision loss
	•	Ensure the function block executes within real-time control limits

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a modular, efficient, and reusable function block that enables a PLC to compute statistical metrics in real time. This allows industrial systems to:
	•	Monitor data quality and consistency
	•	Detect process variability
	•	Trigger alarms or adjustments based on standard deviation thresholds

The function block should be easy to integrate into existing control programs and maintain performance and accuracy across scan cycles.
(* IEC 61131-3 Structured Text: Poisson Probability Function Block *)
(* Purpose: Calculates the Poisson probability for a given mean and sample size *)

FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Mean : REAL;                  (* Mean value of Poisson distribution *)
    SampleSize : INT;            (* Number of observed events *)
END_VAR
VAR_OUTPUT
    Probability : REAL;           (* Probability of observing k events *)
END_VAR
VAR
    e : REAL;                     (* Euler's number, e = 2.71828 *)
    k : INT;                      (* Number of observed events *)
    k_factorial : REAL;           (* Factorial of k *)
    k_logarithm : REAL;           (* Logarithm of k *)
    k_sum : REAL;                 (* Sum of (e^-x) for x = 0 to k *)
    k_sum_logarithm : REAL;       (* Sum of ln(e^-x) for x = 0 to k *)
    k_sum_logarithm_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-1 *)
    k_sum_logarithm_minus_1_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-2 *)
    k_sum_logarithm_minus_1_minus_1_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-3 *)
    k_sum_logarithm_minus_1_minus_1_minus_1_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-4 *)
    k_sum_logarithm_minus_1_minus_1_minus_1_minus_1_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-5 *)
    k_sum_logarithm_minus_1_minus_1_minus_1_minus_1_minus_1_minus_1 : REAL; (* Sum of ln(e^-x) for x = 0 to k-6 *)
    k_sum_logarith
