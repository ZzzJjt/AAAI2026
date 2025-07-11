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

⸻

🟧 S (Solution) – How to Complete the Task

To complete the task, follow these steps:

1. **Research the OSCAT library** – Familiarize yourself with the available mathematical function blocks. You can find the library documentation online or consult with colleagues who have used it before.

2. **Categorize the blocks** – Group the function blocks into categories based on their primary mathematical operation (e.g., trigonometric, algebraic, statistical, exponential/logarithmic, array operations).

3. **Document each block** – For each block, provide a name, a concise description of its functionality, and an example use case. If applicable, note any constraints or limitations.

4. **Organize the information** – Structure your output in a table or bullet-point list format, organized by category. Ensure that the document is easy to read and understand, suitable for use in manuals, onboarding kits, or engineering wikis.

5. **Review and revise** – Double-check your work for accuracy and completeness. Make any necessary revisions to improve clarity or address any missing information.

6. **Share your findings** – Once you have completed the task, share your reference document or cheat sheet with your team, colleagues, or the OSCAT community. This will help improve development efficiency and facilitate knowledge sharing.

⸻

🟨 A (Assistance) – What to Do If You Need Help

If you encounter any difficulties or have questions while completing the task, consider reaching out to colleagues, mentors, or the OSCAT community for assistance. You can also consult the OSCAT library documentation or online resources to find additional information or examples.

⸻

🟩 R (Review) – What to Do Before Submitting Your Answer

Before submitting your answer, review it to ensure that it meets the requirements of the instruction. Check that you have:
	•	Provided a detailed list of all mathematical function blocks in the OSCAT library
	•	Organized the blocks into categories
	•	Provided a concise description of each block's functionality and a typical use case
	•	Ensured the document is easy to read and understand, suitable for use in manuals, onboarding kits, or engineering wikis

If you have completed all these steps and are confident in your answer, you can submit it for review.
