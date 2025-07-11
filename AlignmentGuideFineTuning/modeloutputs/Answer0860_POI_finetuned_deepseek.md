### Intent:
**Intent Summary:**  
Design a distillation column control system with instrumentation (pressure, temperature, level), actuators (valves, reboiler, condenser), and safety interlocks (pressure/temperature limits) to ensure safe and automated separation of feed components, documented via a P&ID.  

*(Focus: Automation logic for process control and safety interlocks in a distillation system.)*

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
Design a distillation column control system with instrumentation (pressure, temperature, level), actuators (valves, reboiler, condenser), and safety interlocks (pressure/temperature limits) to ensure safe and automated separation of feed components, documented via a P&ID.  

*(Focus: Automation logic for process control and safety interlocks in a distillation system.)*
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
(* IEC 61131-3 Structured Text: Motor Interlock Function Block *)
(* Purpose: Prevent motor start if any associated equipment is still running *)

FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL;
    Equipment2Running : BOOL;
    Equipment3Running : BOOL;
END_VAR
VAR_OUTPUT
    AllowStart : BOOL;
END_VAR
VAR
    AllEquipmentStopped : BOOL;
END_VAR

(* Interlock logic *)
AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;

(* Output logic *)
AllEquipmentStopped := Equipment1Running OR Equipment2Running OR Equipment3Running;
AllowStart := AllEquipmentStopped;
END_FUNCTION_BLOCK

(* Example Use: Motor Start Command *)
IF AllowStart THEN
    (* Allow motor to start *)
END_IF;

(* Example Use: HMI Display *)
IF AllEquipmentStopped THEN
    AllowStart := TRUE;
ELSE
    AllowStart := FALSE;
END_IF;

(* Example Use: PLC Output *)
IF AllowStart THEN
    (* Allow motor to start *)
ELSE
    (* Block motor start until all equipment is stopped *)
END_IF;

(* Example Use: Alarm *)
IF AllowStart AND AllEquipmentStopped THEN
    (* Allow motor to start *)
ELSE
    (* Raise interlock fault or alarm *)
END_IF;

(* Example Use: PLC Output *)
IF AllowStart THEN
    MotorStart := TRUE;
ELSE
    MotorStart := FALSE;
END_IF;

(* Example Use: HMI Display *)
IF AllEquipmentStopped THEN
    AllowStart := TRUE;
ELSE
    AllowStart := FALSE;
END_IF;

(* Example Use: PLC Output *)
IF AllowStart THEN
    MotorStart := TRUE;
ELSE
    MotorStart := FALSE;
END_IF;

(* Example Use: Alarm *)
IF AllowStart AND AllEquipmentStopped THEN
    MotorStart := TRUE;
ELSE
    MotorStart := FALSE;
END_IF;

(* Example Use: PLC Output *)
IF AllowStart THEN
    MotorStart := TRUE;
ELSE
    MotorStart := FALSE;
END_IF;
