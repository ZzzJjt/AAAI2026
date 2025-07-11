### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a heating system using three temperature sensors, maintaining a stable range (20°C–22°C) with hysteresis, fault detection for abnormal readings (<10°C or >30°C), and diagnostic logging for safety and traceability.  

*(Key focus: Temperature regulation, sensor fault handling, hysteresis, and logging in industrial automation.)*

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
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a heating system using three temperature sensors, maintaining a stable range (20°C–22°C) with hysteresis, fault detection for abnormal readings (<10°C or >30°C), and diagnostic logging for safety and traceability.  

*(Key focus: Temperature regulation, sensor fault handling, hysteresis, and logging in industrial automation.)*
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
FUNCTION_BLOCK TemperatureControlFB
VAR_INPUT
    TempSensor1, TempSensor2, TempSensor3 : REAL; // Input temperature sensors
END_VAR

VAR_OUTPUT
    HeatingOn : BOOL; // Output: ON if heating is active
    SensorFault : BOOL; // Output: TRUE if any sensor is faulty
    LogError : BOOL; // Output: TRUE if an error occurred
END_VAR

VAR
    AvgTemp : REAL; // Calculated average temperature
    TempMin, TempMax : REAL; // Setpoint limits
    Hysteresis : REAL; // Hysteresis value
    ErrorCount : INT := 0; // Error counter
END_VAR

// Initialize outputs
HeatingOn := FALSE;
SensorFault := FALSE;
LogError := FALSE;

// Set temperature limits
TempMin := 20.0;
TempMax := 22.0;

// Hysteresis value (e.g., 2°C)
Hysteresis := 2.0;

// Calculate average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Check if any sensor is faulty
IF ANY_OF(TempSensor1 < 10.0, TempSensor1 > 30.0, TempSensor2 < 10.0, TempSensor2 > 30.0, TempSensor3 < 10.0, TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    LogError := TRUE;
ELSE
    SensorFault := FALSE;
END_IF;

// Check if heating should be turned on
IF AvgTemp < TempMin THEN
    HeatingOn := TRUE;
ELSEIF AvgTemp > TempMax THEN
    HeatingOn := FALSE;
ELSE
    // Apply hysteresis
    IF HeatingOn AND AvgTemp > TempMax - Hysteresis THEN
        HeatingOn := FALSE;
    ELSIF NOT HeatingOn AND AvgTemp < TempMin + Hysteresis THEN
        HeatingOn := TRUE;
    END_IF;
END_IF;
END_FUNCTION_BLOCK

// Example usage:
// TempSensor1 := 20.0; // Normal temperature
// TempSensor2 := 21.0; // High temperature
