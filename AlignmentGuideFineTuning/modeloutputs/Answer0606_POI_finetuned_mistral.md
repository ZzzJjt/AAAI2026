### Intent:
**Intent Summary:**  
Create a structured reference document listing all mathematical function blocks in the OSCAT library, categorized by type (e.g., trigonometric, statistical), with descriptions and industrial use cases to streamline PLC programming and team onboarding.  

**Industrial Control Task (UreaReactionControl):**  
Automate a urea synthesis process by controlling valve operations, monitoring pressure/temperature, and timing the reaction while ensuring safety via fault detection and state-based logic.  

**Code Generation Intent:**  
Generate a state-machine-driven PLC program to manage urea production phases (loading, reacting, completion) with valve control, sensor validation, and fault handling.

### Prompt:
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer using the OSCAT library to implement complex mathematical operations in control systems. To improve your workflow and assist your team, you aim to create a clear and accessible reference.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library documentation or source files, which contain numerous mathematical function blocks (e.g., trigonometric, algebraic, statistical). However, these blocks are not centrally organized, and many lack contextual descriptions or usage examples.

⸻

🟧 S (Steps) – How to Proceed
	1.	Explore the OSCAT library (docs or codebase) and extract all function blocks under the mathematical category.
	2.	Organize the function blocks into logical categories such as:
	•	Trigonometric
	•	Exponential & Logarithmic
	•	Statistical
	•	Algebraic
	3.	For each function block, write:
	•	Its name
	•	A brief functional description
	•	A typical industrial use case or application context
	4.	Optionally, provide notes on parameter types, return values, or limitations (e.g., expected units, input range).
	5.	Present the final list in a structured format (table or markdown list).

⸻

🟦 E (Expectation) – What the Output Should Look Like

A well-organized reference list of OSCAT’s mathematical function blocks that:
	•	Helps engineers quickly find the right block for a task
	•	Serves as a training tool for newcomers
	•	Boosts development speed and reduces reliance on searching through source code
	•	Enhances code reliability by encouraging proper block selection based on descriptions and use cases

### Generated Code:
**Intent Summary:**  
Create a structured reference document listing all mathematical function blocks in the OSCAT library, categorized by type (e.g., trigonometric, statistical), with descriptions and industrial use cases to streamline PLC programming and team onboarding.  

**Industrial Control Task (UreaReactionControl):**  
Automate a urea synthesis process by controlling valve operations, monitoring pressure/temperature, and timing the reaction while ensuring safety via fault detection and state-based logic.  

**Code Generation Intent:**  
Generate a state-machine-driven PLC program to manage urea production phases (loading, reacting, completion) with valve control, sensor validation, and fault handling.
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer using the OSCAT library to implement complex mathematical operations in control systems. To improve your workflow and assist your team, you aim to create a clear and accessible reference.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library documentation or source files, which contain numerous mathematical function blocks (e.g., trigonometric, algebraic, statistical). However, these blocks are not centrally organized, and many lack contextual descriptions or usage examples.

⸻

🟧 S (Steps) – How to Proceed
	1.	Explore the OSCAT library (docs or codebase) and extract all function blocks under the mathematical category.
	2.	Organize the function blocks into logical categories such as:
	•	Trigonometric
	•	Exponential & Logarithmic
	•	Statistical
	•	Algebraic
	3.	For each function block, write:
	•	Its name
	•	A brief functional description
	•	A typical industrial use case or application context
	4.	Optionally, provide notes on parameter types, return values, or limitations (e.g., expected units, input range).
	5.	Present the final list in a structured format (table or markdown list).

⸻

🟦 E (Expectation) – What the Output Should Look Like

A well-organized reference list of OSCAT’s mathematical function blocks that:
	•	Helps engineers quickly find the right block for a task
	•	Serves as a training tool for newcomers
	•	Boosts development speed and reduces reliance on searching through source code
	•	Enhances code reliability by encouraging proper block selection based on descriptions and use cases
(* IEC 61131-3 Structured Text Program for Urea Reaction Control *)
(* Manages urea synthesis process with valve control, pressure/temperature monitoring, *)
(* and timed reaction *)

PROGRAM UreaReactionControl
VAR
    (* Inputs *)
    StartReaction : BOOL;                  (* TRUE to start reaction *)
    AmmoniaValveOpen : BOOL;              (* TRUE if ammonia valve is open *)
    CO2ValveOpen : BOOL;                  (* TRUE if CO₂ valve is open *)
    PressureSensor : REAL;                (* Pressure reading in bar *)
    TemperatureSensor : REAL;             (* Temperature reading in °C *)
    EmergencyStop : BOOL;                 (* TRUE if emergency stop activated *)
    
    (* Outputs *)
    AmmoniaValve : BOOL;                  (* TRUE to open ammonia valve *)
    CO2Valve : BOOL;                      (* TRUE to open CO₂ valve *)
    ReactionComplete : BOOL;              (* TRUE when reaction complete *)
    FaultDetected : BOOL;                (* TRUE if fault detected *)
    
    (* Internal Variables *)
    ReactionState : INT := 0;             (* 0=Idle, 1=Loading, 2=Reacting, 3=Complete *)
    ReactionTimer : TON;                  (* Timer for reaction timing *)
    AmmoniaValveTimer : TON;             (* Timer for ammonia valve delay *)
    CO2ValveTimer : TON;                 (* Timer for CO₂ valve delay *)
    LoadingComplete : BOOL;              (* TRUE when loading complete *)
    ReactionFault : BOOL;                (* TRUE if fault during reaction *)
    ValveFault : BOOL;                   (* TRUE if valve issue *)
    TempOutOfRange : BOOL;               (* TRUE if temperature out of range *)
    PressureOutOfRange : BOOL;           (* TRUE if pressure out of range *)
    
    (* Constants *)
    AmmoniaValveDelay : TIME := T#10s;    (* Delay to open ammonia valve
