### Intent:
**Intent Summary:**  
Explain how to configure and implement a PID function block from the OSCAT library for industrial process control, detailing parameter roles (SP, PV, Kp/Ki/Kd), signal flow, and practical tuning to regulate variables like temperature or pressure.

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
Explain how to configure and implement a PID function block from the OSCAT library for industrial process control, detailing parameter roles (SP, PV, Kp/Ki/Kd), signal flow, and practical tuning to regulate variables like temperature or pressure.
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

⸻

✅ Example Use Case:
Control a steam pressure in a boiler:
	•	SP = 12.0 bar
	•	PV = 11.5 bar
	•	Kp = 2.0, Ki = 0.1, Kd = 0.5
	•	OUT = 1.5 amps to steam valve

The PID block adjusts the valve position to maintain 12 bar, compensating for fluctuations in steam demand or heat loss.
FUNCTION_BLOCK FB_PID
VAR_INPUT
    SP : REAL;                     // Setpoint (desired value)
    PV : REAL;                     // Measured value
    Kp : REAL;                     // Proportional gain
    Ki : REAL;                     // Integral gain
    Kd : REAL;                     // Derivative gain
    Manual : BOOL;                 // Manual override flag
    Enable : BOOL;                 // Enable PID computation
    Reset : BOOL;                  // Reset internal accumulators
    Limit_HI : REAL;               // High output limit
    Limit_LO : REAL;               // Low output limit
END_VAR

VAR_OUTPUT
    OUT : REAL;                    // Control signal (e.g., to a valve or actuator)
    Error : REAL;                  // Difference between SP and PV
    Integral : REAL;               // Integral term
    Derivative : REAL;             // Derivative term
    Saturation : BOOL;             // Output saturated flag
    Saturated_Value : REAL;        // Saturated output value
END_VAR

VAR
    Prev_PV : REAL;                // Previous PV for derivative calculation
    Integral_Accumulator : REAL;   // Accumulated integral
    Prev_Time : TIME;              // Previous time for derivative
    Delta_Time : TIME;             // Time difference for derivative
    Saturation_Limit : REAL;       // User-defined saturation limit
END_VAR

// Reset accumulators when Reset = TRUE
IF Reset THEN
    Integral_Acc
