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

**Control Narrative for Steps 4 to 6:**

**Step 4: Gas Flow Reduction**

- **Objective:** Gradually reduce the fuel gas flow rate to the burners over 12 hours.
- **Setpoints:**
  - Initial flow rate: 100% of maximum capacity.
  - Final flow rate: 0% of maximum capacity.
- **Timing:** 12 hours.
- **Safety Checks:**
  - Ensure furnace temperature remains above 500°C.
  - Monitor oxygen levels to prevent combustion.
- **Control Logic:**
  - Use a timer (TON) to control the duration of each step.
  - Implement a proportional control loop to adjust the flow rate based on temperature and oxygen levels.
  - Include safety interlocks to halt the process if temperature or oxygen levels fall below acceptable thresholds.

**Step 5: Oxygen Level Management**

- **Objective:** Maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown.
- **Setpoints:**
  - Initial oxygen level: 20%.
  - Final oxygen level: 10%.
- **Timing:** 12 hours.
- **Safety Checks:**
  - Ensure oxygen levels do not drop below 10%.
  - Monitor furnace temperature to prevent combustion.
- **Control Logic:**
  - Use a timer (TON) to control the duration of each step.
  - Implement a proportional control loop to adjust the oxygen supply based on temperature and oxygen levels.
  - Include safety interlocks to halt the process if temperature or oxygen levels fall below acceptable thresholds.

**Step 6: Final Cooling and Shutdown**

- **Objective:** Safely cool the furnace to ambient temperature.
- **Setpoints:**
  - Initial furnace temperature: 1000°C.
  - Final furnace temperature: 500°C.
- **Timing:** 12 hours.
- **Safety Checks:**
  - Ensure furnace temperature remains above 500°C.
  - Monitor oxygen levels to prevent combustion.
- **Control Logic:**
  - Use a timer (TON) to control the duration of each step.
  - Implement a proportional control loop to adjust the cooling rate based on temperature and oxygen levels.
  - Include safety interlocks to halt the process if temperature or oxygen levels fall below acceptable thresholds.

**IEC 61131-3 Structured Text Program:**

```plaintext
// Shutdown Sequence
