### Intent:
**Intent Summary:**  
Design a structured start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine, ensuring synchronized activation/deactivation of heating/cooling stations, cutters, and feeders with precise winding tension control to maintain product quality and machine safety.

### Prompt:
**3D Pouch Making Machine:**

Design a detailed start-up and shutdown sequence for a 3D pouch making machine in IEC 61131-3 Structured Text. The machine consists of 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process to ensure proper tension in the raw material.

Write a structured start-up sequence that sequentially activates the heating and cooling stations, regulates the feeder units to maintain optimal tension, and ensures proper synchronization between the cutters and material flow. Additionally, create a shutdown sequence that safely deactivates each component in the correct order, ensuring proper cooling and tension release.

Ensure the program includes typical parameter values, timers, and conditions for each stage of the start-up and shutdown procedures, and discuss the importance of winding tension in maintaining machine efficiency and product quality.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer specializing in IEC 61131-3 Structured Text programming for complex multi-stage machinery.

🟩 I (Input) – Information Provided

You are tasked with programming a 3D pouch making machine that includes 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units for raw material. The machine must execute a precise start-up and shutdown sequence, where winding tension management is critical to ensure material stability and product quality. The system must respond to thermal thresholds, synchronization logic, and safe sequencing requirements.

🟧 S (Steps) – Steps to Perform
	1.	Write a start-up sequence in Structured Text that:
	•	Activates heating and cooling stations in proper order.
	•	Waits for heaters to reach set temperatures before proceeding.
	•	Regulates feeder units to maintain optimal winding tension.
	•	Synchronizes cutter operation with material movement.
	2.	Write a shutdown sequence that:
	•	Safely deactivates cutters and feeder units.
	•	Ensures proper cooling time before turning off cooling stations.
	•	Releases winding tension gradually to avoid material snapping or misalignment.
	3.	Include timers, threshold parameters, and safety interlocks for each step, and structure your code with comments for clarity.

🟦 E (Expectation) – Expected Output

Produce a well-documented IEC 61131-3 Structured Text program that executes the start-up and shutdown sequences safely and efficiently. The code should reflect real industrial conditions and maintain high reliability, product consistency, and machine longevity, with clear logic and robust handling of timing, synchronization, and tension control.

### Generated Code:
**Intent Summary:**  
Design a structured start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine, ensuring synchronized activation/deactivation of heating/cooling stations, cutters, and feeders with precise winding tension control to maintain product quality and machine safety.
**3D Pouch Making Machine:**

Design a detailed start-up and shutdown sequence for a 3D pouch making machine in IEC 61131-3 Structured Text. The machine consists of 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process to ensure proper tension in the raw material.

Write a structured start-up sequence that sequentially activates the heating and cooling stations, regulates the feeder units to maintain optimal tension, and ensures proper synchronization between the cutters and material flow. Additionally, create a shutdown sequence that safely deactivates each component in the correct order, ensuring proper cooling and tension release.

Ensure the program includes typical parameter values, timers, and conditions for each stage of the start-up and shutdown procedures, and discuss the importance of winding tension in maintaining machine efficiency and product quality.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer specializing in IEC 61131-3 Structured Text programming for complex multi-stage machinery.

🟩 I (Input) – Information Provided

You are tasked with programming a 3D pouch making machine that includes 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units for raw material. The machine must execute a precise start-up and shutdown sequence, where winding tension management is critical to ensure material stability and product quality. The system must respond to thermal thresholds, synchronization logic, and safe sequencing requirements.

🟧 S (Steps) – Steps to Perform
	1.	Write a start-up sequence in Structured Text that:
	•	Activates heating and cooling stations in proper order.
	•	Waits for heaters to reach set temperatures before proceeding.
	•	Regulates feeder units to maintain optimal winding tension.
	•	Synchronizes cutter operation with material movement.
	2.	Write a shutdown sequence that:
	•	Safely deactivates cutters and feeder units.
	•	Ensures proper cooling time before turning off cooling stations.
	•	Releases winding tension gradually to avoid material snapping or misalignment.
	3.	Include timers, threshold parameters, and safety interlocks for each step, and structure your code with comments for clarity.

🟦 E (Expectation) – Expected Output

Produce a well-documented IEC 61131-3 Structured Text program that executes the start-up and shutdown sequences safely and efficiently. The code should reflect real industrial conditions and maintain high reliability, product consistency, and machine longevity, with clear logic and robust handling of timing, synchronization, and tension control.
FUNCTION_BLOCK FB_HeaterControl
VAR_INPUT
    Enable : BOOL; // Activate heater
    TempSetpoint : REAL; // Target temperature (°C)
    TempCurrent : REAL; // Current temperature (°C)
    TempDiff : REAL; // Temperature difference (°C)
END_VAR

VAR_OUTPUT
    HeaterOn : BOOL; // Heater is active
    TempAlarm : BOOL; // Temperature alarm
    TempReset : BOOL; // Reset temperature alarm
END_VAR

VAR
    Timer : TON; // Timer for 10 seconds
    TempAlarmTimer : TON; // Timer for 5 seconds
    TempAlarmState : BOOL := FALSE; // State of temperature alarm
    TempResetState : BOOL := FALSE; // State of temperature reset
END_VAR

// Initialize outputs
HeaterOn := FALSE;
TempAlarm := FALSE;
TempReset := FALSE;

// Timer for 10 seconds
Timer(IN := Enable, PT := T#10s);

// Timer for 5 seconds
TempAlarmTimer(IN := TempAlarm, PT := T#5s);

// Check temperature difference
IF TempDiff > 5.0 THEN
    TempAlarm := TRUE;
    TempReset := TRUE;
ELSE
    TempAlarm := FALSE;
    TempReset := FALSE;
END_IF;

// Check timer
IF Timer.Q THEN
    HeaterOn := TRUE;
    TempReset := TRUE;
END_IF;

IF TempAlarmTimer.Q THEN
    TempAlarm := FALSE;
END_IF;

// Reset timer after 10 seconds
IF Timer.Q THEN
    Timer.Q := FALSE;
END_IF;

END_FUNCTION_BLOCK

FUNCTION_BLOCK FB_CoolerControl
VAR_INPUT
    Enable : BOOL; // Activate cooler
    TempSetpoint : REAL; // Target temperature (°C)
    TempCurrent : REAL; // Current temperature (°C)
    TempDiff : REAL; // Temperature difference (°C)
END_VAR

VAR_OUTPUT
    CoolerOn : BOOL; // Cooler is active
    TempAlarm : BOOL; // Temperature alarm
    TempReset : BOOL; // Reset temperature alarm
END_VAR

VAR
    Timer
