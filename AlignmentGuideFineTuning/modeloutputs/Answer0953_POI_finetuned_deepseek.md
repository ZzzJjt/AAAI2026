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
% IEC 61131-3 Structured Text: ISA-88 Batch Control for Aspirin Reaction Stage
% Reactor: Heating, Mixing, Holding, Cooling, Drying
% Modular, ISA-88-compliant, and ready for PLC deployment

PROGRAM AspirinReactionControl
VAR
    (* Process Parameters *)
    Educts_AceticAnhydride : REAL := 100.0;
    Educts_SalicylicAcid : REAL := 100.0;
    Educts_SulfuricAcid : REAL := 100.0;
    Products_AcetylsalicylicAcid : REAL := 100.0;
    Products_AceticAcid : REAL := 0.0;
    Temperature_Heating : REAL := 120.0;
    Temperature_Holding : REAL := 80.0;
    Temperature_Cooling : REAL := 60.0;
    Temperature_Drying : REAL := 90.0;
    Pressure_Heating : REAL := 1.0;
    Pressure_Holding : REAL := 0.5;
    Pressure_Cooling : REAL := 0.1;
    Pressure_Drying : REAL := 0.0;
    Time_Heating : TIME := T#10m;
    Time_Holding : TIME := T#2h;
    Time_Cooling : TIME := T#3h;
    Time_Drying : TIME := T#4h;

    (* Control Variables *)
    Heating_ON : BOOL := FALSE;
    Mixing_ON : BOOL := FALSE;
    Holding_ON : BOOL := FALSE;
    Cooling_ON : BOOL := FALSE;
    Drying_ON : BOOL := FALSE;
    Heating_Done : BOOL := FALSE;
    Mixing_Done : BOOL := FALSE;
    Holding_Done : BOOL := FALSE;
    Cooling_Done : BOOL := FALSE;
    Drying_Done : BOOL := FALSE;

    (* Control Logic *)
    Heating_Timer : TON;
    Mixing_Timer : TON;
    Holding_Timer : TON;
    Cooling_Timer : TON;
    Drying
