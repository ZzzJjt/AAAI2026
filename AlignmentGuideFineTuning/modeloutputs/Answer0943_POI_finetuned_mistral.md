### Intent:
The task is to develop an ISA-88-compliant batch control recipe for aspirin production, including a Structured Text implementation for the reaction stage with precise temperature, pressure, and timing controls, while ensuring proper transitions between process phases and maintaining 90°C during drying.  

**Intent Summary:**  
*Create an ISA-88 batch control system for aspirin manufacturing, featuring a Structured Text program to automate the reaction stage with parameterized heating, mixing, and drying processes.*

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
The task is to develop an ISA-88-compliant batch control recipe for aspirin production, including a Structured Text implementation for the reaction stage with precise temperature, pressure, and timing controls, while ensuring proper transitions between process phases and maintaining 90°C during drying.  

**Intent Summary:**  
*Create an ISA-88 batch control system for aspirin manufacturing, featuring a Structured Text program to automate the reaction stage with parameterized heating, mixing, and drying processes.*
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
(* IEC 61131-3 Structured Text program for ISA-88 batch control of aspirin production *)
(* Implements reaction stage with temperature, pressure, and timing control *)

PROGRAM AspirinReactionControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                  (* TRUE to start batch *)
    StopBatch : BOOL;                   (* TRUE to stop batch *)
    Temperature_PV : REAL;              (* Measured reactor temperature, °C *)
    Pressure_PV : REAL;                 (* Measured reactor pressure, bar *)
    AgitatorSpeed_PV : REAL;            (* Measured agitator speed, RPM *)
    BatchID : DWORD;                    (* Unique batch identifier *)
    
    (* Outputs *)
    HeaterOn : BOOL;                    (* TRUE to activate heater *)
    AgitatorSpeed : REAL;               (* Target agitator speed, RPM *)
    CoolerOn : BOOL;                    (* TRUE to activate cooler *)
    MixingOn : BOOL;                    (* TRUE to activate mixing *)
    ReactionComplete : BOOL;            (* TRUE when reaction complete *)
    Error : BOOL;                       (* TRUE if error occurs *)
    ErrorID : DWORD;                    (* Error code *)
    
    (* Internal variables *)
    Phase : INT := 0;                   (* Current phase: 0=Idle, 1=Heating, 2=Mixing, 3=Holding, 4=Cooling, 5=Complete *)
    TargetTemperature : REAL := 90.0;   (* Target temperature for reaction, °C *)
    TargetPressure : REAL := 1.0;       (* Target pressure for reaction, bar *)
    MixingDuration : TIME := T#10m;     (* Duration for mixing, 10 minutes *)
    CoolingDuration : TIME := T#30m;    (* Duration for cooling, 30 minutes *)
    ReactionTimer : TON;                (* Timer for phase transitions *)
    AgitatorTimer : TON;                (* Timer for agitator control *)
    Ag
