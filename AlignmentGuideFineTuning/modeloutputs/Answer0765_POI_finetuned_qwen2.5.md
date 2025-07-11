### Intent:
The task involves creating a PLC program (IEC 61131-3) to automate urea synthesis by controlling raw material loading, reaction conditions (pressure/temperature), and emergency shutdowns via a state machine with safety interlocks and timing logic.  

**Intent summary for code generation:**  
*"Generate a state-driven PLC program for urea synthesis automation, handling phased control (loading/reaction/shutdown), sensor validation, safety interlocks, and configurable process parameters."*  

(Key focus: Sequential control + safety in chemical processes)

### Prompt:
**Learning IEC 61499:**
Provide a concise introduction to the IEC 61499 programming language, emphasizing key concepts for someone already familiar with IEC 61131-3. Include a comparison of their fundamental differences in terms of architecture, execution models, and flexibility for distributed control systems. Additionally, compile a list of five key references for further reading on IEC 61499, highlighting its relevance in modern industrial applications.

**R-T-F:**

🟥 R (Role) – Your Role

You are an experienced automation or control engineer who is already proficient in IEC 61131-3. You are now looking to learn and document IEC 61499, with a focus on understanding how it differs from 61131-3 and how it supports modern, distributed control systems.

⸻

🟩 T (Task) – What You Need to Do

Write a concise technical introduction to IEC 61499 for engineers already familiar with IEC 61131-3. Your tasks include:
	1.	Explain key concepts of IEC 61499:
	•	Event-driven function blocks
	•	Distribution across devices
	•	Separation of event and data flows
	2.	Compare IEC 61499 with IEC 61131-3, focusing on:
	•	Architecture (centralized vs. distributed)
	•	Execution models (scan-based vs. event-driven)
	•	Modularity, portability, and reuse in control systems
	3.	Provide five essential references for further reading that explore:
	•	Theoretical foundations
	•	Practical use cases in industrial automation
	•	Real-world implementations

⸻

🟦 F (Format) – What the Output Should Look Like

Prepare your output as a structured technical briefing or onboarding guide suitable for:
	•	Training sessions
	•	Engineering team knowledge sharing
	•	Personal reference for system architecture decisions

It should include:
	•	A short introduction paragraph
	•	A comparison table or bullet list of differences
	•	A recommended reading list with titles, authors, and focus areas
	•	Optional: diagrams or short code examples to illustrate function block behavior

### Generated Code:
The task involves creating a PLC program (IEC 61131-3) to automate urea synthesis by controlling raw material loading, reaction conditions (pressure/temperature), and emergency shutdowns via a state machine with safety interlocks and timing logic.  

**Intent summary for code generation:**  
*"Generate a state-driven PLC program for urea synthesis automation, handling phased control (loading/reaction/shutdown), sensor validation, safety interlocks, and configurable process parameters."*  

(Key focus: Sequential control + safety in chemical processes)
**Learning IEC 61499:**
Provide a concise introduction to the IEC 61499 programming language, emphasizing key concepts for someone already familiar with IEC 61131-3. Include a comparison of their fundamental differences in terms of architecture, execution models, and flexibility for distributed control systems. Additionally, compile a list of five key references for further reading on IEC 61499, highlighting its relevance in modern industrial applications.

**R-T-F:**

🟥 R (Role) – Your Role

You are an experienced automation or control engineer who is already proficient in IEC 61131-3. You are now looking to learn and document IEC 61499, with a focus on understanding how it differs from 61131-3 and how it supports modern, distributed control systems.

⸻

🟩 T (Task) – What You Need to Do

Write a concise technical introduction to IEC 61499 for engineers already familiar with IEC 61131-3. Your tasks include:
	1.	Explain key concepts of IEC 61499:
	•	Event-driven function blocks
	•	Distribution across devices
	•	Separation of event and data flows
	2.	Compare IEC 61499 with IEC 61131-3, focusing on:
	•	Architecture (centralized vs. distributed)
	•	Execution models (scan-based vs. event-driven)
	•	Modularity, portability, and reuse in control systems
	3.	Provide five essential references for further reading that explore:
	•	Theoretical foundations
	•	Practical use cases in industrial automation
	•	Real-world implementations

⸻

🟦 F (Format) – What the Output Should Look Like

Prepare your output as a structured technical briefing or onboarding guide suitable for:
	•	Training sessions
	•	Engineering team knowledge sharing
	•	Personal reference for system architecture decisions

It should include:
	•	A short introduction paragraph
	•	A comparison table or bullet list of differences
	•	A recommended reading list with titles, authors, and focus areas
	•	Optional: diagrams or short code examples to illustrate function block behavior

Ensure clarity, precision, and relevance to the target audience’s level of expertise.

**Learning IEC 61499:**

Develop a concise introduction to IEC 61499 for engineers already familiar with IEC 61131-3. Emphasize key concepts such as event-driven function blocks, distributed architecture, and modularity. Provide a comparison of IEC 61499 with IEC 61131-3, highlighting differences in execution models, flexibility, and suitability for distributed control systems. Include a list of five key references for further reading on IEC 61499, covering both theoretical and practical aspects of the language in industrial applications.

**R-T-F:**

⸻

🟥 R (Role) – Your Role

You are an experienced automation or control engineer already familiar with IEC 61131-3. Your goal is to understand and explain IEC 61499 to your team or for your own reference, focusing on key concepts, differences from IEC 61131-3, and practical applications.

⸻

🟩 T (Task) – What You Need to Do

Create a concise introduction to IEC 61499 for someone already familiar with IEC 61131-3. Include the following elements:

	1.	Explain the fundamental concepts of IEC 61499, particularly:
	•	How it uses event-driven function blocks to manage distributed control logic
	•	The role of function blocks in modularity and reusability
	•	The concept of a control network where each node can execute a part of the overall control program
	2.	Compare IEC 61499 with IEC 61131-3, focusing on:
	•	The scan-cycle execution model of IEC 61131-3 versus the event-driven execution of IEC 61499
	•	The flexibility of IEC 61499 in terms of distributed deployment and real-time responsiveness
	•	The advantages of IEC 61499 for systems with strict timing requirements or where control logic is spread across multiple devices
	3.	Compile a list of five key references for further reading on IEC 61499, including:
	•	Works that explain the architecture and execution models of IEC
