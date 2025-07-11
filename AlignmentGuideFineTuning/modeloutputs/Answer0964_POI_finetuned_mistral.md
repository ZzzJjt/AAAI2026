### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to accurately convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and output flags for reliability in PLC systems.  

*(Focus: Modular conversion, safety checks, and industrial applicability.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to accurately convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and output flags for reliability in PLC systems.  

*(Focus: Modular conversion, safety checks, and industrial applicability.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.
(* IEC 61131-3 Structured Text Function Block for Fahrenheit to Celsius Conversion *)
(* Implements conversion with input validation and output flags *)
(* Ensures safe and reliable operation in industrial automation systems *)

FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Execute : BOOL;                  (* Trigger conversion on rising edge *)
    Fahrenheit : REAL;               (* Temperature in Fahrenheit, e.g., 212.0 *)
END_VAR

VAR_OUTPUT
    Celsius : REAL;                  (* Converted temperature in Celsius *)
    ValidInput : BOOL;               (* TRUE if input is valid *)
    Error : BOOL;                    (* TRUE if invalid input detected *)
END_VAR

VAR
    AbsoluteZero : REAL := -459.67;  (* Absolute zero in Fahrenheit *)
END_VAR

(* Main Conversion Logic *)
IF Execute THEN
    (* Validate Input *)
    IF Fahrenheit >= AbsoluteZero THEN
        (* Perform Conversion *)
        Celsius := (Fahrenheit - 32.0) * 5.0 / 9.0;
        ValidInput := TRUE;
        Error := FALSE;
    ELSE
        (* Input is Invalid: Absolute Zero or Below *)
        Celsius := 0.0;
        ValidInput := FALSE;
        Error := TRUE;
    END_IF;
ELSE
    (* Reset Outputs on Idle *)
    Celsius := 0.0;
    ValidInput := FALSE;
    Error := FALSE;
END_IF;

(* Documentation *)
(*
    FahrenheitToCelsius
    IEC 61131-3 Structured Text Function Block
    ----------------------------------------
    Purpose:
    Converts a temperature input in Fahrenheit to Celsius with validation and error handling.
   
    Overview:
    - Inputs: Fahrenheit (REAL), Execute (BOOL)
    - Outputs: Celsius (REAL), ValidInput (BOOL), Error (BOOL)
    - Validates input against absolute zero (-4
