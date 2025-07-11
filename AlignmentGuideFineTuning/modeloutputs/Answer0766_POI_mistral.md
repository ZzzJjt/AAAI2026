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

### Exponential & Logarithmic Functions
- **EXP(x)** – Returns e raised to the power of x.  
  *Use case*: Exponential decay or growth models.

- **LN(x)** – Computes the natural logarithm of x.  
  *Use case*: Process kinetics, reaction rate calculations.

### Array Operations
- **SUM_ARRAY(array)** – Sums the elements of an array.  
  *Use case*: Totalizing sensor data or accumulated values.

- **MAX_ARRAY(array)** – Returns the maximum value in an array.  
  *Use case*: Finding the maximum temperature or pressure in a process.

- **MIN_ARRAY(array)** – Returns the minimum value in an array.  
  *Use case*: Finding the minimum temperature or pressure in a process.

- **AVERAGE_ARRAY(array)** – Computes the average of an array.  
  *Use case*: Smoothing sensor data in process control.
