### Intent:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)

### Generated Code:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)
(* Program: PID Controller for Distillation Column*)
PROGRAM PRG_PID_DistillationColumn
VAR
    (* Inputs *)
    Temp_PV : REAL;                 (* Process variable: temperature in °C *)
    Temp_SP : REAL;                 (* Setpoint: target temperature in °C *)
    Temp_Output : REAL;             (* Control signal: output to heater in kW *)
    Temp_Error : REAL;              (* Error: Temp_SP - Temp_PV *)
    Temp_Proportional : REAL;       (* Proportional term *)
    Temp_Integral : REAL;           (* Integral term *)
    Temp_Derivative : REAL;         (* Derivative term *)
    Temp_PID_Output : REAL;         (* Final control signal *)
    
    (* Parameters *)
    Kp : REAL := 1.5;               (* Proportional gain *)
    Ki : REAL := 0.7;               (* Integral gain *)
    Kd : REAL := 0.3;               (* Derivative gain *)
    Temp_Min : REAL := 50.0;        (* Minimum temperature in °C *)
    Temp_Max : REAL := 100.0;       (* Maximum temperature in °C *)
    
    (* Internal variables *)
    Temp_PV_Prev : REAL;            (* Previous temperature for derivative *)
    Temp_Integral_Sum : REAL;       (* Accumulated integral *)
    Temp_Error_Prev : REAL;         (* Previous error for derivative *)
    Temp_Output_Prev : REAL;        (* Previous output for reset *)
    
    (* Outputs *)
    Temp_Heater_On : BOOL;          (* Heater control: TRUE = ON, FALSE = OFF *)
    Temp_Alarm : BOOL;              (* Alarm: TRUE if temperature out of bounds *)
END_VAR

(* Main control loop: 100 ms sampling period *)
IF NOT T#100ms THEN
    EXIT;
END_IF;

(* Update inputs *)
Temp_PV := Read_Temp();             (* Read current temperature *)
Temp_SP := Set
