### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compare two REAL numbers with configurable decimal precision, outputting equality/greater/less flags and handling invalid inputs, for reliable floating-point comparisons in PLC applications.  

*(Focus: Precision-controlled comparison, error handling, modularity)*

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
Create a reusable IEC 61131-3 function block to compare two REAL numbers with configurable decimal precision, outputting equality/greater/less flags and handling invalid inputs, for reliable floating-point comparisons in PLC applications.  

*(Focus: Precision-controlled comparison, error handling, modularity)*
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

    IF Input1 = Input2 THEN
        Equal := TRUE;
        Greater := FALSE;
        Less := FALSE;
        Error := FALSE;
        RETURN;
    END_IF;

    IF Input1 > Input2 THEN
        Greater := TRUE;
        Equal := FALSE;
        Less := FALSE;
        Error := FALSE;
        RETURN;
    END_IF;

    IF Input1 < Input2 THEN
        Less := TRUE;
        Equal := FALSE;
        Greater := FALSE;
        Error := FALSE;
        RETURN;
    END_IF;

    Error := TRUE;
END_METHOD

METHOD ScaleInput : REAL
BEGIN
    IF NOT Enable THEN
        Scale := 1.0;
        RETURN;
    END_IF;

    IF Input1 = 0.0 OR Input2 = 0.0 THEN
        Scale := 1.0;
        RETURN;
    END_IF;

    Scale := 10.0 ** Precision;
END_METHOD

METHOD ScaleInputScaled : INT
BEGIN
    IF NOT Enable THEN
        Input1_Scaled := 0;
        Input2_Scaled := 0;
        RETURN;
    END_IF;

    IF Input1 = 0.0 OR Input2 = 0.0 THEN
        Input1_Scaled := 0;
        Input2_Scaled := 0;
        RETURN;
    END_IF;

    Input1_Scaled := (Input1 * Scale) + 0.5;
    Input2_Scaled := (
