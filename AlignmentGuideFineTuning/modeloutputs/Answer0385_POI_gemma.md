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
CoolingValveClose
OUT
RM2002
D
â€”
0 or 1
0
P&ID-03
MotorDrive1
OUT
RM3001
D
â€”
0 or 1
1
P&ID-04
MotorDrive2
OUT
RM3002
D
â€”
0 or 1
1
P&ID-04
TensionFeedback
IN
RM4001
A
kN
0â€“100
50
P&ID-05
TensionSetpoint
OUT
RM4002
A
kN
0â€“100
50
P&ID-05
RollGapSensor1
IN
RM5001
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor2
IN
RM5002
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor3
IN
RM5003
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor4
IN
RM5004
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor5
IN
RM5005
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor6
IN
RM5006
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor7
IN
RM5007
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor8
IN
RM5008
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor9
IN
RM5009
A
mm
0â€“50
22.5
P&ID-06
RollGapSensor10
IN
RM5010
A
mm
0â€“50
22.5
P&ID-06
RollGap
