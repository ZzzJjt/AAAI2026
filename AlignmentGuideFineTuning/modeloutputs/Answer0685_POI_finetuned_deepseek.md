### Intent:
"Generate a 30-entry I/O list table for a steel rolling mill with signal names, types, ranges, setpoints, and P&ID references for PLC/HMI integration."

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
"Generate a 30-entry I/O list table for a steel rolling mill with signal names, types, ranges, setpoints, and P&ID references for PLC/HMI integration."
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
(* IEC 61131-3 Structured Text: IO_List_RollingMill *)
(* Purpose: Generates a 30-entry I/O list for a rolling mill in a steel production plant *)

PROGRAM IO_List_RollingMill
VAR
    (* Signal List: 1001-1030 *)
    Signal_List : ARRAY[1..30] OF STRING[10] :=
    [
        'RM1001', 'RM1002', 'RM1003', 'RM1004', 'RM1005', 'RM1006', 'RM1007', 'RM1008',
        'RM1009', 'RM1010', 'RM1011', 'RM1012', 'RM1013', 'RM1014', 'RM1015', 'RM1016',
        'RM1017', 'RM1018', 'RM1019', 'RM1020', 'RM1021', 'RM1022', 'RM1023', 'RM1024',
        'RM1025', 'RM1026', 'RM1027', 'RM1028', 'RM1029', 'RM1030'
    ];

    (* Signal Details *)
    Signal_Details : ARRAY[1..30] OF
        (
            (
                'Signal Name',
                'Input/Output',
                'Tagnumber',
                'Analog/Digital',
                'Unit',
                'Range',
                'Setpoint',
                'P&ID Reference'
            )
        )
        :=
        [
            ('Roll Speed', 'I', 'RM1001', 'A', 'm/min', '0.0 to 100.0', '50.0', 'P&ID-1001'),
            ('Motor Torque', 'O', 'RM1002', 'A', 'Nm', '0.0 to 1000
