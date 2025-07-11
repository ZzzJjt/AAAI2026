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

⸻

🟦 E (Example) – Provide an Example

```
+------+                 +------+
| Analog Input |         | TON  |
| IN  |------->|         | ET  |
+------+       |         +------+
                 |
                 +------+
                 | PID  |
                 | PV  |------->| SP |
                 | CV  |------->| CV |
                 +------+       |
                                 +------+
                                 | Analog Output |
                                 | OUT |------->|
+------+
```

🟦 S (Steps) – Break Down the Task

1. Create a new plain-text file for the ASCII diagram.
2. Define the block shapes and labeling conventions.
3. Draw the blocks and label the inputs and outputs.
4. Connect the blocks with signal paths.
5. Align the blocks and signal paths for readability.
6. Review the diagram for accuracy and clarity.
7. Save the file and share it with the team for review.

🟦 C (Constraints) – Define any Constraints

* Use ASCII characters for blocks and connections.
* Keep the diagram simple and easy to understand.
* Use common control variable names for inputs and outputs.
* Ensure the diagram accurately represents the intended control logic.

🟦 Q (Questions) – Ask any Questions

* Are there any specific requirements for the ASCII characters used for blocks and connections?
* Are there any preferred control variable names for the given components?
* Is there a specific layout or arrangement for the blocks and signal paths?
* Are there any additional details or components that should be included in the diagram?
* Are there any specific formatting or styling requirements for the ASCII diagram?
