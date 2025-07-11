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

// Explanation:
// The MotorInterlock function block checks the running status of three equipment inputs.
// If any of them are TRUE, AllowStart is FALSE, preventing the motor from starting.
// This logic ensures that the motor only starts when all associated equipment is safely shut down.
// This approach is critical for preventing premature motor activation, which can lead to equipment damage or safety hazards.
(* IEC 61131-3 Structured Text: Motor Interlock Function Block *)
(* Purpose: Prevents motor startup if any associated equipment is still running *)

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

(* Implementation Details *)
(* - Checks running status of 3 equipment inputs *)
(* - Prevents motor start if any are TRUE *)
(* - Ensures safe startup sequence *)
(* - Can be reused in other control systems *)
(* - Supports safety and regulatory compliance *)
(* - Example usage: MotorStart := AllowStart; *)
(* - Can be expanded to monitor more equipment or add fault handling *)
(* - Can be integrated with PLC alarm logic or HMI shutdown triggers *)
(* - Supports real-time execution and safety-critical applications *)
(* - Example: Motor1Start := AllowStart; *)
(* - Can be used in PLCs, HMI, or SCADA systems *)
(* - Supports IEC 61131-3 standards and industrial automation best practices *)
(* - Can be deployed in real-world industrial control systems *)
(* - Supports safety and compliance requirements *)
(* - Can be extended to monitor more equipment or add fault handling *)
(* - Supports real-time execution and safety-critical applications *)
(* - Supports integration with PLC alarm logic or HMI shutdown triggers *)
(* - Supports IEC 6
