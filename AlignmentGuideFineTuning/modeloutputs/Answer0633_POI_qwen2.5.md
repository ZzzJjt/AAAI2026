### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for aspirin production, automating reactor, crystallizer, centrifuge, and dryer stages with precise temperature (90°C drying), timing, and phase transitions.  

*(Key focus: ISA-88 modularity, parameter-driven phases, and safety-critical controls for pharmaceutical batch processes.)*

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
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for aspirin production, automating reactor, crystallizer, centrifuge, and dryer stages with precise temperature (90°C drying), timing, and phase transitions.  

*(Key focus: ISA-88 modularity, parameter-driven phases, and safety-critical controls for pharmaceutical batch processes.)*
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
**Batch Aspirin Control Program in IEC 61131-3 Structured Text**

```structuredtext
PROGRAM BatchAspirin
VAR
    // Physical Model
    Reactor : Reactor;
    Crystallizer : Crystallizer;
    Centrifuge : Centrifuge;
    Dryer : Dryer;

    // Procedural Model
    ReactionPhase : Phase;
    CrystallizationPhase : Phase;
    DryingPhase : Phase;

    // Control Parameters
    ReactionTemperature : REAL := 100.0; // °C
    ReactionTime : REAL := 60.0; // minutes
    CrystallizationTime : REAL := 30.0; // minutes
    DryingTemperature : REAL := 90.0; // °C
    DryingTime : REAL := 60.0; // minutes

    // Timers
    ReactionTimer : Timer;
    CrystallizationTimer : Timer;
    DryingTimer : Timer;

    // Conditions
    ReactionComplete : BOOL;
    CrystallizationComplete : BOOL;
    DryingComplete : BOOL;
END_VAR

// Initialize Timers
ReactionTimer := Timer(ReactionTime);
CrystallizationTimer := Timer(CrystallizationTime);
DryingTimer := Timer(DryingTime);

// Main Control Loop
WHILE TRUE DO
    // Reaction Phase
    IF ReactionTimer.IsExpired() THEN
        ReactionComplete := TRUE;
    END_IF;

    // Crystallization Phase
    IF ReactionComplete AND NOT CrystallizationComplete THEN
        CrystallizationTimer.Start();
        CrystallizationComplete := TRUE;
    END_IF;

    // Drying Phase
    IF CrystallizationComplete AND NOT DryingComplete THEN
        Dryer.SetTemperature(DryingTemperature);
        DryingTimer.Start();
        DryingComplete := TRUE;
    END_IF;

    // Check for Completion
    IF DryingTimer.IsExpired() THEN
        // Batch Complete
        Break;
    END_IF;

    // Update Timers
    ReactionTimer.Update();
    CrystallizationTimer.Update();
    DryingTimer.Update();
END_WHILE

// End of Batch
```

**Explanation:**

1. **Physical Model**: The program defines the physical components of the process (reactor, crystallizer,
