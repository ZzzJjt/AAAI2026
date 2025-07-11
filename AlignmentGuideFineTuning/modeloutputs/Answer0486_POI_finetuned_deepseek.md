### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automatically close a vessel's inlet valve when a high liquid level is detected (with fail-safe handling for faults), ensuring overfill protection until the level resets to a safe threshold.  

*(Focus: Safety interlock logic for level control with fault resilience.)*

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
Develop an IEC 61131-3 Structured Text program to automatically close a vessel's inlet valve when a high liquid level is detected (with fail-safe handling for faults), ensuring overfill protection until the level resets to a safe threshold.  

*(Focus: Safety interlock logic for level control with fault resilience.)*
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
FUNCTION_BLOCK FB_LevelSensor
VAR_INPUT
    Enable : BOOL; // Enable the level sensor
    Reset : BOOL; // Reset the level sensor
END_VAR

VAR_OUTPUT
    Level : REAL; // Level of the vessel
    Fault : BOOL; // Level sensor fault
END_VAR

VAR
    Level_Sensor : REAL; // Level sensor reading
    Fault_State : BOOL; // Fault state
END_VAR

// Initialize variables
Level := 0.0;
Fault := FALSE;
Fault_State := FALSE;

// Enable the level sensor
IF Enable THEN
    // Read the level sensor
    Level_Sensor := 0.0;
    IF Reset THEN
        Level_Sensor := 0.0;
    END_IF;

    // Check if the level sensor is valid
    IF Level_Sensor > 0.0 THEN
        IF NOT Fault_State THEN
            Fault := FALSE;
        END_IF;
    ELSE
        IF NOT Fault_State THEN
            Fault := TRUE;
        END_IF;
    END_IF;

    // Store the level in the output
    Level := Level_Sensor;
END_IF;

// Reset the level sensor
IF Reset THEN
    Level_Sensor := 0.0;
    Fault_State := FALSE;
END_IF;

END_FUNCTION_BLOCK

FUNCTION_BLOCK FB_Interlock
VAR_INPUT
    Enable : BOOL; // Enable the interlock
    Reset : BOOL; // Reset the interlock
END_VAR

VAR_OUTPUT
    Interlock : BOOL; // Enable or disable the interlock
END_VAR

VAR
    High_Level : REAL; // High-level setpoint
    Low_Level : REAL; // Low-level setpoint
    High_Level_Fault : BOOL; // High-level fault
    Low_Level_Fault : BOOL; // Low-level fault
    High_Level_Reset : BOOL; // High-level reset
    Low_Level_Reset : BOOL; // Low-level reset
END_VAR

// Initialize variables
Interlock := FALSE;
High_Level := 0.0;
Low_Level := 0.0;
High_Level_Fault := FALSE;
Low_Level
