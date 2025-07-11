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
- **EXP(x)** – Raises e to the power of x.  
  *Use case*: Temperature scaling, pressure conversion.

- **LOG(x)** – Returns the natural logarithm of x.  
  *Use case*: Process rate calculations.

### Array Operations
- **ARRAY_MUL(array1, array2)** – Multiplies corresponding elements of two arrays.  
  *Use case*: Signal processing, data normalization.

- **ARRAY_ADD(array1, array2)** – Adds corresponding elements of two arrays.  
  *Use case*: Summation in control loops.

### Algebraic Functions
- **ABS(x)** – Returns the absolute value of x.  
  *Use case*: Signal conditioning, deadband implementation.

- **SQRT(x)** – Computes the square root of x.  
  *Use case*: Power distribution, energy calculations.

### Other Mathematical Functions
- **RND(x)** – Generates a random number between 0 and x.  
  *Use case*: Randomized control, fault injection.

- **ROUND(x, n)** – Rounds x to n decimal places.  
  *Use case*: Precision control, data formatting.

⸻

🟪 A (Action) – What to Do

Create a detailed list of all mathematical function blocks available in the OSCAT library, including a brief description of their functionality and typical use cases. Organize the blocks into categories such as trigonometric, algebraic, statistical, exponential & logarithmic, array operations, and other mathematical functions. Ensure that the list is comprehensive and self-contained, suitable for use as a reference document or cheat sheet in industrial automation contexts.

⸻

🟥 T (Time) – When to Do It

Complete this task within 30 minutes, focusing on clarity and completeness in your descriptions.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or technical documenter working with the OSCAT (Open Source Community for Automation Technology) library in an industrial automation context. You aim to improve development efficiency by providing clear documentation of available mathematical tools.

⸻

🟩 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT library
