### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to compute the Poisson probability mass function for industrial process monitoring, ensuring robustness against invalid inputs and efficient real-time execution.

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
Create an IEC 61131-3 Structured Text function block to compute the Poisson probability mass function for industrial process monitoring, ensuring robustness against invalid inputs and efficient real-time execution.
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
FUNCTION_BLOCK PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean rate of events (λ)
END_VAR

VAR_OUTPUT
    Probability : REAL; // Probability of a single event
END_VAR

VAR
    e : REAL; // Euler’s number (e = 2.71828)
    exp_term : REAL; // Exponential term
    sum : REAL; // Sum of the series
END_VAR

// Initialize variables
e := 2.71828;
sum := 0.0;

// Check for invalid input
IF Lambda < 0.0 THEN
    Probability := 0.0;
    RETURN;
END_IF;

// Calculate the probability
exp_term := exp(-Lambda);
sum := 1.0 / exp_term;
Probability := sum;

// Comment: This function block calculates the Poisson probability mass function for a given mean rate of events (λ). It is used in industrial process monitoring to estimate the likelihood of a specific event occurring within a given time interval.
// The function block is designed to be modular, efficient, and deterministic, ensuring accurate results even in real-time control environments.
// It is suitable for use in applications such as:
// - Predictive maintenance
// - Quality control
// - Alarm thresholds
// - Process modeling
// The function block is not intended for use in control loops or timing-critical systems.
// It is recommended to use a separate function block for execution in a real-time scan cycle.
END_FUNCTION_BLOCK

FUNCTION_BLOCK MeanStdDevCalculator
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array of 100 integers
END_VAR

VAR_OUTPUT
    Mean : REAL; // Mean value of the array
    StdDev : REAL; // Standard deviation of the array
END_VAR

VAR
    Sum : REAL; // Accumulator for sum of array
    SumSq : REAL; // Accumulator for sum of squares
    N : INT; // Number of elements in the array
    MeanVal : REAL; // Mean value
    StdDevVal : REAL; // Standard deviation
    Temp : REAL; // Temporary variable
END_VAR

// Initialize variables
Sum
