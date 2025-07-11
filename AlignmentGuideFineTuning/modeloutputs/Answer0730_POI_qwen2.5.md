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

The MotorInterlock function block takes three Boolean inputs representing the running status of three pieces of equipment (Equipment1Running, Equipment2Running, Equipment3Running). It outputs a single Boolean value, AllowStart, which is TRUE only if all three inputs are FALSE. This means that the motor can only start if all associated equipment is stopped.

**Role of Motor Interlocks in Process Safety and Equipment Coordination:**

Motor interlocks play a critical role in industrial safety by preventing premature or unsafe motor operation. They ensure that motors are only started when all associated equipment is safely shut down, reducing the risk of accidents and equipment damage. By coordinating the startup sequence of multiple pieces of equipment, interlocks help prevent conflicts and ensure that operations are carried out in a safe and controlled manner. This is particularly important in industries where equipment failures can have severe consequences, such as in chemical processing or power generation. Interlocks also contribute to regulatory compliance by ensuring that safety standards are met and that operations are conducted in a manner that minimizes risk to personnel and the environment.
