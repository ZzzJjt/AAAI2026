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

Produce a modular, ISA-88-compliant Structured Text program that reliably executes the reaction and downstream stages of aspirin production. The system should handle transitions between phases based on parameters and process conditions, support safe and efficient batch execution, and ensure product quality through accurate control of temperature, timing, and material handling.
FUNCTION_BLOCK FB_BatchControl
VAR_INPUT
    Execute : BOOL; // Starts the batch process
    Stop : BOOL;    // Stops the batch process
    Phase : INT;    // Current phase index (1–5)
    Temp_PV : REAL; // Measured temperature (°C)
    Temp_SP : REAL; // Setpoint temperature (°C)
    Temp_PID : BOOL; // TRUE to enable PID control
    PID_Kp : REAL;  // PID gain
    PID_Ki : REAL;  // PID integral gain
    PID_Kd : REAL;  // PID derivative gain
    Timer_Ton : TIME; // Timer ON time for heating
    Timer_Tco : TIME; // Timer CO time for heating
    Timer_Toc : TIME; // Timer CO time for drying
    Timer_Ton_d : TIME; // Timer ON time for drying
    Timer_Tco_d : TIME; // Timer CO time for drying
    Timer_Ton_c : TIME; // Timer ON time for cooling
    Timer_Tco_c : TIME; // Timer CO time for cooling
    Timer_Ton_e : TIME; // Timer ON time for evacuation
    Timer_Tco_e : TIME; // Timer CO time for evacuation
    Timer_Ton_f : TIME; // Timer ON time for filling
    Timer_Tco_f : TIME; // Timer CO time for filling
    Timer_Ton_s : TIME; // Timer ON time for sealing
    Timer_Tco_s : TIME; // Timer CO time for sealing
    Timer_Ton_r : TIME; // Timer ON time for reactor
    Timer_Tco_r : TIME; // Timer CO time for reactor
    Timer_Ton_d : TIME; // Timer ON time for dryer
    Timer_Tco_d : TIME; // Timer CO time for dryer
    Timer_Ton_c : TIME; // Timer ON time for cooler
    Timer
