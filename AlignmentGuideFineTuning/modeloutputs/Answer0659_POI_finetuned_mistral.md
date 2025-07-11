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
FUNCTION_BLOCK FB_RealComparator
VAR_INPUT
    Enable : BOOL; // Enable comparison
    Input1 : REAL; // First input value
    Input2 : REAL; // Second input value
    Precision : INT; // Number of decimal places for comparison
END_VAR

VAR_OUTPUT
    Equal : BOOL; // TRUE if Input1 = Input2
    Greater : BOOL; // TRUE if Input1 > Input2
    Less : BOOL; // TRUE if Input1 < Input2
    Error : BOOL; // TRUE if invalid input or Enable = FALSE
END_VAR

VAR
    Scale : REAL; // Scaling factor for precision
    Rounded1 : INT; // Rounded Input1
    Rounded2 : INT; // Rounded Input2
    ValidInput : BOOL; // Input validation flag
END_VAR

// Initialize outputs
Equal := FALSE;
Greater := FALSE;
Less := FALSE;
Error := FALSE;

// Validate inputs
ValidInput := (Enable) AND (Precision >= 0);

// Scale and round inputs
IF ValidInput THEN
    Scale := POWER(10, Precision);
    Rounded1 := REAL_TO_INT(Input1 * Scale);
    Rounded2 := REAL_TO_INT(Input2 * Scale);

    // Compare results
    Equal := (Rounded1 = Rounded2);
    Greater := (Rounded1 > Rounded2);
    Less := (Rounded1 < Rounded2);
ELSE
    // Set error if invalid input or Enable = FALSE
    Error := TRUE;
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
END_IF;

// Reset outputs when disabled
IF NOT ValidInput OR NOT Enable THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
END_IF;

// Add comments for clarity and safety
// * Scale and round inputs to compare up to Precision decimal places
// * Use REAL_TO_INT to avoid floating-point inaccuracies
// * Validate Enable and Precision to ensure safe operation
// * Return error flag
