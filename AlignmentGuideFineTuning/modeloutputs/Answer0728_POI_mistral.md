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

**Interlocks for Ammonium Nitrate Prilling Station:**

1. **Overtemperature in Prill Tower:**
   - Monitored Condition: Temperature in the prill tower exceeds the safe operating limit (e.g., 120°C)
   - Trigger Threshold: Temperature > 120°C
   - Safety Action: Stop melt feed, shut down prilling tower, and activate cooling system
   - System Logic: Automatic activation upon temperature threshold exceedance; reset upon temperature drop below threshold

2. **High Pressure in Melt System:**
   - Monitored Condition: Pressure in the melt system exceeds the safe operating limit (e.g., 10 bar)
   - Trigger Threshold: Pressure > 10 bar
   - Safety Action: Stop melt feed, shut down prilling tower, and open pressure relief valve
   - System Logic: Automatic activation upon pressure threshold exceedance; reset upon pressure drop below threshold

3. **Cooling Air Failure:**
   - Monitored Condition: Failure of cooling air supply to the prill tower
   - Trigger Threshold: Loss of cooling air flow
   - Safety Action: Stop melt feed, shut down prilling tower, and activate emergency cooling system
   - System Logic: Automatic activation upon loss of cooling air flow; reset upon restoration of cooling air flow

4. **Melt Pump or Feeder Failure:**
   - Monitored Condition: Failure of the melt pump or feeder
   - Trigger Threshold: Loss of signal or power to the pump or feeder
   - Safety Action: Stop prilling tower operation and initiate maintenance procedures
   - System Logic: Automatic activation upon loss of signal or power; reset upon repair and re-initialization

5. **High Product Accumulation:**
   - Monitored Condition: Excessive accumulation of prills in the prill tower
   - Trigger Threshold: Prill level exceeds the safe operating limit
   - Safety Action: Stop melt feed, shut down prilling tower, and activate product discharge system
   - System Logic: Automatic activation upon prill level exceedance; reset upon prill level reduction below threshold

6. **Scrubber Fail
