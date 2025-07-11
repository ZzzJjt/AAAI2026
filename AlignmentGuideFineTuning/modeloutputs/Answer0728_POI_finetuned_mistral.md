### Intent:
**Intent Summary:**  
Design a motor interlock system in IEC 61131-3 Structured Text to prevent motor startup if associated equipment is running, ensuring safe coordinated operation with audit logging for industrial control applications.

### Prompt:
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a process control or safety systems engineer tasked with designing interlocks for a prilling station that handles ammonium nitrate, a highly reactive and regulated chemical compound.

⸻

🟩 T (Task) – What You Need to Do

Create a comprehensive list of interlocks necessary for the safe and efficient operation of an ammonium nitrate prilling station. For each interlock, clearly define:
	•	The hazardous condition being monitored (e.g., overtemperature, overpressure, loss of air flow)
	•	The trigger value or fault (e.g., cooling air flow < minimum, temperature > threshold)
	•	The automated safety response (e.g., stop melt feed, shut down prilling tower, open vent valve)

The interlocks should address at least the following conditions:
	1.	Overtemperature in the prill tower
	2.	High pressure in melt system
	3.	Cooling air failure
	4.	Melt pump or feeder failure
	5.	High product accumulation
	6.	Scrubber failure or bypass
	7.	Emergency stop trigger
	8.	Loss of inerting gas (if applicable)
	9.	Power failure
	10.	Explosion vent activation

Explain the importance of these interlocks in preventing catastrophic outcomes, complying with safety regulations (e.g., OSHA, ATEX), and protecting operators and the environment.

⸻

🟧 F (Format) – Expected Output

Deliver a clear and structured output that includes:
	•	A numbered list of interlocks with each one’s monitored condition, trigger threshold, and safety action
	•	A brief description of the system logic for activation and reset (manual or automatic)
	•	A summary paragraph explaining how these interlocks contribute to process safety, regulatory compliance, and equipment protection

Optional: Provide a draft of how these interlocks could be implemented in IEC 61131-3 Structured Text or as a cause-and-effect matrix.

### Generated Code:
**Intent Summary:**  
Design a motor interlock system in IEC 61131-3 Structured Text to prevent motor startup if associated equipment is running, ensuring safe coordinated operation with audit logging for industrial control applications.
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a process control or safety systems engineer tasked with designing interlocks for a prilling station that handles ammonium nitrate, a highly reactive and regulated chemical compound.

⸻

🟩 T (Task) – What You Need to Do

Create a comprehensive list of interlocks necessary for the safe and efficient operation of an ammonium nitrate prilling station. For each interlock, clearly define:
	•	The hazardous condition being monitored (e.g., overtemperature, overpressure, loss of air flow)
	•	The trigger value or fault (e.g., cooling air flow < minimum, temperature > threshold)
	•	The automated safety response (e.g., stop melt feed, shut down prilling tower, open vent valve)

The interlocks should address at least the following conditions:
	1.	Overtemperature in the prill tower
	2.	High pressure in melt system
	3.	Cooling air failure
	4.	Melt pump or feeder failure
	5.	High product accumulation
	6.	Scrubber failure or bypass
	7.	Emergency stop trigger
	8.	Loss of inerting gas (if applicable)
	9.	Power failure
	10.	Explosion vent activation

Explain the importance of these interlocks in preventing catastrophic outcomes, complying with safety regulations (e.g., OSHA, ATEX), and protecting operators and the environment.

⸻

🟧 F (Format) – Expected Output

Deliver a clear and structured output that includes:
	•	A numbered list of interlocks with each one’s monitored condition, trigger threshold, and safety action
	•	A brief description of the system logic for activation and reset (manual or automatic)
	•	A summary paragraph explaining how these interlocks contribute to process safety, regulatory compliance, and equipment protection

Optional: Provide a draft of how these interlocks could be implemented in IEC 61131-3 Structured Text or as a cause-and-effect matrix.
(* IEC 61131-3 Structured Text Program: MotorInterlock *)
(* Purpose: Implements a motor interlock system to prevent unsafe startup *)

PROGRAM MotorInterlock
VAR
    (* Inputs *)
    StartCommand : BOOL;                  (* TRUE to initiate startup *)
    EquipmentRunning : BOOL;              (* TRUE if associated equipment is running *)
    EmergencyStop : BOOL;                 (* TRUE if emergency stop is triggered *)
    
    (* Outputs *)
    MotorEnabled : BOOL;                  (* TRUE if motor is allowed to run *)
    StartAllowed : BOOL;                  (* TRUE if startup is allowed *)
    Fault : BOOL;                         (* TRUE if interlock condition is active *)
    AuditLog : ARRAY[1..100] OF STRING[80]; (* Audit log for faults and actions *)
    AuditLogIndex : INT := 0;             (* Index for logging *)
    
    (* Internal Variables *)
    LastStartCommand : BOOL;              (* Previous value of StartCommand *)
    LastEquipmentRunning : BOOL;          (* Previous value of EquipmentRunning *)
    LastEmergencyStop : BOOL;             (* Previous value of EmergencyStop *)
    LastMotorState : BOOL;                (* Previous motor state *)
    LogEntry : STRING[80];               (* Temporary log entry *)
END_VAR

(* Main Logic *)
(* Check for emergency stop or equipment running *)
IF EmergencyStop THEN
    MotorEnabled := FALSE;
    StartAllowed := FALSE;
    Fault := TRUE;
    LogEntry := 'Emergency stop activated';
    AuditLog[AuditLogIndex] := LogEntry;
    AuditLogIndex := AuditLogIndex + 1;
ELSE
    (* Check if associated equipment is running *)
    IF EquipmentRunning THEN
        (* Prevent motor startup while equipment is running *)
        MotorEnabled := FALSE;
        StartAllowed := FALSE;
        Fault := TRUE;
        LogEntry := 'Equipment running, motor startup blocked';
        AuditLog[AuditLogIndex] := LogEntry;
        AuditLogIndex := AuditLogIndex + 1
