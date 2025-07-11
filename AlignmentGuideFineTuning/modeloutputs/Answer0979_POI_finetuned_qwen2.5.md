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

**T-A-G:**

🟥 T（Task）

Implement a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places. Include configurable precision and error handling.

⸻

🟩 A（Action）

	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Scale the inputs based on the precision:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Perform the comparison:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Generate an Error flag if Precision is invalid or Enable is FALSE
	•	Ensure scan-cycle safety and modularity for reuse in PLC logic

⸻

🟦 G（Goal）

Create a reliable and configurable comparator that handles floating-point values with precision control, improving accuracy in industrial control systems where real-time decisions depend on precise numerical comparisons.

**T-A-G:**

🟥 T（Task）

Implement a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places. Include configurable precision and error handling.

⸻

🟩 A（Action）

	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Scale the inputs based on the precision:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Perform the comparison:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Generate an Error flag if Precision is invalid or Enable is FALSE
	•	Ensure scan-cycle safety and modularity for reuse in PLC logic

⸻

🟦 G（Goal）

Create a reliable and configurable comparator that handles floating-point values with precision control, improving accuracy in industrial control systems where real-time decisions depend on precise numerical comparisons.

**T-A-G:**

🟥 T（Task
