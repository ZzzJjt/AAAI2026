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
	•	ISA-88-aligned sequencing that is adaptable, scalable, and easy to integrate with plant systems
FUNCTION_NAME: FuelGasFlowReduction
VAR_TYPE: REAL
VAR_NAME: STRING[10]
FUNCTION_DESC:
    "Ramp down fuel gas flow over 12 hours, with safety checks and timing"

VAR
    StartTime : TIME; // Current time
    EndTime   : TIME; // 12 hours later
    FlowRate  : REAL; // Current flow rate (%)
    FlowTarget : REAL; // Target flow rate (%)
    FlowRate_Max : REAL; // Max flow rate (%)
    FlowRate_Min : REAL; // Min flow rate (%)
    FlowAlarm : BOOL; // Flow alarm flag
    FlowAlarm_Active : BOOL; // Active flag
END_VAR

// Initialize variables
FlowRate := 100.0;
FlowAlarm := FALSE;
FlowAlarm_Active := FALSE;

// Check if current time is within the 12-hour window
IF StartTime <= EndTime THEN
    // Calculate remaining time
    RemainingTime := (EndTime - TIME('HH:MM:SS')) / 1000.0;

    // Check if time is within the 12-hour window
    IF RemainingTime >= 0.0 AND RemainingTime <= 12.0 THEN
        // Calculate target flow rate
        FlowTarget := FlowRate - (12.0 / 100.0);

        // Check if target flow rate is within the allowed range
        IF FlowTarget >= FlowRate_Min AND FlowTarget <= FlowRate_Max THEN
            // Set flow alarm flag
            FlowAlarm := FALSE;
            FlowAlarm_Active := FALSE;
        ELSE
            // Set flow alarm flag
            FlowAlarm := TRUE;
            FlowAlarm_Active := TRUE;
        END_IF;
    ELSE
        // Set flow alarm flag
        FlowAlarm := TRUE;
        FlowAlarm_Active := TRUE;
    END_IF;
ELSE
    // Set flow alarm flag
    FlowAlarm := TRUE;
    FlowAlarm_Active := TRUE;
END_IF;

RETURN FlowAlarm;
END_FUNCTION

FUNCTION_NAME: OxygenSupplyAdjustment
VAR_TYPE: REAL
VAR_NAME: STRING[10]
FUNCTION_DESC:
    "
