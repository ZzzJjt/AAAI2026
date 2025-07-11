### Intent:
**Intent Summary:**  
Generate a 30-entry I/O list table for a steel rolling mill, including signal names, types, ranges, setpoints, and P&ID references, to standardize control system documentation and integration.  

**Code-Generation Intent:**  
*"Create a structured I/O list table with 30 entries for a rolling mill’s control system, covering analog/digital signals, engineering units, ranges, setpoints, and P&ID links."*

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
**Intent Summary:**  
Generate a 30-entry I/O list table for a steel rolling mill, including signal names, types, ranges, setpoints, and P&ID references, to standardize control system documentation and integration.  

**Code-Generation Intent:**  
*"Create a structured I/O list table with 30 entries for a rolling mill’s control system, covering analog/digital signals, engineering units, ranges, setpoints, and P&ID links."*
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
The purpose of this control narrative is to define the operational and safety control logic for the Ammonium Nitrate (AN) reactor in a fertilizer production facility. The narrative covers both manual and automatic modes of operation, ensuring safe and efficient operation of the reactor, and includes detailed descriptions of control loops, setpoints, interlocks, and alarm conditions.

#### 2. Overview
The AN reactor is a continuous-feed, pressure-controlled vessel that produces ammonium nitrate by reacting ammonia and nitric acid under controlled temperature and pressure conditions. The reactor operates in both manual and automatic modes, with the automatic mode ensuring precise control of temperature, pressure, and feed rates. This narrative outlines the control logic for each operational phase, including start-up, normal operation, and shutdown, as well as safety interlocks and alarm responses.

#### 3. Control Loops and Setpoints

##### 3.1 Temperature Control Loop
- **Setpoint**: 175°C
- **Control Element**: Reactor temperature transmitter (TIC-101)
- **Manual/Automatic**: Automatic
- **Control Element**: Temperature control valve (TCV-101)
- **Feedback**: Reactor temperature transmitter (TIC-101)

##### 3.2 Pressure Control Loop
- **Setpoint**: 12.5 bar
- **Control Element**: Reactor pressure transmitter (PIC-101)
- **Manual/Automatic**: Automatic
- **Control Element**: Pressure control valve (PCV-101)
- **Feedback**: Reactor pressure transmitter (PIC-101)

##### 3.3 Flow Control Loop
- **Setpoint**: Ammonia flow rate: 200 kg/h, Nitric acid flow rate: 150 kg/h
- **Control Element**: Ammonia flow transmitter (FIC-101), Nitric acid flow transmitter (FIC-102)
- **Manual/Automatic**: Automatic
- **Control Element**: Ammonia control
