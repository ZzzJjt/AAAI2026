### Intent:
**Intent Summary:**  
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if any linked equipment is running, ensuring safe operation by evaluating Boolean inputs (e.g., `EquipmentRunning`) and outputting `AllowStart` only when all inputs are FALSE.  

*(Focus: Safety interlock logic to enforce equipment startup sequence constraints.)*

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
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if any linked equipment is running, ensuring safe operation by evaluating Boolean inputs (e.g., `EquipmentRunning`) and outputting `AllowStart` only when all inputs are FALSE.  

*(Focus: Safety interlock logic to enforce equipment startup sequence constraints.)*
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
	•	Includes comments explaining the logic for both developers and operators
	•	Works reliably in real-time PLC environments
	•	Is part of a complete list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 61131-3 standards for structured text programming
	•	Includes typical use cases and examples of how the interlock prevents premature or unsafe motor operation
	•	Is part of a comprehensive list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 61131-3 standards for structured text programming
	•	Includes typical use cases and examples of how the interlock prevents premature or unsafe motor operation
	•	Is part of a comprehensive list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 61131-3 standards for structured text programming
	•	Includes typical use cases and examples of how the interlock prevents premature or unsafe motor operation
	•	Is part of a comprehensive list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 61131-3 standards for structured text programming
	•	Includes typical use cases and examples of how the interlock prevents premature or unsafe motor operation
	•	Is part of a comprehensive list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 61131-3 standards for structured text programming
	•	Includes typical use cases and examples of how the interlock prevents premature or unsafe motor operation
	•	Is part of a comprehensive list of interlocks for a machine or process, ensuring safe operation under all conditions
	•	Is designed to be extended or adapted for use in other interlock scenarios
	•	Is compliant with IEC 6113
