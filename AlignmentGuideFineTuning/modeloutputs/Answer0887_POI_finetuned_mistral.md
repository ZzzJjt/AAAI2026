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
(* Program: Elevator Control System *)
(* Version: 1.0, Date: 2025-05-21 *)
(* Manages elevator movement, floor requests, and door timing *)
(* Uses priority-based control for safety and efficiency *)
PROGRAM ElevatorControl
VAR
    (* Inputs *)
    CurrentFloor : INT := 1;                 (* Current floor position, 1-100 *)
    CallButton : ARRAY[1..100] OF BOOL;     (* Floor call buttons, TRUE=request *)
    DoorOpen : BOOL;                        (* TRUE when door is open *)
    EmergencyStop : BOOL;                   (* TRUE if emergency stop activated *)
    PowerFailure : BOOL;                    (* TRUE if power fails *)
    
    (* Outputs *)
    MoveUp : BOOL;                          (* TRUE to move up *)
    MoveDown : BOOL;                        (* TRUE to move down *)
    DoorOpenRequest : BOOL;                 (* TRUE to open door *)
    DoorCloseRequest : BOOL;                (* TRUE to close door *)
    Alarm : BOOL;                           (* TRUE if system error *)
    ErrorMessage : STRING[80];              (* Error message for operator *)
    
    (* Internal Variables *)
    TargetFloor : INT;                      (* Target floor for movement *)
    RequestQueue : ARRAY[1..100] OF BOOL;   (* Pending floor requests *)
    RequestPriority : ARRAY[1..100] OF INT; (* Request priority: 1=highest *)
    CurrentRequest : INT;                   (* Current request index *)
    RequestCount : INT;                     (* Number of requests *)
    Moving : BOOL;                          (* TRUE when elevator is moving *)
    Idle : BOOL;                            (* TRUE when elevator is idle *)
    EmergencyMode : BOOL;                   (* TRUE for emergency mode *)
    PowerRestored : BOOL;                   (* TRUE if power restored *)
    SystemState : INT := 0;                 (* System state: 0=Normal, 1=Emergency, 2=PowerFailure *)
END_VAR

(* Initialize variables *)
Moving := FALSE;
Idle
