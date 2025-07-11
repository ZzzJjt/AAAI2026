### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the reaction stage of urea fertilizer production, including modular control of heating, cooling, and pressure regulation with condition-based transitions and industrial safety checks.  

*(Focus: Batch process automation, reactor control, and ISA-88/61131-3 compliance.)*

### Prompt:
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch control systems for industrial chemical processes using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with designing a control solution for the reaction stage of a urea fertilizer batch production process. This stage involves managing heating, cooling, and pressure regulation within a reactor. You are expected to use typical parameter values such as temperature (e.g., 180°C), pressure (e.g., 140 bar), and time (e.g., 30 minutes). The program must follow ISA-88 principles and be written in IEC 61131-3 Structured Text. It should include code snippets, transition conditions, timers, and inline explanations.

🟧 S (Steps) – Steps to Perform
	1.	Define the reaction stage as a series of modular ISA-88-compliant phases (e.g., StartHeating, HoldPressure, StartCooling).
	2.	Implement Structured Text logic for each phase, using IF statements, comparison logic, and TON timers to manage transitions between operations based on actual process conditions.
	3.	Create method/function blocks for each core operation (e.g., EvacuateReactor, RegulatePressure, CoolDown) with clear parameter inputs.
	4.	Add comments and structured control logic to facilitate readability, modularity, and industrial maintainability.
	5.	Discuss control challenges such as timing accuracy, thermal inertia, and maintaining pressure thresholds in real time.

🟦 E (Expectation) – Expected Outcome

The result should be a robust, modular Structured Text control program that handles the urea reaction stage safely and efficiently. It should be ISA-88-compliant, support industrial scalability, and clearly manage each sub-phase with condition-based transitions and well-defined control blocks—enabling accurate thermal and pressure control and easy integration with the broader batch system.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the reaction stage of urea fertilizer production, including modular control of heating, cooling, and pressure regulation with condition-based transitions and industrial safety checks.  

*(Focus: Batch process automation, reactor control, and ISA-88/61131-3 compliance.)*
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch control systems for industrial chemical processes using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with designing a control solution for the reaction stage of a urea fertilizer batch production process. This stage involves managing heating, cooling, and pressure regulation within a reactor. You are expected to use typical parameter values such as temperature (e.g., 180°C), pressure (e.g., 140 bar), and time (e.g., 30 minutes). The program must follow ISA-88 principles and be written in IEC 61131-3 Structured Text. It should include code snippets, transition conditions, timers, and inline explanations.

🟧 S (Steps) – Steps to Perform
	1.	Define the reaction stage as a series of modular ISA-88-compliant phases (e.g., StartHeating, HoldPressure, StartCooling).
	2.	Implement Structured Text logic for each phase, using IF statements, comparison logic, and TON timers to manage transitions between operations based on actual process conditions.
	3.	Create method/function blocks for each core operation (e.g., EvacuateReactor, RegulatePressure, CoolDown) with clear parameter inputs.
	4.	Add comments and structured control logic to facilitate readability, modularity, and industrial maintainability.
	5.	Discuss control challenges such as timing accuracy, thermal inertia, and maintaining pressure thresholds in real time.

🟦 E (Expectation) – Expected Outcome

The result should be a robust, modular Structured Text control program that handles the urea reaction stage safely and efficiently. It should be ISA-88-compliant, support industrial scalability, and clearly manage each sub-phase with condition-based transitions and well-defined control blocks—enabling accurate thermal and pressure control and easy integration with the broader batch system. The code should be self-contained, with inline explanations for each operation and transition, ensuring that it can be easily understood and maintained by other engineers in the field.

**T-A-B:**

🟥 T (Task) – What You Need to Do

Develop a self-contained IEC 61131-3 Structured Text program to manage the reaction stage of urea fertilizer production, following ISA-88 principles. Include code snippets for heating, cooling, and pressure regulation, and explain the use of modular control logic and condition-based transitions in industrial batch processes.

🟩 A (Action) – What You Should Do

Create a self-contained IEC 61131-3 Structured Text program to manage the reaction stage of urea fertilizer production, following ISA-88 principles. Include code snippets for heating, cooling, and pressure regulation, and explain the use of modular control logic and condition-based transitions in industrial batch processes.

🟠 B (Behavior) – What You Should Notice

The program should be modular, with each phase defined as a separate ISA-88 batch control operation. The logic should include self-contained code snippets for heating, cooling, and pressure regulation, with clear transitions between phases based on process conditions. The use of timers and condition-based logic should ensure accurate control of temperature, pressure, and timing.

🟩 I (Interaction) – How to Respond

Provide a self-contained IEC 61131-3 Structured Text program that manages the reaction stage of urea fertilizer production, following ISA-88 principles. Include code snippets for heating, cooling, and pressure regulation, and explain the use of modular control logic and condition-based transitions in industrial batch processes.

**C:**

🟥 C (Context) – The Situation

In the chemical industry, batch control is a critical process for managing the production of urea fertilizer. The reaction stage involves precise control of temperature, pressure, and timing to ensure efficient and safe operation. ISA-88 provides a standardized framework for batch control, while IEC 61131-3 Structured Text is a widely used programming language for industrial automation. Developing a self-contained program that follows these standards is essential for ensuring consistent and reliable operation in a batch control environment.

🟩 I (Input) – The Information

You are tasked with developing a self-contained IEC 61131-3 Structured
