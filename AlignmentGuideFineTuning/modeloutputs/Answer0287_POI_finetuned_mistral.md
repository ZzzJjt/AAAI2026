### Intent:
The task involves writing a Structured Text program to control a heating system using three temperature sensors, maintaining a stable range (20-22°C) with hysteresis and safety checks for sensor faults.  

*(For code generation: Create a PLC program that averages three sensor inputs, controls heating with hysteresis, and handles out-of-range sensor faults.)*

### Prompt:
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**C-A-R-E:**

🟥 C (Context) – The Background

Maintaining a stable temperature range in a heating system is critical for comfort, energy efficiency, and safety. When using multiple temperature sensors, it’s essential to calculate a reliable average and include safety logic to handle sensor faults or abnormal temperature deviations. A well-structured IEC 61131-3 Structured Text program is ideal for managing this kind of control task in industrial or building automation environments.

⸻

🟩 A (Action) – The Implementation Task

Write a self-contained Structured Text (ST) program that performs the following:
	1.	Reads temperature from three sensors
	2.	Calculates the average temperature to ensure reliable control
	3.	Turns the heating ON when average temperature is below 20°C
	4.	Turns the heating OFF when average temperature is above 22°C
	5.	Implements hysteresis to avoid frequent toggling between ON/OFF states
	6.	Adds safety logic:
	•	If any sensor reads below 10°C or above 30°C, treat it as a fault
	•	In the event of a fault, turn off heating and flag the error

⸻

🟨 R (Result) – The Expected Outcome

The program will:
	•	Maintain room temperature in the desired 20°C–22°C range
	•	Avoid frequent switching by using hysteresis control
	•	Ensure safe operation by turning off the heating system if any sensor reports abnormal values
	•	Be suitable for deployment on industrial PLCs for reliable, real-time temperature management

⸻

🟦 E (Example) – A Practical Code Snippet
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

// Calculate average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Fault detection
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE;
ELSE
    SensorFault := FALSE;

    // Hysteresis control logic
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;

### Generated Code:
The task involves writing a Structured Text program to control a heating system using three temperature sensors, maintaining a stable range (20-22°C) with hysteresis and safety checks for sensor faults.  

*(For code generation: Create a PLC program that averages three sensor inputs, controls heating with hysteresis, and handles out-of-range sensor faults.)*
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**C-A-R-E:**

🟥 C (Context) – The Background

Maintaining a stable temperature range in a heating system is critical for comfort, energy efficiency, and safety. When using multiple temperature sensors, it’s essential to calculate a reliable average and include safety logic to handle sensor faults or abnormal temperature deviations. A well-structured IEC 61131-3 Structured Text program is ideal for managing this kind of control task in industrial or building automation environments.

⸻

🟩 A (Action) – The Implementation Task

Write a self-contained Structured Text (ST) program that performs the following:
	1.	Reads temperature from three sensors
	2.	Calculates the average temperature to ensure reliable control
	3.	Turns the heating ON when average temperature is below 20°C
	4.	Turns the heating OFF when average temperature is above 22°C
	5.	Implements hysteresis to avoid frequent toggling between ON/OFF states
	6.	Adds safety logic:
	•	If any sensor reads below 10°C or above 30°C, treat it as a fault
	•	In the event of a fault, turn off heating and flag the error

⸻

🟨 R (Result) – The Expected Outcome

The program will:
	•	Maintain room temperature in the desired 20°C–22°C range
	•	Avoid frequent switching by using hysteresis control
	•	Ensure safe operation by turning off the heating system if any sensor reports abnormal values
	•	Be suitable for deployment on industrial PLCs for reliable, real-time temperature management

⸻

🟦 E (Example) – A Practical Code Snippet
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

// Calculate average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Fault detection
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE;
ELSE
    SensorFault := FALSE;

    // Hysteresis control logic
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;
This code block:
	•	Reads sensor values
	•	Calculates the average
	•	Applies hysteresis to minimize switching
	•	Handles sensor faults by disabling heating and setting a flag
	•	Is modular, readable, and suitable for deployment in a PLC environment
PROGRAM PLC_PRG
TITLE 'Heating System Control with Sensor Fault Handling'

(*
    Description:
    Controls a heating system using three temperature sensors.
    Maintains a stable temperature range (20-22°C) with hysteresis and fault handling.

    Safety Features:
    - Fault detection for out-of-range sensor values
    - Emergency shutdown logic for unsafe conditions
    - Clear variable names and modular structure

    IEC 61131-3 Compliance:
    - Structured Text (ST)
    - Modular design with function blocks (not used in this example)
    - Clear variable declarations
    - Conditional logic for fault detection and emergency shutdown
*)

VAR
    (*
        Inputs
    *)
    TempSensor1 : REAL;                  // Temperature from Sensor 1 (°C)
    TempSensor2 : REAL;                  // Temperature from Sensor 2 (°C)
    TempSensor3 : REAL;                  // Temperature from Sensor 3 (°C)
    SensorFault : BOOL;                  // TRUE if any sensor is faulty

    (*
        Outputs
    *)
    HeatingOn : BOOL;                     // TRUE to activate heating
    EmergencyStop : BOOL;                // TRUE to stop heating immediately
    FaultMessage : STRING[80];           // Diagnostic message for faults

    (*
        Internal Variables
    *)
    AvgTemp : REAL;                      // Average temperature from sensors
    TargetTemp : REAL := 21.0;           // Target temperature (°C)
    Hysteresis : REAL := 1.0;            // Width of hysteresis band (°C)
    HeatingThreshold : REAL;             // Lower threshold for heating
