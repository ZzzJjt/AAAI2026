### Intent:
**Intent Summary:**  
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate vehicle position and velocity from noisy measurements, with input validation, reset capability, and deterministic execution for industrial motion control applications.  

*(Focus: PLC-compatible state estimation with safety, modularity, and real-time performance.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe Kalman filter function block in IEC 61131-3 Structured Text to estimate vehicle position and velocity from noisy measurements, with input validation, reset capability, and deterministic execution for industrial motion control applications.  

*(Focus: PLC-compatible state estimation with safety, modularity, and real-time performance.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications. The function block should be designed to be easily integrated into larger control systems and should adhere to the principles of deterministic execution and safety-critical design in PLC programming.
**Fahrenheit to Celsius Function Block in IEC 61131-3 Structured Text:**

```plaintext
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL;
END_VAR
VAR_OUTPUT
    Celsius : REAL;
    ValidInput : BOOL;
END_VAR

(* Input validation: Reject values below absolute zero *)
IF Fahrenheit >= -459.67 THEN
    (* Perform the conversion *)
    Celsius := (Fahrenheit - 32) * 5 / 9;
    ValidInput := TRUE;
ELSE
    (* Invalid input: Set Celsius to 0 and indicate invalid input *)
    Celsius := 0.0;
    ValidInput := FALSE;
END_IF;

(* Inline comments for clarity *)
(* This function block converts Fahrenheit to Celsius, ensuring input is above absolute zero *)
(* Celsius := (Fahrenheit - 32) * 5 / 9 *)
END_FUNCTION_BLOCK
```

**Testing the Function Block:**

To test the function block, you can use the following test cases:

```plaintext
TEST_CASE_1:
    Fahrenheit := -459.67;
    (* Expected: Celsius := 0.0, ValidInput := FALSE *)

TEST_CASE_2:
    Fahrenheit := 32;
    (* Expected: Celsius := 0.0, ValidInput := TRUE *)

TEST_CASE_3:
    Fahrenheit := 212;
    (* Expected: Celsius := 100.0, ValidInput := TRUE *)

TEST_CASE_4:
    Fahrenheit := -500;
    (* Expected: Celsius := 0.0, ValidInput := FALSE *)
```

These test cases cover the boundary condition (absolute zero) and typical values to ensure the function block behaves as expected.
