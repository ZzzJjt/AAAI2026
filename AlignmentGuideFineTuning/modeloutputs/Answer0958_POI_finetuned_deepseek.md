### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including controlled furnace temperature reduction, fuel gas flow ramp-down over 12 hours, and dynamic oxygen supply adjustment to maintain a 1:2.5 fuel-to-air ratio, with embedded safety checks and modular functions.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**T-A-G:**

🟥 T (Task)

Design a safe and sequenced shutdown control program for a steel production facility using IEC 61131-3 Structured Text, following industrial best practices and safety protocols.

⸻

🟩 A (Action)
	1.	Create a comprehensive shutdown procedure covering stages such as:
	•	Furnace temperature reduction
	•	Controlled fuel gas flow ramp-down
	•	Oxygen level regulation to maintain combustion stability
	2.	Write a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying real values for:
	•	Temperature setpoints (e.g., cool to < 400°C)
	•	Gas flow reduction timeline (e.g., 12 hours)
	•	Fuel-to-air ratio (1:2.5 for oxygen management)
	3.	Implement a Structured Text control program with proper sequencing, interlocks, and safety logic.
	4.	Develop two key IEC 61131-3 functions:
	•	One to gradually reduce fuel gas flow using a linear ramp over 12 hours, with timing and fault checks.
	•	One to adjust oxygen supply dynamically based on gas flow and temperature to ensure the 1:2.5 fuel-to-air ratio, with safeguards for combustion efficiency.

⸻

🟦 G (Goal)

Deliver a modular, ISA-88-aligned shutdown automation solution that ensures:
	•	Safe thermal and combustion transitions
	•	Stable fuel-to-air control under variable process conditions
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including controlled furnace temperature reduction, fuel gas flow ramp-down over 12 hours, and dynamic oxygen supply adjustment to maintain a 1:2.5 fuel-to-air ratio, with embedded safety checks and modular functions.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**T-A-G:**

🟥 T (Task)

Design a safe and sequenced shutdown control program for a steel production facility using IEC 61131-3 Structured Text, following industrial best practices and safety protocols.

⸻

🟩 A (Action)
	1.	Create a comprehensive shutdown procedure covering stages such as:
	•	Furnace temperature reduction
	•	Controlled fuel gas flow ramp-down
	•	Oxygen level regulation to maintain combustion stability
	2.	Write a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying real values for:
	•	Temperature setpoints (e.g., cool to < 400°C)
	•	Gas flow reduction timeline (e.g., 12 hours)
	•	Fuel-to-air ratio (1:2.5 for oxygen management)
	3.	Implement a Structured Text control program with proper sequencing, interlocks, and safety logic.
	4.	Develop two key IEC 61131-3 functions:
	•	One to gradually reduce fuel gas flow using a linear ramp over 12 hours, with timing and fault checks.
	•	One to adjust oxygen supply dynamically based on gas flow and temperature to ensure the 1:2.5 fuel-to-air ratio, with safeguards for combustion efficiency.

⸻

🟦 G (Goal)

Deliver a modular, ISA-88-aligned shutdown automation solution that ensures:
	•	Safe thermal and combustion transitions
	•	Stable fuel-to-air control under variable process conditions
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration
(* IEC 61131-3 Structured Text Program: Steel Production Shutdown *)
(* Purpose: Safely and sequentially shut down a steel production facility *)

PROGRAM ShutdownSteelProduction
VAR
    (* Inputs *)
    StartShutdown : BOOL;                  (* TRUE to initiate shutdown *)
    EmergencyStop : BOOL;                  (* TRUE to stop immediately *)
    EmergencyStopDetected : BOOL;          (* TRUE if emergency stop detected *)
    EmergencyStopDuration : TIME;          (* Duration of emergency stop *)
    EmergencyStopDurationRemaining : TIME;  (* Remaining duration of emergency stop *)
    EmergencyStopTimer : TON;              (* Timer for emergency stop duration *)
    
    (* Outputs *)
    ShutdownComplete : BOOL;                (* TRUE when shutdown is complete *)
    ShutdownInProgress : BOOL;             (* TRUE during shutdown *)
    ShutdownError : BOOL;                 (* TRUE if shutdown fails *)
    ShutdownErrorCode : INT;              (* Error code: 0=Success, 1=Temperature, 2=GasFlow, 3=Oxygen *)
    
    (* Internal Variables *)
    ShutdownTimer : TON;                   (* Timer for shutdown duration *)
    ShutdownStartTime : TIME;              (* Time of shutdown start *)
    ShutdownDuration : TIME;               (* Duration of shutdown *)
    ShutdownErrorCode : INT := 0;         (* Error code for shutdown *)
    ShutdownErrorDetected : BOOL := FALSE; (* TRUE if shutdown error detected *)
    ShutdownErrorDetectedTime : TIME;     (* Time of last error *)
    ShutdownErrorDetectedTimer : TON;     (* Timer for error detection *)
    
    (* Safety Variables *)
    EmergencyStopDetected : BOOL := FALSE; (* TRUE if emergency stop detected *)
    EmergencyStopDetectedTime : TIME;     (* Time of last emergency stop *)
    EmergencyStopDetectedTimer : TON;     (* Timer for emergency stop detection *)
    
    (* State Variables *)
    ShutdownState : INT := 0;             (* 0=Idle, 1=Temperature, 2=GasFlow, 3=Oxygen, 4=Complete *)
    ShutdownStep : INT := 0;              (* Current shutdown step *)
    ShutdownStepTimer : TON;             (* Timer for current shutdown step *)
    ShutdownStepDone : BOOL;             (* TRUE when current step is complete *)
