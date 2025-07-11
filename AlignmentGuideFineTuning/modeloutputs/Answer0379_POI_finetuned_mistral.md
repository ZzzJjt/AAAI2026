### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL numbers with configurable decimal precision, handling rounding errors and invalid inputs, for reliable industrial control logic.  

*(Focus: Precision-aware floating-point comparison, error handling, modularity for automation systems.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, comparing floating-point numbers (REAL values) directly can lead to unpredictable results due to rounding errors and precision limits inherent to binary floating-point representation. This is especially problematic in control logic, threshold detection, or alarm handling where precise decimal-level comparisons are required. A configurable comparator that accounts for decimal precision helps ensure stable and reliable logic decisions.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs with a configurable number of decimal places. The function block should:
	•	Take Input1, Input2 : REAL and Precision : INT as inputs
	•	Round both inputs to the specified precision using a scaling method
	•	Compare the results and set output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Include input validation and an Error : BOOL output in case of invalid precision values
	•	Be written for scan-cycle safety and modular reuse

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, reusable comparator block that accurately determines equality or relational order between two REAL values up to n decimal places, ensuring:
	•	Robust performance under rounding constraints
	•	Clarity in control flow logic
	•	Safe handling of erroneous or extreme inputs
	•	Easy integration into PID tuning, setpoint checks, or quality monitoring systems

⸻

🟦 E (Example) – Concrete Illustration

Example logic (simplified):

Scale := POWER(10, Precision);
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);
Error := (Precision < 0);

Inputs:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL

Outputs:
	•	Equal, Greater, Less, Error : BOOL

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL numbers with configurable decimal precision, handling rounding errors and invalid inputs, for reliable industrial control logic.  

*(Focus: Precision-aware floating-point comparison, error handling, modularity for automation systems.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, comparing floating-point numbers (REAL values) directly can lead to unpredictable results due to rounding errors and precision limits inherent to binary floating-point representation. This is especially problematic in control logic, threshold detection, or alarm handling where precise decimal-level comparisons are required. A configurable comparator that accounts for decimal precision helps ensure stable and reliable logic decisions.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs with a configurable number of decimal places. The function block should:
	•	Take Input1, Input2 : REAL and Precision : INT as inputs
	•	Round both inputs to the specified precision using a scaling method
	•	Compare the results and set output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Include input validation and an Error : BOOL output in case of invalid precision values
	•	Be written for scan-cycle safety and modular reuse

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, reusable comparator block that accurately determines equality or relational order between two REAL values up to n decimal places, ensuring:
	•	Robust performance under rounding constraints
	•	Clarity in control flow logic
	•	Safe handling of erroneous or extreme inputs
	•	Easy integration into PID tuning, setpoint checks, or quality monitoring systems

⸻

🟦 E (Example) – Concrete Illustration

Example logic (simplified):

Scale := POWER(10, Precision);
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);
Error := (Precision < 0);

Inputs:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL

Outputs:
	•	Equal, Greater, Less, Error : BOOL
FUNCTION_BLOCK RealComparator
VAR_INPUT
    Enable : BOOL;
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
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
    ValidPrecision : BOOL;
END_VAR

METHOD Execute : VOID
BEGIN
    ValidPrecision := Precision >= 0;
    IF Enable AND ValidPrecision THEN
        Scale := POWER(10, Precision);
        Rounded1 := REAL_TO_INT(Input1 * Scale);
        Rounded2 := REAL_TO_INT(Input2 * Scale);

        Equal := (Rounded1 = Rounded2);
        Greater := (Rounded1 > Rounded2);
        Less := (Rounded1 < Rounded2);
        Error := NOT ValidPrecision;
    ELSE
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        Error := TRUE;
    END_IF;
END_METHOD

// Call Execute on rising edge of Enable
IF RisingEdge(Enable) THEN
    Execute();
END_IF;

(* IEC 61131-3 Structured Text Function Block *)
(* Purpose: Compares two REAL numbers with configurable precision *)
(* Ensures reliable comparison under rounding errors *)

FUNCTION_BLOCK RealComparator
VAR_INPUT
    Enable : BOOL;                  (* TRUE to execute comparison *)
    Input1 : REAL;                  (* First REAL value to compare *)
    Input2 : REAL;                  (* Second REAL value to compare *)
    Precision : INT;                (* Number of decimal places to compare *)
END_VAR

VAR_OUTPUT
    Equal : BOOL;                   (* TRUE if values are equal *)
    Greater : BOOL;                 (* TRUE if Input1 > Input2 *)
    Less : BOOL;
