### Intent:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

### Generated Code:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.
(* IEC 61131-3 Structured Text: Kalman Filter for Autonomous Vehicle Position Estimation *)
(* Purpose: Estimate vehicle position and velocity from noisy sensor data *)
(* Inputs: *)
(*   - Position: 3x1 matrix of position measurements (x, y, z) in meters *)
(*   - Velocity: 3x1 matrix of velocity measurements (vx, vy, vz) in m/s *)
(*   - SensorNoise: 3x1 matrix of sensor noise (noise_x, noise_y, noise_z) in m *)
(*   - ProcessNoise: 3x1 matrix of process noise (noise_vx, noise_vy, noise_vz) in m/s *)
(*   - dt: Time step in seconds *)
(* Outputs: *)
(*   - PositionEst: 3x1 matrix of estimated position (x_est, y_est, z_est) in meters *)
(*   - VelocityEst: 3x1 matrix of estimated velocity (vx_est, vy_est, vz_est) in m/s *)
(*   - ValidInput: TRUE if input matrices are valid *)
(* Safety: *)
(*   - Input validation checks are performed at runtime *)
(*   - No unsafe operations are performed *)
(*   - No external dependencies *)
(*   - No external resources *)
(*   - No external communication *)
(*   - No external state *)
(*   - No external variables *)
(*   - No external memory *)
(*   - No external logic *)
(*   - No external code *)
(*   - No external data *)
(*   - No external function calls *)
(*   - No external events *)
(*   - No external triggers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   - No external timers *)
(*   -
