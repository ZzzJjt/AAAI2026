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
FUNCTION_BLOCK RealComparatorFB
VAR_INPUT
    Enable : BOOL; // Enable comparison when TRUE
    Input1 : REAL; // First input value
    Input2 : REAL; // Second input value
    Precision : INT; // Number of decimal places to compare
END_VAR

VAR_OUTPUT
    Equal : BOOL; // TRUE if Input1 and Input2 are equal up to Precision
    Greater : BOOL; // TRUE if Input1 > Input2 up to Precision
    Less : BOOL; // TRUE if Input1 < Input2 up to Precision
    Error : BOOL; // TRUE if Precision is invalid
END_VAR

VAR
    Scale : REAL; // Scaling factor for precision
    Rounded1 : INT; // Scaled and rounded Input1
    Rounded2 : INT; // Scaled and rounded Input2
    ValidPrecision : BOOL; // Flag to check if Precision is valid
END_VAR

// Initialize outputs to FALSE and Error to TRUE when disabled
IF NOT Enable THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := TRUE;
    RETURN;
END_IF;

// Validate Precision input
ValidPrecision := (Precision >= 0);

// Set outputs to default values if Precision is invalid
IF NOT ValidPrecision THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := TRUE;
    RETURN;
END_IF;

// Calculate scaling factor based on Precision
Scale := POWER(10, Precision);

// Round and compare inputs
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

// Set outputs based on comparison results
Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);

// Reset Error flag if Precision is valid
Error := FALSE;

// Set outputs to default values if Enable is FALSE
IF NOT Enable THEN
    Equal := FALSE;
    Greater := FALSE
