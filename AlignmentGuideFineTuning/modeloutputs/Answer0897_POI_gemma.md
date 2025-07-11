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

// Heating control
IF HeatingOn THEN
    // Turn on the heating
ELSE
    // Turn off the heating
END_IF;

**Elevator Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control an elevator system. The program should use input from a button to determine the desired floor and output to control the elevator's movement. The program must ensure safe operation by implementing interlocks and state management.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained IEC 61131-3 Structured Text (ST) program to control an elevator system. The program should use input from a button to determine the desired floor and output to control the elevator's movement. The program must ensure safe operation by implementing interlocks and state management.

⸻

🟩 A (Action) – How to Do It
	1.	Read button input:
	•	Button is a BOOL value indicating the desired floor.
	2.	Check for safety:
	•	If the elevator is already moving, raise an interlock flag and stop the elevator.
	3.	Control the elevator:
	•	If the elevator is idle and the button is pressed, move the elevator to the desired floor.
	•	If the elevator is moving and the button is pressed, stop the elevator and raise an interlock flag.
	•	If the elevator is at the desired floor, turn off the button and reset the interlock flag.

⸻

🟦 G (Goal) – What You Want to Achieve

Develop a reliable and efficient control program that:
	•	Handles button inputs to determine the desired floor
	•	Ensures safe operation by implementing interlocks and state management
	•	Is modular and easy to extend for additional features or safety measures

⸻

✅ Sample Code Snippet:
VAR
    Button : BOOL;
    Moving : BOOL := FALSE;
    Interlock : BOOL := FALSE;
END_VAR

// Read button input
Button := ButtonInput;

// Check for safety
IF Moving THEN
    Interlock := TRUE;
    Moving := FALSE;
END_IF;

// Control the elevator
IF NOT Moving AND Button THEN
    Moving := TRUE;
    // Move the elevator to the
