### Intent:
**Intent Summary:**  
Develop a cause-effect matrix mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, agitator stop) for a chemical reactor’s interlock system, ensuring clear, fail-safe logic to prevent operational risks.  

*(Focus: Structured hazard-action mapping for reactor safety interlocks.)*

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a safety systems engineer designing protective logic for a chemical reactor using interlocks and cause-effect matrices.

⸻

🟩 T (Task) – What You Need to Do

Develop an extended cause and process action matrix for a chemical reactor’s interlock system. Each row in the matrix should represent a specific cause (e.g., pressure too high, temperature too low, sensor fault), and each column should correspond to a safety action (e.g., isolate feed, stop agitator, open relief valve). You must also:
	•	Ensure that each cause is linked to one or more appropriate actions
	•	Design the matrix to clearly show which actions are triggered by which conditions
	•	Describe how the matrix supports safe reactor operation by preventing scenarios such as overpressure, underheating, and component failure
	•	Highlight how this format supports clarity, completeness, and maintainability of interlock logic

⸻

🟧 F (Format) – Expected Output

Deliver a structured matrix document or table that includes:
	•	Clearly labeled causes (rows) and process actions (columns)
	•	Logical mappings between causes and actions (e.g., checkmarks or “X”)
	•	A short narrative describing how the matrix improves interlock system reliability, simplifies hazard analysis, and supports safe process control
	•	Optional annotations for priority, severity, or timing (e.g., delay before action)

### Generated Code:
**Intent Summary:**  
Develop a cause-effect matrix mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, agitator stop) for a chemical reactor’s interlock system, ensuring clear, fail-safe logic to prevent operational risks.  

*(Focus: Structured hazard-action mapping for reactor safety interlocks.)*
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a safety systems engineer designing protective logic for a chemical reactor using interlocks and cause-effect matrices.

⸻

🟩 T (Task) – What You Need to Do

Develop an extended cause and process action matrix for a chemical reactor’s interlock system. Each row in the matrix should represent a specific cause (e.g., pressure too high, temperature too low, sensor fault), and each column should correspond to a safety action (e.g., isolate feed, stop agitator, open relief valve). You must also:
	•	Ensure that each cause is linked to one or more appropriate actions
	•	Design the matrix to clearly show which actions are triggered by which conditions
	•	Describe how the matrix supports safe reactor operation by preventing scenarios such as overpressure, underheating, and component failure
	•	Highlight how this format supports clarity, completeness, and maintainability of interlock logic

⸻

🟧 F (Format) – Expected Output

Deliver a structured matrix document or table that includes:
	•	Clearly labeled causes (rows) and process actions (columns)
	•	Logical mappings between causes and actions (e.g., checkmarks or “X”)
	•	A short narrative describing how the matrix improves interlock system reliability, simplifies hazard analysis, and supports safe process control
	•	Optional annotations for priority, severity, or timing (e.g., delay before action)

You may also include a brief discussion of how the matrix supports safety compliance, fault tolerance, and system maintainability.
(* Program: PID Controller for Chemical Reactor *)
(* Sets PID gains and controls reactor temperature *)
PROGRAM PRG_PID_Reactor_Temp_Control
VAR
    (* Inputs *)
    Temp_PV : REAL;                    (* Measured reactor temperature, °C *)
    Temp_SP : REAL;                    (* Setpoint temperature, °C *)
    Temp_Output : REAL;                (* PID output, % valve opening *)
    Temp_Error : REAL;                 (* Error between PV and SP, °C *)
    Temp_Integral : REAL;              (* Integral term, °C·s *)
    Temp_Derivative : REAL;            (* Derivative term, °C/s *)
    
    (* Outputs *)
    Temp_Valve_Opening : REAL;         (* Valve opening, % *)
    Temp_Heater_On : BOOL;             (* Heater on/off *)
    
    (* PID Gains *)
    Kp : REAL := 1.5;                  (* Proportional gain *)
    Ki : REAL := 0.7;                  (* Integral gain *)
    Kd : REAL := 0.3;                  (* Derivative gain *)
    
    (* Internal Variables *)
    Temp_Prev : REAL;                  (* Previous temperature, °C *)
    Temp_Error_Prev : REAL;            (* Previous error, °C *)
    Temp_Output_Prev : REAL;           (* Previous output, % *)
    Temp_Output_Limit : REAL := 100.0; (* Max output, % *)
    Temp_Output_Min : REAL := 0.0;     (* Min output, % *)
    
    (* Timing *)
    T_sample : TIME := T#10s;          (* Sample time *)
    T_last_sample : TIME;              (* Last sample time *)
    Delta_T : TIME;                    (* Time since last sample *)
END_VAR

(* Initialize *)
Temp_PV := 5
