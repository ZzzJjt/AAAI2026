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
(* Function Block Diagram: Motor Interlock *)
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
    EquipmentStatus : ARRAY[1..3] OF BOOL;
END_VAR

METHOD Execute : BOOL
BEGIN
    AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
END_METHOD

(* IEC 61131-3 Structured Text Implementation *)
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
    EquipmentStatus[1..3] : ARRAY[1..3] OF BOOL;
END_VAR

METHOD Execute : BOOL
BEGIN
    AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
END_METHOD

(* Logic *)
IF Equipment1Running THEN
    EquipmentStatus[1] := TRUE;
ELSE
    EquipmentStatus[1] := FALSE;
END_IF;

IF Equipment2Running THEN
    EquipmentStatus[2] := TRUE;
ELSE
    EquipmentStatus[2] := FALSE;
END_IF;

IF Equipment3Running THEN
    EquipmentStatus[3] := TRUE;
ELSE
    EquipmentStatus[3] := FALSE;
END_IF;

AllowStart := NOT (
    EquipmentStatus[1] OR
    EquipmentStatus[2] OR
    EquipmentStatus[3]
);
END_FUNCTION_BLOCK

(* Documentation *)
// Motor Interlock Function Block Diagram
// Purpose: Prevent motor start if any equipment is running
// Inputs:
//   Equipment1Running, Equipment2Running, Equipment3Running: BOOL
// Outputs:
//   AllowStart: BOOL
//   Description:
//     TRUE if all equipment is stopped, FALSE otherwise

// IEC 61131-3 Structured Text Implementation
// Purpose: Execute the interlock logic
// Inputs:
//   Equipment1Running, Equipment2Running, Equipment
