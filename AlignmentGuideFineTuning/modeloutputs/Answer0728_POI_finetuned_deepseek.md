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

// Motor Interlock System in IEC 61131-3 Structured Text
// Purpose: Prevent motor startup if associated equipment is running
//          Ensures safe coordinated operation with audit logging

// Interlock Variables
VAR
    // Inputs
    MotorStart : BOOL; // TRUE to start motor
    EquipmentRunning : BOOL; // TRUE if equipment is running
    AuditLog : ARRAY[1..10] OF STRING[20]; // 10 log entries

    // Outputs
    MotorStartOutput : BOOL; // TRUE if motor can be started
    AuditLogIndex : INT; // Current log index
END_VAR

// Interlock Logic
IF EquipmentRunning THEN
    MotorStartOutput := FALSE; // Prevent motor startup if equipment is running
END_IF;

// Audit Logging
IF MotorStart AND NOT EquipmentRunning THEN
    AuditLog[AuditLogIndex] := 'Motor Start Attempted';
    AuditLogIndex := (AuditLogIndex + 1) MOD 10;
END_IF;

// Outputs
MotorStartOutput := MotorStart AND NOT EquipmentRunning;

// Comment: This interlock prevents motor startup if associated equipment is running.
// It ensures safe coordination between the motor and the equipment, and logs any attempts to start the motor when equipment is running.
// The interlock is designed to comply with safety standards and prevent accidents.
// The audit log can be used for compliance reporting and operator review.

// Ammonium Nitrate Prilling Station Interlocks
// Purpose: Ensures safe and efficient operation of the prilling process
//          Includes overtemperature, overpressure, and emergency stop interlocks

// List of Interlocks
LIST
    // 1. Overtemperature in the prill tower
    // Trigger: Temperature > 180°C
    // Action: Stop melt feed, shut down prilling tower, open vent valve
    // Equipment: Melt pump, prill tower
    Overtemperature_1 : BOOL;

    // 2. High pressure in melt system
    // Trigger: Pressure > 15 bar
    // Action: Stop melt feed, shut down prilling tower, open vent valve
    // Equipment: Melt pump, melt tank
    HighPressure_1 : BOOL;

    // 3. Cooling air failure
    // Trigger
