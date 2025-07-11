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

**Code Generation:**

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer tasked with implementing a state-machine-driven control system for a urea synthesis process. The system must manage valve operations, monitor pressure/temperature, and time the reaction while ensuring safety via fault detection and state-based logic.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library, which contains numerous function blocks for mathematical operations, logic, and state machines. You also have the process specifications and requirements, including:
	•	Three process phases: loading, reacting, and completion
	•	Valve control for loading and reacting
	•	Pressure and temperature monitoring
	•	Reaction timing
	•	Fault detection and handling

⸻

🟧 S (Steps) – How to Proceed
	1.	Define the process states and transitions, including:
	•	Loading: loading urea into the reactor
	•	Reacting: reacting the urea to produce urea
	•	Completion: completing the reaction and shutting down the system
	2.	Create a state machine using the OSCAT library’s state machine function blocks.
	3.	Implement the valve control logic using the OSCAT library’s logic function blocks.
	4.	Implement the pressure and temperature monitoring logic using the OSCAT library’s mathematical function blocks.
	5.	Implement the reaction timing logic using the OSCAT library’s mathematical function blocks.
	6.	Implement the fault detection and handling logic using the OSCAT library’s logic and state machine function blocks.
	7.	Test and debug the control system to ensure it meets the process specifications and requirements.

⸻

🟦 E (Expectation) – What the Output Should Look Like

A state-machine-driven PLC program that manages the urea synthesis process, including valve control, sensor validation, and fault handling. The program should be well-organized, easy to understand, and reliable, with clear comments and documentation.

**Code Generation:**

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer tasked with implementing a state-machine-driven control system for a urea synthesis process. The system must manage valve operations, monitor pressure/temperature, and time the reaction while ensuring safety via fault detection and state-based logic.
