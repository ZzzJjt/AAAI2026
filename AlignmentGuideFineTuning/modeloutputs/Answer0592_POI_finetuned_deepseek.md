### Intent:
**Intent Summary:**  
Explain the PID function block's inputs, outputs, and tuning parameters in the OSCAT library for industrial PLC applications, demonstrating how to configure it to regulate process variables (e.g., temperature, pressure) with stability and precision.

### Prompt:
**Explanation PID Function Block:**
Provide a comprehensive explanation of the inputs and outputs of the PID function block in the OSCAT library, including the role of each parameter in process control and examples of practical implementation in industrial applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a controls engineer or automation programmer working with the OSCAT library in an industrial PLC environment. Your task is to understand and explain how to configure and apply the PID function block to regulate key process variables such as pressure, temperature, or flow.

⸻

🟩 I (Input) – What You’re Given

You are working with a standard PID function block, which includes the following key parameters and signals:
	•	Inputs:
	•	SP: Setpoint (desired value)
	•	PV: Process Variable (measured value)
	•	Kp, Ki, Kd: Proportional, Integral, and Derivative gains
	•	MANUAL: Optional mode flag for manual override
	•	LIMIT_HI, LIMIT_LO: Optional high/low output clamps
	•	Outputs:
	•	OUT: Control signal (e.g., to a valve or actuator)
	•	ERROR: Difference between SP and PV
	•	Optional: Status flags (e.g., output limited, saturated)

⸻

🟧 S (Steps) – What to Do
	1.	Configure your tuning parameters (Kp, Ki, Kd) based on the dynamics of your process.
	2.	Feed real-time values into the block:
	•	SP: Your target process value (e.g., 75°C for a reactor)
	•	PV: Your actual process value (e.g., from a temperature sensor)
	3.	The block automatically computes the error (SP - PV)
	4.	Internally, it calculates:
	•	Proportional output = Kp * error
	•	Integral output = sum of past errors (Ki * ∫ error dt)
	•	Derivative output = rate of change (Kd * d(error)/dt)
	5.	Combines the three terms to generate OUT
	6.	Applies output limiting, anti-windup, and optional manual control logic
	7.	Sends OUT to your actuator (e.g., control valve, pump, heater)

⸻

🟦 E (Expectation) – What You Should Achieve
	•	Achieve stable and accurate control of your process variable (e.g., temperature, pressure, flow)
	•	Minimize overshoot, undershoot, and steady-state error
	•	Allow for real-time adaptation and continuous process optimization
	•	Easily re-tune or adapt PID parameters for new process requirements
	•	Reduce manual adjustments and improve system reliability and safety

### Generated Code:
**Intent Summary:**  
Explain the PID function block's inputs, outputs, and tuning parameters in the OSCAT library for industrial PLC applications, demonstrating how to configure it to regulate process variables (e.g., temperature, pressure) with stability and precision.
**Explanation PID Function Block:**
Provide a comprehensive explanation of the inputs and outputs of the PID function block in the OSCAT library, including the role of each parameter in process control and examples of practical implementation in industrial applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a controls engineer or automation programmer working with the OSCAT library in an industrial PLC environment. Your task is to understand and explain how to configure and apply the PID function block to regulate key process variables such as pressure, temperature, or flow.

⸻

🟩 I (Input) – What You’re Given

You are working with a standard PID function block, which includes the following key parameters and signals:
	•	Inputs:
	•	SP: Setpoint (desired value)
	•	PV: Process Variable (measured value)
	•	Kp, Ki, Kd: Proportional, Integral, and Derivative gains
	•	MANUAL: Optional mode flag for manual override
	•	LIMIT_HI, LIMIT_LO: Optional high/low output clamps
	•	Outputs:
	•	OUT: Control signal (e.g., to a valve or actuator)
	•	ERROR: Difference between SP and PV
	•	Optional: Status flags (e.g., output limited, saturated)

⸻

🟧 S (Steps) – What to Do
	1.	Configure your tuning parameters (Kp, Ki, Kd) based on the dynamics of your process.
	2.	Feed real-time values into the block:
	•	SP: Your target process value (e.g., 75°C for a reactor)
	•	PV: Your actual process value (e.g., from a temperature sensor)
	3.	The block automatically computes the error (SP - PV)
	4.	Internally, it calculates:
	•	Proportional output = Kp * error
	•	Integral output = sum of past errors (Ki * ∫ error dt)
	•	Derivative output = rate of change (Kd * d(error)/dt)
	5.	Combines the three terms to generate OUT
	6.	Applies output limiting, anti-windup, and optional manual control logic
	7.	Sends OUT to your actuator (e.g., control valve, pump, heater)

⸻

🟦 E (Expectation) – What You Should Achieve
	•	Achieve stable and accurate control of your process variable (e.g., temperature, pressure, flow)
	•	Minimize overshoot, undershoot, and steady-state error
	•	Allow for real-time adaptation and continuous process optimization
	•	Easily re-tune or adapt PID parameters for new process requirements
	•	Reduce manual adjustments and improve system reliability and safety

Example:

If SP = 75°C and PV = 74.5°C, the PID block would output:
OUT = 10.0 (10% of error)
ERROR = 0.5°C

This would drive a heater to add 10°C/min to the process, ensuring it reaches 75°C within a few minutes.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "oscat_pid.h"

// Define PID constants
#define Kp 1.0 // Proportional gain
#define Ki 0.5 // Integral gain
#define Kd 0.2 // Derivative gain

#define MAX_ERROR 10.0 // Max error allowed
#define MIN_ERROR -10.0 // Min error allowed

// Define PID function block inputs
float SP; // Setpoint
float PV; // Process variable
float MANUAL; // Manual override flag
float LIMIT_HI; // High output limit
float LIMIT_LO; // Low output limit

// Define PID function block outputs
float OUT; // Control signal
float ERROR; // Error between SP and PV

// Define PID function block status flags
bool ERROR_LIMITED; // Error limit exceeded
bool ERROR_SATURATED; // Output saturated

// Define PID function block internal variables
float sum_error; // Sum of past errors
float integral_error; // Integral of past errors
float derivative_error; // Derivative of past errors

// Define PID function block tuning parameters
float Kp_val; // Proportional gain
float Ki_val; // Integral gain
float Kd_val; // Derivative gain

// Define PID function block tuning parameters
float Kp_val; // Proportional gain
float Ki_val; // Integral gain
float Kd_val; // Derivative gain

// Define PID function block tuning parameters
float Kp_val; // Proportional gain
float Ki_val; // Integral gain
float Kd_val; // Derivative gain

// Define PID function block tuning parameters
float Kp
