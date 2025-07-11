### Intent:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using real-time control charts, anomaly detection, and corrective actions to reduce variability and defects.  

*(Focus: Steel quality monitoring, real-time SPC, defect minimization via Python automation.)*

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.

### Generated Code:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using real-time control charts, anomaly detection, and corrective actions to reduce variability and defects.  

*(Focus: Steel quality monitoring, real-time SPC, defect minimization via Python automation.)*
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.
(* Program: PID Controller for PVC Pressure Regulation *)
(* Version: 1.0, Date: 2025-05-21 *)
(* Controls PVC pressure at 15 bar with 100 ms sampling *)
PROGRAM PVC_PRESSURE_CONTROLLER
VAR
    (* Inputs *)
    PV : REAL;                    (* Measured PVC pressure in bar *)
    SP : REAL := 15.0;            (* Setpoint pressure in bar *)
    Kp : REAL := 1.2;             (* Proportional gain *)
    Ki : REAL := 0.6;             (* Integral gain *)
    Kd : REAL := 0.3;             (* Derivative gain *)
    Error : REAL;                 (* Error between PV and SP *)
    Prev_Error : REAL := 0.0;     (* Previous error for integral *)
    Delta_Error : REAL;           (* Error change for derivative *)
    Output : REAL;                (* Control output to valve *)
    T_sample : TIME := T#100ms;   (* Sample time *)
    T_last : TIME;                 (* Last sample time *)
    T_now : TIME;                 (* Current time *)
    Error_flag : BOOL := FALSE;   (* Error flag for control logic *)
    Alarm_High : BOOL := FALSE;   (* High pressure alarm *)
    Alarm_Low : BOOL := FALSE;    (* Low pressure alarm *)
    Reset_flag : BOOL := FALSE;   (* Reset flag for control logic *)
    
    (* Outputs *)
    Error_High : BOOL;            (* High pressure alarm *)
    Error_Low : BOOL;             (* Low pressure alarm *)
    Control_Status : STRING;      (* Status: OK, High, Low *)
END_VAR

(* Initialize *)
T_last := T_now := T#0s;

(* Main control loop *)
T_now := NOW();
IF T_now >= T_last + T_sample THEN
    (* Update error *)
    Error := SP - PV;
    
    (* Check for limits *)
    IF PV <
