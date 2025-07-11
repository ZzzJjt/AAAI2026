### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely execute a controlled shutdown of a steel production facility, including gradual fuel gas reduction over 12 hours, dynamic oxygen supply adjustment (1:2.5 ratio), and precise temperature control, with modular functions and safety interlocks.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer tasked with developing a safe, programmable shutdown sequence for a steel production facility using IEC 61131-3 Structured Text, following best practices in sequencing, safety, and process control.

⸻

🟩 I (Input) – Information Provided

You are required to:
	•	Design a controlled shutdown procedure for a steel plant.
	•	Cover steps such as reducing furnace temperature, ramping down fuel gas flow, and maintaining safe oxygen levels.
	•	Focus particularly on steps 4 to 6 in the sequence, which include precise temperature control, gas flow reduction, and oxygen regulation.
	•	Include a Structured Text program that sequences these operations with timers and safety interlocks.
	•	Write two IEC 61131-3 functions:
	1.	One to reduce fuel gas flow over a 12-hour period.
	2.	One to adjust oxygen supply dynamically to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow and temperature variations.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Define the overall shutdown sequence, with clearly labeled stages (e.g., Furnace Cooling, Gas Ramp-Down, Oxygen Adjustment).
	2.	Write a control narrative for steps 4–6, specifying exact setpoints such as:
	•	Target temperature: < 400°C
	•	Gas flow ramp: 100% to 0% over 12 hours
	•	Fuel-to-air ratio: 1:2.5, adjusted in real-time
	3.	Implement the Structured Text logic for the sequence using timers (TON), analog comparisons, and safety interlocks.
	4.	Create a function for linear flow reduction based on elapsed time.
	5.	Develop a second function that calculates and regulates the oxygen supply dynamically, including safety limits and alarms.
	6.	Add comments and modular code structure for clarity and ease of maintenance.

⸻

🟦 E (Expectation) – Expected Outcome

The final solution will be a robust and modular IEC 61131-3 control program that enables a safe, efficient, and traceable shutdown of the steel facility. It will ensure:
	•	Thermal safety through gradual temperature reduction
	•	Combustion efficiency via real-time oxygen adjustment
	•	Smooth fuel transition through long-duration gas ramp-down
	•	ISA-88-aligned sequencing that is adaptable, scalable, and easy to integrate with plant systems

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely execute a controlled shutdown of a steel production facility, including gradual fuel gas reduction over 12 hours, dynamic oxygen supply adjustment (1:2.5 ratio), and precise temperature control, with modular functions and safety interlocks.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer tasked with developing a safe, programmable shutdown sequence for a steel production facility using IEC 61131-3 Structured Text, following best practices in sequencing, safety, and process control.

⸻

🟩 I (Input) – Information Provided

You are required to:
	•	Design a controlled shutdown procedure for a steel plant.
	•	Cover steps such as reducing furnace temperature, ramping down fuel gas flow, and maintaining safe oxygen levels.
	•	Focus particularly on steps 4 to 6 in the sequence, which include precise temperature control, gas flow reduction, and oxygen regulation.
	•	Include a Structured Text program that sequences these operations with timers and safety interlocks.
	•	Write two IEC 61131-3 functions:
	1.	One to reduce fuel gas flow over a 12-hour period.
	2.	One to adjust oxygen supply dynamically to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow and temperature variations.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Define the overall shutdown sequence, with clearly labeled stages (e.g., Furnace Cooling, Gas Ramp-Down, Oxygen Adjustment).
	2.	Write a control narrative for steps 4–6, specifying exact setpoints such as:
	•	Target temperature: < 400°C
	•	Gas flow ramp: 100% to 0% over 12 hours
	•	Fuel-to-air ratio: 1:2.5, adjusted in real-time
	3.	Implement the Structured Text logic for the sequence using timers (TON), analog comparisons, and safety interlocks.
	4.	Create a function for linear flow reduction based on elapsed time.
	5.	Develop a second function that calculates and regulates the oxygen supply dynamically, including safety limits and alarms.
	6.	Add comments and modular code structure for clarity and ease of maintenance.

⸻

🟦 E (Expectation) – Expected Outcome

The final solution will be a robust and modular IEC 61131-3 control program that enables a safe, efficient, and traceable shutdown of the steel facility. It will ensure:
	•	Thermal safety through gradual temperature reduction
	•	Combustion efficiency via real-time oxygen adjustment
	•	Smooth fuel transition through long-duration gas ramp-down
	•	ISA-88-aligned sequencing that is adaptable, scalable, and easy to integrate with plant systems.

⸻

**Control Narrative for Steps 4 to 6:**

**Step 4: Gradual Temperature Reduction**
- Target temperature: 400°C
- Ramp rate: 10°C/hour
- Safety interlock: If temperature exceeds 450°C, halt the ramp and trigger an alarm.

**Step 5: Fuel Gas Flow Reduction**
- Initial flow rate: 100%
- Final flow rate: 0%
- Duration: 12 hours
- Safety interlock: If flow rate drops below 50%, halt the ramp and trigger an alarm.

**Step 6: Oxygen Supply Adjustment**
- Initial ratio: 1:2.5
- Target ratio: 1:2.5
- Safety interlock: If ratio deviates by more than 0.1, halt the adjustment and trigger an alarm.

**IEC 61131-3 Structured Text Program:**

```structuredtext
PROGRAM ShutdownSteelProduction
VAR
    T_Furnace : REAL; // Furnace temperature
    T_Target : REAL := 400.0; // Target temperature
    T_RampRate : REAL := 10.0; // Temperature ramp rate
    T_SafetyLimit : REAL := 450.0; // Safety limit for temperature

    F_GasFlow : REAL; // Fuel gas flow rate
    F_RampDuration : REAL := 12.0; // Duration of gas flow ramp
    F_RampRate : REAL := 100.0; // Gas flow ramp rate
    F_SafetyLimit : REAL := 50.0; // Safety limit for gas flow

    O2_Ratio : REAL; // Oxygen supply ratio
    O2_TargetRatio : REAL := 2.5; // Target oxygen ratio
    O2_SafetyLimit : REAL := 0.1; // Safety limit for oxygen ratio
END_VAR

// Step 4: Gradual Temperature Reduction
IF T_Furnace > T_Target THEN
    T_Furnace := T_Furnace - T_RampRate;
    IF T_Furnace > T_SafetyLimit THEN
        // Trigger alarm and halt ramp
        Alarm("Temperature Exceeded Safety Limit");
        T_Furnace := T_Target;
    END_IF;
END_IF;

// Step 5: Fuel Gas Flow Reduction
IF F_GasFlow > F
