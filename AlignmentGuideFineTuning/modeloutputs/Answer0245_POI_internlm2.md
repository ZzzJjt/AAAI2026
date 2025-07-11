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

A manual reset input, such as RESET := TRUE, must be activated by maintenance personnel after inspection to re-enable the system. This ensures that any issues are addressed before restarting, reducing the risk of recurrent failures.

⸻

🟩 A (Action) – The Implementation Task

1. **Define the I/O requirements:**
	•	Pressure Transmitter (PT) – PT_101 (0-1500 psi)
	•	Temperature Transmitter (TT) – TT_101 (0-120°C)
	•	Flow Transmitter (FT) – FT_101 (0-100%)
	•	Master Valve (MV) – MV_101 (ON/OFF)
	•	Shutdown Flag – SHUTDOWN (TRUE/FALSE)
	•	Reset Flag – RESET (TRUE/FALSE)
2. **Design the Structured Text program:**
	•	Define variables and constants for safety limits and thresholds.
	•	Create logic blocks for monitoring and control.
	•	Implement conditional statements to trigger safety actions.
	•	Ensure manual reset is required before restarting the system.
3. **Test the program:**
	•	Perform unit tests to verify individual logic blocks.
	•	Conduct integration tests to ensure the interlock system functions as expected.
	•	Validate the program under various operating conditions and failure scenarios.
4. **Document the program:**
	•	Provide a detailed description of the interlock system's purpose, design, and operation.
	•	Include a list of safety-related standards and regulations followed.
	•	Document any assumptions, limitations, or known issues.
5. **Deploy and maintain the program:**
	•	Install the program in the target control system.
	•	Train operators on the interlock system's operation and maintenance procedures.
	•	Regularly review and update the program to address any changes in the system or safety requirements.

**C-A-R-E:**

🟥 C (Context) – The Background

Emergency interlocks are essential components in subsea gas wellhead operations, as they provide a reliable and immediate response to abnormal conditions. These interlocks help prevent catastrophic failures, such as blowouts, gas leaks, or equipment damage, which can have severe consequences for the environment, personnel, and assets.

⸻

🟩 A (Action) – The Implementation Task

Developing an IEC 61131-3 Structured Text program for an emergency interlock system involves several steps:

1.
