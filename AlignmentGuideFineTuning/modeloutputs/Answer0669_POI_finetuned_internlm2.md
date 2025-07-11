### Intent:
**Intent Summary:**  
Create a precision comparator function block in IEC 61131-3 Structured Text that reliably compares two real numbers up to a configurable number of decimal places, with error handling and scan-cycle safety for industrial PLC applications.  

*(Focus: Configurable floating-point comparison, robustness, and real-time compliance.)*

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
Create a precision comparator function block in IEC 61131-3 Structured Text that reliably compares two real numbers up to a configurable number of decimal places, with error handling and scan-cycle safety for industrial PLC applications.  

*(Focus: Configurable floating-point comparison, robustness, and real-time compliance.)*
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

🟪 A (Action) – Execute the Plan

Implement the function block in IEC 61131-3 Structured Text, ensuring it handles precision, rounding, and error conditions as described in the steps above. Include comments and safety checks to make the block self-contained and suitable for industrial automation.

**🔶 R-E-S-P-O-N-S-E 🟥**

R – Role

A PLC programmer responsible for developing a precision comparator function block in IEC 61131-3 Structured Text for real-time industrial applications.

E – Environment

The function block should be self-contained, with no external dependencies, and able to handle real-time comparisons of floating-point values with configurable precision. It should be safe to run in a PLC scan-cycle environment, with clear error handling and diagnostic output.

P – Process

Implement a function block in IEC 61131-3 Structured Text to compare two real inputs up to a configurable number of decimal places. Include input validation, error handling, and clear output flags for equal, greater, less, and error conditions. Ensure the block is self-contained and safe to run in a PLC scan cycle.

S – Skills

🟥 R – Role

A PLC programmer responsible for developing a precision comparator function block in IEC 61131-3 Structured Text for real-time industrial applications.

E – Environment

The function block should be self-contained, with no external dependencies, and able to handle real-time comparisons of floating-point values with configurable precision. It should be safe to run in a PLC scan-cycle environment, with clear error handling and diagnostic output.

P – Process

Implement a function block in IEC 61131-3 Structured Text to compare two real inputs up to a configurable number of decimal places. Include input validation, error handling, and clear output flags for equal, greater, less, and error conditions. Ensure the block is self-contained and safe to run in a PLC scan cycle.

A – Action

Develop a function block in IEC 61131-3 Structured Text to compare two real inputs up to a configurable number of decimal places. Ensure the block handles input validation, rounding, and error conditions, and is self-contained and safe to run in a PLC scan cycle.

R – Result

Implement a function block in IEC 61131-3
