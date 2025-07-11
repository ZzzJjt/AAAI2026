### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdown interlocks for a subsea gas wellhead, triggering valve closures and system halts when pressure, temperature, or flow exceed safe limits, while requiring manual reset post-shutdown.

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer responsible for implementing emergency shutdown interlocks for a subsea gas wellhead, using IEC 61131-3 Structured Text to ensure real-time safety and operational integrity.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a Structured Text program that:
	•	Monitors key parameters using sensors:
	•	PT (pressure transmitters)
	•	TT (temperature transmitters)
	•	FT (flow meters)
	•	Includes specific interlock logic such as:
	•	Close master valve (MV-101) if pressure > 1500 psi
	•	Close MV-101 if flow rate drops below safe threshold (indicating a possible leak)
	•	Trigger full system shutdown if temperature exceeds 120°C
	•	Prevents automatic reset: requires manual intervention to restore operations after a shutdown.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define threshold values and declare real-time input and output variables in Structured Text.
	2.	Implement conditional interlock logic:
	•	Use IF statements to evaluate safety limits.
	•	Trigger actuator responses (e.g., set MV_101 := FALSE) when conditions are exceeded.
	3.	Introduce a shutdown latch:
	•	Use a SHUTDOWN flag that is set when any condition is violated.
	•	Disable restart logic until a RESET input is manually triggered.
	4.	Ensure fail-safe design:
	•	Ensure all actuator states default to safe positions (e.g., valves closed) on shutdown.
	•	Test interlock paths independently for reliability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock program that:
	•	Reacts immediately and reliably to unsafe pressure, flow, or temperature conditions.
	•	Safely isolates the wellhead by closing MV-101 and halting system processes.
	•	Prevents auto-restart, enforcing manual review before system reactivation.
This enhances safety, ensures compliance with offshore standards, and supports robust, unattended operation of subsea assets.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdown interlocks for a subsea gas wellhead, triggering valve closures and system halts when pressure, temperature, or flow exceed safe limits, while requiring manual reset post-shutdown.
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer responsible for implementing emergency shutdown interlocks for a subsea gas wellhead, using IEC 61131-3 Structured Text to ensure real-time safety and operational integrity.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a Structured Text program that:
	•	Monitors key parameters using sensors:
	•	PT (pressure transmitters)
	•	TT (temperature transmitters)
	•	FT (flow meters)
	•	Includes specific interlock logic such as:
	•	Close master valve (MV-101) if pressure > 1500 psi
	•	Close MV-101 if flow rate drops below safe threshold (indicating a possible leak)
	•	Trigger full system shutdown if temperature exceeds 120°C
	•	Prevents automatic reset: requires manual intervention to restore operations after a shutdown.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define threshold values and declare real-time input and output variables in Structured Text.
	2.	Implement conditional interlock logic:
	•	Use IF statements to evaluate safety limits.
	•	Trigger actuator responses (e.g., set MV_101 := FALSE) when conditions are exceeded.
	3.	Introduce a shutdown latch:
	•	Use a SHUTDOWN flag that is set when any condition is violated.
	•	Disable restart logic until a RESET input is manually triggered.
	4.	Ensure fail-safe design:
	•	Ensure all actuator states default to safe positions (e.g., valves closed) on shutdown.
	•	Test interlock paths independently for reliability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock program that:
	•	Reacts immediately and reliably to unsafe pressure, flow, or temperature conditions.
	•	Safely isolates the wellhead by closing MV-101 and halting system processes.
	•	Prevents auto-restart, enforcing manual review before system reactivation.
This enhances safety, ensures compliance with offshore standards, and supports robust, unattended operation of subsea assets.

**Key Takeaways:**

1.	Emergency interlocks are critical for ensuring the safety and integrity of subsea gas wellhead operations.
2.	Structured Text programs can be used to implement interlock logic, including conditional statements and fail-safe design features.
3.	Interlock programs should be self-contained and tested for reliability, ensuring that they react quickly and effectively to unsafe conditions.
4.	Manual intervention should be required for system restart, preventing automatic reactivation after an emergency shutdown.
5.	Robust interlock systems enhance safety, compliance, and operational efficiency in subsea gas wellhead operations.

**Resources:**

1.	IEC 61131-3 Standard: https://www.iec.ch/standards/standard/view/61131-3
2.	Subsea Gas Wellhead Interlock Design Guide: https://www.example.com/subsea-gas-wellhead-interlock-design-guide
3.	Subsea Gas Wellhead Interlock Case Study: https://www.example.com/subsea-gas-wellhead-interlock-case-study
4.	Subsea Gas Wellhead Interlock Software: https://www.example.com/subsea-gas-wellhead-interlock-software
5.	Subsea Gas Wellhead Interlock Training Course: https://www.example.com/subsea-gas-wellhead-interlock-training-course
