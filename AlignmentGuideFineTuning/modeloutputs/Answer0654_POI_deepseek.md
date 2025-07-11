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

⸻

🟪 I (Implementation) – Implement the Function Block

```structuredtext
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL;
END_VAR
VAR_OUTPUT
    Celsius : REAL;
    ValidInput : BOOL;
END_VAR

// Input validation
IF Fahrenheit >= -459.67 THEN
    ValidInput := TRUE;
ELSE
    ValidInput := FALSE;
    Celsius := 0.0;
END_IF

// Conversion
IF ValidInput THEN
    Celsius := (Fahrenheit - 32) \* 5 / 9;
END_IF
```

⸻

🟩 E (Explanation) – Explanation of the Function Block

The function block `FahrenheitToCelsius` takes a temperature value in Fahrenheit as input and outputs the corresponding Celsius temperature and a boolean flag indicating whether the input is valid.

1. The function block first checks if the input Fahrenheit temperature is greater than or equal to -459.67°F. If it is, the function block proceeds to perform the conversion.
2. If the input temperature is below this threshold, the function block sets the Celsius output to 0.0 and the ValidInput flag to FALSE, indicating that the input is invalid.
3. The conversion is performed using the standard formula for Fahrenheit to Celsius: Celsius = (Fahrenheit - 32) \* 5 / 9.
4. The function block includes inline comments to explain each step of the process and to ensure that the code is self-explanatory.
5. The function block is designed to be robust and can handle edge cases, such as extremely low temperatures, without causing any issues.

The function block can be easily integrated into other PLC programs and can be used for various purposes, such as displaying temperature values in the HMI, logging temperature data, or controlling temperature-based processes in industrial automation systems.
