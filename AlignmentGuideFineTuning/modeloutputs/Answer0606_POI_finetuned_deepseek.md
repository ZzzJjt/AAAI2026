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
FUNCTION_BLOCK FB_UreaReactionControl
VAR_INPUT
    Valve1_IN : BOOL; // Control valve for urea feed
    Valve2_IN : BOOL; // Control valve for CO2 feed
    Valve3_IN : BOOL; // Control valve for NH3 feed
    Pressure_IN : REAL; // Pressure sensor (bar)
    Temperature_IN : REAL; // Temperature sensor (°C)
    Phase_IN : BOOL; // Phase detection (0=loading, 1=reacting, 2=completed)
    Fault_IN : BOOL; // Fault detection (0=normal, 1=emergency stop)
END_VAR

VAR_OUTPUT
    Valve1_OUT : BOOL; // Control valve for urea feed
    Valve2_OUT : BOOL; // Control valve for CO2 feed
    Valve3_OUT : BOOL; // Control valve for NH3 feed
    Pressure_OUT : REAL; // Pressure setpoint (bar)
    Temperature_OUT : REAL; // Temperature setpoint (°C)
    Phase_OUT : BOOL; // Phase setpoint (0=loading, 1=reacting, 2=completed)
    Fault_OUT : BOOL; // Fault setpoint (0=normal, 1=emergency stop)
END_VAR

VAR
    Phase_State : INT := 0; // Phase state (0=loading, 1=reacting, 2=completed)
    Pressure_Setpoint : REAL := 1.5; // Pressure setpoint (bar)
    Temperature_Setpoint : REAL := 120.0; // Temperature setpoint (°C)
    Fault_Setpoint : BOOL := FALSE; // Fault setpoint (0=normal, 1=emergency stop)
END_VAR

METHOD Execute : BOOL
BEGIN
    // Phase control
    IF Phase_State = 0 THEN
        IF Valve1_IN AND Valve2_IN AND Valve3_IN THEN
            Phase_State := 1;
        END_IF;
    ELSIF Phase_State = 1 THEN
        IF NOT Valve1_IN THEN
            Phase_State := 2;
        END_IF;
    END_IF;

    // Pressure control
    IF Pressure_IN > Pressure_Setpoint THEN
