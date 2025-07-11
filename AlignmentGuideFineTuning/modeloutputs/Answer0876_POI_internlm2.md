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

The function block should be easy to integrate into existing control programs and maintain performance and accuracy across scan cycles. It should also be adaptable to different data types and array sizes, as long as the input array is of fixed size.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained IEC 61131-3 Structured Text function block that calculates the Poisson probability for discrete events in real-time industrial control systems. The function block should include input validation, error handling, and numerical stability checks.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block named PoissonProbabilityCalculator with the following structure:
	•	Input:
	•	Events : INT
	•	Time : REAL
	•	Outputs:
	•	Probability : REAL
	2.	Implement the calculation logic:
	•	Check if the input values are valid:
	•	Events must be a non-negative integer
	•	Time must be a non-negative real number
	•	If the input values are invalid, return an error code or set a flag
	•	Calculate the Poisson probability using the formula:
	•	Probability = (Events^Time) * (Time^Events) * EXP(-Events * Time)
	•	Ensure numerical stability by using the LN function to calculate EXP
	3.	Add inline comments to explain:
	•	Each step of the calculation
	•	Why the input values must be non-negative
	•	How the LN function improves numerical stability
	4.	Handle potential issues related to overflow or precision:
	•	Use the LN function to calculate EXP instead of directly raising to a power
	•	Ensure the function block executes within real-time control limits

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a function block that accurately calculates the Poisson probability for discrete events in real-time industrial control systems. This allows industrial systems to:
	•	Analyze event occurrence rates
	•	Assess the likelihood of specific event sequences
	•	Optimize resource allocation and prevent bottlenecks

The function block should be easy to integrate into existing control programs and maintain performance and accuracy across scan cycles. It should also be adaptable to different data types and array sizes, as long as the input values are of fixed type.

**T-A-G:**

🟥 T (Task
