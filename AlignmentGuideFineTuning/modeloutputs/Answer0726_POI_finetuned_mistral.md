### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety

You may also include a brief discussion on how this interlock fits into a broader safety instrumented function (SIF) strategy or P&I diagram.
FUNCTION_BLOCK FB_PressureReliefValveControl
VAR_INPUT
    // Inputs from pressure sensor
    PressureSensorValue : REAL; // Pressure reading in bar
    PressureSensorFault : BOOL; // TRUE if sensor is faulty

    // Inputs from valve position sensor
    ValvePositionSensorValue : REAL; // Valve position in percent
    ValvePositionSensorFault : BOOL; // TRUE if sensor is faulty

    // Inputs from manual override
    ManualOverride : BOOL; // TRUE if manual override is active

    // Inputs from safety interlocks
    HighPressureAlarm : BOOL; // TRUE if high pressure alarm is triggered
    LowPressureAlarm : BOOL; // TRUE if low pressure alarm is triggered

    // Inputs from valve control logic
    ValveOpen : BOOL; // TRUE if valve is open
    ValveClosed : BOOL; // TRUE if valve is closed

    // Inputs from system status
    SystemRunning : BOOL; // TRUE if system is running
    SystemFault : BOOL; // TRUE if system is in fault

    // Inputs from HMI
    OpenValve : BOOL; // TRUE to open valve
    CloseValve : BOOL; // TRUE to close valve

    // Inputs from PLC communication
    CommStatus : BOOL; // TRUE if PLC communication is active
    CommError : BOOL; // TRUE if PLC communication has an error
END_VAR

VAR_OUTPUT
    // Outputs to valve control system
    ValveControlCommand : BOOL; // TRUE to open valve, FALSE to close valve

    // Outputs to HMI
    ValveStatus : BOOL; // TRUE if valve is open, FALSE if valve is closed
    ValveFault : BOOL; // TRUE if valve is faulty
    SystemStatus : BOOL; // TRUE if system is running, FALSE if system is in fault
    HighPressureAlarm : BOOL; // TRUE if high pressure alarm is triggered
