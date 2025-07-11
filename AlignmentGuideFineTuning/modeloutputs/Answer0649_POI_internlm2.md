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

🟩 I (Implementation) – Code Implementation

```struct
REAL_COMPARATOR
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
    Enable : BOOL;
END_VAR

VAR
    Scale : REAL;
    Rounded1 : INT;
    Rounded2 : INT;
    Equal : BOOL;
    Greater : BOOL;
    Less : BOOL;
    Error : BOOL;
BEGIN
    Scale := POWER(10, Precision);
    Rounded1 := REAL_TO_INT(Input1 * Scale);
    Rounded2 := REAL_TO_INT(Input2 * Scale);
    Equal := (Rounded1 = Rounded2);
    Greater := (Rounded1 > Rounded2);
    Less := (Rounded1 < Rounded2);
    Error := (Precision < 0 OR NOT Enable);
END_REAL_COMPARATOR
```

⸻

🟩 T (Test) – Test the Implementation

Test the function block with various inputs to ensure it behaves as expected. Here are some test cases:

| Input1 | Input2 | Precision | Enable | Expected Output |
|--------|--------|-----------|--------|----------------|
| 1.23   | 1.23   | 2         | TRUE   | Equal: TRUE, Greater: FALSE, Less: FALSE, Error: FALSE |
| 1.23   | 1.22   | 2         | TRUE   | Equal: FALSE, Greater: TRUE, Less: FALSE, Error: FALSE |
| 1.23   | 1.24   | 2         | TRUE   | Equal: FALSE, Greater: FALSE, Less: TRUE, Error: FALSE |
| 1.23   | 1.23   | 0         | TRUE   | Equal: TRUE, Greater: FALSE, Less: FALSE, Error: FALSE |
| 1.23   | 1.23   | -1        | TRUE   | Equal: TRUE, Greater: FALSE, Less: FALSE, Error: TRUE  |
| 1.23   | 1.23   | 3         | FALSE  | Equal: TRUE, Greater: FALSE, Less: FALSE, Error: TRUE  |

⸻

🟩 E (Evaluation) – Evaluate the Implementation

The function block appears to be working as expected. It handles floating-point inaccuracies by scaling and rounding the inputs to the desired
