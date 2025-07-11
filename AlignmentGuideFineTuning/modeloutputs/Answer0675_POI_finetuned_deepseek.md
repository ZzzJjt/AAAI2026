### Intent:
**Intent Summary:**  
Generate a 30-entry I/O list table for a steel rolling mill, specifying signal names, types (input/output, analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC/HMI integration.  

*(Context: Industrial control system documentation for instrumentation and automation teams.)*

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support

### Generated Code:
**Intent Summary:**  
Generate a 30-entry I/O list table for a steel rolling mill, specifying signal names, types (input/output, analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC/HMI integration.  

*(Context: Industrial control system documentation for instrumentation and automation teams.)*
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support
	•	Is reusable and maintainable for future automation and instrumentation upgrades
(* IEC 61131-3 Structured Text: PID Control for Steel Rolling Mill *)
(* Purpose: Adjusts roll speed and gap to maintain optimal rolling conditions *)

PROGRAM SteelRollingMillControl
VAR
    (* Inputs *)
    RollSpeedSetpoint : REAL; (* Target roll speed in mm/min, e.g., 1000.0 *)
    GapSetpoint : REAL; (* Target gap in mm, e.g., 10.0 *)
    MotorTorque : REAL; (* Motor torque in Nm, e.g., 100.0 *)
    CoolingActuation : BOOL; (* Cooling system on/off, TRUE = active *)
    GapFeedback : REAL; (* Measured gap in mm, e.g., 9.5 *)
    TensionFeedback : REAL; (* Measured tension in N, e.g., 100.0 *)
    
    (* Outputs *)
    RollMotorSpeed : REAL; (* Output roll motor speed in mm/min, e.g., 1000.0 *)
    CoolingActuation : BOOL; (* Cooling system output, TRUE = active *)
    GapFeedback : REAL; (* Feedback signal, e.g., 9.5 *)
    TensionFeedback : REAL; (* Feedback signal, e.g., 100.0 *)
    
    (* Internal Variables *)
    RollSpeedPV : REAL; (* Current roll speed, e.g., 980.0 *)
    GapPV : REAL; (* Current gap, e.g., 9.6 *)
    TensionPV : REAL; (* Current tension, e.g., 99.0 *)
    ErrorPV : REAL; (* Error signal, e.g., 1.5 *)
    ErrorPV_100 : REAL; (* Error signal scaled to 100, e.g., 15.0 *)
    ErrorPV_10 : REAL; (* Error signal scaled to 10, e.g., 1.5 *)
    ErrorPV_1000 : REAL; (* Error signal scaled to 1000, e.g., 150.0 *)
    
    (* PID Parameters *)
