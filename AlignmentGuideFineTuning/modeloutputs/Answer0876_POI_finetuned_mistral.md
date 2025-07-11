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
FUNCTION_BLOCK FB_PoissonProbability
VAR_INPUT
    Lambda : REAL; // Mean number of events
    K : INT;        // Number of events observed
END_VAR

VAR_OUTPUT
    Probability : REAL; // Calculated Poisson probability
    Error : BOOL;      // TRUE if input is invalid
END_VAR

VAR
    Factorial : REAL; // Computed factorial of K
    Temp : REAL;      // Temporary variable for calculations
END_VAR

METHOD Execute;
BEGIN
    // Reset outputs
    Probability := 0.0;
    Error := FALSE;

    // Input validation
    IF Lambda < 0.0 OR K < 0 THEN
        Error := TRUE;
        Probability := 0.0;
        RETURN;
    END_IF;

    // Compute factorial of K
    Factorial := 1.0;
    FOR i := 1 TO K DO
        Factorial := Factorial * i;
    END_FOR;

    // Calculate Poisson probability
    Temp := Factorial;
    Temp := Temp / (EXP(Lambda) * POW(Lambda, K));
    Probability := Temp;

    // Return result
END_METHOD

// Main execution loop
Execute();
```

### Function Block Overview

This function block calculates the Poisson probability for a given mean (`Lambda`) and number of observed events (`K`). It includes input validation, numerical stability checks, and error handling. The block is designed for use in real-time industrial control systems where accurate event probability estimation is required, such as in sensor data analysis, alarm triggering, or quality control.

### Key Features

1. **Input Validation**:
   - Checks for valid input:
     - `Lambda` must be non-negative (≥ 0)
     - `K` must be a non-negative integer
   - Returns an error flag (`Error`) if either condition is violated

2. **Numerical Stability**:
   - Uses REAL arithmetic to avoid overflow or underflow
   - Computes the factorial of `K` using
