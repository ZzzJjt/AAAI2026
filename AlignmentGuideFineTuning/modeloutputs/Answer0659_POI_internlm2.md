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

⸻

🟨 S (Safety) – Safety Considerations

Ensure that the function block is safe to run in a PLC scan-cycle environment. This includes:
	•	Properly handling input validation to prevent undefined behavior
	•	Ensuring that the function block does not interfere with the PLC's normal operation
	•	Providing clear error messages to aid in troubleshooting

⸻

🟩 I (Implementation) – Implementation Details

Implement the function block in IEC 61131-3 Structured Text, following the steps outlined above. Ensure that the function block is self-contained and can be easily integrated into a PLC program.

⸻

🟥 E (Evaluation) – Evaluation Criteria

Evaluate the function block based on the following criteria:
	•	Accuracy: Does the function block correctly compare the two REAL inputs up to the specified number of decimal places?
	•	Configurability: Can the precision be easily adjusted to suit different requirements?
	•	Error Handling: Does the function block handle invalid inputs and floating-point representation issues gracefully?
	•	Scan Safety: Does the function block run safely in a PLC scan-cycle environment without interfering with the PLC's normal operation?
	•	Clarity: Is the function block well-documented and easy to understand?

⸻

🟩 T (Test) – Test Cases

Test the function block with the following test cases:
	•	Input1 = 1.23456789, Input2 = 1.23456789, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.2345678, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.23456788, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.23456790, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.23456791, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.23456792, Precision = 6
	•	Input1 = 1.23456789, Input2 = 1.2345
