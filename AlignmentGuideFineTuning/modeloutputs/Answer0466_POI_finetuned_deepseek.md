### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement a fail-safe interlock system for a prill station, monitoring temperature, pressure, flow, and safety signals to automatically shut down equipment and trigger alarms during hazardous conditions, with manual reset capability.  

*(Focus: Safety interlocks, multi-parameter monitoring, automated shutdown, and fault recovery.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer or process control engineer responsible for implementing overfill protection in a vessel using IEC 61131-3 Structured Text to ensure safe, automatic operation in an industrial environment.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text program that:
	•	Uses a level sensor to monitor the liquid level in a vessel
	•	Controls an inlet valve to prevent overfilling
	•	Implements interlock logic based on safety thresholds
	•	Includes fail-safe handling in case of sensor or valve failure

Specific control conditions:
	•	Close the inlet valve if the level exceeds a high-level setpoint
	•	Keep the valve closed until the level falls below a reset threshold
	•	Default to a safe state (valve closed) if a sensor fault or valve fault is detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the variables and thresholds, including LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, and INLET_VALVE.
	2.	Implement interlock logic using Structured Text:
	•	Detect high-level condition and close the valve
	•	Latch the shutdown state until the level is safely below reset
	•	Monitor sensor/valve faults and trigger fail-safe action
	3.	Add logic for manual reset or alarm signaling, if needed, to meet process safety standards.
	4.	Comment and structure the code clearly for operational teams and future maintenance.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement a fail-safe interlock system for a prill station, monitoring temperature, pressure, flow, and safety signals to automatically shut down equipment and trigger alarms during hazardous conditions, with manual reset capability.  

*(Focus: Safety interlocks, multi-parameter monitoring, automated shutdown, and fault recovery.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer or process control engineer responsible for implementing overfill protection in a vessel using IEC 61131-3 Structured Text to ensure safe, automatic operation in an industrial environment.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text program that:
	•	Uses a level sensor to monitor the liquid level in a vessel
	•	Controls an inlet valve to prevent overfilling
	•	Implements interlock logic based on safety thresholds
	•	Includes fail-safe handling in case of sensor or valve failure

Specific control conditions:
	•	Close the inlet valve if the level exceeds a high-level setpoint
	•	Keep the valve closed until the level falls below a reset threshold
	•	Default to a safe state (valve closed) if a sensor fault or valve fault is detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the variables and thresholds, including LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, and INLET_VALVE.
	2.	Implement interlock logic using Structured Text:
	•	Detect high-level condition and close the valve
	•	Latch the shutdown state until the level is safely below reset
	•	Monitor sensor/valve faults and trigger fail-safe action
	3.	Add logic for manual reset or alarm signaling, if needed, to meet process safety standards.
	4.	Comment and structure the code clearly for operational teams and future maintenance.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications.
FUNCTION_BLOCK FB_TemperatureControl
VAR_INPUT
    Temp_Setpoint : REAL; // Target temperature in °C
    Temp_Current : REAL; // Current temperature in °C
    Temp_Sensor_Fault : BOOL; // TRUE if temperature sensor is faulty
END_VAR

VAR_OUTPUT
    Temp_Valve_Open : BOOL; // TRUE to open the valve
    Temp_Valve_Closed : BOOL; // TRUE to close the valve
    Temp_Alarm : BOOL; // TRUE if temperature exceeds setpoint
    Temp_Alarm_Reset : BOOL; // TRUE to reset the alarm
END_VAR

VAR
    Temp_Diff : REAL; // Temperature difference between setpoint and current
    Temp_Alarm_Active : BOOL; // TRUE if temperature alarm is active
END_VAR

// Initialize outputs
Temp_Valve_Open := FALSE;
Temp_Valve_Closed := FALSE;
Temp_Alarm := FALSE;
Temp_Alarm_Reset := FALSE;

// Check if temperature sensor is faulty
IF Temp_Sensor_Fault THEN
    Temp_Valve_Open := FALSE;
    Temp_Alarm := FALSE;
    Temp_Alarm_Reset := FALSE;
    RETURN;
END_IF;

// Calculate temperature difference
Temp_Diff := Temp_Setpoint - Temp_Current;

// Check if temperature alarm is active
IF Temp_Alarm_Active THEN
    // Reset the alarm if it is active
    Temp_Alarm_Reset := TRUE;
    RETURN;
END_IF;

// Check if temperature exceeds setpoint
IF Temp_Diff > 5.0 THEN // Setpoint is 5.0°C
    Temp_Alarm := TRUE;
    Temp_Alarm_Active := TRUE;
END_IF;

// Check if temperature is below setpoint
IF Temp_Diff < -5.0 THEN // Setpoint is -5.0°C
    Temp_Alarm := TRUE;
    Temp_Alarm_Active := TRUE;
END_IF;

// Open the valve if temperature is within setpoint range
IF Temp_Alarm_Reset THEN
    Temp_Valve_Open := TRUE;
END_IF;

// Close the valve if temperature is outside setpoint range
IF Temp_Alarm_Active THEN
    Temp_Valve_Closed :=
