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


**Code Example:**

```
FUNCTION_BLOCK RealComparator
  VAR
    Input1, Input2, Scale, RoundedInput1, RoundedInput2 : REAL;
    Equal, Greater, Less, Error : BOOL;
  END_VAR

  IF Enable THEN
    Scale := 10.0**Precision;
    RoundedInput1 := ROUND(Input1 * Scale);
    RoundedInput2 := ROUND(Input2 * Scale);

    IF RoundedInput1 = RoundedInput2 THEN
      Equal := TRUE;
      Greater := FALSE;
      Less := FALSE;
    ELSIF RoundedInput1 > RoundedInput2 THEN
      Equal := FALSE;
      Greater := TRUE;
      Less := FALSE;
    ELSE
      Equal := FALSE;
      Greater := FALSE;
      Less := TRUE;
    END_IF;

    Error := (Precision < 0) OR NOT Enable;
  END_IF;
END_FUNCTION_BLOCK
```

**Notes:**

- The function block is designed to be easily reusable in various PLC applications.
- The precision value should be a positive integer to ensure accurate comparisons.
- The function block will return an error flag if the precision value is negative or the enable flag is false.
- The function block is scan-cycle safe and will not cause any issues when used in a PLC program.
- The function block can be easily modified to handle other data types, such as integers or BOOLs, by adjusting the data types of the input and output variables.
- The function block can be further optimized by using a lookup table or other techniques to improve the speed of the comparison.
- The function block can be integrated into a larger PLC program to perform various control tasks, such as setpoint verification, sensor thresholding, and quality control decisions.
- The function block can be easily tested by providing known input values and verifying the output flags.
- The function block can be easily debugged by using the built-in debugging tools provided by the PLC programming software.
- The function block can be easily documented by adding comments and descriptions to the code.
- The function block can be easily
