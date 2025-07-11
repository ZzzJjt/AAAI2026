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

Deliver a robust and reusable real-number comparator function block that reliably handles floating-point comparisons with configurable precision. This will improve accuracy and reliability in PLC-based control applications involving setpoint verification, sensor thresholds, and quality control decisions. The function block should be compatible with IEC 61131-3 and easily integrated into existing PLC codebases.

**Example Usage:**

```ST
VAR
  Input1 : REAL := 3.14159;
  Input2 : REAL := 3.14;
  Precision : INT := 4;
  Equal : BOOL;
  Greater : BOOL;
  Less : BOOL;
  Error : BOOL;
END_VAR

CALL RealComparator(Input1, Input2, Precision, Equal, Greater, Less, Error);

IF Error THEN
  -- Handle error condition
ELSE
  IF Equal THEN
    -- Process equal condition
  ELSIF Greater THEN
    -- Process greater condition
  ELSIF Less THEN
    -- Process less condition
  END_IF;
END_IF;
```

**Expected Output:**

- If Input1 = Input2, Equal = TRUE, Greater = FALSE, Less = FALSE.
- If Input1 > Input2, Equal = FALSE, Greater = TRUE, Less = FALSE.
- If Input1 < Input2, Equal = FALSE, Greater = FALSE, Less = TRUE.
- If Precision < 0 or Enable = FALSE, Error = TRUE.

**Additional Considerations:**

- The function block should be designed to handle large and small floating-point values without overflow or underflow.
- The function block should be compatible with different PLC platforms and programming languages.
- The function block should be thoroughly tested and documented to ensure reliability and ease of use in industrial applications.
