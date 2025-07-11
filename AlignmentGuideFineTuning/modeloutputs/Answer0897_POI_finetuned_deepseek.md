### Intent:
**Intent Summary:**  
Create a safety-focused car wash control program in IEC 61131-3 Structured Text that automatically starts washing when a car is detected, immediately stops and alarms if a human is present, and requires manual reset after interruptions—ensuring safe operation through interlocks and state management.  

*(Key aspects: human/car detection, emergency stop, manual reset, and safe-state enforcement)*

### Prompt:
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained IEC 61131-3 Structured Text (ST) program to control a heating system using input from three temperature sensors. The system must maintain the room temperature between 20°C and 22°C, ensure energy-efficient operation, and handle sensor faults or abnormal values safely.

⸻

🟩 A (Action) – How to Do It
	1.	Read sensor inputs:
	•	TempSensor1, TempSensor2, TempSensor3 are REAL values in °C.
	2.	Compute average temperature:
	•	Use the three sensors to calculate a reliable average (AvgTemp) for smooth control.
	3.	Check for safety:
	•	If any sensor reads below 10°C or above 30°C, raise a SensorFault flag and turn off the heating for safety.
	4.	Control the heating system with hysteresis:
	•	If AvgTemp < 20.0°C and no fault → turn heating ON
	•	If AvgTemp > 22.0°C and no fault → turn heating OFF
	•	Maintain current state when AvgTemp is between 20–22°C to avoid frequent switching.

⸻

🟦 G (Goal) – What You Want to Achieve

Develop a reliable and efficient control program that:
	•	Maintains a stable room temperature within the 20–22°C range
	•	Minimizes energy waste by avoiding unnecessary toggling of the heater
	•	Protects the system by handling abnormal sensor readings gracefully
	•	Is modular and easy to extend for alarm handling, overrides, or data logging

⸻

✅ Sample Code Snippet:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Sensor fault detection
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE;
ELSE
    SensorFault := FALSE;

    // Hysteresis-based control
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a safety-focused car wash control program in IEC 61131-3 Structured Text that automatically starts washing when a car is detected, immediately stops and alarms if a human is present, and requires manual reset after interruptions—ensuring safe operation through interlocks and state management.  

*(Key aspects: human/car detection, emergency stop, manual reset, and safe-state enforcement)*
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained IEC 61131-3 Structured Text (ST) program to control a heating system using input from three temperature sensors. The system must maintain the room temperature between 20°C and 22°C, ensure energy-efficient operation, and handle sensor faults or abnormal values safely.

⸻

🟩 A (Action) – How to Do It
	1.	Read sensor inputs:
	•	TempSensor1, TempSensor2, TempSensor3 are REAL values in °C.
	2.	Compute average temperature:
	•	Use the three sensors to calculate a reliable average (AvgTemp) for smooth control.
	3.	Check for safety:
	•	If any sensor reads below 10°C or above 30°C, raise a SensorFault flag and turn off the heating for safety.
	4.	Control the heating system with hysteresis:
	•	If AvgTemp < 20.0°C and no fault → turn heating ON
	•	If AvgTemp > 22.0°C and no fault → turn heating OFF
	•	Maintain current state when AvgTemp is between 20–22°C to avoid frequent switching.

⸻

🟦 G (Goal) – What You Want to Achieve

Develop a reliable and efficient control program that:
	•	Maintains a stable room temperature within the 20–22°C range
	•	Minimizes energy waste by avoiding unnecessary toggling of the heater
	•	Protects the system by handling abnormal sensor readings gracefully
	•	Is modular and easy to extend for alarm handling, overrides, or data logging

⸻

✅ Sample Code Snippet:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Sensor fault detection
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE;
ELSE
    SensorFault := FALSE;

    // Hysteresis-based control
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;

// Manual reset
IF ManualReset THEN
    HeatingOn := FALSE;
    SensorFault := FALSE;
END_IF;
This program ensures smooth temperature regulation, prevents overheating or freezing, and handles sensor faults safely.
PROGRAM CarWashControl
VAR
    // Inputs
    CarDetected : BOOL; // TRUE when a car is detected
    HumanDetected : BOOL; // TRUE when a human is detected
    EmergencyStop : BOOL; // TRUE to stop the wash
    ManualReset : BOOL; // TRUE to reset the system

    // Outputs
    WashMotor : BOOL; // TRUE to start washing
    Alarm : BOOL; // TRUE to trigger an alarm
    EmergencyStopButton : BOOL; // TRUE to stop the wash
    ManualResetButton : BOOL; // TRUE to reset the system

    // Internal state
    State : INT := 0; // 0 = Idle, 1 = Washing, 2 = EmergencyStop, 3 = ManualReset
    Timer : TON; // Timer for 30 seconds
END_VAR

// Initialize outputs
WashMotor := FALSE;
Alarm := FALSE;
EmergencyStopButton := FALSE;
ManualResetButton := FALSE;

// Main loop
LOOP
    CASE State OF
        0: // Idle
            IF CarDetected THEN
                State := 1; // Start washing
                WashMotor := TRUE;
                Timer(IN := FALSE, PT := T#30s);
            ELSIF HumanDetected THEN
                State := 2; // Stop washing and trigger alarm
                WashMotor := FALSE;
                Alarm := TRUE;
                Timer(IN := FALSE, PT := T#30s);
            ELSIF EmergencyStop THEN
                State := 3; // Reset system
                WashMotor := FALSE;
                Alarm := FALSE;
                ManualResetButton := TRUE;
                Timer(IN := FALSE, PT := T#30s);
            END_CASE;

        1: // Washing
            IF Timer.Q THEN
                State := 0; // Reset to idle
                WashMotor := FALSE;
                Alarm := FALSE;
                ManualResetButton := FALSE;
                Timer(IN := FALSE, PT := T#30s);
            END_IF;

        2: // EmergencyStop
            IF Timer.Q THEN
