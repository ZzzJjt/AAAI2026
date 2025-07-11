### Intent:
**Intent Summary:**  
Create a standardized control narrative for beer brewing automation, specifying setpoints, instrumentation, and step-by-step lautering logic (including equipment, sensors, and conditional actions like turbidity-based flow diversion).  

*(Focus: Documentation for PLC/DCS implementation with precise parameters and procedural clarity.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity

### Generated Code:
**Intent Summary:**  
Create a standardized control narrative for beer brewing automation, specifying setpoints, instrumentation, and step-by-step lautering logic (including equipment, sensors, and conditional actions like turbidity-based flow diversion).  

*(Focus: Documentation for PLC/DCS implementation with precise parameters and procedural clarity.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity
(* IEC 61131-3 Structured Text Program: Beer Brewing Control *)
(* Purpose: Automates brewing process with precise control of temperature, flow, and timing *)

PROGRAM BeerBrewingControl
VAR
    (* Inputs *)
    StartBrewing : BOOL;                    (* TRUE to start brewing process *)
    StopBrewing : BOOL;                     (* TRUE to stop brewing process *)
    MashTempSetpoint : REAL;                (* Mash temperature setpoint, e.g., 67.0 °C *)
    SpargeTempSetpoint : REAL;              (* Sparge temperature setpoint, e.g., 75.0 °C *)
    MashFlowSetpoint : REAL;                (* Mash flow setpoint, e.g., 1.5 L/min *)
    SpargeFlowSetpoint : REAL;              (* Sparge flow setpoint, e.g., 2.0 L/min *)
    MashTimeSetpoint : TIME;                (* Mash time setpoint, e.g., T#30m *)
    SpargeTimeSetpoint : TIME;              (* Sparge time setpoint, e.g., T#60m *)
    MashTurbiditySetpoint : REAL;           (* Mash turbidity setpoint, e.g., 1000 NTU *)
    SpargeTurbiditySetpoint : REAL;         (* Sparge turbidity setpoint, e.g., 500 NTU *)
    MashTemperatureSensor : REAL;           (* Measured mash temperature, e.g., 66.5 °C *)
    SpargeTemperatureSensor : REAL;         (* Measured sparge temperature, e.g., 74.5 °C *)
    MashFlowSensor : REAL;                  (* Measured mash flow, e.g., 1.4 L/min *)
    SpargeFlowSensor : REAL;                (* Measured sparge flow, e.g., 1.8 L/min *)
    MashTurbiditySensor : REAL;             (* Measured mash turbidity
