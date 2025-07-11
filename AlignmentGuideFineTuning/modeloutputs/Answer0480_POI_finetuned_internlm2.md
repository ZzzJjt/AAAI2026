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

**T-A-B-L-E:**

| T (Title) | Motor Interlock System |
| :--- | :--- |
| A (Action) | Design a motor interlock function block in IEC 61131-3 Structured Text, ensuring that a motor only starts when all associated equipment is safely shut down. |
| B (Benefit) | Enhance system safety by preventing motors from starting while other critical equipment is still running, reducing the risk of sequence conflicts and equipment damage. |
| C (Context) | Motor interlocks are essential in industrial automation to ensure safe and coordinated operation of multiple equipment. They prevent premature or unsafe motor operation, which can lead to equipment damage, production delays, or safety hazards. |
| D (Detail) | Develop a function block diagram and implement the logic in Structured Text, ensuring that the motor can only start when all associated equipment is stopped. Discuss the role of motor interlocks in industrial safety and how this logic prevents unsafe motor operation. |
| E (Example) | 🔹	Define the function block interface with inputs for Equipment1Running, Equipment2Running, and Equipment3Running, and an output for AllowStart. 🔹	Implement the logic in Structured Text, using a Boolean AND operation to ensure that all equipment is stopped before allowing the motor to start. 🔹	Document the logic and explain its safety purpose in both functional and operator terms, emphasizing the importance of interlocks in preventing unsafe motor operation. |
| F (Focus) | Develop a motor interlock function block in IEC 61131-3 Structured Text, ensuring that a motor only starts when all associated equipment is safely shut down. |
| G (Goal) | Design a self-contained function block that prevents motor startup during unsafe conditions, ensuring safe and coordinated operation of multiple equipment. |
| H (Hint) | Focus on the safety aspect of motor interlocks and how they prevent premature or unsafe motor operation. Discuss the importance of interlocks in industrial safety and their role in preventing sequence conflicts and equipment damage. |

**☸️ IEC 61131-3 Structured Text:**

Implement the motor interlock logic in IEC 61131-3 Structured Text, ensuring that the motor can only start when all associated equipment is stopped. Document the safety purpose of the interlock and its role in preventing unsafe motor operation.

**☸️ Safety Considerations:**

Discuss
