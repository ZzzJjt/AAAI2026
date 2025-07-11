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

**Code Generation Intent:**

Generate a state-machine-driven PLC program to manage urea production phases (loading, reacting, completion) with valve control, sensor validation, and fault handling.

**Urea Reaction Control State Machine:**

```plaintext
State Machine: UreaReactionControl

States:
1. Loading
2. Reacting
3. Completion
4. Fault

Transitions:
1. Loading -> Reacting: When loading is complete
2. Reacting -> Completion: When reaction is complete
3. Reacting -> Fault: If pressure/temperature exceeds safe limits
4. Completion -> Loading: When reaction is complete
5. Fault -> Loading: When fault is resolved

Actions:
1. Loading: Open loading valve, close reaction valve, monitor pressure/temperature
2. Reacting: Close loading valve, open reaction valve, monitor pressure/temperature
3. Completion: Close reaction valve, monitor pressure/temperature
4. Fault: Stop all valves, alert operator, monitor fault resolution

Conditions:
1. Loading: Loading valve open, reaction valve closed, pressure/temperature within safe limits
2. Reacting: Loading valve closed, reaction valve open, pressure/temperature within safe limits
3. Completion: Reaction valve closed, pressure/temperature within safe limits
4. Fault: Pressure/temperature exceeds safe limits, fault not resolved

Fault Handling:
1. If pressure/temperature exceeds safe limits, transition to Fault state
2. If fault is resolved, transition back to Loading state
```

**Mathematical Function Blocks Reference:**

| Category | Function Block | Description | Industrial Use Case |
| --- | --- | --- | --- |
| Trigonometric | Sin | Computes the sine of an angle | Calculating angles in mechanical systems |
| Trigonometric | Cos | Computes the cosine of an angle | Calculating angles in mechanical systems |
| Trigonometric | Tan | Computes the tangent of an angle | Calculating angles in mechanical systems |
| Exponential & Logarithmic | Exp | Computes the exponential of a number | Calculating growth rates in chemical processes |
| Exponential & Logarithmic | Log | Computes the natural logarithm of a number | Calculating decay rates in chemical processes |
| Statistical | Mean | Computes the mean of a set of numbers | Calculating average values in sensor data |
| Statistical | Median | Computes the median of a set of numbers | Calculating central tendency in sensor data |
| Statistical | Standard Deviation | Computes the standard deviation of a
