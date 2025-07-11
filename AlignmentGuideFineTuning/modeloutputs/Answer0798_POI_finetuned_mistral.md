### Intent:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201)

### Generated Code:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201)

This format ensures clarity and readability for engineers, automation teams, and control system implementers.
(* IEC 61131-3 Structured Text Program for PID Control of a Heating System *)
(* Sets temperature using PID control with 100 ms sampling *)
(* Uses PV: Temperature, SP: Setpoint, Kp: Proportional Gain, Ki: Integral Gain, Kd: Derivative Gain *)
(* Controls heating element with output range 0.0 to 100.0 *)

PROGRAM HeatingSystemControl
VAR
    (* Inputs *)
    PV : REAL;                      (* Current temperature in °C *)
    SP : REAL;                      (* Target temperature in °C *)
    Kp : REAL := 2.0;               (* Proportional gain *)
    Ki : REAL := 0.1;               (* Integral gain *)
    Kd : REAL := 0.05;              (* Derivative gain *)
    T_sample : TIME := T#100ms;     (* Sampling time *)
    
    (* Outputs *)
    Output : REAL;                  (* Control signal to heating element *)
    Error : REAL;                   (* Error between PV and SP *)
    Integral : REAL;                (* Accumulated error *)
    Derivative : REAL;              (* Rate of change of error *)
    
    (* Internal Variables *)
    LastPV : REAL;                  (* Previous temperature for derivative *)
    LastSP : REAL;                  (* Previous setpoint for integral *)
    LastTime : TIME;                (* Time of last sample for derivative *)
    
    (* Constants *)
    HeatingElementMax : REAL := 100.0; (* Max output to heating element *)
    HeatingElementMin : REAL := 0.0;   (* Min output to heating element *)
END_VAR

(* Main Control Loop *)
WHILE TRUE DO
    (* Update last values *)
    LastPV := PV;
    LastSP := SP;
    LastTime := NOW();
    
    (* Calculate error *)
    Error := SP - PV
