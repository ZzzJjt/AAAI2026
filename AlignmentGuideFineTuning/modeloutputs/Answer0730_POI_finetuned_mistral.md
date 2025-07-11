### Intent:
**Intent Summary:**  
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if associated equipment is running, ensuring safe operation through coordinated logic.  

*(Focus: Safety interlock logic, conditional motor enable, equipment status monitoring.)*

### Prompt:
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**R-T-F:**

🟥 R (Role) – Your Role

You are an industrial automation engineer responsible for implementing safe motor start logic using IEC 61131-3 Structured Text. Your task is to ensure that a motor can only start when all associated equipment is safely shut down.

⸻

🟩 T (Task) – What You Need to Do

Create a function block in Structured Text named MotorInterlock that:
	•	Accepts Boolean inputs representing the running status of nearby equipment (e.g., Equipment1Running, Equipment2Running)
	•	Outputs a single Boolean value AllowStart that is TRUE only if all inputs are FALSE
	•	Prevents motor startup when any associated equipment is still active
	•	Can be reused in multiple control situations requiring coordinated startup logic

Additionally, briefly describe the role of motor interlocks in process safety and equipment coordination.

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A complete IEC 61131-3 Structured Text implementation of the MotorInterlock function block:

 FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL;
    Equipment2Running : BOOL;
    Equipment3Running : BOOL;
END_VAR
VAR_OUTPUT
    AllowStart : BOOL;
END_VAR

AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;

	•	A brief explanation highlighting how this interlock:
	•	Prevents unsafe motor activation
	•	Ensures correct sequencing of machine operations
	•	Contributes to system safety and regulatory compliance

### Generated Code:
**Intent Summary:**  
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if associated equipment is running, ensuring safe operation through coordinated logic.  

*(Focus: Safety interlock logic, conditional motor enable, equipment status monitoring.)*
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**R-T-F:**

🟥 R (Role) – Your Role

You are an industrial automation engineer responsible for implementing safe motor start logic using IEC 61131-3 Structured Text. Your task is to ensure that a motor can only start when all associated equipment is safely shut down.

⸻

🟩 T (Task) – What You Need to Do

Create a function block in Structured Text named MotorInterlock that:
	•	Accepts Boolean inputs representing the running status of nearby equipment (e.g., Equipment1Running, Equipment2Running)
	•	Outputs a single Boolean value AllowStart that is TRUE only if all inputs are FALSE
	•	Prevents motor startup when any associated equipment is still active
	•	Can be reused in multiple control situations requiring coordinated startup logic

Additionally, briefly describe the role of motor interlocks in process safety and equipment coordination.

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A complete IEC 61131-3 Structured Text implementation of the MotorInterlock function block:

 FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL;
    Equipment2Running : BOOL;
    Equipment3Running : BOOL;
END_VAR
VAR_OUTPUT
    AllowStart : BOOL;
END_VAR

AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;

	•	A brief explanation highlighting how this interlock:
	•	Prevents unsafe motor activation
	•	Ensures correct sequencing of machine operations
	•	Contributes to system safety and regulatory compliance
	•	Can be integrated into PLC control logic for motors, pumps, or conveyors
(* IEC 61131-3 Structured Text: MotorInterlock Function Block *)
(* Purpose: Prevents motor startup if associated equipment is running *)

FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL; (* TRUE if Equipment 1 is running *)
    Equipment2Running : BOOL; (* TRUE if Equipment 2 is running *)
    Equipment3Running : BOOL; (* TRUE if Equipment 3 is running *)
END_VAR
VAR_OUTPUT
    AllowStart : BOOL; (* TRUE if all equipment is stopped, FALSE otherwise *)
END_VAR
VAR
    AllStopped : BOOL; (* Combined status of all equipment *)
END_VAR

(* Main Logic: AllowStart = TRUE only if all equipment is stopped *)
AllStopped := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
AllowStart := AllStopped;

(* Optional: Add diagnostic output for troubleshooting *)
(* Diagnostic.Error := NOT AllStopped; *)
(* Diagnostic.Message := 'Motor startup blocked due to running equipment: ' + CASE (NOT Equipment1Running, 'Equipment 1', NOT Equipment2Running, 'Equipment 2', NOT Equipment3Running, 'Equipment 3') + ''; *)
(* Note: Commented out for production use *)

(* Example usage: *)
(* MotorInterlock.Equipment1Running := Equipment1Running; *)
(* MotorInterlock.Equipment2Running := Equipment2Running; *)
(* MotorInterlock.Equipment3Running := Equipment3Running; *)
(* AllowStart := MotorInterlock.AllowStart; *)

(* Notes: *)
(* - This logic assumes that all equipment is initially stopped *)
(* - For real-time applications, consider using a timer to check status periodically *)
(* - Include error handling and alarms for fault conditions *)
(* - Use this function block in motor start routines or conveyor synchronization *)
(* - Compliant with IEC 61131-3 ST and industrial safety best practices *)
(* End of MotorInterlock.st *)
(*
  Title:   Motor Interlock
