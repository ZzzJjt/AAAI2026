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
    StartButton : BOOL; // Starts the batch process
    StopButton : BOOL;  // Stops the batch process
    EmergencyStop : BOOL; // Emergency stop signal
    BatchID : INT;       // Batch identifier
    BatchType : INT;     // Batch type (1: Aspirin, 2: Acetic Acid)
END_VAR

VAR_OUTPUT
    ReactorHeating : BOOL; // Reactor heating control
    ReactorMixing : BOOL;  // Reactor mixing control
    ReactorHold : BOOL;   // Reactor holding control
    CrystallizerStart : BOOL; // Crystallizer start control
    CrystallizerStop : BOOL; // Crystallizer stop control
    CentrifugeStart : BOOL; // Centrifuge start control
    CentrifugeStop : BOOL; // Centrifuge stop control
    DryerStart : BOOL;     // Dryer start control
    DryerStop : BOOL;      // Dryer stop control
    BatchStatus : INT;     // Batch status (0: Idle, 1: Running, 2: Stopped)
    BatchError : BOOL;     // Batch error flag
    BatchErrorID : INT;    // Batch error ID
END_VAR

VAR
    BatchRunning : BOOL := FALSE; // Flag indicating whether the batch is running
    BatchType_ID : INT;           // Batch type identifier
    BatchType_Name : STRING[20];  // Batch type name
    BatchType_PID : PID;          // Batch type PID controller
    BatchPID_Setpoint : REAL;     // Batch type PID setpoint
    BatchPID_Kp : REAL;           // Batch type PID gain
    BatchPID_Ki : REAL;           // Batch type PID integral gain
    BatchPID_Kd : REAL;           // Batch type PID derivative gain
    BatchPID_Output : REAL;      // Batch type PID output
    BatchPID_Error : REAL;       // Batch type PID error
    BatchPID_Error_Sum : REAL;   // Batch type PID error sum
    BatchPID_Integral : REAL;    // Batch type PID integral
    BatchPID_Derivative : REAL;  // Batch type PID derivative
    BatchPID_Output_Limit : REAL; // Batch type PID output limit
    Batch
