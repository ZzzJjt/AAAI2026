### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control an elevator system, managing floor requests, door timing, and directional movement while prioritizing safety and efficient operation.

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
Create an IEC 61131-3 Structured Text program to control an elevator system, managing floor requests, door timing, and directional movement while prioritizing safety and efficient operation.
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

// Optional: Alarm flag for sensor faults
IF SensorFault THEN
    // Raise alarm or log error
END_IF;
This program ensures smooth temperature regulation, avoids frequent heating on/off transitions, and handles sensor faults safely.
PROGRAM ElevatorControl
VAR
    // Inputs
    FloorRequest : INT; // 0-5 (0=stop, 1=1st floor, 2=2nd floor, etc.)
    DoorOpen : BOOL; // TRUE if door is open
    DoorClosed : BOOL; // TRUE if door is closed
    DoorFault : BOOL; // TRUE if door fault detected
    DoorOpenTime : TIME; // Time when door was opened
    DoorClosedTime : TIME; // Time when door was closed

    // Outputs
    DoorState : BOOL; // TRUE if door is open
    DoorFaultState : BOOL; // TRUE if door fault detected
    DoorOpenTimer : BOOL; // TRUE if door open timer is active
    DoorClosedTimer : BOOL; // TRUE if door closed timer is active
    FloorRequestState : BOOL; // TRUE if floor request is active
    FloorRequestTimer : BOOL; // TRUE if floor request timer is active

    // Internal state
    State : INT := 0; // 0=idle, 1=door open, 2=door closed, 3=floor request
    DoorOpenTimerActive : BOOL := FALSE;
    DoorClosedTimerActive : BOOL := FALSE;
    FloorRequestTimerActive : BOOL := FALSE;
    DoorFaultStateActive : BOOL := FALSE;
END_VAR

// Main control loop
IF State = 0 THEN
    // Idle state
    DoorState := FALSE;
    DoorFaultState := FALSE;
    DoorOpenTimer := FALSE;
    DoorClosedTimer := FALSE;
    FloorRequestTimer := FALSE;
    DoorFaultStateActive := FALSE;
    State := 1;
ELSE
    CASE State OF
        1: // Door open state
            DoorState := TRUE;
            DoorFaultState := FALSE;
            DoorOpenTimer := TRUE;
            DoorClosedTimer := FALSE;
            FloorRequestTimer := FALSE;
            DoorFaultStateActive := FALSE;
            State := 2;

        2: // Door closed state
            DoorState := FALSE;
            DoorFaultState := FALSE;
