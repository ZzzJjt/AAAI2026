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

⸻

🟪 S (Subject) – The Key Information

Focus on the key differences between IEC 61131-3 and IEC 61499, highlighting the benefits of IEC 61499 for distributed control systems. Discuss the event-driven nature of IEC 61499 and how it differs from the scan-based approach of 61131-3. Explain how IEC 61499 supports modularity, portability, and reuse in control systems, and provide a list of five essential references for further reading.

**C** (Circumstances) – The Situation

You are an experienced automation engineer who is already proficient in IEC 61131-3. You are now looking to learn and document IEC 61499, with a focus on understanding how it differs from 61131-3 and how it supports modern, distributed control systems.

**A** (Action) – What You Should Do

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

**R** (Result) – What You Should Achieve

Prepare your output as a structured technical briefing or onboarding guide suitable for:
	•	Training sessions
	•	Engineering team knowledge sharing
	•	Personal reference for system architecture decisions

It should include:
	•	A short introduction paragraph
	•	A comparison table or bullet list of differences
	•	A recommended reading list with titles, authors, and focus areas
	•	Optional: diagrams or short code examples to illustrate function block behavior
**◻️**

**R** (Role) – Your Role

You are an experienced automation engineer who is already proficient in IEC 61131-3.
