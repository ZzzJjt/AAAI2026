### Intent:
**Intent Summary:**  
Develop an automated control narrative for beer brewing, specifying setpoints, instrumentation, procedural logic, and safety interlocks to ensure consistent quality and operational reliability across milling, mashing, lautering, boiling, fermentation, and conditioning phases.  

*(Focus: Automation-ready process control with precise parameters and fail-safes for PLC/DCS implementation.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.

### Generated Code:
**Intent Summary:**  
Develop an automated control narrative for beer brewing, specifying setpoints, instrumentation, procedural logic, and safety interlocks to ensure consistent quality and operational reliability across milling, mashing, lautering, boiling, fermentation, and conditioning phases.  

*(Focus: Automation-ready process control with precise parameters and fail-safes for PLC/DCS implementation.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define MAX_LENGTH 100
#define MAX_TEMPERATURE 180.0
#define MAX_PRESSURE 10.0
#define MAX_PH 6.0
#define MAX_AMMONIA_TO_ACID_RATIO 1.01
#define MAX_FLOW 100.0

// Constants for PID tuning
#define Kp 1.0
#define Ki 0.1
#define Kd 0.0

// PID control variables
double setpoint, error, integral, derivative, output;
double prev_error, prev_integral, prev_derivative;

// PID tuning parameters
double P, I, D;

// PID tuning constants
double TuningConstants[3] = {0.1, 0.01, 0.001};

// PID tuning function
void PID_Tune(double tuning_constants[3]) {
    P = tuning_constants[0];
    I = tuning_constants[1];
    D = tuning_constants[2];
}

// PID control function
void PID_Control(double setpoint, double current_value) {
    error = setpoint - current_value;
    integral += error * TuningConstants[0];
    derivative = (error - prev_error) / TuningConstants[1];
    output = P * error + I * integral + D * derivative;
    prev_error = error;
    prev_integral = integral;
    prev_derivative = derivative;
}

// PID tuning function
void PID_Tune_PID(double tuning_constants[3]) {
    PID_Tune(tuning_constants);
}

// PID tuning function
void PID_Control_PID(double setpoint, double current_value) {
    PID_Control(setpoint, current_value);
}

// PID tuning function
void PID_Tune_PID_PID(double tuning_constants[3]) {
    PID_Tune(tuning_constants);
}

// PID tuning function
