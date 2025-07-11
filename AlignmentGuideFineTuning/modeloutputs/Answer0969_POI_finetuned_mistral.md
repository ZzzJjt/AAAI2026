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
(* IEC 61131-3 Structured Text Function Block for a 3-Phase Current Monitor *)
(* Implements real-time monitoring and alarm handling for phase currents *)
(* Uses configurable thresholds, handles invalid inputs, and supports scan-cycle safety *)

FUNCTION_BLOCK ThreePhaseCurrentMonitor
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable monitoring *)
    PhaseA_Current : REAL;          (* Amperes, e.g., from CT or current sensor *)
    PhaseB_Current : REAL;          (* Amperes, e.g., from CT or current sensor *)
    PhaseC_Current : REAL;          (* Amperes, e.g., from CT or current sensor *)
    ThresholdA : REAL;              (* Alarm threshold for Phase A current *)
    ThresholdB : REAL;              (* Alarm threshold for Phase B current *)
    ThresholdC : REAL;              (* Alarm threshold for Phase C current *)
    SampleTime : TIME;              (* Time between samples, e.g., T#100ms *)
END_VAR

VAR_OUTPUT
    PhaseA_Alarm : BOOL;            (* TRUE if Phase A current exceeds threshold *)
    PhaseB_Alarm : BOOL;            (* TRUE if Phase B current exceeds threshold *)
    PhaseC_Alarm : BOOL;            (* TRUE if Phase C current exceeds threshold *)
    Error : BOOL;                   (* TRUE if invalid input or configuration *)
    Done : BOOL;                    (* TRUE when monitoring is complete *)
END_VAR

VAR
    LastEnable : BOOL;              (* Previous Enable state for scan-cycle safety *)
    CurrentSampleTime : TIME;       (* Current sample time for timing *)
    CurrentSampleCount : INT;       (* Sample counter for scan-cycle safety *)
    ValidInputs : BOOL;             (* TRUE if all inputs are valid *)
    ValidConfig : BOOL;             (* TRUE if thresholds are valid *)
    ValidState : BOOL;              (* TRUE if state is valid *)
    CurrentAmpA : REAL;             (* Temporary storage for Phase A current *)
    CurrentAmpB : REAL;             (* Temporary storage for Phase B current *)
