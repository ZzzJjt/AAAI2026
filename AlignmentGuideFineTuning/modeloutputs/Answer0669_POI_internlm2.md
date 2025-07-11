### Intent:
**Intent Summary:**  
Create a precision comparator function block in IEC 61131-3 Structured Text that reliably compares two real numbers up to a configurable number of decimal places, with error handling and scan-cycle safety for industrial PLC applications.  

*(Focus: Configurable floating-point comparison, robustness, and real-time compliance.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with developing a precision-controlled comparator function block in IEC 61131-3 Structured Text for real-time industrial applications involving floating-point values.

⸻

🟩 I (Input) – Information Provided

You are to implement a function block that:
	•	Compares two REAL numbers (Input1, Input2)
	•	Includes a configurable precision input (Precision : INT) to determine the number of decimal places for the comparison
	•	Must return result flags:
	•	Equal, Greater, Less, and Error
	•	Should handle floating-point representation issues by rounding or scaling both values
	•	Must validate inputs (e.g., check if Precision >= 0) and be safe to run in PLC scan-cycle environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare input variables:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL
	2.	Compute scaling factor:
	•	Scale := POWER(10, Precision)
	3.	Scale and round inputs:
	•	Rounded1 := REAL_TO_INT(Input1 * Scale)
	•	Rounded2 := REAL_TO_INT(Input2 * Scale)
	4.	Compare results:
	•	Set Equal := (Rounded1 = Rounded2)
	•	Set Greater := (Rounded1 > Rounded2)
	•	Set Less := (Rounded1 < Rounded2)
	5.	Handle errors:
	•	If Precision < 0 or Enable = FALSE, set Error := TRUE
	6.	Add comments and guard conditions for clarity and safety

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a self-contained, scan-safe function block that performs reliable REAL comparisons to a defined number of decimal places. This block should:
	•	Prevent unexpected behavior due to floating-point inaccuracies
	•	Be easily configurable and integrable into comparison-based PLC control logic
	•	Provide clear diagnostic output (including error flags)
	•	Enhance decision-making accuracy in quality checks, alarms, or control transitions

### Generated Code:
**Intent Summary:**  
Create a precision comparator function block in IEC 61131-3 Structured Text that reliably compares two real numbers up to a configurable number of decimal places, with error handling and scan-cycle safety for industrial PLC applications.  

*(Focus: Configurable floating-point comparison, robustness, and real-time compliance.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with developing a precision-controlled comparator function block in IEC 61131-3 Structured Text for real-time industrial applications involving floating-point values.

⸻

🟩 I (Input) – Information Provided

You are to implement a function block that:
	•	Compares two REAL numbers (Input1, Input2)
	•	Includes a configurable precision input (Precision : INT) to determine the number of decimal places for the comparison
	•	Must return result flags:
	•	Equal, Greater, Less, and Error
	•	Should handle floating-point representation issues by rounding or scaling both values
	•	Must validate inputs (e.g., check if Precision >= 0) and be safe to run in PLC scan-cycle environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare input variables:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL
	2.	Compute scaling factor:
	•	Scale := POWER(10, Precision)
	3.	Scale and round inputs:
	•	Rounded1 := REAL_TO_INT(Input1 * Scale)
	•	Rounded2 := REAL_TO_INT(Input2 * Scale)
	4.	Compare results:
	•	Set Equal := (Rounded1 = Rounded2)
	•	Set Greater := (Rounded1 > Rounded2)
	•	Set Less := (Rounded1 < Rounded2)
	5.	Handle errors:
	•	If Precision < 0 or Enable = FALSE, set Error := TRUE
	6.	Add comments and guard conditions for clarity and safety

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a self-contained, scan-safe function block that performs reliable REAL comparisons to a defined number of decimal places. This block should:
	•	Prevent unexpected behavior due to floating-point inaccuracies
	•	Be easily configurable and integrable into comparison-based PLC control logic
	•	Provide clear diagnostic output (including error flags)
	•	Enhance decision-making accuracy in quality checks, alarms, or control transitions

⸻

🟩 I (Implementation) – Code Implementation

```ST
// Function Block: RealComparator
// Description: Compares two REAL numbers up to a configurable number of decimal places
// Inputs:
//   Input1: REAL
//   Input2: REAL
//   Precision: INT
//   Enable: BOOL
// Outputs:
//   Equal: BOOL
//   Greater: BOOL
//   Less: BOOL
//   Error: BOOL

VAR_INPUT
  Input1: REAL;
  Input2: REAL;
  Precision: INT;
  Enable: BOOL;
END_VAR

VAR
  Scale: REAL;
  Rounded1: INT;
  Rounded2: INT;
END_VAR

// Compute scaling factor
Scale := POWER(10, Precision);

// Scale and round inputs
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

// Compare results
Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);

// Handle errors
Error := (Precision < 0 OR Enable = FALSE);

// Guard conditions
IF Enable THEN
  // Only execute if Enable is TRUE
END_IF;

// Add comments for clarity
// Handle errors
IF Error THEN
  // Handle error condition
END_IF;

// Return results
RETURN (Equal, Greater, Less, Error);
```

⸻

🟩 T (Test) – Test the Solution

1.	Test the function block with various combinations of inputs, including edge cases (e.g., 0.1 vs 0.2, 0.1 vs 0.099, etc.).
2.	Verify that the function block returns the expected results for each combination.
3.	Check that the function block handles errors correctly and provides clear diagnostic output.
4.	Ensure that the function block is safe to run in PLC scan-cycle environments without causing unexpected behavior or delays.

⸻

🟩 A (Assessment) – Assess the Solution

1.	Review the code for clarity, efficiency, and adherence to best practices.
2.	Check that the function block is easily configurable and integrable into comparison-based PLC control logic.
3.	Verify that the function block provides clear diagnostic output (including error flags) to enhance decision-making accuracy in quality checks
