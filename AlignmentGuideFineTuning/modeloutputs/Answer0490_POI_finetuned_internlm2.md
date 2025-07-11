### Intent:
**Intent Summary:**  
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if any monitored equipment is running, ensuring safe operation by evaluating Boolean inputs (equipment statuses) and outputting an enable signal only when all are stopped.  

*(Focus: Safety interlock logic to block motor start during unsafe conditions.)*

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
Design a motor interlock function block in IEC 61131-3 Structured Text that prevents motor startup if any monitored equipment is running, ensuring safe operation by evaluating Boolean inputs (equipment statuses) and outputting an enable signal only when all are stopped.  

*(Focus: Safety interlock logic to block motor start during unsafe conditions.)*
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

**T-A-B-L-E:**

| T | A | B | L | E |
|---|---|---|---|---|
| Task | Automation engineer | Design a motor interlock function block in IEC 61131-3 Structured Text, ensuring safe motor operation by blocking startup when associated equipment is still running. | Discuss the role of motor interlocks in industrial safety and how this logic prevents premature or unsafe motor operation. | 🟥 R (Role) – Your Role | 🟩 I (Input) – What You’re Given | 🟧 S (Steps) – What You Need to Do | 🟦 E (Expectation) – What Success Looks Like |
| A | Develop a function block diagram and implement it in code, ensuring that the motor can only start when all associated equipment is safely shut down. | ⸻ | 1.	Define the function block interface: Inputs (Equipment1Running, Equipment2Running, etc.) and Output (AllowStart). 2.	Implement the logic in Structured Text: AllowStart = NOT (Equipment1Running OR Equipment2Running OR Equipment3Running). 3.	Integrate the function block into the main program, linking it to the motor start circuit or HMI control logic. 4.	Document the logic and explain its safety purpose in both functional and operator terms. | 🟥 R (Role) – Your Role | 🟩 I (Input) – What You’re Given | 🟧 S (Steps) – What You Need to Do |
| B | Motor interlock function block: | ⸻ | •	Inputs: Equipment1Running, Equipment2Running, Equipment3Running (Boolean) •	Output: AllowStart (Boolean) | 🟩 I (Input) – What You’re Given | 🟧 S (Steps) – What You Need to Do |
| L | Motor interlock function block implementation: | ⸻ | AllowStart := NOT (Equipment1Running OR Equipment2Running OR Equipment3Running); | 🟩 I (Input) – What You’re Given | 🟧 S (Steps) – What You Need to Do |
| E | Motor interlock function block: | ⸻ | •
