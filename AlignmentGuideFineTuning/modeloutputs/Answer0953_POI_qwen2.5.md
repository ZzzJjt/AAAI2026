### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the aspirin production reaction stage, including precise temperature, mixing, and timing control, with modular logic for heating, mixing, holding, and fault handling.  

*(Focus: Code generation for a reactor phase with parameterized transitions, safety checks, and ISA-88 alignment.)*

### Prompt:
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**T-A-G:**

🟥 T (Task)

Create an ISA-88-compliant batch control recipe for the production of aspirin (acetylsalicylic acid), and implement the reaction stage using IEC 61131-3 Structured Text.

🟩 A (Action)

Define the overall process structure, including a reactor, crystallizer, centrifuge, and dryer, and outline the key materials involved: acetic anhydride, salicylic acid, and sulfuric acid as catalyst. Then, develop a self-contained Structured Text program for the reaction stage, including process parameters such as temperature, pressure, and timing. Incorporate logic to manage transitions between operations (e.g., heating, mixing, holding), and include control routines for the crystallization and drying phases, ensuring accurate control—particularly maintaining 90°C during drying.

🟦 G (Goal)

Deliver a modular, maintainable control solution that adheres to ISA-88 standards, enabling reliable and flexible execution of batch stages with precise timing and parameter control, ensuring safe operation and high-quality aspirin production.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the aspirin production reaction stage, including precise temperature, mixing, and timing control, with modular logic for heating, mixing, holding, and fault handling.  

*(Focus: Code generation for a reactor phase with parameterized transitions, safety checks, and ISA-88 alignment.)*
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**T-A-G:**

🟥 T (Task)

Create an ISA-88-compliant batch control recipe for the production of aspirin (acetylsalicylic acid), and implement the reaction stage using IEC 61131-3 Structured Text.

🟩 A (Action)

Define the overall process structure, including a reactor, crystallizer, centrifuge, and dryer, and outline the key materials involved: acetic anhydride, salicylic acid, and sulfuric acid as catalyst. Then, develop a self-contained Structured Text program for the reaction stage, including process parameters such as temperature, pressure, and timing. Incorporate logic to manage transitions between operations (e.g., heating, mixing, holding), and include control routines for the crystallization and drying phases, ensuring accurate control—particularly maintaining 90°C during drying.

🟦 G (Goal)

Deliver a modular, maintainable control solution that adheres to ISA-88 standards, enabling reliable and flexible execution of batch stages with precise timing and parameter control, ensuring safe operation and high-quality aspirin production. **Batch Aspirin Control Program in IEC 61131-3 Structured Text**

```structuredtext
PROGRAM BatchAspirin
VAR
    // Process Variables
    ReactorTemp : REAL := 0.0; // Reactor temperature in °C
    ReactorPressure : REAL := 0.0; // Reactor pressure in bar
    MixingTime : REAL := 0.0; // Mixing time in minutes
    ReactionTime : REAL := 0.0; // Reaction time in minutes
    CrystallizationTime : REAL := 0.0; // Crystallization time in minutes
    DryingTime : REAL := 0.0; // Drying time in minutes
    DryingTemp : REAL := 90.0; // Drying temperature in °C

    // ISA-88 Parameters
    BatchNumber : INT := 1; // Batch number
    BatchStatus : INT := 0; // Batch status (0: Idle, 1: Running, 2: Completed)
    Transition : INT := 0; // Current transition (0: Heating, 1: Mixing, 2: Reaction, 3: Crystallization, 4: Drying)

    // Control Logic
    HeatingControl : BOOL := FALSE; // Heating control signal
    MixingControl : BOOL := FALSE; // Mixing control signal
    ReactionControl : BOOL := FALSE; // Reaction control signal
    CrystallizationControl : BOOL := FALSE; // Crystallization control signal
    DryingControl : BOOL := FALSE; // Drying control signal
END_VAR

// Main Program Logic
MAIN
    // Initialize Batch
    IF BatchStatus = 0 THEN
        BatchStatus := 1;
        Transition := 0;
        HeatingControl := TRUE;
    END_IF;

    // Transition Logic
    CASE Transition OF
        0: // Heating
            IF ReactorTemp >= 100.0 THEN
                Transition := 1;
                HeatingControl := FALSE;
                MixingControl := TRUE;
            END_IF;
        1: // Mixing
            IF MixingTime > 0.0 THEN
                MixingTime := MixingTime - 1.0;
                MixingControl := TRUE;
            ELSE
                Transition := 2;
                MixingControl := FALSE;
                ReactionControl := TRUE;
            END_IF;
        2: // Reaction
            IF Reaction
