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

Deliver a modular, maintainable control solution that adheres to ISA-88 standards, enabling reliable and flexible execution of batch stages with precise timing and parameter control, ensuring safe operation and high-quality aspirin production.
(* IEC 61131-3 Structured Text Program: AspirinBatchControl *)
(* Purpose: Implements ISA-88-compliant batch control for aspirin production *)

PROGRAM AspirinBatchControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                    (* TRUE to start batch process *)
    StopBatch : BOOL;                     (* TRUE to stop batch process *)
    EmergencyStop : BOOL;                 (* TRUE to stop all operations *)
    
    (* Outputs *)
    BatchComplete : BOOL;                 (* TRUE when batch completes successfully *)
    BatchFailed : BOOL;                   (* TRUE if batch fails *)
    Fault : BOOL;                         (* TRUE if emergency stop or fault *)
    
    (* Internal Variables *)
    CurrentPhase : INT := 0;              (* 0=Idle, 1=Reaction, 2=Crystallization, 3=Drying, 4=Finishing *)
    PhaseState : INT := 0;                (* 0=Idle, 1=Heating, 2=Mixing, 3=Holding, 4=Cooling, 5=Centrifuging, 6=Drying, 7=Finishing *)
    TempReactor : REAL := 80.0;           (* Reactor temperature in °C *)
    TempCryst : REAL := 25.0;            (* Crystallizer temperature in °C *)
    TempDryer : REAL := 90.0;            (* Dryer temperature in °C *)
    Pressure : REAL := 1.0;              (* Reactor pressure in bar *)
    MixSpeed : REAL := 100.0;            (* Mixing speed in RPM *)
    TimeRemaining : TIME := T#1h;         (* Remaining time for current operation *)
    Timer : TON;                          (* Phase timer *)
    FaultDetected : BOOL;                (* TRUE if fault condition *)
    
    (* Equipment Interfaces *)
    Reactor : REFERENCE;                  (* Reactor interface *)
    Crystallizer : REFERENCE;             (* Crystallizer
