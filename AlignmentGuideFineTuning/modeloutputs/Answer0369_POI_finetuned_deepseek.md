### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, including error handling and relational outputs (equal/greater/less), ensuring robustness against floating-point rounding errors in industrial control logic.

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
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, including error handling and relational outputs (equal/greater/less), ensuring robustness against floating-point rounding errors in industrial control logic.
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
	•	Valid : BOOL (indicates valid input)
FUNCTION_BLOCK RealComparator
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
END_VAR

VAR_OUTPUT
    Equal : BOOL;
    Greater : BOOL;
    Less : BOOL;
    Error : BOOL;
    Valid : BOOL;
END_VAR

VAR
    Scale : REAL;
    Rounded1 : INT;
    Rounded2 : INT;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Validate inputs
    IF Precision < 0 THEN
        Error := TRUE;
        Valid := FALSE;
        RETURN;
    END_IF;

    // Scale inputs to specified precision
    Scale := POWER(10, Precision);
    Rounded1 := REAL_TO_INT(Input1 * Scale);
    Rounded2 := REAL_TO_INT(Input2 * Scale);

    // Compare rounded values
    Equal := (Rounded1 = Rounded2);
    Greater := (Rounded1 > Rounded2);
    Less := (Rounded1 < Rounded2);

    // Set outputs
    Equal := Equal AND Valid;
    Greater := Greater AND Valid;
    Less := Less AND Valid;
    Error := NOT Valid;
    Valid := TRUE;
END_METHOD

METHOD Reset : BOOL
VAR_INPUT
    Reset : BOOL;
END_VAR

IF Reset THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
    Valid := FALSE;
END_IF;
END_METHOD

METHOD SetInput : BOOL
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
END_VAR

IF SetInput THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
    Valid := FALSE;

    // Reset outputs
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
    Valid := FALSE;

    // Set inputs
    Input1 := Input1;
    Input2 := Input2;
    Precision := Precision;

    // Execute comparison
