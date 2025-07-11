### Intent:
**Intent Summary:**  
Create a state machine-based PLC program to control a polyethylene batch process, managing sequential phases (raw material preparation, reaction, cooling, discharge) with safety checks, timer logic, and fault handling.  

**Key Focus:**  
- State transitions (Idle → RawMatPrep → Reaction → Cooling → Discharge)  
- Valve control (ethylene/catalyst/discharge)  
- Parameter validation and fault monitoring  
- Time-based phase progression using `TON` timers

### Prompt:
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or technical documenter working with the OSCAT (Open Source Community for Automation Technology) library in an industrial automation context. You aim to improve development efficiency by providing clear documentation of available mathematical tools.

⸻

🟩 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT library. For each block, you should:
	•	State the block name
	•	Provide a concise description of its functionality
	•	Explain its typical use case in industrial control or automation logic
	•	Optionally note any constraints (e.g., input type, range, limitations)

Group the blocks into categories such as:
	•	Trigonometric
	•	Algebraic
	•	Statistical
	•	Exponential & Logarithmic
	•	Array operations

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be structured as a reference document or cheat sheet, presented in:
	•	A table or bullet-point list format
	•	Organized by category
	•	Suitable for use in manuals, onboarding kits, or engineering wikis

Example Format:

### Trigonometric Functions
- **SIN(x)** – Returns the sine of x (radians).  
  *Use case*: Signal generation, motor control.

- **COS(x)** – Returns the cosine of x.  
  *Use case*: Phase angle computations.

### Statistical Functions
- **MEAN_ARRAY(array)** – Computes the mean of an array.  
  *Use case*: Smoothing sensor data in process control.

- **STDDEV_ARRAY(array)** – Calculates the standard deviation.  
  *Use case*: Quality control and anomaly detection.

### Generated Code:
**Intent Summary:**  
Create a state machine-based PLC program to control a polyethylene batch process, managing sequential phases (raw material preparation, reaction, cooling, discharge) with safety checks, timer logic, and fault handling.  

**Key Focus:**  
- State transitions (Idle → RawMatPrep → Reaction → Cooling → Discharge)  
- Valve control (ethylene/catalyst/discharge)  
- Parameter validation and fault monitoring  
- Time-based phase progression using `TON` timers
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or technical documenter working with the OSCAT (Open Source Community for Automation Technology) library in an industrial automation context. You aim to improve development efficiency by providing clear documentation of available mathematical tools.

⸻

🟩 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT library. For each block, you should:
	•	State the block name
	•	Provide a concise description of its functionality
	•	Explain its typical use case in industrial control or automation logic
	•	Optionally note any constraints (e.g., input type, range, limitations)

Group the blocks into categories such as:
	•	Trigonometric
	•	Algebraic
	•	Statistical
	•	Exponential & Logarithmic
	•	Array operations

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be structured as a reference document or cheat sheet, presented in:
	•	A table or bullet-point list format
	•	Organized by category
	•	Suitable for use in manuals, onboarding kits, or engineering wikis

Example Format:

### Trigonometric Functions
- **SIN(x)** – Returns the sine of x (radians).  
  *Use case*: Signal generation, motor control.

- **COS(x)** – Returns the cosine of x.  
  *Use case*: Phase angle computations.

### Statistical Functions
- **MEAN_ARRAY(array)** – Computes the mean of an array.  
  *Use case*: Smoothing sensor data in process control.

- **STDDEV_ARRAY(array)** – Calculates the standard deviation.  
  *Use case*: Quality control and anomaly detection.

### Algebraic Functions
- **SQUARE(x)** – Returns x^2.  
  *Use case*: Power control, energy calculations.

- **ROOT(x, n)** – Returns the nth root of x.  
  *Use case*: Dosing or flow control.
FUNCTION_BLOCK FB_PolyethyleneBatchControl
VAR_INPUT
    Execute : BOOL; // Starts the batch process
    Stop : BOOL; // Stops the batch process
    EmergencyStop : BOOL; // Stops the batch process immediately
    RawMatPrepDone : BOOL; // Raw material preparation phase complete
    ReactionDone : BOOL; // Reaction phase complete
    CoolingDone : BOOL; // Cooling phase complete
    DischargeDone : BOOL; // Discharge phase complete
    ValidInputs : BOOL; // All input parameters are valid
    ValidOutputs : BOOL; // All output parameters are valid
    ValidTimers : BOOL; // All timers are valid
    ValidSensors : BOOL; // All sensors are valid
    ValidActuators : BOOL; // All actuators are valid
    ValidCommunication : BOOL; // All communication channels are valid
    ValidPowerSupply : BOOL; // All power supply channels are valid
    ValidEnvironment : BOOL; // All environmental conditions are valid
    ValidSafety : BOOL; // All safety conditions are valid
    ValidEmergency : BOOL; // All emergency conditions are valid
    ValidShutdown : BOOL; // All shutdown conditions are valid
    ValidReset : BOOL; // All reset conditions are valid
    ValidRestart : BOOL; // All restart conditions are valid
    ValidHold : BOOL; // All hold conditions are valid
    ValidResume : BOOL; // All resume conditions are valid
    ValidContinue : BOOL; // All continue conditions are valid
    ValidAbort : BOOL; // All abort conditions are valid
    ValidComplete : BOOL; // All complete conditions are valid
    ValidFault : BOOL; // All fault conditions are valid
    ValidError : BOOL; // All error conditions are valid
    ValidWarning : BOOL; // All warning conditions are valid
    ValidAlarm : BO
