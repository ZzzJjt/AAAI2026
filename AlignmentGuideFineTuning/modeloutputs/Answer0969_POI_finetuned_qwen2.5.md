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

**T-A-G:**

⸻

	•	Implement a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places, with configurable precision and error handling.
	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Perform the comparison using scaling and rounding to ensure precision up to the specified number of decimal places.
	•	Generate the following outputs:
	•	Equal : BOOL – TRUE if the inputs are equal within the specified precision
	•	Greater : BOOL – TRUE if Input1 is greater than Input2 within the specified precision
	•	Less : BOOL – TRUE if Input1 is less than Input2 within the specified precision
	•	Error : BOOL – TRUE if Precision is invalid (Precision < 0) or if Enable is FALSE
	•	Ensure that the function block is scan-cycle-safe, modular, and reusable for applications where precise floating-point comparisons are required, such as in industrial control systems, sensor validation, and process monitoring.  

	•	Implement a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places, with configurable precision and error handling.

	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Perform the comparison using scaling and rounding to ensure precision up to the specified number of decimal places.

	•	Generate the following outputs:
	•	Equal : BOOL – TRUE if the inputs are equal within the specified precision
	•	Greater : BOOL – TRUE if Input1 is greater than Input2 within the specified precision
	•	Less : BOOL – TRUE if Input1 is less than Input2 within the specified precision
	•	Error : BOOL – TRUE if Precision is invalid (Precision < 0) or if Enable is FALSE
	•	Ensure that the function block is scan-cycle-safe, modular, and reusable for applications where precise floating-point comparisons are required, such as in industrial control systems, sensor validation, and process monitoring.

	•	Implement a self-contained function block in IEC 61131-
