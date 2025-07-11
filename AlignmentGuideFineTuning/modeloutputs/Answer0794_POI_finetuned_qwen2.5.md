### Intent:
**Intent Summary:**  
Create an ASCII-formatted IEC 61131-3 Function Block Diagram (FBD) showing an analog input feeding a timer and PID block, with the PID output driving an analog output, including labeled signals and connections.  

*(Focus: Structured PLC logic documentation for control system design.)*

### Prompt:
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC systems designer tasked with documenting control logic using IEC 61131-3 Function Block Diagram (FBD) principles in ASCII format for use in design documentation and peer review.

⸻

🟩 T (Task) – Define the Objective

Create a readable ASCII function block diagram that includes the following components:
	•	An Analog Input block
	•	A TON (On-delay Timer) block
	•	A PID control block
	•	An Analog Output block

Ensure the diagram follows this flow:
	•	The Analog Input feeds both the Timer and PID block
	•	Only the PID output (Control Variable, CV) connects to the Analog Output
	•	Display typical signal names (e.g., IN, OUT, PV, SP, CV, ET) inside each block
	•	Arrange and label the blocks and connections clearly using ASCII characters (e.g., +---+, -->)

⸻

🟧 F (Format) – Specify the Output Format

Deliver:
	•	A plain-text ASCII diagram with:
	•	Each block represented as a boxed unit (+------+)
	•	Clearly labeled signal paths between blocks
	•	Inputs and outputs shown with common control variable names
	•	A layout that shows how the signal flows from input to output, including branches to multiple blocks
	•	All blocks and signal paths aligned for easy readability in code editors or printed docs

### Generated Code:
**Intent Summary:**  
Create an ASCII-formatted IEC 61131-3 Function Block Diagram (FBD) showing an analog input feeding a timer and PID block, with the PID output driving an analog output, including labeled signals and connections.  

*(Focus: Structured PLC logic documentation for control system design.)*
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC systems designer tasked with documenting control logic using IEC 61131-3 Function Block Diagram (FBD) principles in ASCII format for use in design documentation and peer review.

⸻

🟩 T (Task) – Define the Objective

Create a readable ASCII function block diagram that includes the following components:
	•	An Analog Input block
	•	A TON (On-delay Timer) block
	•	A PID control block
	•	An Analog Output block

Ensure the diagram follows this flow:
	•	The Analog Input feeds both the Timer and PID block
	•	Only the PID output (Control Variable, CV) connects to the Analog Output
	•	Display typical signal names (e.g., IN, OUT, PV, SP, CV, ET) inside each block
	•	Arrange and label the blocks and connections clearly using ASCII characters (e.g., +---+, -->)

⸻

🟧 F (Format) – Specify the Output Format

Deliver:
	•	A plain-text ASCII diagram with:
	•	Each block represented as a boxed unit (+------+)
	•	Clearly labeled signal paths between blocks
	•	Inputs and outputs shown with common control variable names
	•	A layout that shows how the signal flows from input to output, including branches to multiple blocks
	•	All blocks and signal paths aligned for easy readability in code editors or printed docs
	•	Include a brief explanation of the control logic flow for clarity

⸻

**B-A-B:**

Before starting, ensure:
	•	You understand the control logic: analog input → timer → PID → analog output
	•	You are familiar with the ASCII art conventions for function blocks and signal flow
	•	You have a list of typical signal names for each block

After completing the ASCII diagram:
	•	Review the layout for clarity and accuracy
	•	Ensure all signal names inside the blocks are consistent and make sense
	•	Replace any ambiguous or non-standard signal names with clear, descriptive terms
	•	Perform a final check to ensure the control flow is logical and the diagram is easy to follow
	•	(Optional) Create a second version with signal values (e.g., 0–100%) to illustrate practical use cases
	•	(Optional) Discuss the diagram with a colleague to validate the control logic and notation

Following these steps will help you create a well-structured, readable ASCII FBD diagram for use in control system documentation and design reviews.

**B-A-B:**

Before starting, ensure:
	•	You understand the control logic: analog input → timer → PID → analog output
	•	You are familiar with the ASCII art conventions for function blocks and signal flow
	•	You have a list of typical signal names for each block

After completing the ASCII diagram:
	•	Review the layout for clarity and accuracy
	•	Ensure all signal names inside the blocks are consistent and make sense
	•	Replace any ambiguous or non-standard signal names with clear, descriptive terms
	•	Perform a final check to ensure the control flow is logical and the diagram is easy to follow
	•	(Optional) Create a second version with signal values (e.g., 0–100%) to illustrate practical use cases
	•	(Optional) Discuss the diagram with a colleague to validate the control logic and notation
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID output (Control Variable, CV) connects to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**R-T-F:**

⸻

�
