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

**UreaReactionControl:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer responsible for implementing a state-machine-driven PLC program to manage the urea production process.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library, which contains various mathematical function blocks, as well as the UreaReactionControl task description.

⸻

🟧 S (Steps) – How to Proceed
	1.	Review the UreaReactionControl task description to understand the process phases (loading, reacting, completion) and required control actions (valve operations, sensor validation, fault handling).
	2.	Identify the mathematical function blocks from the OSCAT library that will be useful for implementing the control logic, such as:
	•	Trigonometric functions for angle calculations (e.g., sin, cos, tan)
	•	Exponential and logarithmic functions for pressure and temperature calculations
	•	Statistical functions for data analysis (e.g., mean, standard deviation)
	•	Algebraic functions for simple calculations (e.g., addition, subtraction, multiplication, division)
	3.	Design a state machine to manage the urea production phases, incorporating the identified mathematical function blocks as needed.
	4.	Implement the state machine in the PLC program, ensuring proper valve control, sensor validation, and fault handling.
	5.	Test the PLC program in a simulated environment or on a test rig to verify its functionality and safety.
	6.	Iterate on the design and implementation as needed to optimize the urea production process and address any identified issues.

⸻

🟦 E (Expectation) – What the Output Should Look Like

A state-machine-driven PLC program that effectively manages the urea production process by:
	•	Controlling valve operations during the loading, reacting, and completion phases
	•	Monitoring pressure and temperature sensors to ensure safe operating conditions
	•	Timing the reaction to optimize urea yield
	•	Implementing fault detection and state-based logic to ensure safety and reliability
	•
