### Intent:
The task is to **create a detailed control narrative for the fermentation phase of ethanol production, specifying setpoints, control strategies, equipment, and safety interlocks in structured paragraphs for automation design and operational documentation**.  

*(Intent: Generate a process control document with precise parameters, logic, and safety measures for ethanol fermentation.)*

### Prompt:
**Control Narrative for Ethanol Production**

Create a control narrative for ethanol production including concrete setpoints and ranges.

Create a detailed explanation of each control step during Fermentation. Create one paragraph per subsection in Section 3.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process automation engineer preparing documentation for the fermentation phase of an ethanol production process, intended for use in control system design, validation, and operations.

⸻

🟩 T (Task) – Define the Objective

Create a control narrative for the ethanol production process, including specific setpoints and acceptable ranges for key parameters.
Focus specifically on the fermentation phase (Section 3) and break it into multiple subsections (e.g., temperature control, pH regulation, inoculation).
For each subsection:
	•	Provide a detailed explanation of the control strategy
	•	Define the target values, such as temperature range or pH band
	•	Describe the equipment involved, control actions, and feedback mechanisms
	•	Write each explanation in one paragraph per subsection

Include mentions of interlocks, alarms, and control system responses to deviations.

⸻

🟧 F (Format) – Specify the Output Format

Produce:
	•	A written control narrative document
	•	Section 3: Fermentation, structured as multiple one-paragraph subsections (e.g., 3.1, 3.2, 3.3…)
	•	Each paragraph should contain:
	•	The control objective
	•	Setpoints/ranges (e.g., 32–35 °C, pH 4.5–5.0)
	•	Descriptions of control logic (e.g., PID loops, on/off valves)
	•	Safety conditions like alarm thresholds or shutdown criteria

### Generated Code:
The task is to **create a detailed control narrative for the fermentation phase of ethanol production, specifying setpoints, control strategies, equipment, and safety interlocks in structured paragraphs for automation design and operational documentation**.  

*(Intent: Generate a process control document with precise parameters, logic, and safety measures for ethanol fermentation.)*
**Control Narrative for Ethanol Production**

Create a control narrative for ethanol production including concrete setpoints and ranges.

Create a detailed explanation of each control step during Fermentation. Create one paragraph per subsection in Section 3.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process automation engineer preparing documentation for the fermentation phase of an ethanol production process, intended for use in control system design, validation, and operations.

⸻

🟩 T (Task) – Define the Objective

Create a control narrative for the ethanol production process, including specific setpoints and acceptable ranges for key parameters.
Focus specifically on the fermentation phase (Section 3) and break it into multiple subsections (e.g., temperature control, pH regulation, inoculation).
For each subsection:
	•	Provide a detailed explanation of the control strategy
	•	Define the target values, such as temperature range or pH band
	•	Describe the equipment involved, control actions, and feedback mechanisms
	•	Write each explanation in one paragraph per subsection

Include mentions of interlocks, alarms, and control system responses to deviations.

⸻

🟧 F (Format) – Specify the Output Format

Produce:
	•	A written control narrative document
	•	Section 3: Fermentation, structured as multiple one-paragraph subsections (e.g., 3.1, 3.2, 3.3…)
	•	Each paragraph should contain:
	•	The control objective
	•	Setpoints/ranges (e.g., 32–35 °C, pH 4.5–5.0)
	•	Descriptions of control logic (e.g., PID loops, on/off valves)
	•	Safety conditions like alarm thresholds or shutdown criteria
	•	Use clear, structured language suitable for automation design, HMI specification, and operator training
(* IEC 61131-3 Structured Text Program for PID Control of a Heating Loop *)
(* Sets temperature using PID control with 100 ms sampling *)
(* Uses PID parameters: Kp = 1.0, Ki = 0.5, Kd = 0.2 *)
(* Inputs: Setpoint (SP), Process Variable (PV), Output (OU), Error (E), Integral (I), Derivative (D), Reset Timer (T), Done (DONE) *)
(* Outputs: Heating Valve (HV), Cooling Valve (CV), Heater (HT), Cooler (CL), Pump (PUMP) *)
(* Controls temperature using PID with 100 ms sampling *)

PROGRAM HeatingLoopControl
VAR
    (* Inputs *)
    SP : REAL;                    (* Temperature setpoint, °C *)
    PV : REAL;                    (* Measured temperature, °C *)
    OU : REAL;                    (* PID output, % *)
    HV : BOOL;                    (* Heating valve, TRUE = Open, FALSE = Closed *)
    CV : BOOL;                    (* Cooling valve, TRUE = Open, FALSE = Closed *)
    HT : BOOL;                    (* Heater, TRUE = On, FALSE = Off *)
    CL : BOOL;                    (* Cooler, TRUE = On, FALSE = Off *)
    PUMP : BOOL;                  (* Pump, TRUE = On, FALSE = Off *)
    
    (* PID Parameters *)
    Kp : REAL := 1.0;             (* Proportional gain *)
    Ki : REAL := 0.5;             (* Integral gain *)
    Kd : REAL := 0.2;             (* Derivative gain *)
    
    (* Control Variables *)
    E : REAL;                     (* Error: SP - PV *)
    I : REAL;                     (* Integral *)
    D : REAL;                     (* Derivative *)
    T : TON
