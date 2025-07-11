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

### Control Narrative for Shutdown Sequence

#### Overview
The following control narrative outlines the steps for performing a controlled shutdown of a steel production facility. The shutdown sequence is designed to ensure safe and efficient deactivation of all major equipment, including the furnace, gas flow control, and oxygen supply systems. The process is structured into six main stages, each with specific tasks and timelines, and includes interlocks and safety checks to prevent hazardous conditions.

#### Stage 1: Preparation
- **Objective:** Ensure the facility is in a safe state for shutdown.
- **Tasks:**
  - **Step 1:** Confirm all personnel have evacuated the production area.
  - **Step 2:** Close all manual valves and isolate energy sources.
  - **Step 3:** Verify that all equipment is in a safe operating state.

#### Stage 2: Furnace Cooling
- **Objective:** Safely reduce the furnace temperature to below 400°C.
- **Tasks:**
  - **Step 1:** Initiate furnace cooling by activating the cooling system.
  - **Step 2:** Monitor furnace temperature using a temperature sensor.
  - **Step 3:** Maintain cooling until the furnace temperature reaches below 400°C.

#### Stage 3: Gas Flow Ramp-Down
- **Objective:** Gradually reduce fuel gas flow over a 12-hour period.
- **Tasks:**
  - **Step 1:** Start the ramp-down sequence by setting a target gas flow rate (e.g., 100 Nm³/h).
  - **Step 2:** Use a linear ramp-down algorithm to reduce gas flow by 10 Nm³/h per hour.
  - **Step 3:** Monitor gas flow using a flow meter and ensure it matches the ramp-down schedule.

#### Stage 4: Oxygen Supply Adjustment
- **Objective:** Maintain a fuel-to-air ratio of 1:2.5 during shutdown.
- **Tasks:**
  - **Step 1:** Measure the current gas flow rate.
  - **Step 2:** Calculate the required oxygen flow based on the 1:2.5 ratio
