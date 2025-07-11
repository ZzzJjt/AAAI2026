### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely and gradually shut down a steel production facility by controlling furnace temperature, fuel gas flow (ramped down over 12 hours), and oxygen levels (maintaining a 1:2.5 fuel-to-air ratio), with modular functions for sequencing and safety interlocks.

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
Develop an IEC 61131-3 Structured Text program to safely and gradually shut down a steel production facility by controlling furnace temperature, fuel gas flow (ramped down over 12 hours), and oxygen levels (maintaining a 1:2.5 fuel-to-air ratio), with modular functions for sequencing and safety interlocks.
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
FUNCTION_BLOCK FB_FurnaceShutdown
VAR_INPUT
    Execute : BOOL; // Starts the shutdown sequence
END_VAR

VAR_OUTPUT
    Done : BOOL; // Indicates completion of the shutdown sequence
    Error : BOOL; // Raised if an error occurs
    ErrorID : DWORD; // Error code
END_VAR

VAR
    // Step 4: Furnace Cooling
    TargetTemp : REAL := 400.0; // Target furnace temperature in °C
    CurrentTemp : REAL; // Current furnace temperature
    TempReached : BOOL; // Flag to check if target temperature is reached
    TempRampTime : TIME := T#12h; // Time to reach target temperature
    TempTimer : TON;
    TempComplete : BOOL; // Flag to indicate completion of Step 4

    // Step 5: Gas Flow Ramp-Down
    GasFlowSetpoint : REAL := 100.0; // Initial fuel gas flow in %
    GasFlowRampTime : TIME := T#12h; // Time to ramp down to 0%
    GasFlowTimer : TON;
    GasFlowRampComplete : BOOL; // Flag to indicate completion of Step 5

    // Step 6: Oxygen Adjustment
    FuelAirRatio : REAL := 1.0; // Fuel-to-air ratio
    OxygenSetpoint : REAL := 250.0; // Oxygen flow in Nm³/h
    OxygenFlow : REAL; // Current oxygen flow
    OxygenTimer : TON;
    OxygenComplete : BOOL; // Flag to indicate completion of Step 6

    // Timers
    TempTimerComplete : BOOL; // Flag to check if TempTimer is complete
    GasFlowTimerComplete : BOOL; // Flag to check if GasFlowTimer is complete
    OxygenTimerComplete : BOOL; // Flag to check if OxygenTimer is complete

    // Safety Interlocks
    TempSafe : BOOL; // Flag to check if current temperature is safe
    GasFlowSafe : BOOL; // Flag to check if current gas flow is safe
    OxygenSafe : BO
