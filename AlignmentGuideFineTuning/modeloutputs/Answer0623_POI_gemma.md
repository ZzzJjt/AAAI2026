### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text for aspirin production, automating reactor heating/mixing, crystallization, and drying (90°C) with phase transitions, parameterized timing, and temperature/pressure controls.

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
Develop an ISA-88-compliant batch control program in Structured Text for aspirin production, automating reactor heating/mixing, crystallization, and drying (90°C) with phase transitions, parameterized timing, and temperature/pressure controls.
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

**Deliverables:**

1.	A self-contained Structured Text program for the sequential control of the reaction stage of aspirin production, including parameter-driven control for heating, mixing, and holding the reaction conditions.
2.	A Structured Text program for the sequential control of the crystallization and drying stages, ensuring the dryer operates at 90°C for the specified time with proper phase transition logic.
3.	A modular, ISA-88-compliant Structured Text program that reliably executes the reaction and downstream stages of aspirin production.
4.	A Structured Text program that handles transitions between phases based on parameters and process conditions, supports safe and efficient batch execution, and ensures product quality through accurate control of temperature, timing, and material handling.
5.	A Structured Text program that follows ISA-88 concepts such as modular equipment phases, procedural elements, and reusable control blocks.
6.	A Structured Text program that is well-documented, with clear comments and variable names, and is easy to understand and maintain.
7.	A Structured Text program that is tested and debugged, with a test plan and test results included.
8.	A Structured Text program that is delivered in a format that can be easily imported into a PLC programming environment.
9.	A Structured Text program that is delivered with a user manual that explains the program's functionality and how to use it.
10.	A Structured Text program that is delivered with a maintenance manual that explains how to troubleshoot and maintain the program.
11.	A Structured Text program that is delivered with a training manual that explains how to use the program and how to train operators on its use.
12.	A Structured Text program that is delivered with a support contract that includes regular updates and support for any issues that may arise.
13.	A Structured Text program that is delivered with a warranty that covers any defects in the program for a specified period of time.
14.	A Structured Text program that is delivered with a license agreement that outlines the terms and conditions of use.
15.	A Structured Text program that is delivered with a maintenance contract that includes regular updates and support for any issues that may arise.
16.	A Structured Text program that is delivered with a training contract that includes regular training sessions for operators and maintenance personnel.
17.	A Structured Text program that is delivered with a support contract that includes regular updates and support for any issues that
