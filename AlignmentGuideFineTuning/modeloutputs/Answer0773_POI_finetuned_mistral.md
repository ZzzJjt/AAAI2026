### Intent:
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for aspirin production, automating the reaction, crystallization, and drying phases with precise temperature, pressure, and timing controls.

### Prompt:
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch automation programs using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a batch control recipe for the production of aspirin (acetylsalicylic acid) in accordance with ISA-88 standards. The process includes a reactor, crystallizer, centrifuge, and dryer. You must:
	•	Outline the full batch process, including inputs (acetic anhydride, salicylic acid, sulfuric acid) and products (acetylsalicylic acid and acetic acid).
	•	Focus on implementing a self-contained Structured Text program for the reaction stage, with parameters for temperature, pressure, and time.
	•	Include control logic for initiating and transitioning between sub-steps like heating, mixing, and reaction hold.
	•	Extend the logic to include the crystallization and drying phases, with the drying phase maintained at 90°C and controlled by timers and interlocks.

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text program that includes:
	•	Parameterized method or function block calls (e.g., StartHeating, StartMixing, HoldReaction)
	•	Sequencing logic using timers and conditions
	•	Modular, ISA-88-aligned structure (e.g., phases, operations)
	•	Inline comments for clarity
	•	Accurate representation of batch transitions and equipment states

### Generated Code:
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for aspirin production, automating the reaction, crystallization, and drying phases with precise temperature, pressure, and timing controls.
**Batch Aspirin:**

Develop an ISA-88 batch control recipe for the production of aspirin (acetylsalicylic acid), outlining the process stages and the physical structure, which includes a reactor, crystallizer, centrifuge, and dryer. The process involves the following educts: acetic anhydride, salicylic acid, and sulfuric acid as a catalyst, with products being acetylsalicylic acid and acetic acid. The drying stage should occur at 90°C.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the reaction stage, incorporating typical parameter values for temperature, pressure, and timing. Ensure that the program logic follows the batch control principles of ISA-88, with clear transitions between operations like heating, mixing, and reaction completion. Additionally, include control parameters for initiating and managing the crystallization and drying phases, ensuring that temperature and time controls are accurate.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch automation programs using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a batch control recipe for the production of aspirin (acetylsalicylic acid) in accordance with ISA-88 standards. The process includes a reactor, crystallizer, centrifuge, and dryer. You must:
	•	Outline the full batch process, including inputs (acetic anhydride, salicylic acid, sulfuric acid) and products (acetylsalicylic acid and acetic acid).
	•	Focus on implementing a self-contained Structured Text program for the reaction stage, with parameters for temperature, pressure, and time.
	•	Include control logic for initiating and transitioning between sub-steps like heating, mixing, and reaction hold.
	•	Extend the logic to include the crystallization and drying phases, with the drying phase maintained at 90°C and controlled by timers and interlocks.

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text program that includes:
	•	Parameterized method or function block calls (e.g., StartHeating, StartMixing, HoldReaction)
	•	Sequencing logic using timers and conditions
	•	Modular, ISA-88-aligned structure (e.g., phases, operations)
	•	Inline comments for clarity
	•	Accurate representation of batch transitions and equipment states
(* IEC 61131-3 Structured Text program for ISA-88-compliant batch control of aspirin production *)
(* Implements reaction, crystallization, and drying phases with precise temperature, pressure, and timing control *)

PROGRAM AspirinBatchControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                      (* TRUE to start batch process *)
    BatchComplete : BOOL;                   (* TRUE when batch completes *)
    CurrentTemp : REAL;                     (* Current reactor temperature, °C *)
    CurrentPressure : REAL;                 (* Current reactor pressure, bar *)
    CurrentTime : TON;                      (* Current elapsed time since batch start *)
    
    (* Outputs *)
    HeatReactor : BOOL;                     (* TRUE to heat reactor *)
    MixReaction : BOOL;                     (* TRUE to mix reaction *)
    HoldReaction : BOOL;                    (* TRUE to hold reaction *)
    StartCrystallization : BOOL;            (* TRUE to start crystallization *)
    StartDrying : BOOL;                     (* TRUE to start drying *)
    StopDrying : BOOL;                      (* TRUE to stop drying *)
    CompleteBatch : BOOL;                   (* TRUE when batch completes *)
    
    (* Internal Variables *)
    Phase : INT := 0;                       (* 0=Idle, 1=Reaction, 2=Crystallization, 3=Drying *)
    ReactionComplete : BOOL;                (* TRUE when reaction complete *)
    CrystallizationComplete : BOOL;         (* TRUE when crystallization complete *)
    DryingComplete : BOOL;                  (* TRUE when drying complete *)
    TargetTemp : REAL := 80.0;             (* Target temperature for reaction, °C *)
    TargetPressure : REAL := 1.0;          (* Target pressure for reaction, bar *)
    TargetCrystTemp : REAL := 5.0;         (* Target temperature for crystallization, °C *)
    TargetDryTemp : REAL := 90.0;          (* Target temperature for drying, °C *)
    DryingDuration : TIME
