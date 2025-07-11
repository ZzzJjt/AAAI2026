### Intent:
**Intent Summary:**  
Create a comprehensive, categorized list of all mathematical function blocks in the OSCAT library, detailing their functionality and industrial use cases to serve as a quick-reference guide for PLC programmers.

### Prompt:
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT (Open Source Community for Automation Technology) library for PLC programming. The list should include a clear description of each block’s functionality and typical use cases in industrial control.

⸻

🟩 A (Action) – How You Should Do It

To complete this task:
	1.	Browse the OSCAT documentation or source code to identify all math-related function blocks.
	2.	For each function block, include:
	•	Function block name (e.g., SIN, MEAN_ARRAY)
	•	A brief functional description
	•	Typical use case (e.g., waveform generation, process data smoothing, quality control)
	3.	Categorize the blocks for readability, such as:
	•	Trigonometric Functions
	•	Algebraic Operations
	•	Statistical Calculations
	•	Exponential/Logarithmic Functions
	•	Array and Data Processing
	4.	Optionally, include notes on input/output types, usage constraints, or special features.

⸻

🟦 G (Goal) – What You Aim to Deliver

Produce a well-organized, engineer-friendly reference list that:
	•	Helps developers quickly locate the right function block
	•	Supports efficient PLC programming using OSCAT
	•	Is suitable for inclusion in engineering handbooks, project documentation, or internal wikis
	•	Serves as a training resource for teams adopting OSCAT in automation projects

### Generated Code:
**Intent Summary:**  
Create a comprehensive, categorized list of all mathematical function blocks in the OSCAT library, detailing their functionality and industrial use cases to serve as a quick-reference guide for PLC programmers.
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT (Open Source Community for Automation Technology) library for PLC programming. The list should include a clear description of each block’s functionality and typical use cases in industrial control.

⸻

🟩 A (Action) – How You Should Do It

To complete this task:
	1.	Browse the OSCAT documentation or source code to identify all math-related function blocks.
	2.	For each function block, include:
	•	Function block name (e.g., SIN, MEAN_ARRAY)
	•	A brief functional description
	•	Typical use case (e.g., waveform generation, process data smoothing, quality control)
	3.	Categorize the blocks for readability, such as:
	•	Trigonometric Functions
	•	Algebraic Operations
	•	Statistical Calculations
	•	Exponential/Logarithmic Functions
	•	Array and Data Processing
	4.	Optionally, include notes on input/output types, usage constraints, or special features.

⸻

🟦 G (Goal) – What You Aim to Deliver

Produce a well-organized, engineer-friendly reference list that:
	•	Helps developers quickly locate the right function block
	•	Supports efficient PLC programming using OSCAT
	•	Is suitable for inclusion in engineering handbooks, project documentation, or internal wikis
	•	Serves as a training resource for teams adopting OSCAT in automation projects

⸻

🟪 I (Input) – What You Need to Know

•	OSCAT is an open-source library of function blocks for PLC programming, focusing on automation and control applications.
•	Function blocks are self-contained units of code that perform specific tasks, such as mathematical operations, data processing, or control logic.
•	Developers need a comprehensive list of available math-related function blocks to streamline their programming tasks and ensure they have the right tools for their projects.

⸻

🟫 O (Output) – What You Need to Produce

A well-organized list of all mathematical function blocks in the OSCAT library, including:
	•	Function block name
	•	Functional description
	•	Typical use case
	•	Categorization (e.g., Trigonometric Functions, Algebraic Operations, Statistical Calculations, etc.)
	•	Optional notes on input/output types, usage constraints, or special features

⸻

🟩 R (Reasoning) – Why It Matters

Developers working with PLCs need a clear understanding of the available mathematical function blocks in OSCAT to efficiently implement control logic, data processing, and other automation tasks. By providing a comprehensive list with descriptions and use cases, this resource helps engineers quickly locate the right function block for their needs, reducing development time and improving project efficiency.

⸻

🟧 E (Example) – A Practical Illustration

**Function Block:** SIN

**Functional Description:** Generates a sinusoidal waveform based on the input angle (in radians) and amplitude.

**Typical Use Case:** Generating a waveform for motor control, signal modulation, or process simulation.

**Categorization:** Trigonometric Functions

**Optional Notes:** The input angle should be in the range [0, 2π] for a complete cycle. The output is scaled between -1 and 1, representing the sine of the input angle.

**Function Block:** MEAN_ARRAY

**Functional Description:** Calculates the mean value of an array of numbers.

**Typical Use Case:** Smoothing process data, calculating average values, or implementing quality control checks.

**Categorization:** Statistical Calculations

**Optional Notes:** The input array should contain at least one element. The output is the sum of all
