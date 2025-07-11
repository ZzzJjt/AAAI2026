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
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration

---

**Shutdown Procedure:**

1. **Preparation:**
   - Ensure all personnel are evacuated from the production area.
   - Verify that all safety interlocks and emergency shutdown systems are in place and functioning correctly.

2. **Furnace Temperature Reduction:**
   - Gradually reduce the furnace temperature to a safe level, such as < 400°C, over a period of 4 hours.
   - Monitor the temperature and adjust the cooling rate as needed to prevent thermal shocks and maintain structural integrity.

3. **Gas Flow Ramp-Down:**
   - Initiate a 12-hour ramp-down of the fuel gas flow to the burners.
   - Use a linear ramp function to ensure a smooth transition and avoid sudden fluctuations in temperature and pressure.

4. **Oxygen Supply Adjustment:**
   - Continuously monitor the gas flow rate and temperature to maintain a fuel-to-air ratio of 1:2.5.
   - Adjust the oxygen supply dynamically to compensate for any fluctuations in gas flow or temperature.

5. **Final Cooling:**
   - After the gas flow has been reduced to a minimum, allow the furnace to cool down to ambient temperature.
   - Monitor the temperature and ensure it does not overshoot or undershoot the target.

6. **Post-Shutdown Inspection:**
   - Perform a thorough inspection of the facility to ensure no damage or safety hazards have occurred during the shutdown process.
   - Record all observations and make necessary repairs or adjustments before restarting the facility.

---

**Control Narrative:**

**Step 4: Furnace Temperature Reduction**

- Setpoint: Cool to < 400°C
- Cooling rate: 10°C per hour
- Target temperature: 400°C

**Step 5: Gas Flow Ramp-Down**

- Ramp-down period: 12 hours
- Target flow rate: 10% of initial flow rate

**Step 6: Oxygen Supply Adjustment**

- Fuel-to-air ratio: 1:2.5
- Oxygen supply adjustment: Continuous, based on gas flow and temperature

---

**Structured Text Program:**

```ST
// Define variables
VAR
  FurnaceTemperature : INT;
  GasFlowRate : REAL;
  OxygenSupply : REAL;
  FuelToAirRatio : REAL;
END_VAR

// Function to reduce gas flow rate over 12 hours
FUNCTION ReduceGasFlow
