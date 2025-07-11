### Intent:
The task is to develop an IEC 61131-3 Structured Text program for safely controlling the startup and shutdown sequences of a 3D pouch making machine, including temperature regulation of heating/cooling stations, feeder speed synchronization, tension control, and cutter coordination with safety interlocks.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer specializing in industrial shutdown procedures using IEC 61131-3 Structured Text, with a focus on safe, phased deactivation of high-temperature equipment in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Develop a Structured Text-based shutdown program for a steel production facility. The task includes:
	•	Creating a complete step-by-step shutdown sequence, covering essential phases such as furnace cooldown, gas flow reduction, and oxygen level management.
	•	Writing a detailed control narrative for steps 4 to 6, including exact setpoints and timing requirements for variables like temperature, gas flow, and oxygen concentration.
	•	Implementing a self-contained IEC 61131-3 program that handles the sequencing logic and enforces safety protocols.
	•	Designing a function block to ramp down fuel gas flow over 12 hours, with safety checks and timer-based control.
	•	Creating another function that adjusts oxygen supply to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow rate and furnace temperature changes.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block implementing the shutdown sequence
	•	Modular function blocks with parameter inputs (e.g., time, flow rate, ratio target)
	•	Usage of timers (TON), IF conditions, and real-time analog signal processing
	•	In-line comments explaining control logic and safety transitions
	•	Optional summary of integration challenges and how your solution supports safe, scalable shutdown automation

### Generated Code:
The task is to develop an IEC 61131-3 Structured Text program for safely controlling the startup and shutdown sequences of a 3D pouch making machine, including temperature regulation of heating/cooling stations, feeder speed synchronization, tension control, and cutter coordination with safety interlocks.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer specializing in industrial shutdown procedures using IEC 61131-3 Structured Text, with a focus on safe, phased deactivation of high-temperature equipment in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Develop a Structured Text-based shutdown program for a steel production facility. The task includes:
	•	Creating a complete step-by-step shutdown sequence, covering essential phases such as furnace cooldown, gas flow reduction, and oxygen level management.
	•	Writing a detailed control narrative for steps 4 to 6, including exact setpoints and timing requirements for variables like temperature, gas flow, and oxygen concentration.
	•	Implementing a self-contained IEC 61131-3 program that handles the sequencing logic and enforces safety protocols.
	•	Designing a function block to ramp down fuel gas flow over 12 hours, with safety checks and timer-based control.
	•	Creating another function that adjusts oxygen supply to maintain a 1:2.5 fuel-to-air ratio, with adaptability to gas flow rate and furnace temperature changes.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block implementing the shutdown sequence
	•	Modular function blocks with parameter inputs (e.g., time, flow rate, ratio target)
	•	Usage of timers (TON), IF conditions, and real-time analog signal processing
	•	In-line comments explaining control logic and safety transitions
	•	Optional summary of integration challenges and how your solution supports safe, scalable shutdown automation

⸻

🟨 S (Scope) – Define the Scope

The scope of this task includes:
	•	Developing a Structured Text program for a steel production facility shutdown
	•	Incorporating safety interlocks and emergency stop procedures
	•	Ensuring compliance with IEC 61131-3 and safety standards
	•	Providing a detailed control narrative for steps 4 to 6 of the shutdown sequence
	•	Designing a function block to ramp down fuel gas flow over 12 hours
	•	Creating a function block to adjust oxygen supply to maintain a 1:2.5 fuel-to-air ratio

⸻

🟩 C (Constraints) – Define the Constraints

The constraints for this task are:
	•	IEC 61131-3 Structured Text programming language
	•	Use of timers (TON), IF conditions, and real-time analog signal processing
	•	Compliance with safety standards and IEC 61131-3 guidelines
	•	Integration with existing control systems and equipment
	•	Scalability to accommodate future expansion and modifications
	•	Ensuring safe and efficient shutdown procedures

⸻

🟩 A (Assumptions) – Make Assumptions

Assumptions for this task:
	•	Access to the existing control system architecture and equipment specifications
	•	Availability of necessary hardware and software tools for programming
	•	Comprehensive knowledge of IEC 61131-3 and safety standards
	•	Expertise in Structured Text programming and control system design
	•	Ability to work independently and within a team environment

⸻

🟩 D (Deliverables) – List the Deliverables

The deliverables for this task are:
	•	IEC 61131-3 Structured Text code block implementing the shutdown sequence
	•	Modular function blocks with parameter inputs for gas flow rate, oxygen supply, and time
	•	In-line comments explaining control logic and safety transitions
	•	Optional summary of integration challenges and how your solution supports safe, scalable shutdown automation

⸻

🟩 E (Evaluation) – Define the Evaluation Criteria

The evaluation criteria for this task are:
	•	Compliance with IEC 61131-3 and safety standards
	•
