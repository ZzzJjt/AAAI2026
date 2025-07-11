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
FUNCTION_BLOCK MotorInterlock
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

// Main program integration
VAR
    MotorInterlock : MotorInterlock;
END_VAR

// Call the function block in a scan cycle
MotorInterlock(Execute);

// Use AllowStart to control the motor start circuit or HMI
IF AllowStart THEN
    // Start motor
ELSE
    // Prevent motor from starting
END_IF;
```

### Example Use Case: Pump Interlock with Level Sensors

Suppose we have a tank with a pump and two level sensors (HighLevel and LowLevel) installed. The pump is connected to a motor, and the motor must not start if the tank is above a certain high level or below a certain low level.

To implement this interlock using the MotorInterlock function block, follow these steps:

1. **Define the Function Block Interface**:

```
FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    Equipment1Running : BOOL; // Pump motor running
    Equipment2Running : BOOL; // Other equipment running
    Equipment3Running : BOOL; // Other equipment running
END_VAR
VAR_OUTPUT
    AllowStart : BOOL;
END_VAR
```

2. **Implement the Logic**:

```
METHOD Execute : BOOL
BEGIN
    AllowStart := NOT Equipment1Running; // Prevent motor from running if it's already running
    // Add interlock conditions
    AllowStart := AllowStart AND NOT HighLevel; // Prevent start if tank is above high level
    AllowStart := AllowStart AND NOT LowLevel; // Prevent start if tank is below low level
    RETURN TRUE;
END_METHOD
```

3. **Integrate into the Main Program**:

```
VAR
    MotorInterlock : MotorInterlock;
END_VAR

// Call
