### Intent:
**Intent Summary:**  
Design an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including furnace temperature reduction, controlled gas flow ramp-down, and dynamic oxygen ratio management, with modular functions for industrial deployment.

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
Design an IEC 61131-3 Structured Text program to safely and sequentially shut down a steel production facility, including furnace temperature reduction, controlled gas flow ramp-down, and dynamic oxygen ratio management, with modular functions for industrial deployment.
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
- **Control Strategy:** Gradually reduce the fuel gas flow rate to the burners while monitoring the furnace temperature.
- **Setpoints and Ranges:**
  - Furnace Temperature: < 400°C
  - Fuel Gas Flow Rate: Gradually decrease from current level to 0 over 12 hours.

**Step 5: Controlled Gas Flow Ramp-Down**
- **Objective:** Reduce the fuel gas flow rate to the burners to a minimum safe level.
- **Control Strategy:** Implement a linear ramp-down function to reduce the fuel gas flow rate over 12 hours.
- **Setpoints and Ranges:**
  - Fuel Gas Flow Rate: Decrease from current level to 0 over 12 hours.

**Step 6: Dynamic Oxygen Ratio Management**
- **Objective:** Maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown.
- **Control Strategy:** Adjust the oxygen supply to the burners based on the fuel gas flow rate and furnace temperature.
- **Setpoints and Ranges:**
  - Fuel-to-Air Ratio: 1:2.5
  - Oxygen Supply: Adjust based on fuel gas flow rate and furnace temperature to maintain the 1:2.5 ratio.

**IEC 61131-3 Structured Text Program:**

```structuredtext
PROGRAM ShutdownSteelProduction
VAR
    furnaceTemp : REAL;
    fuelGasFlow : REAL;
    oxygenSupply : REAL;
    startTime : TIME;
    endTime : TIME;
    rampDuration : TIME := 12 HOURS;
    currentFuelGasFlow : REAL;
    currentOxygenSupply : REAL;
    targetFuelGasFlow : REAL;
    targetOxygenSupply : REAL;
END_VAR

// Initialize variables
startTime := TIME_NOW;
endTime := startTime + rampDuration;

// Step 4: Furnace Temperature Reduction
WHILE furnaceTemp > 400 DO
    // Reduce fuel gas flow rate
    currentFuelGasFlow := currentFuelGasFlow - (currentFuelGasFlow / rampDuration);
    // Monitor furnace temperature
    furnaceTemp := furnaceTemp - 10; // Example cooling rate
END_WHILE

// Step 5: Controlled Gas Flow Ramp-Down
WHILE fuelGasFlow
