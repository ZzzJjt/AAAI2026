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
FUNCTION_BLOCK FB_BatchControl
VAR_INPUT
    Execute : BOOL; // Starts the batch process
    Stop : BOOL;    // Stops the batch process
    Phase : INT;    // Current phase index (1–6)
    Temp_PV : REAL; // Measured reactor temperature (°C)
    Pressure_PV : REAL; // Measured reactor pressure (bar)
    Agitate : BOOL; // Agitation status
    Heater : BOOL;  // Heater status
    Cooler : BOOL;  // Cooler status
    Valve_Open : BOOL; // Valve status
    Mixing_Speed : REAL; // Mixing speed (RPM)
    Timer : TON; // Timer for phase transitions
    Timer_Value : TIME; // Duration for phase transitions
    Phase_Complete : BOOL; // Flag for phase completion
    Phase_Error : BOOL; // Flag for phase error
    Error_Code : INT; // Error code (0 = No error, 1 = Temperature out of range, 2 = Pressure out of range, 3 = Agitation fault, 4 = Heater/Cooler fault, 5 = Valve fault)
END_VAR

VAR_OUTPUT
    Temp_Setpoint : REAL; // Reactor temperature setpoint (°C)
    Pressure_Setpoint : REAL; // Reactor pressure setpoint (bar)
    Mixing_Setpoint : REAL; // Mixing speed setpoint (RPM)
    Heater_Setpoint : BOOL; // Heater setpoint
    Cooler_Setpoint : BOOL; // Cooler setpoint
    Valve_Setpoint : BOOL; // Valve setpoint
    Phase_Transition : BOOL; // Flag for phase transition
    Phase_Complete_Output : BOOL; // Phase completion output
    Phase_Error_Output : BOOL; // Phase error output
    Error_Code_Output : INT; // Error code output
END_VAR

VAR
    Phase_Sequence : ARRAY[1..6] OF INT := [
        1, // Heating
        2, // Mixing
        3, // Reaction
        4,
