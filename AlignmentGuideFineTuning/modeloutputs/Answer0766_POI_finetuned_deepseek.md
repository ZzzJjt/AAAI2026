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

### Exponential and Logarithmic Functions
- **EXP(x)** – Returns e^x.  
  *Use case*: Modeling growth or decay.

- **LN(x)** – Returns the natural logarithm of x.  
  *Use case*: Power-law distributions.

### Array Operations
- **ARRAY_SUM(array)** – Computes the sum of all elements in an array.  
  *Use case*: Batch processing or signal averaging.

- **ARRAY_PRODUCT(array)** – Computes the product of all elements in an array.  
  *Use case*: Matrix multiplication or signal convolution.

---

### Example Code Block

```plc
// Code: PID_Controller
VAR
    // Inputs
    Setpoint : REAL;
    CurrentValue : REAL;
    Error : REAL;

    // PID Parameters
    Kp : REAL := 1.0;
    Ki : REAL := 0.5;
    Kd : REAL := 0.2;

    // Internal Variables
    PrevError : REAL;
    PrevTime : TIME;
    Integral : REAL := 0.0;
    Derivative : REAL;

    // Output
    Output : REAL;
END_VAR

// PID Logic
Derivative := (Error - PrevError) / (TIC - PTIC);
Integral := Integral + Error * (TIC - PTIC);
Output := (Kp * Error) + (Ki * Integral) + (Kd * Derivative);

// Clamp Output
Output := MAX(MIN(Output, 100.0), -100.0);

// Reset Integral and Derivative
Integral := 0.0;
PrevError := Error;
PTIC := TIC;

// Output to actuator
Actuator(Output);
```

---

### Example Function Block

```plc
// Code: FunctionBlock_Add
VAR
    // Inputs
    A : REAL;
    B : REAL;

    // Output
    C : REAL;
END_VAR

// Addition Logic
C := A + B;

// Output to actuator
Actuator(C);
