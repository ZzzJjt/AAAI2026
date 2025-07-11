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
	•	Readable, scalable, and maintainable code suitable for industrial deployment and HMI integration

---

**Shutdown Procedure:**

1. **Furnace Temperature Reduction:**
   - Gradually cool the furnace to a safe temperature below 400°C over a period of 12 hours.
   - Monitor the temperature and ensure it does not drop below 350°C to prevent thermal shock.
   - Use a PID controller to maintain a steady cooling rate of 5°C per hour.

2. **Controlled Gas Flow Ramp-Down:**
   - Reduce the fuel gas flow rate to the burners over a period of 12 hours.
   - Start with a full flow rate and decrease it by 10% every hour.
   - Monitor the gas flow rate and ensure it does not drop below 50% of the initial rate to maintain combustion efficiency.

3. **Dynamic Oxygen Ratio Management:**
   - Maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown.
   - Adjust the oxygen supply based on the current gas flow rate and temperature.
   - Use a proportional control strategy to compensate for fluctuations in gas flow and temperature.
   - Implement safety checks to prevent oxygen levels from exceeding 10% of the total air supply.

---

**Control Narrative:**

**Step 4: Furnace Temperature Reduction**

- Setpoint: Cool to < 400°C
- Cooling rate: 5°C per hour
- Temperature monitoring: Continuous
- Safety check: Ensure temperature does not drop below 350°C

**Step 5: Controlled Gas Flow Ramp-Down**

- Initial flow rate: Full
- Final flow rate: 50% of initial
- Ramp-down rate: 10% per hour
- Gas flow monitoring: Continuous
- Safety check: Ensure flow rate does not drop below 50% of initial

**Step 6: Dynamic Oxygen Ratio Management**

- Fuel-to-air ratio: 1:2.5
- Oxygen supply adjustment: Proportional control
- Gas flow and temperature monitoring: Continuous
- Safety check: Prevent oxygen levels from exceeding 10% of total air supply

---

**Structured Text Program:**

```ST
// Define variables
VAR
  FurnaceTemp : REAL;
  GasFlowRate : REAL;
  OxygenLevel : REAL;
END_VAR

// Function to gradually reduce fuel gas flow rate
FUNCTION ReduceGasFlowRate
  VAR
    InitialFlowRate : REAL;
    CurrentFlow
