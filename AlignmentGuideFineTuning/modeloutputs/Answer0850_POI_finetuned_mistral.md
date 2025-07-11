### Intent:
**Intent Summary:**  
Design a motor interlock system that prevents motor startup when associated equipment is running, implemented via a function block diagram and IEC 61131-3 Structured Text, ensuring safe operation through conditional logic.  

*(Focus: Safety interlock logic to block motor start unless all monitored equipment is stopped.)*

### Prompt:
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement a Motor Interlock using a Function Block Diagram and IEC 61131-3 Structured Text. The system must prevent a motor from starting when other associated equipment is still running.

⸻

🟩 A (Action) – How to Do It
	1.	Create a function block named MotorInterlock with Boolean inputs such as Equipment1Running, Equipment2Running, etc.
	2.	Implement interlock logic that evaluates whether all connected equipment is stopped:

 AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
 	3.	Output a Boolean signal AllowStart that is TRUE only when all input equipment statuses are FALSE
	4.	Use this output to enable or block the motor start command
	5.	Optionally, display or log interlock conditions on an HMI or SCADA system

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a safe and modular interlock solution that ensures the motor can only be started under safe conditions—specifically, when all monitored equipment is inactive. This improves process coordination, prevents mechanical conflict, and promotes industrial safety compliance.

### Generated Code:
**Intent Summary:**  
Design a motor interlock system that prevents motor startup when associated equipment is running, implemented via a function block diagram and IEC 61131-3 Structured Text, ensuring safe operation through conditional logic.  

*(Focus: Safety interlock logic to block motor start unless all monitored equipment is stopped.)*
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement a Motor Interlock using a Function Block Diagram and IEC 61131-3 Structured Text. The system must prevent a motor from starting when other associated equipment is still running.

⸻

🟩 A (Action) – How to Do It
	1.	Create a function block named MotorInterlock with Boolean inputs such as Equipment1Running, Equipment2Running, etc.
	2.	Implement interlock logic that evaluates whether all connected equipment is stopped:

 AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
 	3.	Output a Boolean signal AllowStart that is TRUE only when all input equipment statuses are FALSE
	4.	Use this output to enable or block the motor start command
	5.	Optionally, display or log interlock conditions on an HMI or SCADA system

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a safe and modular interlock solution that ensures the motor can only be started under safe conditions—specifically, when all monitored equipment is inactive. This improves process coordination, prevents mechanical conflict, and promotes industrial safety compliance.
(* IEC 61131-3 Structured Text: MotorInterlock Function Block *)
(* Purpose: Prevents motor startup if associated equipment is running *)

FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL; (* TRUE if Equipment 1 is running *)
    Equipment2Running : BOOL; (* TRUE if Equipment 2 is running *)
    Equipment3Running : BOOL; (* TRUE if Equipment 3 is running *)
END_VAR

VAR_OUTPUT
    AllowStart : BOOL; (* TRUE to allow motor start, FALSE to block *)
END_VAR

VAR
    AllStopped : BOOL; (* TRUE if all equipment is stopped *)
END_VAR

(* Initialize outputs *)
AllowStart := FALSE;

(* Check if all equipment is stopped *)
AllStopped := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;

(* Allow motor start only if all equipment is stopped *)
AllowStart := AllStopped;

(* Example: Log interlock status *)
IF AllStopped THEN
    LogInterlockStatus := 'All equipment stopped, motor can start';
ELSE
    LogInterlockStatus := 'Equipment still running, motor blocked';
END_IF;

(* Example: Display interlock status on HMI *)
IF AllStopped THEN
    HMI_InterlockStatus := 'OK';
ELSE
    HMI_InterlockStatus := 'ALARM';
END_IF;

(* Example: Alarm if equipment starts while motor is running *)
IF Equipment1Running AND Equipment2Running AND Equipment3Running THEN
    AllowStart := FALSE;
    LogInterlockStatus := 'Equipment started while motor running';
    HMI_InterlockStatus := 'ALARM';
END_IF;

(* Example: Reset interlock when all equipment stops *)
IF NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running THEN
    AllowStart := TRUE;
    LogInterlockStatus := 'All equipment stopped, motor can start';
    HMI_InterlockStatus := 'OK';
END_IF;

(* Documentation: *)
(* - Prevents motor startup if associated equipment is running *)
(* - Uses conditional logic to block motor start *)
(*
