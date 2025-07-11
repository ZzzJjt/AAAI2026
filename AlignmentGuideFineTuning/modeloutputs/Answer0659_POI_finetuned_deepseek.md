### Intent:
**Intent Summary:**  
Create a precision real-number comparator function block in IEC 61131-3 Structured Text that reliably compares two floating-point values up to *n* decimal places with configurable precision, error handling, and scan-cycle safety for industrial control applications.  

*(Key focus: Accurate floating-point comparison, configurability, and robustness in PLC environments.)*

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
Create a precision real-number comparator function block in IEC 61131-3 Structured Text that reliably compares two floating-point values up to *n* decimal places with configurable precision, error handling, and scan-cycle safety for industrial control applications.  

*(Key focus: Accurate floating-point comparison, configurability, and robustness in PLC environments.)*
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
FUNCTION_BLOCK RealComparator
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
    Enable : BOOL;
END_VAR

VAR_OUTPUT
    Equal : BOOL;
    Greater : BOOL;
    Less : BOOL;
    Error : BOOL;
END_VAR

VAR
    Scale : REAL;
    Rounded1 : INT;
    Rounded2 : INT;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Check inputs
    IF Precision < 0 OR Enable = FALSE THEN
        Error := TRUE;
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        RETURN;
    END_IF;

    // Scale inputs
    Scale := POWER(10, Precision);
    Rounded1 := REAL_TO_INT(Input1 * Scale);
    Rounded2 := REAL_TO_INT(Input2 * Scale);

    // Compare rounded values
    Equal := (Rounded1 = Rounded2);
    Greater := (Rounded1 > Rounded2);
    Less := (Rounded1 < Rounded2);

    Error := FALSE;
    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
//   Execute(TRUE, TRUE, 2, 10.0, 10.1); // Compare 10.0 and 10.1 up to 2 decimal places
//   Execute(TRUE, TRUE, 0, 10.0, 10.1);  // Compare 10.0 and 10.1 with no decimal places
//   Execute(FALSE, FALSE, 0, 10.0, 10.1); // Reset and compare 10.0 and 10.1
//   Execute(TRUE, TRUE, 0, 10.0, 10.1); // Compare 10.0 and 10.1 with no decimal places and enable set to FALSE
//   Execute(TRUE, TRUE, 0, 10.0, 1
