### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PID control program to regulate liquid level by adjusting an inlet valve position, using defined gains (Kp, Ki, Kd) and safety limits, with a 100ms cycle time for stable and safe operation.

### Prompt:
**PID pH Control:**

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) to implement PID feedback control for pH regulation in a process. The program should continuously adjust the addition of acid or base to maintain the pH setpoint, ensuring accurate control in dynamic conditions.

Include the PID parameters (proportional, integral, and derivative gains) and the control logic to handle deviations from the target pH. The program should incorporate safeguards to prevent extreme pH levels by setting operational limits for the dosing mechanism. Discuss the challenges of pH control in industrial processes, particularly focusing on system response time, non-linear behavior of pH control, and maintaining process stability under varying input conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an industrial control engineer responsible for designing a PID control strategy in IEC 61131-3 Structured Text to maintain stable pH levels in a process. Your program will regulate acid/base dosing to handle nonlinear behavior and ensure safety and precision.

⸻

🟩 I (Input) – What You’re Given
	•	pH_PV: Measured pH value from the sensor
	•	pH_SP: Target setpoint (e.g., 7.0)
	•	PID parameters:
	•	Kp := 2.5 (Proportional gain)
	•	Ki := 0.6 (Integral gain)
	•	Kd := 0.3 (Derivative gain)
	•	Cycle time: 100 ms
	•	Dosing limits:
	•	Dosing_Min := 0.0 (% output)
	•	Dosing_Max := 100.0 (% output)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Calculate error: Error := pH_SP - pH_PV
	2.	Update integral term: Integral := Integral + Error * 0.1
	3.	Compute derivative: Derivative := (Error - Prev_Error) / 0.1
	4.	Calculate PID output:
Dosing_Output := (Kp * Error) + (Ki * Integral) + (Kd * Derivative)
	5.	Clamp dosing output within safe operating range:
	•	If above Dosing_Max, set to max
	•	If below Dosing_Min, set to min
	6.	Store current error as Prev_Error for the next cycle

⸻

🟦 E (Expectation) – What You Should Achieve

Your program should:
	•	Maintain stable and accurate pH in a dynamically changing process
	•	Prevent overcorrection and unsafe pH excursions
	•	React quickly to disturbances, especially near neutral pH where nonlinearity is high
	•	Be robust, safe, and PLC-executable, suitable for integration into industrial water treatment, chemical mixing, or fermentation processes

⸻

✅ Example Code

VAR
    pH_PV : REAL;                      // Measured pH
    pH_SP : REAL := 7.0;               // pH setpoint

    // PID tuning
    Kp : REAL := 2.5;
    Ki : REAL := 0.6;
    Kd : REAL := 0.3;

    // Control variables
    Error : REAL;
    Prev_Error : REAL := 0.0;
    Integral : REAL := 0.0;
    Derivative : REAL;
    Dosing_Output : REAL;

    // Safety limits
    Dosing_Min : REAL := 0.0;
    Dosing_Max : REAL := 100.0;
END_VAR

// PID routine (sampled every 100 ms)
Error := pH_SP - pH_PV;
Integral := Integral + Error * 0.1;
Derivative := (Error - Prev_Error) / 0.1;

Dosing_Output := (Kp * Error) + (Ki * Integral) + (Kd * Derivative);

// Clamp output
IF Dosing_Output > Dosing_Max THEN
    Dosing_Output := Dosing_Max;
ELSIF Dosing_Output < Dosing_Min THEN
    Dosing_Output := Dosing_Min;
END_IF

Prev_Error := Error;

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PID control program to regulate liquid level by adjusting an inlet valve position, using defined gains (Kp, Ki, Kd) and safety limits, with a 100ms cycle time for stable and safe operation.
**PID pH Control:**

Develop a self-contained IEC 61131-3 Structured Text program (not a function block) to implement PID feedback control for pH regulation in a process. The program should continuously adjust the addition of acid or base to maintain the pH setpoint, ensuring accurate control in dynamic conditions.

Include the PID parameters (proportional, integral, and derivative gains) and the control logic to handle deviations from the target pH. The program should incorporate safeguards to prevent extreme pH levels by setting operational limits for the dosing mechanism. Discuss the challenges of pH control in industrial processes, particularly focusing on system response time, non-linear behavior of pH control, and maintaining process stability under varying input conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an industrial control engineer responsible for designing a PID control strategy in IEC 61131-3 Structured Text to maintain stable pH levels in a process. Your program will regulate acid/base dosing to handle nonlinear behavior and ensure safety and precision.

⸻

🟩 I (Input) – What You’re Given
	•	pH_PV: Measured pH value from the sensor
	•	pH_SP: Target setpoint (e.g., 7.0)
	•	PID parameters:
	•	Kp := 2.5 (Proportional gain)
	•	Ki := 0.6 (Integral gain)
	•	Kd := 0.3 (Derivative gain)
	•	Cycle time: 100 ms
	•	Dosing limits:
	•	Dosing_Min := 0.0 (% output)
	•	Dosing_Max := 100.0 (% output)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Calculate error: Error := pH_SP - pH_PV
	2.	Update integral term: Integral := Integral + Error * 0.1
	3.	Compute derivative: Derivative := (Error - Prev_Error) / 0.1
	4.	Calculate PID output:
Dosing_Output := (Kp * Error) + (Ki * Integral) + (Kd * Derivative)
	5.	Clamp dosing output within safe operating range:
	•	If above Dosing_Max, set to max
	•	If below Dosing_Min, set to min
	6.	Store current error as Prev_Error for the next cycle

⸻

🟦 E (Expectation) – What You Should Achieve

Your program should:
	•	Maintain stable and accurate pH in a dynamically changing process
	•	Prevent overcorrection and unsafe pH excursions
	•	React quickly to disturbances, especially near neutral pH where nonlinearity is high
	•	Be robust, safe, and PLC-executable, suitable for integration into industrial water treatment, chemical mixing, or fermentation processes

⸻

✅ Example Code

VAR
    pH_PV : REAL;                      // Measured pH
    pH_SP : REAL := 7.0;               // pH setpoint

    // PID tuning
    Kp : REAL := 2.5;
    Ki : REAL := 0.6;
    Kd : REAL := 0.3;

    // Control variables
    Error : REAL;
    Prev_Error : REAL := 0.0;
    Integral : REAL := 0.0;
    Derivative : REAL;
    Dosing_Output : REAL;

    // Safety limits
    Dosing_Min : REAL := 0.0;
    Dosing_Max : REAL := 100.0;
END_VAR

// PID routine (sampled every 100 ms)
Error := pH_SP - pH_PV;
Integral := Integral + Error * 0.1;
Derivative := (Error - Prev_Error) / 0.1;

Dosing_Output := (Kp * Error) + (Ki * Integral) + (Kd * Derivative);

// Clamp output
IF Dosing_Output > Dosing_Max THEN
    Dosing_Output := Dosing_Max;
ELSIF Dosing_Output < Dosing_Min THEN
    Dosing_Output := Dosing_Min;
END_IF

Prev_Error := Error; // Update for next cycle
**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer tasked with developing a self-contained IEC 61131-3 Structured Text program to implement PID feedback control for pH regulation in a chemical mixing process. Your program must maintain the pH at a specified setpoint while adjusting the dosing of acid or base, ensuring accurate control under dynamic conditions.

⸻

🟩 I (Input) – What You’re Given
	•	pH_PV: The measured pH value from the sensor
	•	pH_SP: The target pH setpoint
	•	Kp, Ki, Kd: The proportional, integral, and derivative gains of the PID controller
	•	Cycle time: 100 ms
	•	Dosing limits:
	•	Dosing_Min: The minimum safe dosing rate
	•	Dosing_Max: The maximum safe dosing rate
	•	Control output: The dosing rate to adjust the pH

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the PID parameters and control limits.
	2.	Implement the PID control algorithm:
	•	Compute the error between the setpoint and the process variable (pH_PV).
	•	Accumulate the integral term over time.
	•	Calculate the derivative based on the rate of change of the error.
	•	Compute the PID output using the gains and error terms.
	3.	Clip the PID output to ensure it stays within the safe dosing limits.
	4.	Assign the PID output to the control variable (Dosing_Output) to adjust the dosing mechanism.

⸻

🟦 E (Expectation) – What You Should Achieve
	•	A stable and accurate pH control system that maintains the setpoint within a specified tolerance.
	•	Proper handling of process disturbances, ensuring that the system responds quickly and appropriately.
	•	Protection against extreme pH levels by limiting the dosing rate to safe operational bounds.
	•	A self-contained program that is executable on a PLC and includes all necessary logic for pH regulation.

⸻

✅ Example Code
**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer tasked with developing a self-contained IEC 61131-3 Structured Text program to implement PID feedback control for pH regulation in a chemical
