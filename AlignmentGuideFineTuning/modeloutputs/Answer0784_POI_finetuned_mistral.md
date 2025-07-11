### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and a validity flag, ensuring industrial robustness and scan-cycle efficiency.  

*(Focus: Precision conversion, safety checks, and industrial compatibility.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC engineer responsible for building utility function blocks in IEC 61131-3 Structured Text for use in industrial temperature control systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that converts a Fahrenheit temperature value to Celsius, ensuring:
	•	Accurate conversion using the formula:
Celsius = (Fahrenheit - 32) \times \frac{5}{9}
	•	Input validation to reject values below absolute zero (−459.67°F)
	•	Scan-cycle safety and compatibility with industrial applications
	•	Clear output signaling, including a ValidInput boolean flag

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs: Celsius : REAL, ValidInput : BOOL
	•	Logic structure that includes:
	•	An IF condition to check for valid input
	•	The Celsius conversion calculation
	•	Fallback values when the input is invalid
	•	Inline comments to explain validation, conversion logic, and best practices for reuse

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and a validity flag, ensuring industrial robustness and scan-cycle efficiency.  

*(Focus: Precision conversion, safety checks, and industrial compatibility.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC engineer responsible for building utility function blocks in IEC 61131-3 Structured Text for use in industrial temperature control systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that converts a Fahrenheit temperature value to Celsius, ensuring:
	•	Accurate conversion using the formula:
Celsius = (Fahrenheit - 32) \times \frac{5}{9}
	•	Input validation to reject values below absolute zero (−459.67°F)
	•	Scan-cycle safety and compatibility with industrial applications
	•	Clear output signaling, including a ValidInput boolean flag

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs: Celsius : REAL, ValidInput : BOOL
	•	Logic structure that includes:
	•	An IF condition to check for valid input
	•	The Celsius conversion calculation
	•	Fallback values when the input is invalid
	•	Inline comments to explain validation, conversion logic, and best practices for reuse
(* IEC 61131-3 Structured Text: ISA-88 Compliant Reaction Control Function Block *)
(* Purpose: Implements a reusable function block for reaction control in batch processes *)

FUNCTION_BLOCK ReactionControl
VAR_INPUT
    Execute : BOOL;                  (* TRUE to execute reaction control *)
    ReactionTempSetpoint : REAL;     (* Target temperature in °C *)
    ReactionPressureSetpoint : REAL; (* Target pressure in bar *)
    ReactionTimeSetpoint : TIME;     (* Target reaction time *)
    ReactionComplete : BOOL;         (* TRUE when reaction complete *)
    ReactionError : BOOL;            (* TRUE if control fails *)
    Enable : BOOL;                   (* TRUE to enable control *)
END_VAR

VAR_OUTPUT
    HeaterOn : BOOL;                 (* TRUE to activate heater *)
    PressureValveOn : BOOL;          (* TRUE to open pressure valve *)
    ReactionComplete : BOOL;         (* TRUE when reaction complete *)
    ReactionError : BOOL;            (* TRUE if control fails *)
    Done : BOOL;                     (* TRUE when control sequence completes *)
END_VAR

VAR
    (* Internal state variables *)
    CurrentTemp : REAL;              (* Current temperature in °C *)
    CurrentPressure : REAL;          (* Current pressure in bar *)
    CurrentTime : TIME;              (* Current time since start *)
    ReactionStarted : BOOL;          (* TRUE when reaction started *)
    ReactionRunning : BOOL;          (* TRUE when reaction is active *)
    ReactionCompleteInternal : BOOL; (* Internal flag for reaction completion *)
    ReactionErrorInternal : BOOL;    (* Internal flag for control failure *)
    
    (* Control parameters *)
    TempTolerance : REAL := 2.0;     (* Temperature tolerance in °C *)
    PressureTolerance : REAL := 0.1; (* Pressure tolerance in bar *)
    TimeTolerance : TIME := T#10m;    (* Time tolerance *)
    
    (* Control logic *)
    TempController : REFERENCE;       (* PID controller for temperature *)
    PressureController : RE
