### Intent:
The intent is to generate PLC code for controlling a urea production reaction by sequentially managing ammonia and CO2 valve operations, monitoring pressure and temperature conditions, and timing the reaction duration before completing the process.

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
The intent is to generate PLC code for controlling a urea production reaction by sequentially managing ammonia and CO2 valve operations, monitoring pressure and temperature conditions, and timing the reaction duration before completing the process.
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
    Enable : BOOL; // Activate the process
    Pressure : REAL; // Pressure in bar
    Temperature : REAL; // Temperature in °C
    Valve1 : BOOL; // Control valve for ammonia
    Valve2 : BOOL; // Control valve for CO2
END_VAR

VAR_OUTPUT
    Valve1_Output : BOOL; // Output signal for valve 1
    Valve2_Output : BOOL; // Output signal for valve 2
    Done : BOOL; // Process complete flag
END_VAR

VAR
    // Internal state variables
    ReactionRunning : BOOL := FALSE; // Flag to indicate whether the reaction is running
    ReactionTime : TIME := T#0s; // Time since the reaction started
    ReactionDuration : TIME := T#10m; // Maximum reaction time
    ReactionComplete : BOOL := FALSE; // Flag to indicate whether the reaction is complete
END_VAR

// Main logic
IF Enable THEN
    IF NOT ReactionRunning THEN
        ReactionRunning := TRUE;
        ReactionTime := T#0s;
        ReactionComplete := FALSE;
    END_IF;

    // Check if the reaction is running
    IF ReactionRunning THEN
        // Check if the reaction has completed
        IF ReactionTime >= ReactionDuration THEN
            ReactionRunning := FALSE;
            ReactionComplete := TRUE;
        ELSE
            // Update the reaction time
            ReactionTime := T#100ms + ReactionTime;
        END_IF;
    ELSE
        // Reset the reaction state
        ReactionRunning := FALSE;
        ReactionTime := T#0s;
        ReactionComplete := FALSE;
    END_IF;

    // Control the valves based on the reaction state
    IF ReactionRunning THEN
        // Valve 1: Open if the reaction is running
        Valve1_Output := Valve1;
        // Valve 2: Open if the reaction is running
        Valve2_Output := Valve2;
    ELSE
        // Valve 1: Close if the reaction is not running
        Valve1_Output := NOT Valve1;
        // Valve 2: Close if the reaction is not running
        Valve2_Output := NOT Valve2;
