### Intent:
**Intent Summary:**  
Create a cascade control system for pressure and flow regulation, where an outer PID loop adjusts pressure by dynamically setting the flow setpoint for an inner PID loop, with configurable gains and anti-windup protection.  

*(Concise focus: Dual-loop PID control with pressure as primary and flow as secondary, including diagnostics and output limits.)*

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
Create a cascade control system for pressure and flow regulation, where an outer PID loop adjusts pressure by dynamically setting the flow setpoint for an inner PID loop, with configurable gains and anti-windup protection.  

*(Concise focus: Dual-loop PID control with pressure as primary and flow as secondary, including diagnostics and output limits.)*
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
FUNCTION_BLOCK FB_CascadePressureControl
VAR_INPUT
    PV_Pressure : REAL; // Measured pressure (bar)
    SP_Pressure : REAL; // Desired pressure (bar)
    PV_FlowRate : REAL; // Measured flow rate (m³/h)
    SP_FlowRate : REAL; // Desired flow rate (m³/h)
    Kp_Pressure : REAL; // Outer loop gain
    Kp_Flow : REAL;     // Inner loop gain
    Kd_Pressure : REAL; // Outer loop derivative gain
    Kd_Flow : REAL;     // Inner loop derivative gain
    Min_Flow : REAL;    // Minimum flow rate (m³/h)
    Max_Flow : REAL;    // Maximum flow rate (m³/h)
    Min_Pressure : REAL; // Minimum pressure (bar)
    Max_Pressure : REAL; // Maximum pressure (bar)
END_VAR

VAR_OUTPUT
    Output_FlowRate : REAL; // Flow setpoint for inner loop
    Error_Pressure : REAL;  // Pressure error for outer loop
    Output_Valve : REAL;    // Valve position (0–100%)
    Status : BOOL;          // Status flag (e.g., fault, saturation)
END_VAR

VAR
    Prev_Flow : REAL;
    Prev_Pressure : REAL;
    Integral_Pressure : REAL;
    Integral_Flow : REAL;
END_VAR

// Initialize outputs
Output_FlowRate := 0.0;
Output_Valve := 0.0;
Status := FALSE;

// Outer loop: Pressure control
Error_Pressure := SP_Pressure - PV_Pressure;

// Anti-windup: Clamp output to valid range
IF Output_FlowRate > Max_Flow THEN
    Output_FlowRate := Max_Flow;
    Status := TRUE; // Windup detected
END_IF;

IF Output_FlowRate < Min_Flow THEN
    Output_FlowRate := Min_Flow
