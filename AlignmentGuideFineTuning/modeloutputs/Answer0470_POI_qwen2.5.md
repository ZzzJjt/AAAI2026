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

**IEC 61131-3 Structured Text Implementation:**

```plaintext
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
```

**Explanation:**

The `MotorInterlock` function block takes three Boolean inputs (`Equipment1Running`, `Equipment2Running`, `Equipment3Running`) representing the operational status of three pieces of equipment. It outputs a single Boolean value (`AllowStart`) that determines whether the motor can start.

The logic in the `AllowStart` assignment checks if all equipment is stopped. If any equipment is running, the `AllowStart` output remains FALSE, preventing the motor from starting. This ensures that the motor only starts when all associated equipment is safely shut down, thereby preventing premature or unsafe operation.

**Role of Motor Interlocks in Industrial Safety:**

Motor interlocks play a critical role in industrial safety by enforcing a specific sequence of operations. They ensure that motors do not start until all necessary equipment is ready, preventing potential hazards such as:

1. **Premature Startups:** Preventing motors from starting before other equipment is properly aligned or positioned.
2. **Sequence Conflicts:** Ensuring that the correct sequence of operations is followed, avoiding situations where multiple pieces of equipment could interfere with each other.
3. **Safety Interlocks:** Providing a layer of protection by ensuring that motors cannot start if there is a risk of injury or damage to personnel or equipment.

By implementing the `MotorInterlock` function block, you contribute to a safer and more reliable industrial environment, aligning with international safety standards and best practices.
