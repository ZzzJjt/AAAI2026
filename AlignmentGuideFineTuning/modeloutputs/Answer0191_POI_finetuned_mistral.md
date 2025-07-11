### Intent:
**Intent Summary:**  
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*

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
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*
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
(* Piping & Instrumentation Diagram for Steam-Water Cycle *)
(* Section 1: Steam Generator *)
(* Section 2: Steam Turbine *)
(* Section 3: Condenser *)
(* Section 4: Feedwater System *)
(* Section 5: Boiler Feed Pump *)
(* Section 6: Deaerator *)
(* Section 7: Feedwater Heater *)
(* Section 8: Steam Drum *)
(* Section 9: Steam Traps *)
(* Section 10: Steam Valves *)
(* Section 11: Instrumentation *)
(* Section 12: Control Loops *)
(* Section 13: Alarms and Interlocks *)
(* Section 14: Control Narrative *)
(* Section 15: PLC/HMI Configuration *)
(* Section 16: Safety and Maintenance *)
(* Section 17: Piping Layout *)
(* Section 18: Equipment List *)
(* Section 19: Control Valve Schedules *)
(* Section 20: P&ID Revision History *)
(* Section 21: P&ID Signature Block *)
(* Section 22: P&ID Approval Workflow *)
(* Section 23: P&ID Quality Assurance *)
(* Section 24: P&ID Training and Documentation *)
(* Section 25: P&ID Compliance Checklist *)
(* Section 26: P&ID Risk Assessment *)
(* Section 27: P&ID Change Management *)
(* Section 28: P&ID Integration with DCS/PLC *)
(* Section 29: P&ID Validation and Verification *)
(* Section 30: P&ID Sign-off *)
(* Section 31: P&ID Maintenance Plan *)
(* Section 32: P&ID Spare Parts List *)
(* Section 33: P&ID Training Materials *)
(* Section 34: P&ID Operator Procedures *)
(* Section 35: P&ID Troubleshooting Guide *)
(* Section 36: P&ID Fault Diagrams *)
(* Section 37: P&ID Failure Modes and
