### Intent:
The task is to implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time position and velocity estimation in industrial control systems, with process noise handling and reset capability.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.

### Generated Code:
The task is to implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time position and velocity estimation in industrial control systems, with process noise handling and reset capability.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.  

**B-A-B-E:**

🟥 B (Before) – The Challenge

In industrial automation, temperature values often need to be processed in both Fahrenheit and Celsius. However, many PLC platforms lack built-in conversion utilities, and direct calculations can lead to errors or safety risks, especially when handling edge cases like absolute zero.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that:
	•	Accepts Fahrenheit input
	•	Converts it to Celsius using the formula
	•	Includes input validation to reject values below absolute zero
	•	Returns both the Celsius temperature and a boolean flag indicating the validity of the input
	•	Ensures scan-cycle-safe execution and accurate results

⸻

🟧 B (Bridge) – The Implementation Steps

	1.	Define the function block interface with:
	•	Input: Fahrenheit : REAL
	•	Outputs: Celsius : REAL, ValidInput : BOOL
	2.	Implement input validation:
	•	Reject Fahrenheit values below -459.67°F
	•	Set Celsius to 0.0 and ValidInput to FALSE for invalid inputs
	3.	Perform the conversion:
	•	Use the formula Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Include comments explaining the steps
	4.	Compile and test the function block with edge cases to ensure accuracy and safety
	5.	Replace manual calculations or external utilities with this function block in relevant control logic

⸻

🟦 E (Example) – A Code Snippet

	// FahrenheitToCelsius function block
	FUNCTION_BLOCK FahrenheitToCelsius
		FLOAT Fahrenheit : IN;
		FLOAT Celsius : OUT;
		BOOL ValidInput : OUT;

		// Input validation
		IF Fahrenheit >= -459.67 THEN
			// Conversion
			Celsius := (Fahrenheit - 32) \times 5 / 9;
			ValidInput := TRUE;
		ELSE
			Celsius := 0.0;
			ValidInput := FALSE;
		END_IF;
	END_FUNCTION_BLOCK
	// End of function block
	// (C) 2023 Your Name
	// This function block is provided under the terms of the IEC 61131-3 Struct
