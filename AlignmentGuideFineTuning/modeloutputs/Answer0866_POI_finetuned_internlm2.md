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

The function block should be easy to integrate into existing control programs and maintain performance and accuracy across scan cycles. It should also be robust against edge cases and system constraints, ensuring reliable operation in industrial environments.

**R:**

🟥 R (Role) – Who You Are

You are a control engineer responsible for developing self-contained function blocks in IEC 61131-3 Structured Text for industrial automation systems. Your role is to create modular, efficient, and reusable code that can be easily integrated into control logic, ensuring reliable operation and data processing in real-time environments.

**C:**

🟥 C (Context) – What You Need to Know

You are tasked with creating a function block to calculate the mean and standard deviation of an array of 100 integer values. This function block will be used in industrial control systems to monitor data quality and consistency, detect process variability, and trigger alarms or adjustments based on standard deviation thresholds. The function block must be modular, efficient, and self-contained, ensuring that it can be easily integrated into existing control programs and maintain performance and accuracy across scan cycles. You must also address edge cases and system constraints, ensuring that the function block is robust against integer overflow, floating-point precision loss, and real-time control limits.

**I:**

🟥 I (Input) – What You Need to Consider

When developing the function block, consider the following:

•	Input: An array of 100 integer values
•	Output: The mean and standard deviation of the input array
•	Modularity: Ensure the function block is self-contained and can be easily integrated into control logic
•	Efficiency: Optimize the calculation logic to minimize processing time and ensure deterministic timing for PLC scan cycles
•	Robustness: Address edge cases and system constraints, such as preventing integer overflow and avoiding floating-point precision loss
•	Reusability: Design the function block to be easily adaptable for use in other control applications

**O:**

🟥 O (Output) – What You Need to Produce

Create a self-contained IEC 61131-3 Structured Text function block named MeanStdDevCalculator that calculates the mean and standard deviation of an input array consisting of 100 integer values. The function block should include detailed comments explaining each step of the calculation, including the use of REAL instead of INT and the divisor of 99 for the standard deviation. Address potential issues related to integer overflow, floating-point precision, and real-time control constraints. Ensure that the function block is modular, efficient
