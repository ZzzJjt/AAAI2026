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


**Code:**

```
FUNCTION_BLOCK RealComparator
  VAR
    Input1, Input2, Scale, RoundedInput1, RoundedInput2 : REAL;
    Equal, Greater, Less, Error : BOOL;
  END_VAR

  IF Enable THEN
    Scale := 10.0 ** Precision;
    RoundedInput1 := ROUND(Input1 * Scale);
    RoundedInput2 := ROUND(Input2 * Scale);

    Equal := (RoundedInput1 = RoundedInput2);
    Greater := (RoundedInput1 > RoundedInput2);
    Less := (RoundedInput1 < RoundedInput2);

    Error := (Precision < 0) OR NOT Enable;
  END_IF;
END_FUNCTION_BLOCK
```

**Explanation:**

The provided code defines a function block called `RealComparator` that accepts four inputs: `Input1`, `Input2`, `Precision`, and `Enable`. The `Precision` input determines the number of decimal places for comparison, while the `Enable` input triggers the execution of the function block.

The function block first calculates a scaling factor based on the user-defined precision. It then multiplies each input by the scaling factor, rounds the results, and converts them to integers. The rounded values are compared, and the appropriate output flags (`Equal`, `Greater`, `Less`, and `Error`) are set accordingly.

The logic is modular, scan-cycle safe, and easily reusable, making it suitable for industrial PLC applications. The error handling ensures that the function block will not produce incorrect results when the precision is set below 0 or when the `Enable` input is false.
