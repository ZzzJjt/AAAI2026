### Intent:
**Intent Summary:**  
Design a PLC/DCS control system for a continuous ammonium nitrate reactor, ensuring safe and precise regulation of temperature, pressure, pH, feed ratios, and level through PID loops, interlocks, and alarm logic to maintain stable production.  

*(Focus: Automation-ready control logic for reactor safety, quality, and efficiency.)*

### Prompt:
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**T-A-G:**

🟥 T (Task)

Design a 61131-3 Function Block Diagram (FBD) using ASCII art that visually represents a basic control structure involving an analog input, a timer, a PID controller, and an analog output.

⸻

🟩 A (Action)
	•	Create a clear ASCII layout with the following blocks:
	•	Analog Input block (OUT = AI)
	•	TON timer block (IN = AI, ET, Q)
	•	PID block (PV = AI, SP = 50.0, CV)
	•	Analog Output block (IN = CV)
	•	Ensure the Analog Input feeds both the TON and the PID block.
	•	Show that only the PID’s output (CV) connects to the Analog Output.
	•	Use ASCII symbols (+-----+, -->, |) to create block shapes and signal lines.
	•	Label all signals clearly inside or beside the blocks.

⸻

🟦 G (Goal)

Produce a plain-text diagram that visually communicates the data flow and block interaction within a control loop—useful for documentation, PLC training, version-controlled codebases, or text-only environments where graphical editors are unavailable.

### Generated Code:
**Intent Summary:**  
Design a PLC/DCS control system for a continuous ammonium nitrate reactor, ensuring safe and precise regulation of temperature, pressure, pH, feed ratios, and level through PID loops, interlocks, and alarm logic to maintain stable production.  

*(Focus: Automation-ready control logic for reactor safety, quality, and efficiency.)*
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**T-A-G:**

🟥 T (Task)

Design a 61131-3 Function Block Diagram (FBD) using ASCII art that visually represents a basic control structure involving an analog input, a timer, a PID controller, and an analog output.

⸻

🟩 A (Action)
	•	Create a clear ASCII layout with the following blocks:
	•	Analog Input block (OUT = AI)
	•	TON timer block (IN = AI, ET, Q)
	•	PID block (PV = AI, SP = 50.0, CV)
	•	Analog Output block (IN = CV)
	•	Ensure the Analog Input feeds both the TON and the PID block.
	•	Show that only the PID’s output (CV) connects to the Analog Output.
	•	Use ASCII symbols (+-----+, -->, |) to create block shapes and signal lines.
	•	Label all signals clearly inside or beside the blocks.

⸻

🟦 G (Goal)

Produce a plain-text diagram that visually communicates the data flow and block interaction within a control loop—useful for documentation, PLC training, version-controlled codebases, or text-only environments where graphical editors are unavailable.
### Control Narrative for Ammonium Nitrate Reactor

#### 1. Purpose
The control narrative for the ammonium nitrate reactor is designed to ensure safe, stable, and efficient operation of the reactor by managing critical process variables such as temperature, pressure, pH, feed ratios, and level. The narrative provides clear logic for setting setpoints, triggering alarms, and activating interlocks to maintain safe operating conditions and prevent equipment damage or process failure.

#### 2. Process Overview
The ammonium nitrate reactor is a continuous-flow reactor that produces ammonium nitrate by reacting ammonia and nitric acid in a controlled environment. The reactor operates at a fixed temperature (170°C) and pressure (120 psi) with a pH range of 6.0–6.5. The feed ratio of ammonia to nitric acid is maintained at 1:1. The reactor is equipped with a level sensor, temperature controller, pressure transmitter, pH probe, and flow meters for ammonia and nitric acid.

#### 3. Control Loops
The following control loops are implemented:

- **Temperature Control Loop**:
  - **Setpoint**: 170°C
  - **Controller**: PID (Proportional-Integral-Derivative)
  - **Output**: Heating system control signal
  - **Feedback**: Temperature sensor
  - **Alarm/Interlock**:
    - **High Temperature**: Triggered if temperature exceeds 180°C
    - **Low Temperature**: Triggered if temperature falls below 160°C
    - **Shutdown**: Activate emergency shutdown if temperature exceeds 190°C

- **Pressure Control Loop**:
  - **Setpoint**: 120 psi
  - **Controller**: PID
  - **Output**: Pressure relief valve control signal
  - **Feedback**: Pressure transmitter
  - **Alarm/Interlock**:
    - **High Pressure**: Triggered if pressure exceeds 130 psi
    - **Low Pressure**: Triggered if pressure falls below 110 psi
    -
