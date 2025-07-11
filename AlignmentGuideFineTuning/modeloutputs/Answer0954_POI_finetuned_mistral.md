### Intent:
The task involves developing an ISA-88-compliant batch control recipe and automation program in IEC 61131-3 Structured Text to produce 100 kg of cocoa milk, specifying ingredients, processing parameters, and sequential control logic for mixing, heating, and blending phases. 

**Intent Summary:**  
*"Create a modular, scalable batch control program for cocoa milk production that follows ISA-88 standards, with ingredient dosing, temperature-controlled mixing, and industrial integration capabilities."*

### Prompt:
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**T-A-G:**

🟥 T (Task)

Develop an ISA-88-compliant batch control recipe and automation program for producing 100 kg of cocoa milk using IEC 61131-3 Structured Text.

🟩 A (Action)

Specify the required ingredients—milk, water, liquid sugar, and cocoa—along with their respective quantities. Define the processing parameters such as heating temperature (e.g., 70°C), stirring speed (e.g., 200 RPM), and mixing duration (e.g., 10 minutes). Write a self-contained Structured Text program that controls the sequential execution of the mixing process, including ingredient addition, heating, and blending. Ensure the program structure reflects ISA-88 principles, with modular logic and clearly defined phases.

🟦 G (Goal)

Deliver a robust, modular, and scalable control program that ensures product consistency, process efficiency, and easy integration into industrial batch control systems, supporting future adjustments in batch size or formula while maintaining ISA-88 compliance.

### Generated Code:
The task involves developing an ISA-88-compliant batch control recipe and automation program in IEC 61131-3 Structured Text to produce 100 kg of cocoa milk, specifying ingredients, processing parameters, and sequential control logic for mixing, heating, and blending phases. 

**Intent Summary:**  
*"Create a modular, scalable batch control program for cocoa milk production that follows ISA-88 standards, with ingredient dosing, temperature-controlled mixing, and industrial integration capabilities."*
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**T-A-G:**

🟥 T (Task)

Develop an ISA-88-compliant batch control recipe and automation program for producing 100 kg of cocoa milk using IEC 61131-3 Structured Text.

🟩 A (Action)

Specify the required ingredients—milk, water, liquid sugar, and cocoa—along with their respective quantities. Define the processing parameters such as heating temperature (e.g., 70°C), stirring speed (e.g., 200 RPM), and mixing duration (e.g., 10 minutes). Write a self-contained Structured Text program that controls the sequential execution of the mixing process, including ingredient addition, heating, and blending. Ensure the program structure reflects ISA-88 principles, with modular logic and clearly defined phases.

🟦 G (Goal)

Deliver a robust, modular, and scalable control program that ensures product consistency, process efficiency, and easy integration into industrial batch control systems, supporting future adjustments in batch size or formula while maintaining ISA-88 compliance.
(* IEC 61131-3 Structured Text Program: CocoaMilkBatchControl *)
(* Purpose: Implements ISA-88 batch control recipe for cocoa milk production *)

PROGRAM CocoaMilkBatchControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                    (* TRUE to start batch *)
    StopBatch : BOOL;                     (* TRUE to stop batch *)
    BatchComplete : BOOL;                 (* TRUE when batch completes *)
    CurrentWeight : REAL;                 (* Current batch weight in kg *)
    TargetWeight : REAL := 100.0;         (* Target batch weight in kg *)
    IngredientAvailable : ARRAY[1..4] OF BOOL; (* TRUE if ingredient available *)
    MilkAvailable : BOOL;                 (* TRUE if milk available *)
    WaterAvailable : BOOL;                (* TRUE if water available *)
    SugarAvailable : BOOL;                (* TRUE if sugar available *)
    CocoaAvailable : BOOL;                (* TRUE if cocoa available *)
    
    (* Outputs *)
    DoseMilk : BOOL;                      (* TRUE to dose milk *)
    DoseWater : BOOL;                     (* TRUE to dose water *)
    DoseSugar : BOOL;                     (* TRUE to dose sugar *)
    DoseCocoa : BOOL;                     (* TRUE to dose cocoa *)
    StartHeating : BOOL;                  (* TRUE to start heating *)
    StopHeating : BOOL;                   (* TRUE to stop heating *)
    MixingSpeed : REAL := 200.0;          (* Mixing speed in RPM *)
    MixingDuration : TIME := T#10m;       (* Mixing duration *)
    BatchDone : BOOL;                     (* TRUE when batch done *)
    
    (* Internal Variables *)
    Phase : INT := 0;                     (* 0=Idle, 1=IngredientAddition, 2=Heating, 3=Mixing *)
    CurrentPhase : STRING[20];           (* Current phase name *)
    CurrentStep : STRING[20];            (* Current step name *)
    Step
