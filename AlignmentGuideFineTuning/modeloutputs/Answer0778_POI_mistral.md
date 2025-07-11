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

**Shutdown Steel Production:**

**Step-by-Step Shutdown Sequence:**

1. Notify operators and initiate shutdown procedures
2. Reduce feeder speed to minimum
3. Stop production and isolate power sources
4. Initiate furnace cooldown by reducing fuel gas flow and increasing cooling water flow
5. Monitor and control temperature drop to 1200°C (2192°F)
6. Reduce cooling water flow and continue temperature drop to 1000°C (1832°F)
7. Reduce oxygen supply to maintain 1:2.5 fuel-to-air ratio
8. Monitor and control temperature drop to 800°C (1472°F)
9. Reduce oxygen supply to minimum
10. Monitor and control temperature drop to 600°C (1112°F)
11. Shut off fuel gas and oxygen supply
12. Ventilate furnace and cool to ambient temperature

**Control Narrative (Steps 4-6):**

4. Reduce fuel gas flow to 50% of initial value and increase cooling water flow to 150% of initial value.
	•	Maintain temperature drop rate of 10°C/min (18°F/min) until 1200°C (2192°F) is reached.
	•	If temperature drops below 1150°C (2092°F), reduce cooling water flow to 125% of initial value and increase fuel gas flow to 60% of initial value.
	•	If temperature rises above 1250°C (2282°F), reduce fuel gas flow to 40% of initial value and increase cooling water flow to 175% of initial value.

5. Reduce cooling water flow to 100% of initial value and continue temperature drop to 1000°C (1832°F).
	•	Maintain temperature drop rate of 5°C/min (9°F/min) until 1000°C (1832°F) is reached.
	•	If temperature drops
