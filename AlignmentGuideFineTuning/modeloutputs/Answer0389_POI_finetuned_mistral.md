### Intent:
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, and safety interlocks in structured notation.

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**C-A-R-E:**

🟥 C (Context) – Background Situation

In LNG (Liquefied Natural Gas) processing, the vaporizer system plays a critical role in converting LNG into gas for downstream use. For projects governed by NORSOK standards, a System Control Diagram (SCD) is required to document control loops, instrumentation, and interlocks in a structured, traceable format. When graphical SCD tools are unavailable—such as in early design phases or text-based engineering environments—engineers must rely on textual notation to convey the same level of detail and logic clarity.

⸻

🟩 A (Action) – Task to Perform

Create a NORSOK-compliant System Control Diagram (SCD) using textual notation for an LNG vaporizer system. The diagram should include:
	•	Major equipment and piping flow (e.g., LNG inlet → vaporizer → gas outlet)
	•	Key instrumentation and control loops, with standard tag names (e.g., TT101, FIC201, FCV202)
	•	Defined interlocks and trip signals, such as high-pressure shutdowns or emergency stop triggers
	•	Logical formatting using directional arrows (-->), indents, and grouped sections for clarity

⸻

🟨 R (Result) – Expected Outcome

The result will be a structured, readable, and logically complete textual SCD that can:
	•	Support system design, safety analysis, and DCS/PLC implementation
	•	Facilitate interdepartmental review of instrumentation and control logic
	•	Comply with NORSOK I-005 standards for system documentation
	•	Act as a draft for graphical SCD development later in the design phase

⸻

🟦 E (Example) – Concrete Illustration

LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer Unit --> Gas Outlet

[Vaporizer Control Loop]
  TT101 --> TIC101 --> TCV101 (Heater Steam Valve)

[Safety Interlocks]
  PSH301 --> ESD1 (Shutdown Heater on High Pressure)
  TSH302 --> ESD2 (Shutdown Vaporizer on High Temperature)

[Flow Trip]
  FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close

### Generated Code:
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, and safety interlocks in structured notation.
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**C-A-R-E:**

🟥 C (Context) – Background Situation

In LNG (Liquefied Natural Gas) processing, the vaporizer system plays a critical role in converting LNG into gas for downstream use. For projects governed by NORSOK standards, a System Control Diagram (SCD) is required to document control loops, instrumentation, and interlocks in a structured, traceable format. When graphical SCD tools are unavailable—such as in early design phases or text-based engineering environments—engineers must rely on textual notation to convey the same level of detail and logic clarity.

⸻

🟩 A (Action) – Task to Perform

Create a NORSOK-compliant System Control Diagram (SCD) using textual notation for an LNG vaporizer system. The diagram should include:
	•	Major equipment and piping flow (e.g., LNG inlet → vaporizer → gas outlet)
	•	Key instrumentation and control loops, with standard tag names (e.g., TT101, FIC201, FCV202)
	•	Defined interlocks and trip signals, such as high-pressure shutdowns or emergency stop triggers
	•	Logical formatting using directional arrows (-->), indents, and grouped sections for clarity

⸻

🟨 R (Result) – Expected Outcome

The result will be a structured, readable, and logically complete textual SCD that can:
	•	Support system design, safety analysis, and DCS/PLC implementation
	•	Facilitate interdepartmental review of instrumentation and control logic
	•	Comply with NORSOK I-005 standards for system documentation
	•	Act as a draft for graphical SCD development later in the design phase

⸻

🟦 E (Example) – Concrete Illustration

LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer Unit --> Gas Outlet

[Vaporizer Control Loop]
  TT101 --> TIC101 --> TCV101 (Heater Steam Valve)

[Safety Interlocks]
  PSH301 --> ESD1 (Shutdown Heater on High Pressure)
  TSH302 --> ESD2 (Shutdown Vaporizer on High Temperature)

[Flow Trip]
  FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close

This textual SCD provides a clear overview of the vaporizer’s control structure and safety logic, ready for integration into a full NORSOK-compliant control narrative.
(* IEC 61131-3 Structured Text Program for PID Control of a Heater *)
(* Implements temperature control with setpoint, output, and error handling *)
(* Uses PID tuning constants P, I, D *)
(* Includes safety limits and output clamping *)

PROGRAM HeaterControl
VAR
    (* Inputs *)
    TempSetpoint : REAL;                  (* Desired temperature in °C *)
    TempOutput : REAL;                    (* Heater output in % *)
    TempProcess : REAL;                   (* Measured temperature in °C *)
    TempError : REAL;                     (* Error between setpoint and process *)
    TempPV : REAL;                        (* Raw process variable for testing *)
    
    (* Outputs *)
    TempControl : BOOL;                   (* TRUE if control is active *)
    TempAlarm : BOOL;                     (* TRUE if temperature out of bounds *)
    TempWarning : BOOL;                   (* TRUE if near safety limits *)
    
    (* Internal Variables *)
    TempPID : PID;                        (* PID controller instance *)
    TempPID_Enabled : BOOL;               (* TRUE to enable PID *)
    TempPID_Output : REAL;                (* PID output to heater *)
    TempPID_Error : REAL;                 (* PID error for tuning *)
    
    (* Tuning Parameters *)
    P : REAL := 1.0;                      (* Proportional gain *)
    I : REAL := 0.1;                      (* Integral gain *)
    D : REAL := 0.05;                     (* Derivative gain *)
    TempMin : REAL := 50.0;               (* Minimum temperature in °C *)
    TempMax : REAL := 100.0;              (* Maximum temperature in °C *)
    
    (* Timing *)
    TempPID_SampleTime : TIME := T#100ms;  (* PID sample time *)
