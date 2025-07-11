### Intent:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers, looping indefinitely.  

*(Focus: SFC structure, timing logic, ASCII visualization, cyclic operation.)*

### Prompt:
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer or automation engineer tasked with designing a Sequential Function Chart (SFC) for a traffic light control system using IEC 61131-3 standards in ASCII format.

⸻

🟩 I (Input) – Information Provided

You need to design a traffic light cycle with the following features:
	•	Three sequential states: Green, Yellow, and Red
	•	Each light stays on for a fixed duration:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use TON (on-delay) timers to manage timing
	•	The diagram should be presented as ASCII art that visually represents steps, transitions, and timers

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the SFC structure with three steps (S1: Green, S2: Yellow, S3: Red)
	2.	For each step, assign a TON timer with an appropriate preset time
	3.	Add transitions that are triggered when each timer completes (tGreen.Q, tYellow.Q, tRed.Q)
	4.	Format the steps and transitions using clear ASCII blocks and arrows to represent flow
	5.	Close the cycle by looping the final transition (Red → Green)

⸻

🟦 E (Expectation) – Expected Outcome

Produce a plain-text Sequential Function Chart that clearly outlines the logic and timing of a traffic light control system. This SFC should be:
	•	Standards-compliant with IEC 61131-3
	•	Readable and understandable in environments without graphics
	•	Useful for PLC implementation, documentation, and training

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers, looping indefinitely.  

*(Focus: SFC structure, timing logic, ASCII visualization, cyclic operation.)*
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer or automation engineer tasked with designing a Sequential Function Chart (SFC) for a traffic light control system using IEC 61131-3 standards in ASCII format.

⸻

🟩 I (Input) – Information Provided

You need to design a traffic light cycle with the following features:
	•	Three sequential states: Green, Yellow, and Red
	•	Each light stays on for a fixed duration:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use TON (on-delay) timers to manage timing
	•	The diagram should be presented as ASCII art that visually represents steps, transitions, and timers

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the SFC structure with three steps (S1: Green, S2: Yellow, S3: Red)
	2.	For each step, assign a TON timer with an appropriate preset time
	3.	Add transitions that are triggered when each timer completes (tGreen.Q, tYellow.Q, tRed.Q)
	4.	Format the steps and transitions using clear ASCII blocks and arrows to represent flow
	5.	Close the cycle by looping the final transition (Red → Green)

⸻

🟦 E (Expectation) – Expected Outcome

Produce a plain-text Sequential Function Chart that clearly outlines the logic and timing of a traffic light control system. This SFC should be:
	•	Standards-compliant with IEC 61131-3
	•	Readable and understandable in environments without graphics
	•	Useful for PLC implementation, documentation, and training
	•	Easily adaptable if timing or state requirements change
FUNCTION_BLOCK FB_PumpControl
VAR_INPUT
    Enable : BOOL; // Enable signal to start pump operation
    SpeedSetpoint : REAL; // Desired pump speed in RPM
    MaxSpeed : REAL := 1000.0; // Maximum allowed speed in RPM
    MinSpeed : REAL := 500.0; // Minimum allowed speed in RPM
    MaxFlow : REAL := 1000.0; // Maximum allowed flow rate in L/min
    MinFlow : REAL := 500.0; // Minimum allowed flow rate in L/min
    MaxPressure : REAL := 1000.0; // Maximum allowed pressure in bar
    MinPressure : REAL := 500.0; // Minimum allowed pressure in bar
    MaxTemperature : REAL := 80.0; // Maximum allowed temperature in °C
    MinTemperature : REAL := 20.0; // Minimum allowed temperature in °C
END_VAR

VAR_OUTPUT
    SpeedControl : REAL; // Speed control output in RPM
    FlowControl : REAL; // Flow control output in L/min
    PressureControl : REAL; // Pressure control output in bar
    TemperatureControl : REAL; // Temperature control output in °C
    Error : BOOL; // Error flag if any condition is violated
    ErrorMessage : STRING(255); // Detailed error message
END_VAR

VAR
    CurrentSpeed : REAL; // Current pump speed in RPM
    CurrentFlow : REAL; // Current flow rate in L/min
    CurrentPressure : REAL; // Current pressure in bar
    CurrentTemperature : REAL; // Current temperature in °C
    SpeedError : BOOL; // Speed error flag
    FlowError : BOOL; // Flow error flag
    PressureError : BOOL; // Pressure error flag
    TemperatureError : BOOL; // Temperature error flag
    SpeedPID : TPID; // Speed PID controller
    FlowPID : TPID; // Flow PID controller
