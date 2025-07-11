### Intent:
**Intent Summary:**  
Design an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including furnace temperature reduction, controlled gas flow ramp-down, and dynamic oxygen ratio management, with modular functions for industrial deployment.

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
Design an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including furnace temperature reduction, controlled gas flow ramp-down, and dynamic oxygen ratio management, with modular functions for industrial deployment.
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

PROGRAM ShutdownSteel
VAR
    (* Inputs *)
    ShutdownRequested : BOOL; (* TRUE to initiate shutdown *)
    EmergencyStop : BOOL; (* TRUE to stop all operations *)
    
    (* Outputs *)
    BurnerStatus : INT; (* 0=Off, 1=On, 2=Fault *)
    GasFlow : REAL; (* Flow rate in kg/h *)
    OxygenLevel : REAL; (* 0-100% *)
    Temperature : REAL; (* 0-1000°C *)
    BurnerStatusLED : BOOL; (* TRUE if burners are active *)
    
    (* Internal Variables *)
    ShutdownTimer : TON; (* 100 ms timer for shutdown *)
    GasFlowRamp : REAL; (* Ramp rate for gas flow *)
    OxygenRamp : REAL; (* Ramp rate for oxygen supply *)
    BurnerState : INT; (* Burner state: 0=Off, 1=On, 2=Fault *)
    BurnerFault : BOOL; (* TRUE if burners are faulty *)
    BurnerFaultLED : BOOL; (* TRUE if burners are faulty *)
    BurnerFaultTimer : TON; (* 100 ms timer for burners *)
    BurnerFaultCount : INT; (* Burner fault count *)
    BurnerFaultCountMax : INT := 5; (* Max fault count *)
    BurnerFaultReset : BOOL; (* TRUE to reset fault count *)
    BurnerFaultResetTimer : TON; (* 100 ms timer for reset *)
    BurnerFaultResetCount : INT; (* Burner fault reset count *)
    BurnerFaultResetCountMax : INT := 5; (* Max reset count *)
    
    (* Internal Functions *)
    (* Function: FuelGasRamp *)
    FUNCTION FuelGasRamp : REAL
VAR_INPUT
    RampRate : REAL; (* Ramp rate in kg/h *)
END_VAR
VAR_OUTPUT
    RampRate : REAL; (* Ramp rate *)
END_VAR
VAR
    RampTimer : TON; (* 100 ms timer for ramp *)
    RampCount
