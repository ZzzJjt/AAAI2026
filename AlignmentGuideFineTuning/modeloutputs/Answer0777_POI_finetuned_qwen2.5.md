### Intent:
The task is to develop an ISA-88-compliant Structured Text program for controlling the reaction stage of urea fertilizer production, including heating, cooling, and pressure regulation with precise phase transitions and parameter monitoring.

### Prompt:
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer and batch automation engineer implementing ISA-88-compliant control logic for chemical production using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a self-contained Structured Text program for the reaction stage of urea fertilizer batch production, following ISA-88 standards.
Your implementation must include:
	•	Control of heating, cooling, and pressure regulation within a reactor
	•	Use of typical parameters (e.g., 180°C temperature, 140 bar pressure, 30-minute hold time)
	•	Clearly defined transitions between sub-operations using timers, process conditions, and interlocks
	•	Modular function blocks or methods for operations like StartHeating, RegulatePressure, and StartCooling

You should also explain how the program structure supports modular control and discuss typical PLC challenges such as real-time synchronization, resource management, and maintaining ISA-88 compliance.

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block
	•	Modular logic blocks with clearly labeled phases and transitions
	•	Timers (e.g., TON), Boolean flags, and setpoint comparisons
	•	Inline comments explaining the control sequence and parameter logic
	•	(Optional) Notes on optimizing phase transitions for energy efficiency and system reliability

### Generated Code:
The task is to develop an ISA-88-compliant Structured Text program for controlling the reaction stage of urea fertilizer production, including heating, cooling, and pressure regulation with precise phase transitions and parameter monitoring.
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer and batch automation engineer implementing ISA-88-compliant control logic for chemical production using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a self-contained Structured Text program for the reaction stage of urea fertilizer batch production, following ISA-88 standards.
Your implementation must include:
	•	Control of heating, cooling, and pressure regulation within a reactor
	•	Use of typical parameters (e.g., 180°C temperature, 140 bar pressure, 30-minute hold time)
	•	Clearly defined transitions between sub-operations using timers, process conditions, and interlocks
	•	Modular function blocks or methods for operations like StartHeating, RegulatePressure, and StartCooling

You should also explain how the program structure supports modular control and discuss typical PLC challenges such as real-time synchronization, resource management, and maintaining ISA-88 compliance.

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block
	•	Modular logic blocks with clearly labeled phases and transitions
	•	Timers (e.g., TON), Boolean flags, and setpoint comparisons
	•	Inline comments explaining the control sequence and parameter logic
	•	(Optional) Notes on optimizing phase transitions for energy efficiency and system reliability
	•	A discussion of ISA-88 principles applied to batch control in industrial chemical processes
	•	Concrete examples of parameter values and control ranges for the reaction stage
	•	A focus on providing a complete, executable control recipe for the reaction phase of urea production
**Batch Urea Fertilizer:**

Create a self-contained IEC 61131-3 Structured Text program to implement the sequential control of the reaction stage in the production of urea fertilizer. The program should follow the principles of ISA-88 batch control, with specific control logic for heating, cooling, and pressure regulation. Include typical parameter values for temperature, pressure, and timing, and ensure that the transitions between each operation are based on concrete conditions and timers.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer implementing ISA-88 batch control for the production of urea fertilizer, using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a self-contained Structured Text program to control the reaction stage of urea production, including heating, cooling, and pressure regulation. The program should follow ISA-88 principles and include typical parameter values for temperature, pressure, and timing.

🟧 F (Format) – Specify the Output Format

Provide a self-contained IEC 61131-3 Structured Text program with the following structure:

	•	Define the required data types and variables (e.g., REAL, BOOL, TIME)
	•	Implement the control logic for heating, cooling, and pressure regulation
	•	Use typical parameter values for temperature, pressure, and timing (e.g., 180°C, 140 bar, 30 minutes)
	•	Include concrete transitions between operations based on conditions and timers
	•	Ensure the program follows ISA-88 principles for batch control
	•	Provide comments explaining the control logic and parameter values
	•	(Optional) Discuss the challenges of optimizing the control sequence for energy efficiency and system reliability
	•	Include a discussion of ISA-88 principles applied to batch control in industrial chemical processes
	•	Concrete examples of parameter values and control ranges for the reaction stage
	•	A focus on providing a complete, executable control recipe for the reaction phase of urea production
**Batch Urea Fertilizer:**

Create a self-contained IEC 61
