### Intent:
"Generate a 30-entry I/O list table for a steel rolling mill with columns for signal name, type, tag number, data format, units, ranges, setpoints, and P&ID references to support control system development."

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**T-A-G:**

🟥 T (Task)

Develop a detailed I/O list table with 30 entries for a rolling mill in a steel production plant.

⸻

🟩 A (Action)
	•	Create a table with the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference
	•	Populate the table with 30 realistic signals, such as roll speed feedback, hydraulic pressure, motor current, cooling valve control, and strip tension measurement.
	•	Ensure values like engineering units, ranges, and setpoints reflect typical rolling mill operations.
	•	Format the list clearly for use in documentation, HMI/PLC configuration, or system integration.

⸻

🟦 G (Goal)

Produce a well-structured and complete I/O list that serves as a foundational reference for control system development, instrumentation wiring, and P&ID alignment—ensuring accurate communication between automation, mechanical, and electrical engineering teams.

### Generated Code:
"Generate a 30-entry I/O list table for a steel rolling mill with columns for signal name, type, tag number, data format, units, ranges, setpoints, and P&ID references to support control system development."
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**T-A-G:**

🟥 T (Task)

Develop a detailed I/O list table with 30 entries for a rolling mill in a steel production plant.

⸻

🟩 A (Action)
	•	Create a table with the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference
	•	Populate the table with 30 realistic signals, such as roll speed feedback, hydraulic pressure, motor current, cooling valve control, and strip tension measurement.
	•	Ensure values like engineering units, ranges, and setpoints reflect typical rolling mill operations.
	•	Format the list clearly for use in documentation, HMI/PLC configuration, or system integration.

⸻

🟦 G (Goal)

Produce a well-structured and complete I/O list that serves as a foundational reference for control system development, instrumentation wiring, and P&ID alignment—ensuring accurate communication between automation, mechanical, and electrical engineering teams.
### Control Narrative for Ammonium Nitrate Reactor

#### 1. Purpose
The purpose of this control narrative is to define the operational and safety control logic for the ammonium nitrate reactor in a fertilizer production facility. The narrative provides detailed instructions for setting setpoints, controlling equipment, and ensuring safe and efficient operation of the reactor.

#### 2. Overview
The ammonium nitrate reactor is a critical component in the production process, responsible for converting ammonia and nitric acid to form ammonium nitrate. The reactor operates under strict temperature, pressure, and flow conditions to ensure product quality and safety. This narrative outlines the control strategy for maintaining these parameters, as well as the safety interlocks and alarm logic.

#### 3. Control Loops
The following control loops are defined for the ammonium nitrate reactor:

   - **Temperature Control Loop**:
      - **Setpoint**: 175°C
      - **Control Element**: Steam flow to the reactor
      - **Measured Variable**: Reactor outlet temperature
      - **Control Logic**: Adjust steam flow to maintain the outlet temperature at 175°C ± 2°C

   - **Pressure Control Loop**:
      - **Setpoint**: 12.5 bar
      - **Control Element**: Nitric acid inlet valve
      - **Measured Variable**: Reactor pressure
      - **Control Logic**: Adjust nitric acid flow to maintain the inlet pressure at 12.5 bar ± 0.5 bar

   - **Flow Control Loop**:
      - **Setpoint**: 200 kg/h ammonia + 150 kg/h nitric acid
      - **Control Element**: Ammonia and nitric acid flow controllers
      - **Measured Variable**: Actual flow rates
      - **Control Logic**: Adjust the flow controllers to maintain the desired ammonia-to-nitric acid ratio

#### 4. Control Sequence
The following control sequence is used to start and stop the reactor safely:

   - **Start-up Sequence**:
      1. Close all inlet valves
      2. Open steam val
