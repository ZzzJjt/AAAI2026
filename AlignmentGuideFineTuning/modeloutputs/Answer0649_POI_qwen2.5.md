### Intent:
**Intent Summary:**  
Create a structured text function block to compare two real numbers with configurable decimal precision, handling floating-point inaccuracies and providing comparison results (equal/greater/less) with error detection for PLC applications.

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
Create a structured text function block to compare two real numbers with configurable decimal precision, handling floating-point inaccuracies and providing comparison results (equal/greater/less) with error detection for PLC applications.
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

**Note:** The function block should be designed with PLC safety and efficiency in mind, ensuring it can be used in real-time control systems without causing scan-cycle delays or errors. **Real Comparator Function Block in IEC 61131-3 Structured Text**

```structuredtext
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

// Step 1: Declare input variables
// Step 2: Compute scaling factor
Scale := POWER(10, Precision);

// Step 3: Scale and round inputs
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

// Step 4: Compare results
Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);

// Step 5: Handle errors
IF Precision < 0 OR NOT Enable THEN
    Error := TRUE;
ELSE
    Error := FALSE;
END_IF;

// Step 6: Add comments and guard conditions for clarity and safety
// Ensure Precision is non-negative and Enable is true for valid operation
// This function block is designed to be used in real-time control systems
// without causing scan-cycle delays or errors.
END_FUNCTION_BLOCK
```

**Explanation:**

1. **Input Variables:**
   - `Input1` and `Input2`: The two real numbers to be compared.
   - `Precision`: The number of decimal places to consider for the comparison.
   - `Enable`: A boolean flag to enable or disable the comparison.

2. **Output Variables:**
   - `Equal`: True if `Input1` equals `Input2` within the specified precision.
   - `Greater`: True if `Input1` is greater than `Input2` within the specified precision.
   - `Less`: True if `Input1` is less than `Input2` within the specified precision.
   - `Error`: True if there is an error in the input parameters (e.g., negative precision or disabled comparison).

3. **Internal Variables:**
   - `Scale`: The scaling factor used to
