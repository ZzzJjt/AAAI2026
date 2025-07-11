### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control an automatic car wash station, ensuring safe operation by starting the wash only when a car is present and no humans are detected, immediately stopping and alarming on human intrusion, and maintaining safety interlocks until conditions are cleared.

### Prompt:
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC automation engineer responsible for developing safe and responsive control logic for an automatic car wash station. Your work must comply with IEC 61131-3 Structured Text (ST) standards and prioritize both operational flow and human safety.

⸻

🟩 T (Task) – What You Need to Do

Create a Structured Text program that controls a single-bay automatic car wash with the following behavior:
	•	Use input sensors to detect:
	•	CarPresentSensor : BOOL — car detected inside the wash bay
	•	HumanDetectedSensor : BOOL — human presence detected in the wash zone
	•	Implement output logic to:
	•	WashActive : BOOL — TRUE when wash is running
	•	AlarmActive : BOOL — TRUE when a person is detected in a danger zone
	•	SafeToRun : BOOL — internal flag to allow or lock the start of a new wash cycle
	•	Core logic must:
	•	Start the wash only if a car is present, no human is detected, and the system is in a safe state
	•	Immediately stop the wash and raise an alarm if a human is detected at any time
	•	Lock out the wash system (SafeToRun := FALSE) until the area is clear and no cycle is active
	•	Reset SafeToRun only after the wash has stopped and the area is confirmed safe

⸻

🟧 F (Format) – Expected Output

You should deliver a complete and clear IEC 61131-3 Structured Text function block or program section, for example:
CarPresent := CarPresentSensor;
HumanDetected := HumanDetectedSensor;

IF HumanDetected THEN
    WashActive := FALSE;
    AlarmActive := TRUE;
    SafeToRun := FALSE;
ELSIF CarPresent AND NOT HumanDetected AND SafeToRun THEN
    WashActive := TRUE;
    AlarmActive := FALSE;
END_IF;

// Reset safety flag after conditions are met
IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
Your final solution should:
	•	Be easy to read and maintain
	•	Prevent hazardous conditions through robust interlocks
	•	Be ready for integration with HMI systems, emergency stops, and actuator control

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control an automatic car wash station, ensuring safe operation by starting the wash only when a car is present and no humans are detected, immediately stopping and alarming on human intrusion, and maintaining safety interlocks until conditions are cleared.
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC automation engineer responsible for developing safe and responsive control logic for an automatic car wash station. Your work must comply with IEC 61131-3 Structured Text (ST) standards and prioritize both operational flow and human safety.

⸻

🟩 T (Task) – What You Need to Do

Create a Structured Text program that controls a single-bay automatic car wash with the following behavior:
	•	Use input sensors to detect:
	•	CarPresentSensor : BOOL — car detected inside the wash bay
	•	HumanDetectedSensor : BOOL — human presence detected in the wash zone
	•	Implement output logic to:
	•	WashActive : BOOL — TRUE when wash is running
	•	AlarmActive : BOOL — TRUE when a person is detected in a danger zone
	•	SafeToRun : BOOL — internal flag to allow or lock the start of a new wash cycle
	•	Core logic must:
	•	Start the wash only if a car is present, no human is detected, and the system is in a safe state
	•	Immediately stop the wash and raise an alarm if a human is detected at any time
	•	Lock out the wash system (SafeToRun := FALSE) until the area is clear and no cycle is active
	•	Reset SafeToRun only after the wash has stopped and the area is confirmed safe

⸻

🟧 F (Format) – Expected Output

You should deliver a complete and clear IEC 61131-3 Structured Text function block or program section, for example:
CarPresent := CarPresentSensor;
HumanDetected := HumanDetectedSensor;

IF HumanDetected THEN
    WashActive := FALSE;
    AlarmActive := TRUE;
    SafeToRun := FALSE;
ELSIF CarPresent AND NOT HumanDetected AND SafeToRun THEN
    WashActive := TRUE;
    AlarmActive := FALSE;
END_IF;

// Reset safety flag after conditions are met
IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
Your final solution should:
	•	Be easy to read and maintain
	•	Prevent hazardous conditions through robust interlocks
	•	Be ready for integration with HMI systems, emergency stops, and actuator control
FUNCTION_BLOCK FB_PumpControl
VAR_INPUT
    Enable : BOOL; // Enable signal to start pump control
    ManualStop : BOOL; // Manual stop signal to halt pump operation
    TargetFlowRate : REAL; // Target flow rate in L/min
    FlowRateFeedback : REAL; // Measured flow rate feedback in L/min
    FlowRateTolerance : REAL := 0.1; // Acceptable deviation from target flow rate
    MaxSpeedLimit : REAL := 100.0; // Maximum pump speed in RPM
    MinSpeedLimit : REAL := 50.0; // Minimum pump speed in RPM
    SpeedFeedback : REAL; // Measured pump speed in RPM
    SpeedTolerance : REAL := 5.0; // Acceptable deviation from target speed
    PumpStatus : BOOL; // Status of pump operation
    EmergencyStop : BOOL; // Emergency stop signal
END_VAR

VAR_OUTPUT
    SpeedCommand : REAL; // Commanded speed to pump motor
    FlowRateCommand : REAL; // Commanded flow rate to valve
    PumpRunning : BOOL; // Pump running status
    Alarm : BOOL; // Alarm flag for fault conditions
    ErrorMessage : STRING(20); // Error message for faults
END_VAR

VAR
    LastEnable : BOOL; // Previous enable state for debouncing
    FlowRateError : BOOL; // Flow rate error flag
    SpeedError : BOOL; // Speed error flag
    FlowRateSet : BOOL; // Flag to set flow rate
    SpeedSet : BOOL; // Flag to set speed
    FlowRateSetPoint : REAL; // Flow rate setpoint
    SpeedSetPoint : REAL; // Speed setpoint
    FlowRatePID : TON; // PID controller for flow rate
    SpeedPID : TON; // PID controller for speed
    PID_P : ARRAY[1..5] OF REAL; // Proportional gain for PID
    PID_I : ARRAY[1..5] OF REAL; // Integral gain for PID
    PID_D : ARRAY[1
