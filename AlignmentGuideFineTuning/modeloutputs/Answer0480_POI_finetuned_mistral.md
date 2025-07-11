### Intent:
**Intent Summary:**  
Design a motor interlock system in IEC 61131-3 Structured Text that prevents motor startup if any linked equipment is running, ensuring safe operation by evaluating equipment status inputs and outputting an enable signal only when all are stopped.  

*(Focus: Safety interlock logic to block motor starts during unsafe conditions.)*

### Prompt:
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an automation engineer tasked with developing a motor interlock system using IEC 61131-3 Structured Text, ensuring that a motor only starts when all associated equipment is safely shut down.

⸻

🟩 I (Input) – What You’re Given

You must design a function block diagram and implement it in code. The function block will:
	•	Accept multiple Boolean inputs (Equipment1Running, Equipment2Running, etc.) representing the status of nearby equipment
	•	Evaluate whether the motor can start safely
	•	Output a Boolean value (AllowStart) that permits the motor to start only if all inputs are FALSE
	•	Prevent startup if any equipment is still running

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
	•	Inputs: statuses of all relevant equipment
	•	Output: AllowStart, which becomes TRUE only if all inputs are FALSE
	2.	Implement the logic in Structured Text:

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

	3.	Integrate the function block into the main program, linking it to the motor start circuit or HMI control logic.
	4.	Document the logic and explain its safety purpose in both functional and operator terms.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, reusable, and fault-resilient interlock function block that:
	•	Ensures motors cannot start while other critical equipment is active
	•	Enhances system safety and prevents sequence conflicts
	•	Contributes to compliance with industry safety standards (e.g., IEC 61508, ISO 13849)
	•	Is easy to integrate, test, and maintain within a larger control system

### Generated Code:
**Intent Summary:**  
Design a motor interlock system in IEC 61131-3 Structured Text that prevents motor startup if any linked equipment is running, ensuring safe operation by evaluating equipment status inputs and outputting an enable signal only when all are stopped.  

*(Focus: Safety interlock logic to block motor starts during unsafe conditions.)*
**Motor Interlock Function Block Diagram:**

Design a motor interlock as a function block diagram that prevents the motor from starting while other associated equipment is still running. The interlock should monitor the operational status of surrounding equipment and block the motor start command if any equipment is still active. Include inputs from sensors or status indicators and outputs that control the motor start circuit.

Provide the implementation of the MotorInterlock function block in IEC 61131-3 Structured Text. This function block should check the statuses of relevant equipment (e.g., EquipmentRunning), and if all equipment is stopped, it should allow the motor to start by setting the output to TRUE. If any equipment is still running, the output should remain FALSE, preventing the motor from starting.

Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an automation engineer tasked with developing a motor interlock system using IEC 61131-3 Structured Text, ensuring that a motor only starts when all associated equipment is safely shut down.

⸻

🟩 I (Input) – What You’re Given

You must design a function block diagram and implement it in code. The function block will:
	•	Accept multiple Boolean inputs (Equipment1Running, Equipment2Running, etc.) representing the status of nearby equipment
	•	Evaluate whether the motor can start safely
	•	Output a Boolean value (AllowStart) that permits the motor to start only if all inputs are FALSE
	•	Prevent startup if any equipment is still running

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
	•	Inputs: statuses of all relevant equipment
	•	Output: AllowStart, which becomes TRUE only if all inputs are FALSE
	2.	Implement the logic in Structured Text:

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

	3.	Integrate the function block into the main program, linking it to the motor start circuit or HMI control logic.
	4.	Document the logic and explain its safety purpose in both functional and operator terms.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, reusable, and fault-resilient interlock function block that:
	•	Ensures motors cannot start while other critical equipment is active
	•	Enhances system safety and prevents sequence conflicts
	•	Contributes to compliance with industry safety standards (e.g., IEC 61508, ISO 13849)
	•	Is easy to integrate, test, and maintain within a larger control system
FUNCTION_BLOCK FB_MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL;
    Equipment2Running : BOOL;
    Equipment3Running : BOOL;
END_VAR

VAR_OUTPUT
    AllowStart : BOOL;
END_VAR

METHOD Execute : BOOL
BEGIN
    AllowStart := NOT Equipment1Running AND NOT Equipment2Running AND NOT Equipment3Running;
    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    AllowStart := FALSE;
    RETURN TRUE;
END_METHOD

END_FUNCTION_BLOCK

(* Example PLC code to call the function block *)
(* Assumes FB_MotorInterlock is loaded at address MotorInterlock *)

(* Initialize inputs *)
Equipment1Running := FALSE;
Equipment2Running := FALSE;
Equipment3Running := FALSE;

(* Call function block *)
MotorInterlock(
    Equipment1Running := Equipment1Running,
    Equipment2Running := Equipment2Running,
    Equipment3Running := Equipment3Running,
    AllowStart := MotorInterlock.AllowStart
);

(* Use AllowStart to control motor start logic *)
IF MotorInterlock.AllowStart THEN
    MotorStart := TRUE;
ELSE
    MotorStart := FALSE;
END_IF;

(* Reset function block on scan cycle *)
MotorInterlock.Reset();

(* Documentation *)
(*
  Function Block: MotorInterlock
  Purpose: Prevents motor startup if associated equipment is running.
  Inputs:
    - Equipment1Running, Equipment2Running, Equipment3Running: Statuses of linked equipment
  Outputs:
    - AllowStart: TRUE if all equipment is stopped, FALSE otherwise
  Logic:
    - Evaluates whether all equipment is stopped
    - Returns TRUE only if all inputs are FALSE
    - Prevents motor startup if any equipment is active
  Usage:
    - Call function block on scan cycle
    - Use AllowStart to control motor start logic
    - Reset function block on scan cycle to clear internal state
  Safety Benefits:
    - Ensures motors cannot start while other critical equipment is active
    - Prevents sequence conflicts and mechanical
