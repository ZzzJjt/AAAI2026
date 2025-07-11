### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a car wash system with safety interlocks, ensuring automatic operation only when a car is present and no humans are detected, while triggering alarms and requiring manual reset after safety breaches.  

*(Focus: Safety prioritization, human detection, conditional wash activation, and manual reset logic.)*

### Prompt:
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**B-A-B:**

🟥 B (Before) – The Challenge

Inconsistent heating control can lead to energy waste, poor temperature stability, or even safety risks. Without proper automation, frequent heater switching and faulty sensor readings can result in discomfort or damage to the system. A structured control program is needed to regulate temperature reliably and efficiently, especially when multiple sensors are involved.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) that:
	•	Uses three temperature sensors to calculate an average temperature
	•	Automatically turns the heating system on when temperature < 20°C and off when > 22°C
	•	Maintains smooth temperature regulation with hysteresis to avoid rapid on/off switching
	•	Includes fault handling logic for:
	•	Sensor failure (e.g., no signal or out-of-range values)
	•	Extreme temperature conditions (outside 10°C–30°C)

This results in a system that ensures comfort, safety, and energy efficiency without manual intervention.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement this logic, structure the program as follows:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL;
END_VAR

// Calculate average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3;

// Check for sensor faults or extreme readings
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE; // Turn off for safety
ELSE
    SensorFault := FALSE;

    // Heating control with hysteresis
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;
This approach ensures:
	•	Stable operation through averaged sensor input
	•	Energy efficiency via hysteresis
	•	Safety through range validation and fallback control logic

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a car wash system with safety interlocks, ensuring automatic operation only when a car is present and no humans are detected, while triggering alarms and requiring manual reset after safety breaches.  

*(Focus: Safety prioritization, human detection, conditional wash activation, and manual reset logic.)*
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**B-A-B:**

🟥 B (Before) – The Challenge

Inconsistent heating control can lead to energy waste, poor temperature stability, or even safety risks. Without proper automation, frequent heater switching and faulty sensor readings can result in discomfort or damage to the system. A structured control program is needed to regulate temperature reliably and efficiently, especially when multiple sensors are involved.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) that:
	•	Uses three temperature sensors to calculate an average temperature
	•	Automatically turns the heating system on when temperature < 20°C and off when > 22°C
	•	Maintains smooth temperature regulation with hysteresis to avoid rapid on/off switching
	•	Includes fault handling logic for:
	•	Sensor failure (e.g., no signal or out-of-range values)
	•	Extreme temperature conditions (outside 10°C–30°C)

This results in a system that ensures comfort, safety, and energy efficiency without manual intervention.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement this logic, structure the program as follows:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL;
END_VAR

// Calculate average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3;

// Check for sensor faults or extreme readings
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE; // Turn off for safety
ELSE
    SensorFault := FALSE;

    // Heating control with hysteresis
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;
This approach ensures:
	•	Stable operation through averaged sensor input
	•	Energy efficiency via hysteresis
	•	Safety through range validation and fallback control logic
	•	Fault handling for sensor failures or extreme temperature conditions

⸻

🟨 B (Bridge) – The Final Outcome

The final outcome is a self-contained IEC 61131-3 Structured Text program that effectively controls the heating system, prioritizing safety and energy efficiency. The program maintains a comfortable temperature range, handles sensor faults, and prevents rapid on/off switching. This ensures a reliable and efficient heating system without manual intervention.
