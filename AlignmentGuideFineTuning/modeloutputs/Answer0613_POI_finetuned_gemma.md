### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to automate the aspirin production process, including reaction, crystallization, and drying phases, with precise temperature, pressure, and timing control.  

*(Focus: ISA-88 compliance, phase transitions, parameter-driven logic for pharmaceutical batch automation.)*

### Prompt:
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process automation engineer implementing ISA-88-compliant control strategies in IEC 61131-3 Structured Text for pharmaceutical production systems.

🟩 I (Input) – Information Provided

You are tasked with developing a batch control recipe for the production of aspirin (acetylsalicylic acid). The physical model includes a reactor, crystallizer, centrifuge, and dryer. The chemical inputs are acetic anhydride, salicylic acid, and sulfuric acid (as catalyst), and the main products are acetylsalicylic acid and acetic acid. The reaction stage requires precise control of temperature, pressure, and timing. The drying phase must occur at 90°C, and all control logic should comply with ISA-88 standards.

🟧 S (Steps) – Implementation Steps
	1.	Define the ISA-88 batch control recipe structure, including the physical and procedural models for the entire process.
	2.	Implement the reaction stage logic in Structured Text using parameter-driven control for heating, mixing, and holding the reaction conditions.
	3.	Design phase transitions using timers, condition checks, and method calls (e.g., StartHeating, StartMixing, HoldReaction).
	4.	Extend the logic to cover the crystallization and drying stages, ensuring the dryer operates at 90°C for the specified time with proper phase transition logic.
	5.	Apply ISA-88 concepts such as modular equipment phases, procedural elements, and reusable control blocks.

🟦 E (Expectation) – Expected Outcome

Produce a modular, ISA-88-compliant Structured Text program that reliably executes the reaction and downstream stages of aspirin production. The system should handle transitions between phases based on parameters and process conditions, support safe and efficient batch execution, and ensure product quality through accurate control of temperature, timing, and material handling.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to automate the aspirin production process, including reaction, crystallization, and drying phases, with precise temperature, pressure, and timing control.  

*(Focus: ISA-88 compliance, phase transitions, parameter-driven logic for pharmaceutical batch automation.)*
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process automation engineer implementing ISA-88-compliant control strategies in IEC 61131-3 Structured Text for pharmaceutical production systems.

🟩 I (Input) – Information Provided

You are tasked with developing a batch control recipe for the production of aspirin (acetylsalicylic acid). The physical model includes a reactor, crystallizer, centrifuge, and dryer. The chemical inputs are acetic anhydride, salicylic acid, and sulfuric acid (as catalyst), and the main products are acetylsalicylic acid and acetic acid. The reaction stage requires precise control of temperature, pressure, and timing. The drying phase must occur at 90°C, and all control logic should comply with ISA-88 standards.

🟧 S (Steps) – Implementation Steps
	1.	Define the ISA-88 batch control recipe structure, including the physical and procedural models for the entire process.
	2.	Implement the reaction stage logic in Structured Text using parameter-driven control for heating, mixing, and holding the reaction conditions.
	3.	Design phase transitions using timers, condition checks, and method calls (e.g., StartHeating, StartMixing, HoldReaction).
	4.	Extend the logic to cover the crystallization and drying stages, ensuring the dryer operates at 90°C for the specified time with proper phase transition logic.
	5.	Apply ISA-88 concepts such as modular equipment phases, procedural elements, and reusable control blocks.

🟦 E (Expectation) – Expected Outcome

Produce a modular, ISA-88-compliant Structured Text program that reliably executes the reaction and downstream stages of aspirin production. The system should handle transitions between phases based on parameters and process conditions, support safe and efficient batch execution, and ensure product quality through accurate control of temperature, timing, and material handling.

**R-I-S-E-T-A-C-T-I-O-N-S-E-T-T-I-N-G-S-I-S-A-88-B-A-T-C-H-C-O-N-T-R-O-L-S-T-R-U-C-T-U-R-E-D-T-E-X-T-S-E-R-I-A-L-T-E-X-T-B-A-T-C-H-C-O-N-T-R-O-L-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-B-A-T-C-H-C-O-N-T-R-O-L-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-B-A-T-C-H-C-O-N-T-R-O-L-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-B-A-T-C-H-C-O-N-T-R-O-L-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-B-A-T-C-H-C-O-N-T-R-O-L-I-E-C-61131-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-B-A-T-C-H-C-O-N-T-R
