### Intent:
**Intent Summary:**  
Design an ISA-88-compliant batch control recipe and IEC 61131-3 Structured Text program to automate the production of 100 kg cocoa milk, ensuring precise ingredient mixing, heating, and scalability while adhering to industrial standards.  

*(Focus: Batch automation, ingredient control, temperature/speed regulation, ISA-88/IEC 61131-3 compliance.)*

### Prompt:
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Cocoa milk production in batch mode requires accurate proportioning, heating, and mixing of ingredients such as milk, water, liquid sugar, and cocoa. In industrial food processing, applying ISA-88 standards ensures that the control system is modular, scalable, and maintains high product consistency. A key challenge lies in precisely managing temperature, mixing speed, and sequence timing to meet quality requirements at scale.

🟩 A (Action) – Task to Perform

Design an ISA-88-compliant batch control recipe to produce 100 kg of cocoa milk, specifying ingredient quantities and process parameters. Then, implement a self-contained IEC 61131-3 Structured Text program to control the mixing and heating process, including:
	•	Ingredient setpoints (e.g., 60 kg milk, 20 kg water, 15 kg liquid sugar, 5 kg cocoa)
	•	Stirring speed (e.g., 200 RPM),
	•	Heating temperature (e.g., 70°C), and
	•	Time durations for each phase (e.g., 10 minutes blending)
The program must follow ISA-88 principles with clearly defined phases, transitions, and reusable logic blocks.

🟨 R (Result) – Expected Outcome

The result should be a modular and maintainable control solution that enables precise, repeatable cocoa milk production. It should support both small and large batch scalability, minimize downtime, and ensure consistency in product texture, temperature, and sweetness balance.

🟦 E (Example) – Concrete Illustration

For example, the control program should first call AddIngredient('Milk', 60) and proceed through StartHeating(Temp := 70) and StartMixing(Speed := 200) phases, holding these conditions for 10 minutes. Once mixing is complete, the system transitions to a hold or unload state, ready for packaging. The program structure should make it easy to adapt setpoints for different batch sizes or formulations.

### Generated Code:
**Intent Summary:**  
Design an ISA-88-compliant batch control recipe and IEC 61131-3 Structured Text program to automate the production of 100 kg cocoa milk, ensuring precise ingredient mixing, heating, and scalability while adhering to industrial standards.  

*(Focus: Batch automation, ingredient control, temperature/speed regulation, ISA-88/IEC 61131-3 compliance.)*
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Cocoa milk production in batch mode requires accurate proportioning, heating, and mixing of ingredients such as milk, water, liquid sugar, and cocoa. In industrial food processing, applying ISA-88 standards ensures that the control system is modular, scalable, and maintains high product consistency. A key challenge lies in precisely managing temperature, mixing speed, and sequence timing to meet quality requirements at scale.

🟩 A (Action) – Task to Perform

Design an ISA-88-compliant batch control recipe to produce 100 kg of cocoa milk, specifying ingredient quantities and process parameters. Then, implement a self-contained IEC 61131-3 Structured Text program to control the mixing and heating process, including:
	•	Ingredient setpoints (e.g., 60 kg milk, 20 kg water, 15 kg liquid sugar, 5 kg cocoa)
	•	Stirring speed (e.g., 200 RPM),
	•	Heating temperature (e.g., 70°C), and
	•	Time durations for each phase (e.g., 10 minutes blending)
The program must follow ISA-88 principles with clearly defined phases, transitions, and reusable logic blocks.

🟨 R (Result) – Expected Outcome

The result should be a modular and maintainable control solution that enables precise, repeatable cocoa milk production. It should support both small and large batch scalability, minimize downtime, and ensure consistency in product texture, temperature, and sweetness balance.

🟦 E (Example) – Concrete Illustration

For example, the control program should first call AddIngredient('Milk', 60) and proceed through StartHeating(Temp := 70) and StartMixing(Speed := 200) phases, holding these conditions for 10 minutes. Once mixing is complete, the system transitions to a hold or unload state, ready for packaging. The program structure should make it easy to adapt setpoints for different batch sizes or formulations.
(* IEC 61131-3 Structured Text Program: Cocoa Milk Batch Control *)
(* Purpose: Automates the production of 100 kg of cocoa milk using ISA-88 principles *)

PROGRAM CocoaMilkBatchControl
VAR
    (* Inputs *)
    StartButton : BOOL;         (* Start/Stop button *)
    BatchSize : INT := 100;     (* Batch size in kg *)
    Milk : REAL := 60.0;        (* Milk volume in kg *)
    Water : REAL := 20.0;       (* Water volume in kg *)
    LiquidSugar : REAL := 15.0; (* Liquid sugar volume in kg *)
    Cocoa : REAL := 5.0;       (* Cocoa volume in kg *)
    StirringSpeed : REAL := 200.0; (* Stirring speed in RPM *)
    HeatingTemp : REAL := 70.0; (* Heating temperature in °C *)
    HeatingDuration : TIME := T#10m; (* Heating duration in minutes *)
    MixingDuration : TIME := T#10m; (* Mixing duration in minutes *)
    MixingPhase : BOOL := FALSE; (* TRUE if mixing is active *)
    HeatingPhase : BOOL := FALSE; (* TRUE if heating is active *)
    CoolingPhase : BOOL := FALSE; (* TRUE if cooling is active *)
    CoolingDuration : TIME := T#10m; (* Cooling duration in minutes *)
    CoolingTemp : REAL := 40.0; (* Cooling temperature in °C *)
    CoolingPhaseTimer : TON; (* Timer for cooling phase *)
    CoolingPhaseDone : BOOL := FALSE; (* TRUE when cooling is complete *)

    (* Outputs *)
    MixingPhaseDone : BOOL; (* TRUE when mixing is complete *)
    HeatingPhaseDone : BOOL; (* TRUE when heating is complete *)
    CoolingPhaseDone : BOOL; (* TRUE when cooling is complete *)
    CoolingTempSetpoint : REAL; (* Cooling temperature setpoint *)
    CoolingPhaseTimerRunning : BOOL; (* TRUE if cooling phase is active *)

    (* Internal Variables *)
    PhaseTimer : TON; (* Timer for each phase *)
    PhaseDone : BOOL; (* TRUE when phase is complete *)
    PhaseTimerRunning : BOOL; (* TRUE if phase timer is running *)
    PhaseTimer
