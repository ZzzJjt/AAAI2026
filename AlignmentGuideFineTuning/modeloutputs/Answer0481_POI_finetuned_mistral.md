### Intent:
**Intent Summary:**  
Design an interlock system for a chemical reactor that automatically triggers safety actions (e.g., opening relief valves, shutdowns) in response to hazardous conditions (e.g., overpressure, sensor/valve faults) while ensuring fail-safe operation and auditability.

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.

### Generated Code:
**Intent Summary:**  
Design an interlock system for a chemical reactor that automatically triggers safety actions (e.g., opening relief valves, shutdowns) in response to hazardous conditions (e.g., overpressure, sensor/valve faults) while ensuring fail-safe operation and auditability.
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.
FUNCTION_BLOCK FB_ReactorInterlock
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    PressureSensor : REAL; // Reactor pressure (bar)
    TemperatureSensor : REAL; // Reactor temperature (°C)
    FeedValvePosition : BOOL; // Feed valve open status
    CoolantValvePosition : BOOL; // Coolant valve open status
    HeaterStatus : BOOL; // Heater status
    EmergencyStop : BOOL; // Emergency stop status
    SensorFault : BOOL; // Sensor fault status
    ValveFault : BOOL; // Valve fault status
    SystemPowerOn : BOOL; // System power status
    SystemPowerOff : BOOL; // System power off status
END_VAR

VAR_OUTPUT
    InterlockActive : BOOL; // Interlock status flag
    Shutdown : BOOL; // Reactor shutdown command
    Alarm : BOOL; // Alarm status
    LogEntry : STRING[80]; // Log entry for audit trail
    LogEntry2 : STRING[80]; // Log entry for faults
END_VAR

VAR
    MaxPressure : REAL := 15.0; // Maximum reactor pressure (bar)
    MinPressure : REAL := 5.0; // Minimum reactor pressure (bar)
    MaxTemperature : REAL := 120.0; // Maximum reactor temperature (°C)
    MinTemperature : REAL := 80.0; // Minimum reactor temperature (°C)
    MaxFeedValve : REAL := 100.0; // Maximum feed valve opening (%)
    MaxCoolantValve : REAL := 100.0; // Maximum coolant valve opening (%)
    MaxHeater : REAL := 100.0; // Maximum heater power (%)
    MaxSensorFault : REAL := 100.0; // Maximum sensor fault (%)
    MaxValveFault : REAL := 100.0; // Maximum valve fault (%)
    MaxPowerOn : REAL
