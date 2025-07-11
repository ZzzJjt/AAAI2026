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
(* IEC 61131-3 Structured Text Function Block for a Precision Comparator *)
(* Compares two REAL inputs up to n decimal places with configurable precision *)
(* Uses scaling and rounding to improve accuracy and robustness *)
(* Conforms to industrial PLC standards for reusability and scan-cycle safety *)

FUNCTION_BLOCK PrecisionComparator
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable comparison *)
    Input1 : REAL;                  (* First REAL input value *)
    Input2 : REAL;                  (* Second REAL input value *)
    Precision : INT;                (* Number of decimal places for comparison, e.g., 2, 3, 4 *)
END_VAR

VAR_OUTPUT
    Equal : BOOL;                   (* TRUE if Input1 = Input2 within precision *)
    Greater : BOOL;                 (* TRUE if Input1 > Input2 within precision *)
    Less : BOOL;                    (* TRUE if Input1 < Input2 within precision *)
    Error : BOOL;                   (* TRUE if invalid Precision or Enable = FALSE *)
END_VAR

VAR
    Scale : REAL;                   (* Scaling factor for precision *)
    Rounded1 : INT;                 (* Rounded Input1 *)
    Rounded2 : INT;                 (* Rounded Input2 *)
    Temp1 : REAL;                   (* Temporary variable for scaling *)
    Temp2 : REAL;                   (* Temporary variable for scaling *)
    AbsDiff : REAL;                 (* Absolute difference *)
    ValidPrecision : BOOL;          (* Flag for valid Precision input *)
END_VAR

(* Initialize outputs *)
Equal := FALSE;
Greater := FALSE;
Less := FALSE;
Error := FALSE;

(* Check Enable and Precision *)
IF Enable AND Precision >= 0 THEN
    (* Calculate scaling factor *)
    Scale := POWER(10.0, Precision);

    (* Scale and round inputs *)
    Temp1 := Input1 * Scale;
    Rounded1 := ROUND(Temp1);
    Temp2 := Input2 * Scale;
    Rounded2 := ROUND(Temp2);
