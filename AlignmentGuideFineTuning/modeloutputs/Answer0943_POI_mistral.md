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

---

**Batch Aspirin Recipe:**

**Process Structure:**

1. Reactor
2. Crystallizer
3. Centrifuge
4. Dryer

**Materials:**

1. Acetic anhydride
2. Salicylic acid
3. Sulfuric acid (catalyst)
4. Acetylsalicylic acid (product)
5. Acetic acid (byproduct)

**Reaction Stage (Structured Text):**

```
PROGRAM Reaction_Stage
VAR
    t_reaction : TIME;
    t_heating : TIME;
    t_mixing : TIME;
    t_holding : TIME;
    t_crystallization : TIME;
    t_drying : TIME;
    T_reactor : TEMPERATURE;
    P_reactor : PRESSURE;
    T_crystallizer : TEMPERATURE;
    T_dryer : TEMPERATURE;
    T_setpoint : TEMPERATURE := 90;
BEGIN
    -- Initialize variables
    t_reaction := T#0;
    t_heating := T#0;
    t_mixing := T#0;
    t_holding := T#0;
    t_crystallization := T#0;
    t_drying := T#0;
    T_reactor := 0;
    P_reactor := 0;
    T_crystallizer := 0;
    T_dryer := 0;

    -- Reaction Stage
    IF (Phase = "Reaction") THEN
        -- Heating
        IF (t_heating = T#0) THEN
            T_reactor := 50;
            P_reactor := 100;
            t_heating := T#10;
        END_IF;

        -- Check if heating is complete
        IF (t_heating < t_reaction) THEN
            -- Update time
            t_heating := t_heating + T#1;
        ELSE
            -- Mixing
            IF
