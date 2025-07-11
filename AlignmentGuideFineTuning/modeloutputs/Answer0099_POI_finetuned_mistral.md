### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to regulate temperature using averaged sensor inputs (20–22°C hysteresis), detect sensor faults (10–30°C range), and safely disable heating during faults.

### Prompt:
**Pneumatic System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a pneumatic system with a control loop frequency of 100 ms. The system should regulate the flow of air to actuators based on input signals, maintaining a flow rate of 50 standard liters per minute. The system must also ensure that the pressure remains within the specified range of 5.5 to 6 bar. Implement safety checks to handle any deviations in flow or pressure and ensure efficient and reliable operation under varying load conditions.

**B-A-B:**

🟥 B (Before) – The Challenge

Controlling pneumatic systems in real time requires balancing air flow regulation and pressure stability while adapting to changing loads. Without structured control logic, the system risks flow inconsistencies, pressure deviations, and unsafe operation. A solution must maintain tight control at a fixed update rate and handle safety checks automatically.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) that:
	•	Runs on a 100 ms control loop
	•	Maintains air flow at a steady rate of 50 standard liters per minute (SLPM)
	•	Monitors and controls pressure within the range 5.5–6 bar
	•	Includes safety checks to detect and respond to deviations in flow or pressure
	•	Ensures stable and adaptive operation under variable load conditions
	•	Provides clear structure and modularity for future expansion or diagnostic integration

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement this, your Structured Text program can follow this structure:
VAR
    FlowInput : REAL;         // Current flow rate input (SLPM)
    PressureInput : REAL;     // Current pressure input (bar)
    FlowSetpoint : REAL := 50.0;
    MinPressure : REAL := 5.5;
    MaxPressure : REAL := 6.0;
    FlowValveOutput : BOOL;
    PressureReliefValve : BOOL;
    FlowError, PressureError : BOOL;
END_VAR

// Flow control logic
IF FlowInput < FlowSetpoint THEN
    FlowValveOutput := TRUE;     // Open valve to increase flow
ELSIF FlowInput >= FlowSetpoint THEN
    FlowValveOutput := FALSE;    // Close or hold to maintain
END_IF

// Pressure monitoring logic
IF PressureInput < MinPressure OR PressureInput > MaxPressure THEN
    PressureError := TRUE;
    PressureReliefValve := TRUE; // Trigger relief or alert
ELSE
    PressureError := FALSE;
    PressureReliefValve := FALSE;
END_IF

// Flow fault detection
IF ABS(FlowInput - FlowSetpoint) > 5.0 THEN
    FlowError := TRUE; // Significant deviation
ELSE
    FlowError := FALSE;
END_IF
This logic ensures:
	•	Closed-loop control on a 100 ms schedule
	•	Continuous regulation of flow and pressure
	•	Error detection flags for out-of-range conditions
	•	Readiness for integration with alarms or HMI interfaces

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to regulate temperature using averaged sensor inputs (20–22°C hysteresis), detect sensor faults (10–30°C range), and safely disable heating during faults.
**Pneumatic System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a pneumatic system with a control loop frequency of 100 ms. The system should regulate the flow of air to actuators based on input signals, maintaining a flow rate of 50 standard liters per minute. The system must also ensure that the pressure remains within the specified range of 5.5 to 6 bar. Implement safety checks to handle any deviations in flow or pressure and ensure efficient and reliable operation under varying load conditions.

**B-A-B:**

🟥 B (Before) – The Challenge

Controlling pneumatic systems in real time requires balancing air flow regulation and pressure stability while adapting to changing loads. Without structured control logic, the system risks flow inconsistencies, pressure deviations, and unsafe operation. A solution must maintain tight control at a fixed update rate and handle safety checks automatically.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) that:
	•	Runs on a 100 ms control loop
	•	Maintains air flow at a steady rate of 50 standard liters per minute (SLPM)
	•	Monitors and controls pressure within the range 5.5–6 bar
	•	Includes safety checks to detect and respond to deviations in flow or pressure
	•	Ensures stable and adaptive operation under variable load conditions
	•	Provides clear structure and modularity for future expansion or diagnostic integration

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement this, your Structured Text program can follow this structure:
VAR
    FlowInput : REAL;         // Current flow rate input (SLPM)
    PressureInput : REAL;     // Current pressure input (bar)
    FlowSetpoint : REAL := 50.0;
    MinPressure : REAL := 5.5;
    MaxPressure : REAL := 6.0;
    FlowValveOutput : BOOL;
    PressureReliefValve : BOOL;
    FlowError, PressureError : BOOL;
END_VAR

// Flow control logic
IF FlowInput < FlowSetpoint THEN
    FlowValveOutput := TRUE;     // Open valve to increase flow
ELSIF FlowInput >= FlowSetpoint THEN
    FlowValveOutput := FALSE;    // Close or hold to maintain
END_IF

// Pressure monitoring logic
IF PressureInput < MinPressure OR PressureInput > MaxPressure THEN
    PressureError := TRUE;
    PressureReliefValve := TRUE; // Trigger relief or alert
ELSE
    PressureError := FALSE;
    PressureReliefValve := FALSE;
END_IF

// Flow fault detection
IF ABS(FlowInput - FlowSetpoint) > 5.0 THEN
    FlowError := TRUE; // Significant deviation
ELSE
    FlowError := FALSE;
END_IF
This logic ensures:
	•	Closed-loop control on a 100 ms schedule
	•	Continuous regulation of flow and pressure
	•	Error detection flags for out-of-range conditions
	•	Readiness for integration with alarms or HMI interfaces
PROGRAM PLC_PRG
TITLE 'Temperature Control System'

(*
    Description:
    A temperature control system using 61131-3 Structured Text to regulate a process
    using 20-22°C setpoint with hysteresis and fault detection.

    Features:
    - Regulates temperature using 20°C to 22°C setpoint
    - Uses averaged sensor input to reduce noise
    - Implements hysteresis to prevent frequent heating/cooling
    - Detects sensor faults and disables heating during faults

    Safety Considerations:
    - Disables heating during sensor faults to prevent damage
    - Hysteresis prevents rapid temperature swings that could damage equipment
    - Modular design allows for easy integration with other control logic
*)

VAR
    // Inputs
    TempSensor1 : REAL;          // Temperature sensor 1 (°C)
    TempSensor2 : REAL;          // Temperature sensor 2 (°C)
    TempSensor3 : REAL;          // Temperature sensor 3 (°C)
    TempSensor4 : REAL;          // Temperature sensor 4 (°C)
    TempSensor5 : REAL;          // Temperature sensor 5 (°C)
    TempSensor6 : REAL;          // Temperature sensor 6 (°C)
    TempSensor7 : REAL;          // Temperature sensor 7 (°C)
    TempSensor8 : REAL;          // Temperature sensor 8 (°C)
    TempSensor9 : REAL;          // Temperature sensor 9 (°C)
    TempSensor10: REAL;          // Temperature sensor 10 (°C)
    TempSensor11: REAL;          // Temperature sensor 11 (°C)
    TempSensor12: REAL;          // Temperature sensor 12 (°C)
    TempSensor13: REAL;          // Temperature sensor 13 (°C)
    TempSensor14: REAL;          // Temperature sensor 14 (°C)
    TempSensor15: RE
