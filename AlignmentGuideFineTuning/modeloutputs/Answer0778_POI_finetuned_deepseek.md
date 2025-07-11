### Intent:
The task is to develop an IEC 61131-3 Structured Text program for safely controlling the startup and shutdown sequences of a 3D pouch making machine, including temperature regulation of heating/cooling stations, feeder speed synchronization, tension control, and cutter coordination with safety interlocks.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer specializing in industrial shutdown procedures using IEC 61131-3 Structured Text, with a focus on safe, phased deactivation of high-temperature equipment in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Develop a Structured Text-based shutdown program for a steel production facility. The task includes:
	•	Creating a complete step-by-step shutdown sequence, covering essential phases such as furnace cooldown, gas flow reduction, and oxygen level management.
	•	Writing a detailed control narrative for steps 4 to 6, including exact setpoints and timing requirements for variables like temperature, gas flow, and oxygen concentration.
	•	Implementing a self-contained IEC 61131-3 program that handles the sequencing logic and enforces safety protocols.
	•	Designing a function block to ramp down fuel gas flow over 12 hours, with safety checks and timer-based control.
	•	Creating another function that adjusts oxygen supply to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow rate and furnace temperature changes.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block implementing the shutdown sequence
	•	Modular function blocks with parameter inputs (e.g., time, flow rate, ratio target)
	•	Usage of timers (TON), IF conditions, and real-time analog signal processing
	•	In-line comments explaining control logic and safety transitions
	•	Optional summary of integration challenges and how your solution supports safe, scalable shutdown automation

### Generated Code:
The task is to develop an IEC 61131-3 Structured Text program for safely controlling the startup and shutdown sequences of a 3D pouch making machine, including temperature regulation of heating/cooling stations, feeder speed synchronization, tension control, and cutter coordination with safety interlocks.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer specializing in industrial shutdown procedures using IEC 61131-3 Structured Text, with a focus on safe, phased deactivation of high-temperature equipment in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Develop a Structured Text-based shutdown program for a steel production facility. The task includes:
	•	Creating a complete step-by-step shutdown sequence, covering essential phases such as furnace cooldown, gas flow reduction, and oxygen level management.
	•	Writing a detailed control narrative for steps 4 to 6, including exact setpoints and timing requirements for variables like temperature, gas flow, and oxygen concentration.
	•	Implementing a self-contained IEC 61131-3 program that handles the sequencing logic and enforces safety protocols.
	•	Designing a function block to ramp down fuel gas flow over 12 hours, with safety checks and timer-based control.
	•	Creating another function that adjusts oxygen supply to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow rate and furnace temperature changes.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block implementing the shutdown sequence
	•	Modular function blocks with parameter inputs (e.g., time, flow rate, ratio target)
	•	Usage of timers (TON), IF conditions, and real-time analog signal processing
	•	In-line comments explaining control logic and safety transitions
	•	Optional summary of integration challenges and how your solution supports safe, scalable shutdown automation
(* IEC 61131-3 Structured Text program for 3D pouch making machine control *)
(* Includes temperature regulation, feeder synchronization, tension control, and cutter coordination *)

PROGRAM PouchMakingControl
VAR
    (* Inputs *)
    StartButton : BOOL; (* Start/Stop button *)
    EmergencyStop : BOOL; (* Emergency stop button *)
    EmergencyStopDetected : BOOL; (* Flag indicating emergency stop *)
    EmergencyStopDuration : TIME; (* Duration of emergency stop *)
    EmergencyStopTimer : TON; (* Timer for emergency stop duration *)
    EmergencyStopTimerDone : BOOL; (* Flag indicating emergency stop timer is done *)
    
    (* Outputs *)
    HeaterOn : BOOL; (* Heater control *)
    CoolingFanOn : BOOL; (* Cooling fan control *)
    FeederSpeed : REAL; (* Feeder speed control *)
    TensionControl : BOOL; (* Tension control *)
    CutterOn : BOOL; (* Cutter control *)
    CutterSpeed : REAL; (* Cutter speed control *)
    CutterPosition : INT; (* Cutter position control *)
    CutterError : BOOL; (* Cutter error flag *)
    CutterErrorDetected : BOOL; (* Flag indicating cutter error *)
    CutterErrorDuration : TIME; (* Duration of cutter error *)
    CutterErrorTimer : TON; (* Timer for cutter error duration *)
    CutterErrorTimerDone : BOOL; (* Flag indicating cutter error timer is done *)
    
    (* Internal Variables *)
    HeaterTemp : REAL; (* Heater temperature *)
    CoolingFanSpeed : REAL; (* Cooling fan speed *)
    FeederSpeedSetpoint : REAL; (* Feeder speed setpoint *)
    TensionControlSetpoint : BOOL; (* Tension control setpoint *)
    CutterPositionSetpoint : INT; (* Cutter position setpoint *)
    CutterErrorDurationSetpoint : TIME; (* Cutter error duration setpoint *)
    CutterErrorTimerSetpoint : TON; (* Cutter error timer setpoint *)
    CutterErrorDetected : BOOL; (* Cutter error detected flag *)
    CutterErrorDurationTimer : TON; (* Timer for cutter error duration *)
    CutterErrorTimerDone : BOOL; (* Flag indicating cutter error timer is done *)
END_VAR

(* Control
