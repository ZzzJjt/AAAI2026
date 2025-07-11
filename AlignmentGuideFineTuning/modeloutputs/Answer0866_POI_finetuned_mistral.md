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
    Lambda : REAL; // Expected number of events (e.g., failures)
    K : INT;        // Number of observed events
END_VAR

VAR_OUTPUT
    Probability : REAL; // Computed Poisson probability
END_VAR

METHOD Execute : BOOL
BEGIN
    // Input validation: Ensure Lambda > 0 and K >= 0
    IF Lambda <= 0.0 OR K < 0 THEN
        Probability := 0.0;
        RETURN TRUE;
    END_IF;

    // Compute Poisson probability using the formula:
    // P(k; lambda) = (e^(-lambda) * lambda^k) / k!
    Probability := EXP(-Lambda) * POW(Lambda, K);

    // Normalize the result by K! to ensure summation over all k values equals 1.0
    // This is necessary to ensure the probabilities sum to 1.0 for a valid probability distribution
    Probability := Probability / FACTORIAL(K);

    RETURN TRUE;
END_METHOD

// Helper function to compute factorial (n!)
FUNCTION FACTORIAL
VAR_INPUT
    N : INT;
END_VAR
VAR
    i : INT;
    Result : REAL;
BEGIN
    Result := 1.0;
    FOR i := 2 TO N DO
        Result := Result * i;
    END_FOR;
    RETURN Result;
END_FUNCTION

// Main program entry point
Execute();
```

This implementation includes:

- A function block with input validation
- A method `Execute()` that calculates the Poisson probability using the formula `P(k; λ) = (e^(-λ) * λ^k) / k!`
- Normalization by `k!` to ensure the sum of probabilities over all `k` values equals 1.0
- A helper function `FACTORIAL(N)` to compute factorials efficiently
- A clear separation of logic for input validation, calculation, and normalization

### Real-Time Execution

The function block
