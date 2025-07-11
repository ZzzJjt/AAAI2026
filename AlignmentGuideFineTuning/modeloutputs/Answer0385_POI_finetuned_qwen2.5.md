### Intent:
**Intent Summary:**  
Generate a structured I/O list table with 30 entries for a rolling mill, including signal names, I/O types, tagnumbers, analog/digital classification, units, ranges, setpoints, and P&ID references, to standardize automation documentation and ensure seamless integration.  

*(Focus: Automation data standardization for PLC/HMI integration in steel production.)*

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In the design and automation of a rolling mill within a steel production plant, a clearly defined I/O list is essential for engineering coordination across instrumentation, control logic, wiring diagrams, and HMIs. This list ensures that all signals are accurately identified and mapped with associated parameters such as range, unit, and control setpoints—critical for system integration and commissioning.

⸻

🟩 A (Action) – Task to Perform

Create a structured I/O list table with 30 signals for a rolling mill. Each row should represent one signal and include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

Ensure that signals represent realistic rolling mill components, such as roll gap sensors, motor drives, cooling valves, and tension feedback. Use consistent units (e.g., °C, bar, kN, m/min) and appropriate setpoints and ranges.

⸻

🟨 R (Result) – Expected Outcome

The result should be a complete, clearly formatted I/O list that serves as a master reference for system design, PLC programming, field wiring, and control documentation. It should improve communication between mechanical, electrical, and automation teams, and reduce integration errors during commissioning.

⸻

🟦 E (Example) – Concrete Illustration

Signal Name
I/O
Tag Number
A/D
Unit
Range
Setpoint
P&ID Ref
EntryRollSpeed
IN
RM1001
A
m/min
0â€“1500
1200
P&ID-01
RollGapFeedback
IN
RM1002
A
mm
0â€“50
22.5
P&ID-01
RollGapSetpoint
OUT
RM1003
A
mm
0â€“50
22.5
P&ID-02
CoolingValveOpen
OUT
RM2001
D
â€”
0 or 1
1
P&ID-03

### Generated Code:
**Intent Summary:**  
Generate a structured I/O list table with 30 entries for a rolling mill, including signal names, I/O types, tagnumbers, analog/digital classification, units, ranges, setpoints, and P&ID references, to standardize automation documentation and ensure seamless integration.  

*(Focus: Automation data standardization for PLC/HMI integration in steel production.)*
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In the design and automation of a rolling mill within a steel production plant, a clearly defined I/O list is essential for engineering coordination across instrumentation, control logic, wiring diagrams, and HMIs. This list ensures that all signals are accurately identified and mapped with associated parameters such as range, unit, and control setpoints—critical for system integration and commissioning.

⸻

🟩 A (Action) – Task to Perform

Create a structured I/O list table with 30 signals for a rolling mill. Each row should represent one signal and include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

Ensure that signals represent realistic rolling mill components, such as roll gap sensors, motor drives, cooling valves, and tension feedback. Use consistent units (e.g., °C, bar, kN, m/min) and appropriate setpoints and ranges.

⸻

🟨 R (Result) – Expected Outcome

The result should be a complete, clearly formatted I/O list that serves as a master reference for system design, PLC programming, field wiring, and control documentation. It should improve communication between mechanical, electrical, and automation teams, and reduce integration errors during commissioning.

⸻

🟦 E (Example) – Concrete Illustration

Signal Name
I/O
Tag Number
A/D
Unit
Range
Setpoint
P&ID Ref
EntryRollSpeed
IN
RM1001
A
m/min
0â€“1500
1200
P&ID-01
RollGapFeedback
IN
RM1002
A
mm
0â€“50
22.5
P&ID-01
RollGapSetpoint
OUT
RM1003
A
mm
0â€“50
22.5
P&ID-02
CoolingValveOpen
OUT
RM2001
D
â€”
0 or 1
1
P&ID-03
TensionSensor
IN
RM3001
A
N
0â€“1000
500
P&ID-04
TensionControl
OUT
RM3002
A
N
0â€“1000
500
P&ID-04
	•	For each signal, include the signal name, whether it’s an input (IN) or output (OUT), the tagnumber, whether it’s analog (A) or digital (D), the engineering unit, the valid range, the setpoint value, and the P&ID reference number.

	•	Ensure that the tagnumber is consistent with the P&ID reference, and that the setpoint values are realistic for the signal’s function.

	•	For signals with ranges, ensure that the setpoint falls within the specified range.

	•	For digital signals, the setpoint should be either 0 or 1, and the engineering unit column should be left blank.

	•	For analog signals, the engineering unit column should contain the appropriate unit of measurement, and the setpoint should be within the specified range.

	•	For signals with no engineering unit, such as a binary state, the engineering unit column should be left blank.

	•	For signals with ranges, ensure that the setpoint is within the specified range.

	•	For signals with no setpoint, such as a sensor, the setpoint column should be left blank.

	•	For signals with no P&ID reference, the P&ID reference column should be left blank.

	•	For signals with no tagnumber, the tagnumber column should be left blank.

	•	For signals with no input/output classification, the input/output column should be left blank.

	•	For signals with no analog/digital classification, the analog/digital column should be left blank.

	•	For signals with no engineering unit, the engineering unit column should be left blank.

	•	For signals with no range, the range column should be left blank.

	•	For signals with no setpoint, the setpoint column should be left blank.

	•	For signals with no P&ID reference, the P&ID reference column should be left blank.

	•	For signals with no tagnumber, the tagnumber column should be left blank.

	•	For signals with no input/output classification, the input/output column
