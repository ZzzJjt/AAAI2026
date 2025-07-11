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

Produce a modular, ISA-88-compliant Structured Text program that reliably executes the reaction and downstream stages of aspirin production. The system should handle transitions between phases based on parameters and process conditions, support safe and efficient batch execution, and ensure product quality through accurate control of temperature, timing, and material handling. The program should be well-documented and include comments explaining the logic and control strategies used.
**Batch Aspirin Control Program in Structured Text**

```structuredtext
PROGRAM BatchAspirinControl
VAR
    // ISA-88 Batch Control Variables
    BatchID : STRING := "Batch1";
    BatchStatus : STRING := "Idle";
    CurrentPhase : STRING := "Idle";
    HeatingTimer : TIME := 0;
    MixingTimer : TIME := 0;
    ReactionTimer : TIME := 0;
    CrystallizationTimer : TIME := 0;
    DryingTimer : TIME := 0;
    // Process Parameters
    HeatingDuration : TIME := 300; // 5 minutes
    MixingDuration : TIME := 10; // 1 minute
    ReactionDuration : TIME := 60; // 1 hour
    CrystallizationDuration : TIME := 30; // 30 minutes
    DryingDuration : TIME := 60; // 1 hour
    // Temperature and Pressure Controls
    TargetTemperature : REAL := 100.0; // °C
    TargetPressure : REAL := 1.0; // bar
    ActualTemperature : REAL := 0.0; // °C
    ActualPressure : REAL := 0.0; // bar
    // Control Logic
    HeatingControl : BOOL := FALSE;
    MixingControl : BOOL := FALSE;
    ReactionControl : BOOL := FALSE;
    CrystallizationControl : BOOL := FALSE;
    DryingControl : BOOL := FALSE;
END_VAR

// Main Control Loop
WHILE TRUE DO
    CASE BatchStatus OF
        "Idle":
            IF CurrentPhase = "Idle" THEN
                // Start the batch
                BatchStatus := "Running";
                CurrentPhase := "Heating";
                HeatingControl := TRUE;
                HeatingTimer := HeatingDuration;
            END_IF;
        "Running":
            CASE CurrentPhase OF
                "Heating":
                    // Control heating
                    IF HeatingTimer > 0 THEN
                        HeatingTimer := HeatingTimer - 1;
                        HeatingControl := TRUE;
                    ELSE
                        HeatingControl := FALSE;
                        CurrentPhase := "Mixing";
                        MixingControl := TRUE;
                        MixingTimer := MixingDuration;
                    END_IF;
                "Mixing":
                    // Control mixing
                    IF MixingTimer > 0 THEN
                        MixingTimer := MixingTimer - 1;
