### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including controlled furnace temperature reduction, fuel gas flow ramp-down over 12 hours, and dynamic oxygen supply adjustment to maintain a 1:2.5 fuel-to-air ratio, with embedded safety checks and modular functions.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**T-A-G:**

🟥 T (Task)

Design a safe and sequenced shutdown control program for a steel production facility using IEC 61131-3 Structured Text, following industrial best practices and safety protocols.

⸻

🟩 A (Action)
	1.	Create a comprehensive shutdown procedure covering stages such as:
	•	Furnace temperature reduction
	•	Controlled fuel gas flow ramp-down
	•	Oxygen level regulation to maintain combustion stability
	2.	Write a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying real values for:
	•	Temperature setpoints (e.g., cool to < 400°C)
	•	Gas flow reduction timeline (e.g., 12 hours)
	•	Fuel-to-air ratio (1:2.5 for oxygen management)
	3.	Implement a Structured Text control program with proper sequencing, interlocks, and safety logic.
	4.	Develop two key IEC 61131-3 functions:
	•	One to gradually reduce fuel gas flow using a linear ramp over 12 hours, with timing and fault checks.
	•	One to adjust oxygen supply dynamically based on gas flow and temperature to ensure the 1:2.5 fuel-to-air ratio, with safeguards for combustion efficiency.

⸻

🟦 G (Goal)

Deliver a modular, ISA-88-aligned shutdown automation solution that ensures:
	•	Safe thermal and combustion transitions
	•	Stable fuel-to-air control under variable process conditions
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including controlled furnace temperature reduction, fuel gas flow ramp-down over 12 hours, and dynamic oxygen supply adjustment to maintain a 1:2.5 fuel-to-air ratio, with embedded safety checks and modular functions.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**T-A-G:**

🟥 T (Task)

Design a safe and sequenced shutdown control program for a steel production facility using IEC 61131-3 Structured Text, following industrial best practices and safety protocols.

⸻

🟩 A (Action)
	1.	Create a comprehensive shutdown procedure covering stages such as:
	•	Furnace temperature reduction
	•	Controlled fuel gas flow ramp-down
	•	Oxygen level regulation to maintain combustion stability
	2.	Write a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying real values for:
	•	Temperature setpoints (e.g., cool to < 400°C)
	•	Gas flow reduction timeline (e.g., 12 hours)
	•	Fuel-to-air ratio (1:2.5 for oxygen management)
	3.	Implement a Structured Text control program with proper sequencing, interlocks, and safety logic.
	4.	Develop two key IEC 61131-3 functions:
	•	One to gradually reduce fuel gas flow using a linear ramp over 12 hours, with timing and fault checks.
	•	One to adjust oxygen supply dynamically based on gas flow and temperature to ensure the 1:2.5 fuel-to-air ratio, with safeguards for combustion efficiency.

⸻

🟦 G (Goal)

Deliver a modular, ISA-88-aligned shutdown automation solution that ensures:
	•	Safe thermal and combustion transitions
	•	Stable fuel-to-air control under variable process conditions
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration.

**Control Narrative for Steps 4 to 6:**

**Step 4: Furnace Temperature Reduction**
- **Objective:** Cool the furnace to a safe temperature below 400°C.
- **Control Strategy:** Gradually reduce the fuel gas flow and adjust the oxygen supply to maintain a stable combustion process while cooling the furnace.
- **Setpoints and Ranges:**
  - Furnace Temperature: < 400°C
  - Fuel Gas Flow: Gradually decrease from current level to 0 over 12 hours
  - Oxygen Supply: Adjust to maintain a 1:2.5 fuel-to-air ratio

**Step 5: Fuel Gas Flow Ramp-Down**
- **Objective:** Reduce the fuel gas flow to the furnace burners over 12 hours.
- **Control Strategy:** Implement a linear ramp-down function to reduce the fuel gas flow rate.
- **Setpoints and Ranges:**
  - Fuel Gas Flow: Decrease from current level to 0 over 12 hours
  - Timing: 12 hours
  - Safety Checks: Ensure no sudden drops in gas flow that could cause combustion instability

**Step 6: Oxygen Supply Adjustment**
- **Objective:** Maintain a 1:2.5 fuel-to-air ratio during the shutdown process.
- **Control Strategy:** Adjust the oxygen supply based on the current fuel gas flow and furnace temperature to maintain the desired ratio.
- **Setpoints and Ranges:**
  - Fuel Gas Flow: Current level
  - Furnace Temperature: Current temperature
  - Oxygen Supply: Adjust to maintain a 1:2.5 fuel-to-air ratio
  - Safety Checks: Ensure the oxygen supply does not exceed safe limits and maintain combustion efficiency

**IEC 61131-3 Structured Text Program:**

```structuredtext
PROGRAM ShutdownSteelProduction
VAR
    CurrentTemperature : REAL;
    CurrentFuelFlow : REAL;
    CurrentOxygenSupply : REAL;
    TargetTemperature : REAL := 400.0;
    TargetFuelFlow : REAL := 0.0;
    TargetOxygenSupply : REAL := 2.5;
    RampDownTime : REAL := 12.0;
    RampDownRate : REAL := TargetFuelFlow / RampDownTime;
    OxygenAdjustmentFactor : REAL := 1.0;
END_VAR

// Step 4: Furnace Temperature Reduction
IF CurrentTemperature > TargetTemperature THEN
    // Reduce
