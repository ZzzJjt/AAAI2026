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

### Control Narrative for Shutdown Sequence

#### Step 1: Prepare Equipment
- **Objective:** Ensure all equipment is in a safe state for shutdown.
- **Actions:**
  - **Furnace:**
    - **Step 1.1:** Close the furnace door.
    - **Step 1.2:** Stop the burners.
    - **Step 1.3:** Stop the gas flow.
  - **Blast Furnace:**
    - **Step 1.4:** Stop the tuyère system.
    - **Step 1.5:** Stop the gas flow to the tuyère system.
  - **Cooling System:**
    - **Step 1.6:** Stop the cooling fans.
    - **Step 1.7:** Stop the water circulation system.
  - **Electrical Systems:**
    - **Step 1.8:** Isolate all electrical power sources.
    - **Step 1.9:** De-energize all motors and drives.
  - **Gas Supply:**
    - **Step 1.10:** Close the gas inlet valves.
    - **Step 1.11:** Stop the gas compressors.
  - **Oxygen Supply:**
    - **Step 1.12:** Close the oxygen inlet valves.
    - **Step 1.13:** Stop the oxygen compressors.

#### Step 2: Reduce Furnace Temperature
- **Objective:** Gradually reduce the furnace temperature to a safe level.
- **Actions:**
  - **Step 2.1:** Monitor furnace temperature using a temperature sensor.
  - **Step 2.2:** If temperature is above 1200°C, begin reducing the temperature by 10°C per hour.
  - **Step 2.3:** Continue reducing the temperature until it reaches 800°C.
  - **Step 2.4:** Hold at 800°C for 2 hours to ensure stable cooling.

#### Step 3: Ramp Down Gas Flow
- **Objective:** Safely reduce the gas flow rate to the furnace.
- **Actions:**
  - **Step 3.1
