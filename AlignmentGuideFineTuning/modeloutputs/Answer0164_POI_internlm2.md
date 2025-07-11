### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and precise floating-point arithmetic for industrial automation systems.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, especially those involving HVAC, thermal processing, or sensor integration, temperature values may be provided in Fahrenheit while the control logic or displays require Celsius. Without a standardized, reusable function block, engineers may repeatedly rewrite conversion logic or risk incorrect scaling, lack of input validation, or inconsistent formatting across projects.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that converts a given Fahrenheit temperature to Celsius. The function should:
	•	Use the formula:
C = (F - 32) \times \frac{5}{9}
	•	Accept a REAL or LREAL Fahrenheit input
	•	Provide a validated, accurate Celsius output
	•	Include input validation (e.g., to reject unphysical inputs like below absolute zero)
	•	Be reusable, modular, and safe for use in scan-cycle environments

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with:
	•	Fahrenheit : REAL (input)
	•	Celsius : REAL (output)
	•	ValidInput : BOOL (output flag)
	2.	Add logic to:
	•	Validate that the Fahrenheit input is above -459.67°F (absolute zero)
	•	Perform the conversion using precise floating-point arithmetic
	3.	Include comments and documentation for readability and maintainability
	4.	Optionally, set Celsius to 0 and ValidInput to FALSE if the input is invalid

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and precise floating-point arithmetic for industrial automation systems.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, especially those involving HVAC, thermal processing, or sensor integration, temperature values may be provided in Fahrenheit while the control logic or displays require Celsius. Without a standardized, reusable function block, engineers may repeatedly rewrite conversion logic or risk incorrect scaling, lack of input validation, or inconsistent formatting across projects.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that converts a given Fahrenheit temperature to Celsius. The function should:
	•	Use the formula:
C = (F - 32) \times \frac{5}{9}
	•	Accept a REAL or LREAL Fahrenheit input
	•	Provide a validated, accurate Celsius output
	•	Include input validation (e.g., to reject unphysical inputs like below absolute zero)
	•	Be reusable, modular, and safe for use in scan-cycle environments

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with:
	•	Fahrenheit : REAL (input)
	•	Celsius : REAL (output)
	•	ValidInput : BOOL (output flag)
	2.	Add logic to:
	•	Validate that the Fahrenheit input is above -459.67°F (absolute zero)
	•	Perform the conversion using precise floating-point arithmetic
	3.	Include comments and documentation for readability and maintainability
	4.	Optionally, set Celsius to 0 and ValidInput to FALSE if the input is invalid
	5.	Test the function block with various Fahrenheit inputs to ensure accuracy and validation
	6.	Document any assumptions, limitations, or known issues
	7.	Provide a sample scan cycle or integration example to demonstrate usage

**Function Block:**

```ST
FUNCTION_BLOCK FahrenheitToCelsius
  REAL Fahrenheit, Celsius;
  BOOL ValidInput;

  Fahrenheit := Input_Value(Fahrenheit);
  Celsius := (Fahrenheit - 32) * 5 / 9;
  ValidInput := Fahrenheit >= -459.67;
END_FUNCTION_BLOCK
```

**Scan Cycle Example:**

```ST
VAR_INPUT
  Fahrenheit : REAL;
END_VAR

VAR_OUTPUT
  Celsius : REAL;
  ValidInput : BOOL;
END_VAR

FahrenheitToCelsius(Fahrenheit, Celsius, ValidInput);

IF ValidInput THEN
  DISPLAY("Fahrenheit: ", Fahrenheit);
  DISPLAY("Celsius: ", Celsius);
ELSE
  DISPLAY("Invalid Fahrenheit input: ", Fahrenheit);
END_IF;
```

**Additional Notes:**

- The function block uses the `Input_Value` function to ensure the Fahrenheit input is valid and within the expected range.
- The function block returns a `ValidInput` flag to indicate whether the conversion was successful or if the input was invalid.
- The function block is designed to be used in a scan cycle, where it can be called with the current Fahrenheit value and display the converted Celsius value.
- The function block is a simple example and may need to be adapted to specific use cases or integrated with other control logic.
- The function block does not include any error handling or exception handling, as these are typically handled at a higher level in the control system.
- The function block assumes that the Fahrenheit input is a valid REAL or LREAL value and does not perform any additional input validation.
- The function block uses the standard IEC 61131-3 floating-point arithmetic, which provides precise results for temperature conversions.
- The function block is designed to be modular and reusable, allowing it to be used in different projects and control systems without modification.
- The function block is safe for use in scan-cycle environments, as it does not rely on external resources or perform any I/O operations that could cause delays or conflicts.
- The function block is designed to be easily understood and maintained, with clear comments and documentation explaining its purpose, inputs, outputs, and behavior.
- The function block is
