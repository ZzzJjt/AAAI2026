### Intent:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating the defined setpoints, control loops, and interlock logic into programmable automation code.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer developing a formal control narrative for a reactor producing ammonium nitrate, intended for automation system configuration, safety documentation, and operator reference.

⸻

🟩 T (Task) – Define the Objective

Draft a control narrative that:
	•	Describes the process purpose and operating principles of the ammonium nitrate reactor
	•	Specifies key process parameters with setpoints and acceptable ranges (e.g., temperature, pressure, pH, flow ratios)
	•	Details the required instrumentation and control equipment, including control loops (e.g., TIC, PIC, FIC), sensors, and valves
	•	Outlines the sequence of operation for startup, normal operation, and shutdown
	•	Includes interlock conditions and alarm logic to ensure safe and stable operation

⸻

🟧 F (Format) – Specify the Output Format

Structure the control narrative as follows:
	1.	Process Overview
	•	Purpose: Neutralize nitric acid with ammonia to produce ammonium nitrate
	•	Reactor Type: Continuous Stirred Tank Reactor (CSTR)
	•	Normal flow conditions and operational limits
	2.	Key Setpoints and Ranges
	•	Temperature (TIC-101): 175 °C ± 2 °C
	•	Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia:Acid Ratio (FRC-103): 1.01:1
	•	pH Control (AIC-105): Target = 6.2, acceptable range = 5.8–6.5
	3.	Instrumentation and Equipment
	•	Flow transmitters (FIC-103, FIC-104), pH analyzer (AIC-105)
	•	Safety interlocks: high-pressure switch, high-temperature alarm, emergency shutoff valve (ESD-106)
	4.	Sequence of Operation
	•	Startup: Initialize controllers, ramp up feed flows, preheat reactor, activate ratio and pH control
	•	Steady-State: Maintain PID loops, monitor deviation alarms, and log key values
	•	Shutdown: Isolate feeds, depressurize, stop heating, drain reactor contents
	5.	Interlocks and Alarms
	•	Temperature > 185 °C → emergency shutdown
	•	Pressure > 5.2 bar → close feed valves
	•	pH < 5.5 → alarm + reduce ammonia flow

### Generated Code:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating the defined setpoints, control loops, and interlock logic into programmable automation code.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer developing a formal control narrative for a reactor producing ammonium nitrate, intended for automation system configuration, safety documentation, and operator reference.

⸻

🟩 T (Task) – Define the Objective

Draft a control narrative that:
	•	Describes the process purpose and operating principles of the ammonium nitrate reactor
	•	Specifies key process parameters with setpoints and acceptable ranges (e.g., temperature, pressure, pH, flow ratios)
	•	Details the required instrumentation and control equipment, including control loops (e.g., TIC, PIC, FIC), sensors, and valves
	•	Outlines the sequence of operation for startup, normal operation, and shutdown
	•	Includes interlock conditions and alarm logic to ensure safe and stable operation

⸻

🟧 F (Format) – Specify the Output Format

Structure the control narrative as follows:
	1.	Process Overview
	•	Purpose: Neutralize nitric acid with ammonia to produce ammonium nitrate
	•	Reactor Type: Continuous Stirred Tank Reactor (CSTR)
	•	Normal flow conditions and operational limits
	2.	Key Setpoints and Ranges
	•	Temperature (TIC-101): 175 °C ± 2 °C
	•	Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia:Acid Ratio (FRC-103): 1.01:1
	•	pH Control (AIC-105): Target = 6.2, acceptable range = 5.8–6.5
	3.	Instrumentation and Equipment
	•	Flow transmitters (FIC-103, FIC-104), pH analyzer (AIC-105)
	•	Safety interlocks: high-pressure switch, high-temperature alarm, emergency shutoff valve (ESD-106)
	4.	Sequence of Operation
	•	Startup: Initialize controllers, ramp up feed flows, preheat reactor, activate ratio and pH control
	•	Steady-State: Maintain PID loops, monitor deviation alarms, and log key values
	•	Shutdown: Isolate feeds, depressurize, stop heating, drain reactor contents
	5.	Interlocks and Alarms
	•	Temperature > 185 °C → emergency shutdown
	•	Pressure > 5.2 bar → close feed valves
	•	pH < 5.5 → alarm + reduce ammonia flow
	6.	Conclusion: Ensure safe, stable, and efficient operation of the ammonium nitrate reactor
(* IEC 61131-3 Structured Text Program for PID Control of a Reactor *)
(* Purpose: Maintains reactor temperature at 175°C with 2% setpoint tolerance *)
(* Uses PID control with tuned gains (Kp=2.0, Ki=0.5, Kd=0.2) *)
(* Includes safety interlocks for over/under temperature *)

PROGRAM PRG_ReactorControl
VAR
    (* Inputs *)
    Temp_PV : REAL;                    (* Measured reactor temperature, °C *)
    Temp_SP : REAL := 175.0;           (* Target temperature, °C *)
    Temp_TOL : REAL := 3.5;            (* Temperature tolerance, °C *)
    
    (* Outputs *)
    Temp_Output : REAL;                (* Control signal to heater, % *)
    Temp_Alarm : BOOL;                 (* TRUE if temperature out of bounds *)
    
    (* Internal Variables *)
    Temp_Error : REAL;                 (* Error between SP and PV, °C *)
    Temp_Integral : REAL;              (* Accumulated error, % *)
    Temp_Derivative : REAL;            (* Rate of change of error, %/s *)
    Temp_Control : REAL;               (* PID output, % *)
    
    (* PID Tuning Parameters *)
    Kp : REAL := 2.0;                  (* Proportional gain *)
    Ki : REAL := 0.5;                  (* Integral gain *)
    Kd : REAL := 0.2;                  (* Derivative gain *)
    
    (* Control Logic *)
    Temp_Control_Enabled : BOOL := TRUE;
    Temp_Control_Init : BOOL := FALSE;
    Temp_Control_Last : REAL := 0.0;
    
    (* Safety Interlocks *)
    Temp_High_Limit : REAL := 185.0;   (* High temperature limit, °C *)
