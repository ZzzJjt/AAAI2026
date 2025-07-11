### Intent:
The task involves creating a detailed control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, control loops, operational sequences, and safety interlocks to ensure safe and efficient continuous operation.  

**Intent Summary:**  
*Generate a structured control system configuration for an ammonium nitrate reactor, including process logic, instrumentation tags, PID loops, sequenced operations (startup/steady-state/shutdown), and safety interlocks, formatted for automation system implementation.*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process engineer or control system designer responsible for creating a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Develop a P&ID in textual notation that clearly describes the steam-water cycle, including:
	•	All major equipment (e.g., boiler, feedwater pump, steam drum, condenser)
	•	Instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping and flow paths, shown using text arrows (-->)
	•	Complete control loops with realistic and consistent tag names (e.g., FT101, FCV102, LT103)

The diagram should reflect actual process logic and signal relationships, structured clearly in text format.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a plain-text diagram, formatted for readability and easy integration into documentation or code repositories. Use a consistent layout to show:
	•	Equipment blocks connected by signal and flow arrows
	•	Control loops such as:

 P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01

 	•	Instrument tags in ISA style and logical grouping by process section (e.g., feedwater, boiler, condensate return)

### Generated Code:
The task involves creating a detailed control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, control loops, operational sequences, and safety interlocks to ensure safe and efficient continuous operation.  

**Intent Summary:**  
*Generate a structured control system configuration for an ammonium nitrate reactor, including process logic, instrumentation tags, PID loops, sequenced operations (startup/steady-state/shutdown), and safety interlocks, formatted for automation system implementation.*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process engineer or control system designer responsible for creating a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Develop a P&ID in textual notation that clearly describes the steam-water cycle, including:
	•	All major equipment (e.g., boiler, feedwater pump, steam drum, condenser)
	•	Instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping and flow paths, shown using text arrows (-->)
	•	Complete control loops with realistic and consistent tag names (e.g., FT101, FCV102, LT103)

The diagram should reflect actual process logic and signal relationships, structured clearly in text format.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a plain-text diagram, formatted for readability and easy integration into documentation or code repositories. Use a consistent layout to show:
	•	Equipment blocks connected by signal and flow arrows
	•	Control loops such as:

 P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01

 	•	Instrument tags in ISA style and logical grouping by process section (e.g., feedwater, boiler, condensate return)

This format ensures that the P&ID can be used for control system design, loop tuning, and documentation of the steam-water cycle.
(* IEC 61131-3 Structured Text Program for Continuous Ammonium Nitrate Reaction *)
(* Implements safe and efficient operation of a reactor with temperature and pressure control *)
(* Includes startup, steady-state, and shutdown sequences, safety interlocks, and PID control *)

PROGRAM AmmoniumNitrateReactorControl
VAR
    (* Inputs *)
    Temp_PV : REAL;                    (* Measured reactor temperature, °C *)
    Pressure_PV : REAL;                (* Measured reactor pressure, bar *)
    Startup_Button : BOOL;             (* TRUE to initiate startup *)
    Shutdown_Button : BOOL;            (* TRUE to initiate shutdown *)
    
    (* Outputs *)
    Temp_Setpoint : REAL;              (* Target temperature for PID control, °C *)
    Pressure_Setpoint : REAL;          (* Target pressure for PID control, bar *)
    Heater_On : BOOL;                  (* TRUE to activate heater *)
    Pressure_Valve_Open : BOOL;        (* TRUE to open pressure relief valve *)
    EmergencyStop : BOOL;              (* TRUE if emergency stop activated *)
    
    (* Internal Variables *)
    Reactor_Running : BOOL;            (* TRUE when reactor is operating *)
    Startup_Sequence_Active : BOOL;    (* TRUE during startup sequence *)
    Shutdown_Sequence_Active : BOOL;   (* TRUE during shutdown sequence *)
    PID_Temp_Controller : PID;         (* PID controller for temperature *)
    PID_Pressure_Controller : PID;     (* PID controller for pressure *)
    Temp_Error : BOOL;                 (* TRUE if temperature control fails *)
    Pressure_Error : BOOL;             (* TRUE if pressure control fails *)
    Control_Mode : INT;                (* 0 = Idle, 1 = Startup, 2 = Steady-State, 3 = Shutdown *)
    
    (* PID Tuning Parameters *)
    P
