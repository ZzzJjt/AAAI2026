### Intent:
**Intent Summary:**  
Create a precision-controlled real-number comparator function block in IEC 61131-3 Structured Text that compares two floating-point values up to *n* decimal places with configurable rounding, error handling, and output flags for equality/inequality, ensuring reliability in industrial PLC applications.  

*(Key focus: Configurable precision, robust error handling, and industrial reusability for floating-point comparisons.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to compare two REAL numbers with precision control up to a user-defined number of decimal places.

⸻

🟩 A (Action)
	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Internally calculate a scaling factor:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Compare the two values and set the appropriate output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (if Precision < 0 or Enable = FALSE)
	•	Ensure the logic is modular, scan-cycle safe, and easily reusable

⸻

🟦 G (Goal)

Deliver a robust and reusable real-number comparator function block that reliably handles floating-point comparisons with configurable precision. This will improve accuracy and reliability in PLC-based control applications involving setpoint verification, sensor thresholds, and quality control decisions.

### Generated Code:
**Intent Summary:**  
Create a precision-controlled real-number comparator function block in IEC 61131-3 Structured Text that compares two floating-point values up to *n* decimal places with configurable rounding, error handling, and output flags for equality/inequality, ensuring reliability in industrial PLC applications.  

*(Key focus: Configurable precision, robust error handling, and industrial reusability for floating-point comparisons.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to compare two REAL numbers with precision control up to a user-defined number of decimal places.

⸻

🟩 A (Action)
	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Internally calculate a scaling factor:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Compare the two values and set the appropriate output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (if Precision < 0 or Enable = FALSE)
	•	Ensure the logic is modular, scan-cycle safe, and easily reusable

⸻

🟦 G (Goal)

Deliver a robust and reusable real-number comparator function block that reliably handles floating-point comparisons with configurable precision. This will improve accuracy and reliability in PLC-based control applications involving setpoint verification, sensor thresholds, and quality control decisions.
FUNCTION_BLOCK RealComparator
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
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
    Input1_Scaled : INT;
    Input2_Scaled : INT;
END_VAR

METHOD Execute : BOOL
BEGIN
    IF NOT Enable THEN
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        Error := TRUE;
        RETURN;
    END_IF;

    // Calculate scaling factor
    Scale := 10^Precision;

    // Check for valid inputs
    IF Precision < 0 OR NOT Enable THEN
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        Error := TRUE;
        RETURN;
    END_IF;

    // Scale inputs
    Input1_Scaled := INT(Input1 * Scale);
    Input2_Scaled := INT(Input2 * Scale);

    // Compare scaled values
    Equal := Input1_Scaled = Input2_Scaled;
    Greater := Input1_Scaled > Input2_Scaled;
    Less := Input1_Scaled < Input2_Scaled;

    Error := FALSE;
END_METHOD

METHOD SetPrecision : INT
VAR_INPUT
    Precision : INT;
END_VAR

VAR
    ValidInput : BOOL;
END_VAR

METHOD ExecuteSetPrecision : BOOL
BEGIN
    IF Precision < 0 THEN
        Error := TRUE;
        RETURN;
    END_IF;

    Precision := MAX(0, MIN(100, Precision));
    ValidInput := TRUE;
END_METHOD
END_FUNCTION_BLOCK

# IEC 61131-3 Structured Text: Real Comparator Function Block
# Purpose: Compares two real numbers up to a specified number of decimal places
#          Includes configurable precision, error handling, and scan-cycle safety

FUNCTION_BLOCK RealComparator
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Enable : BOOL;
    Precision : INT
