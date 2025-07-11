### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and control a subsea gas wellhead's emergency interlocks, automatically triggering shutdowns for overpressure, low flow, or overtemperature conditions while requiring manual reset post-shutdown to ensure safety.  

*(Focus: Safety-critical automation with deterministic responses and no automatic recovery.)*

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**C-A-R-E:**

🟥 C (Context) – The Background

Subsea gas wellheads are critical infrastructure components in offshore oil and gas operations, exposed to extreme conditions and limited physical access. Any delay in responding to abnormal pressure, temperature, or flow conditions can lead to catastrophic failures, such as blowouts, gas leaks, or equipment damage. Emergency interlocks play a vital role in ensuring that safety responses are automated, immediate, and robust—even in fully unmanned environments.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text (ST) program to implement an emergency interlock system for a subsea gas wellhead. The program should:
	•	Monitor key process variables:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	•	Trigger safety actions based on the following conditions:
	•	If pressure > 1500 psi, close the master valve (MV-101)
	•	If flow rate drops below minimum, also close MV-101 (to prevent leaks)
	•	If temperature > 120°C, trigger full shutdown
	•	Prevent automatic restart: Implement a manual reset mechanism that requires operator intervention to re-enable the system after an emergency shutdown.

⸻

🟨 R (Result) – The Expected Outcome

The interlock system provides a deterministic and reliable protection mechanism that instantly reacts to abnormal conditions and ensures that the system enters a safe state. It minimizes the risk of catastrophic events and increases confidence in unmanned or remote operations. By requiring manual resets after shutdown, it ensures issues are reviewed and resolved before restarting, enhancing long-term operational integrity.

⸻

🟦 E (Example) – A Practical Use Case

In the event that PT_101 detects pressure exceeding 1500 psi, the system immediately sets MV_101 := FALSE (closing the valve), sets a SHUTDOWN := TRUE flag, and locks out the restart logic. If FT_101 reports near-zero flow, this might indicate a rupture or leakage—also triggering MV_101 := FALSE. Likewise, if TT_101 > 120°C, the system engages a full shutdown to protect downstream equipment.

A manual reset input, such as RESET := TRUE, must be activated by maintenance personnel after inspection to re-enable the system.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and control a subsea gas wellhead's emergency interlocks, automatically triggering shutdowns for overpressure, low flow, or overtemperature conditions while requiring manual reset post-shutdown to ensure safety.  

*(Focus: Safety-critical automation with deterministic responses and no automatic recovery.)*
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**C-A-R-E:**

🟥 C (Context) – The Background

Subsea gas wellheads are critical infrastructure components in offshore oil and gas operations, exposed to extreme conditions and limited physical access. Any delay in responding to abnormal pressure, temperature, or flow conditions can lead to catastrophic failures, such as blowouts, gas leaks, or equipment damage. Emergency interlocks play a vital role in ensuring that safety responses are automated, immediate, and robust—even in fully unmanned environments.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text (ST) program to implement an emergency interlock system for a subsea gas wellhead. The program should:
	•	Monitor key process variables:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	•	Trigger safety actions based on the following conditions:
	•	If pressure > 1500 psi, close the master valve (MV-101)
	•	If flow rate drops below minimum, also close MV-101 (to prevent leaks)
	•	If temperature > 120°C, trigger full shutdown
	•	Prevent automatic restart: Implement a manual reset mechanism that requires operator intervention to re-enable the system after an emergency shutdown.

⸻

🟨 R (Result) – The Expected Outcome

The interlock system provides a deterministic and reliable protection mechanism that instantly reacts to abnormal conditions and ensures that the system enters a safe state. It minimizes the risk of catastrophic events and increases confidence in unmanned or remote operations. By requiring manual resets after shutdown, it ensures issues are reviewed and resolved before restarting, enhancing long-term operational integrity.

⸻

🟦 E (Example) – A Practical Use Case

In the event that PT_101 detects pressure exceeding 1500 psi, the system immediately sets MV_101 := FALSE (closing the valve), sets a SHUTDOWN := TRUE flag, and locks out the restart logic. If FT_101 reports near-zero flow, this might indicate a rupture or leakage—also triggering MV_101 := FALSE. Likewise, if TT_101 > 120°C, the system engages a full shutdown to protect downstream equipment.

A manual reset input, such as RESET := TRUE, must be activated by maintenance personnel after inspection to re-enable the system. This ensures that the root cause of the emergency shutdown is identified and addressed before restarting the system.

**Code:**

```
PROGRAM Interlock_Gas_Wellhead;
VAR
	PT_101 : REAL;
	TT_101 : REAL;
	FT_101 : REAL;
	MV_101 : BOOL;
	SHUTDOWN : BOOL;
	RESET : BOOL;
END_VAR

IF PT_101 > 1500 THEN
	MV_101 := FALSE;
	SHUTDOWN := TRUE;
	RESET := FALSE;
END_IF

IF FT_101 < 10 THEN
	MV_101 := FALSE;
	SHUTDOWN := TRUE;
	RESET := FALSE;
END_IF

IF TT_101 > 120 THEN
	MV_101 := FALSE;
	SHUTDOWN := TRUE;
	RESET := FALSE;
END_IF

IF RESET = TRUE THEN
	RESET := FALSE;
	SHUTDOWN := FALSE;
	MV_101 := TRUE;
END_IF
```

**Discussion:**

The interlock system is a critical component of subsea gas wellhead operations, ensuring that safety responses are automated, immediate, and robust. The program monitors key process variables and triggers safety actions based on predefined conditions. It also prevents automatic restart, requiring manual intervention to re-enable the system after an emergency shutdown. This ensures that issues are reviewed and resolved before restarting, enhancing long-term operational integrity.

The program is written in IEC 61131-3 Structured Text (ST), a widely used programming language for industrial automation. ST is a high-level language that is easy to read and understand, making it suitable for safety-critical applications. The program is self-contained, meaning that it does not rely on external libraries or functions, and can be easily integrated into a larger control system.

The program is designed to be deterministic, meaning that it always produces the same output for a given input. This is important in safety-critical applications, where the system must respond consistently and reliably to abnormal conditions. The program is also robust, meaning that it can handle unexpected inputs and errors without crashing or causing unintended consequences.

The program is also designed to be maintainable, meaning that it is easy to update and modify as needed. This is important in safety-
